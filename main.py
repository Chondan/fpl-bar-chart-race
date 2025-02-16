from get_data import get_league_info, get_data
import bar_chart_race as bcr
import asyncio

async def main():

    with open("league_id.txt", "r") as f:
        league_id = f.read()
    
    league_info = await get_league_info(league_id)
    league_name = league_info["league_name"]
    users = league_info["users"]
    data = await get_data(league_id, None)

    bcr.bar_chart_race(
        df=data, 
        filename=f"{league_id}.mp4",
        period_length=1500,
        steps_per_period=20,
        n_bars=min(len(users), 50),
        filter_column_colors=True,
        period_fmt='{x:.0f}',
        title=league_name,
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
