# FPL League Bar Chart Race
This is a repository that scrapes the past round scores of all users of a Fantasy Premier League mini league and uses the bar_chart_race package in order to create a bar chart race of this data.

Original: https://github.com/ChrisMusson/FPL_League_Bar_Chart_Race
# Usage
 - `python3 -m venv venv`
 - `pip3 install -r requirements.txt`
 - Edit the `league_id.txt` file so it contains the league ID for which you want to create the bar chart race. This can be found by navigating to your league's page on fantasy.premierleague.com and looking at the URL.
 - `python3 main.py` - This will take roughly 30 seconds, but will eventually create the bar chart race video file called `<league_id>.mp4`
# Example
![](https://github.com/ChrisMusson/FPL_League_Bar_Chart_Race/blob/master/51055_example.gif)
# Notes
 - This only takes into account a maximum of the current top 50 players in a mini league.
 - There are many ways the make the bar chart race look different; these can be found in the bar_char_race [documentation](https://www.dexplo.org/bar_chart_race/tutorial/)
 - If you want a higher framerate, you can raise the `steps_per_period` parameter in `main.py`. Though note that raising this does increase the time taken for the video to be created.