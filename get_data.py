import aiohttp
import pandas as pd


async def fetch(session, url, headers=None):
    async with session.get(url, headers=headers) as resp:
        assert resp.status == 200
        return await resp.json()

async def get_league_info(league_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings"
        data = await fetch(session, url)

        users = data["standings"]["results"]
        league_name = data["league"]["name"]
        league_starting_event = data["league"]["start_event"]

    return {
        "league_name": league_name,
        "starting_event": league_starting_event,
        "users": users
    }

async def get_data(league_id, starting_event=None):

    async with aiohttp.ClientSession() as session:
        league_info = await get_league_info(league_id)
        users = league_info["users"]
        league_starting_event = league_info["starting_event"] if starting_event is None else starting_event

        user_data = {}
        for user in users:
            user_data[user["entry"]] = user["entry_name"].title()

        all_dataframes = []
        i = 0
        for user_id in user_data.keys():
            i += 1
            url = f"https://fantasy.premierleague.com/api/entry/{user_id}/history/"
            json_data = await fetch(session, url)

            dataframe = pd.DataFrame(json_data["current"], columns=["event", "points", "event_transfers_cost"])

            # Starting Week
            dataframe = dataframe[dataframe["event"] >= league_starting_event]

            # Accumulate sum of points
            dataframe["points"] = dataframe["points"] - dataframe["event_transfers_cost"]
            dataframe["points"] = dataframe["points"].cumsum()
            
            dataframe = dataframe.rename(columns={"points": user_data[user_id]})
            dataframe.set_index("event", inplace=True)
            dataframe.drop(["event_transfers_cost"], axis=1, inplace=True)
            
            all_dataframes.append(dataframe)

    data = pd.concat(all_dataframes, axis=1)

    return data
