import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st

def get_schedule_df():
    columns = [x for x in range(1,31)]
    schedule_81= pd.read_csv('./Data/81_game_schedule.csv', usecols = columns)
    schedule_110 = pd.read_csv('./Data/110_game_schedule.csv', usecols = columns)
    schedule_140 = pd.read_csv('./Data/140_game_schedule.csv', usecols = columns)
    schedule_162 = pd.read_csv('./Data/162_game_schedule.csv', usecols = columns)
    dataframes_names = [schedule_81, schedule_110, schedule_140, schedule_162]
    dataframes = []
    for df in dataframes_names:
        dataframes.append(df)
    return dataframes

def opp_win_pct():
    dataframes = get_schedule_df()
    opp_win_pct_dfs = []
    for df in dataframes:
        df = pd.DataFrame(df.mean(axis = 0))
        df.columns = ['Opp_Win_Pct']
        opp_win_pct_dfs.append(df)
    return opp_win_pct_dfs

def pct_of_games_against_500_teams():
    dataframes = get_schedule_df()
    pct_games_against_500_dfs = []
    for df in dataframes:
        pct_games_over_500 = pd.DataFrame(df[df >= 0.5].count()) / (len(df))
        pct_games_over_500.columns = ['PCT']
        pct_games_against_500_dfs.append(pct_games_over_500)
    return pct_games_against_500_dfs

def number_of_games_against_500_teams():
    dataframes = get_schedule_df()
    games_over_500_dfs = []
    for df in dataframes:
        games_over_500 = pd.DataFrame(df[df >= 0.5].count())
        games_over_500.columns = ['Games']
        games_over_500_dfs.append(games_over_500) 
    return games_over_500_dfs

 
# Plots for games against teams projected to finish over .500 for 81,110,140, and 162 game schedules
games_500 = number_of_games_against_500_teams()

# 82 game season
games_500_82_season = games_500[0]
games_500_82_season = games_500_82_season.sort_values(by = 'Games', ascending = False)
color_values = ['#0077c8', '#fdb827', '#fd5a1e', '#1d2d5c', '#33006f', '#7bb2dd', '#c4ced4', '#284898', '#c41e3a', '#212759', '#c6011f', '#df4601', '#0e3386', '#ce1141', 
    '#000000', '#c4ced3', '#b6922e', '#005a9c', '#c0111f', '#002d62', '#ff5910', '#182d55', '#862633', '#e31937', '#092c5c', '#3fc2cc', '#cfac7a', '#eb6e1f', 
    '#bd3039', '#003831'] 
color_keys = []
color_keys = games_500_82_season.index
color_dict = dict(zip(color_keys, color_values))
games_500_82_season['Colors'] = ""
games_500_82_season['Colors'].update(pd.Series(color_dict))
colors = list(games_500_82_season['Colors'].values)

fig = go.Figure(go.Bar(x = games_500_82_season['Games'], y = games_500_82_season.index, orientation = 'h', marker_color = colors  ))
fig.update_layout(autosize = False, height = 750, title_text = 'Games VS Opponents With .500 or Better Win Pct - 82 Game Season', 
            xaxis = dict(title = 'Games'), title_x = 0.5)
st.plotly_chart(fig)

# 110 game season
games_500_110_season = games_500[1]
games_500_110_season = games_500_110_season.sort_values(by = 'Games', ascending = False)

games_500_110_season['Colors'] = ""
games_500_110_season['Colors'].update(pd.Series(color_dict))
colors = list(games_500_110_season['Colors'].values)

fig = go.Figure(go.Bar(x = games_500_110_season['Games'], y = games_500_110_season.index, orientation = 'h', marker_color = colors  ))
fig.update_layout(autosize = False, height = 750, title_text = 'Games VS Opponents With .500 or Better Win Pct - 110 Game Season', 
            xaxis = dict(title = 'Games'), title_x = 0.5)
st.plotly_chart(fig)

# 140 game season
games_500_140_season = games_500[2]
games_500_140_season = games_500_140_season.sort_values(by = 'Games', ascending = False)

games_500_140_season['Colors'] = ""
games_500_140_season['Colors'].update(pd.Series(color_dict))
colors = list(games_500_140_season['Colors'].values)

fig = go.Figure(go.Bar(x = games_500_140_season['Games'], y = games_500_140_season.index, orientation = 'h', marker_color = colors  ))
fig.update_layout(autosize = False, height = 750, title_text = 'Games VS Opponents With .500 or Better Win Pct - 140 Game Season', 
            xaxis = dict(title = 'Games'), title_x = 0.5)
st.plotly_chart(fig)

# 162 game season
games_500_162_season = games_500[3]
games_500_162_season = games_500_162_season.sort_values(by = 'Games', ascending = False)

games_500_162_season['Colors'] = ""
games_500_162_season['Colors'].update(pd.Series(color_dict))
colors = list(games_500_162_season['Colors'].values)

fig = go.Figure(go.Bar(x = games_500_162_season['Games'], y = games_500_162_season.index, orientation = 'h', marker_color = colors  ))
fig.update_layout(autosize = False, height = 750, title_text = 'Games VS Opponents With .500 or Better Win Pct - 162 Game Season', 
            xaxis = dict(title = 'Games'), title_x = 0.5)
st.plotly_chart(fig)

# Plots for PCT of games against opponents with .500 or better projected record
pct_of_games_against_500_teams_dfs = pct_of_games_against_500_teams()

# 82 game season

pct_of_games_against_500_82 = pct_of_games_against_500_teams_dfs[0]
pct_of_games_against_500_82= pct_of_games_against_500_82.sort_values(by = 'PCT', ascending = False).round(2) * 100

pct_of_games_against_500_82['Colors'] = ""
pct_of_games_against_500_82['Colors'].update(pd.Series(color_dict))
colors = list(pct_of_games_against_500_82['Colors'].values)

fig = go.Figure(go.Bar(x = pct_of_games_against_500_82['PCT'], y = pct_of_games_against_500_82.index, orientation = 'h', marker_color = colors  ))
fig.update_layout(autosize = False, height = 750, title_text = 'Percentage of Games Against Teams Over .500 - 82 Game Season', 
            xaxis = dict(title = 'Percent'), title_x = 0.5)
st.plotly_chart(fig)

# 110 game season

pct_of_games_against_500_110 = pct_of_games_against_500_teams_dfs[1]
pct_of_games_against_500_110= pct_of_games_against_500_110.sort_values(by = 'PCT', ascending = False).round(2) * 100

pct_of_games_against_500_110['Colors'] = ""
pct_of_games_against_500_110['Colors'].update(pd.Series(color_dict))
colors = list(pct_of_games_against_500_110['Colors'].values)

fig = go.Figure(go.Bar(x = pct_of_games_against_500_110['PCT'], y = pct_of_games_against_500_110.index, orientation = 'h', marker_color = colors))
fig.update_layout(autosize = False, height = 750, title_text = 'Percentage of Games Against Teams Over .500 - 110 Game Season', 
            xaxis = dict(title = 'Percent'), title_x = 0.5)
st.plotly_chart(fig)

# 140 game season 

pct_of_games_against_500_140 = pct_of_games_against_500_teams_dfs[2]
pct_of_games_against_500_140= pct_of_games_against_500_140.sort_values(by = 'PCT', ascending = False).round(2) * 100

pct_of_games_against_500_140['Colors'] = ""
pct_of_games_against_500_140['Colors'].update(pd.Series(color_dict))
colors = list(pct_of_games_against_500_140['Colors'].values)

fig = go.Figure(go.Bar(x = pct_of_games_against_500_140['PCT'], y = pct_of_games_against_500_140.index, orientation = 'h', marker_color = colors))
fig.update_layout(autosize = False, height = 750, title_text = 'Percentage of Games Against Teams Over .500 - 140 Game Season', 
            xaxis = dict(title = 'Percent'), title_x = 0.5)
st.plotly_chart(fig)

# 162 game season

pct_of_games_against_500_162 = pct_of_games_against_500_teams_dfs[3]
pct_of_games_against_500_162= pct_of_games_against_500_162.sort_values(by = 'PCT', ascending = False).round(2) * 100

pct_of_games_against_500_162['Colors'] = ""
pct_of_games_against_500_162['Colors'].update(pd.Series(color_dict))
colors = list(pct_of_games_against_500_162['Colors'].values)

fig = go.Figure(go.Bar(x = pct_of_games_against_500_162['PCT'], y = pct_of_games_against_500_162.index, orientation = 'h', marker_color = colors))
fig.update_layout(autosize = False, height = 750, title_text = 'Percentage of Games Against Teams Over .500 - 162 Game Season', 
            xaxis = dict(title = 'Percent'), title_x = 0.5)
st.plotly_chart(fig)

# Plots for opponents combined winning percentage

opp_win_pct_dfs = opp_win_pct()

# 82 games season

opp_win_pct_82 = opp_win_pct_dfs[0]
opp_win_pct_82 = opp_win_pct_82.sort_values(by = 'Opp_Win_Pct', ascending = False).round(3)

opp_win_pct_82['Colors'] = ""
opp_win_pct_82['Colors'].update(pd.Series(color_dict))
colors = list(opp_win_pct_82['Colors'].values)

fig = go.Figure(go.Bar(x = opp_win_pct_82['Opp_Win_Pct'], y = opp_win_pct_82.index, orientation = 'h', marker_color = colors))
fig.update_layout(autosize = False, height = 750, title_text = 'Opponents Combined Win Pct - 82 Game Season', xaxis = dict(title = 'Win Pct'), title_x = 0.5)
st.plotly_chart(fig)

# 110 game season

opp_win_pct_110 = opp_win_pct_dfs[1]
opp_win_pct_110 = opp_win_pct_110.sort_values(by = 'Opp_Win_Pct', ascending = False).round(3)

opp_win_pct_110['Colors'] = ""
opp_win_pct_110['Colors'].update(pd.Series(color_dict))
colors = list(opp_win_pct_110['Colors'].values)


fig = go.Figure(go.Bar(x = opp_win_pct_110['Opp_Win_Pct'], y = opp_win_pct_110.index, orientation = 'h', marker_color = colors))
fig.update_layout(autosize = False, height = 750, title_text = 'Opponents Combined Win Pct - 110 Game Season', xaxis = dict(title = 'Win Pct'), title_x = 0.5)
st.plotly_chart(fig)

# 140 game season 

opp_win_pct_140 = opp_win_pct_dfs[2]
opp_win_pct_140 = opp_win_pct_140.sort_values(by = 'Opp_Win_Pct', ascending = False).round(3)

opp_win_pct_140['Colors'] = ""
opp_win_pct_140['Colors'].update(pd.Series(color_dict))
colors = list(opp_win_pct_140['Colors'].values)


fig = go.Figure(go.Bar(x = opp_win_pct_140['Opp_Win_Pct'], y = opp_win_pct_140.index, orientation = 'h', marker_color = colors))
fig.update_layout(autosize = False, height = 750, title_text = 'Opponents Combined Win Pct - 140 Game Season', xaxis = dict(title = 'Win Pct'), title_x = 0.5)
st.plotly_chart(fig)

# 162 game season

opp_win_pct_162 = opp_win_pct_dfs[3]
opp_win_pct_162 = opp_win_pct_162.sort_values(by = 'Opp_Win_Pct', ascending = False).round(3)

opp_win_pct_162['Colors'] = ""
opp_win_pct_162['Colors'].update(pd.Series(color_dict))
colors = list(opp_win_pct_162['Colors'].values)


fig = go.Figure(go.Bar(x = opp_win_pct_162['Opp_Win_Pct'], y = opp_win_pct_162.index, orientation = 'h', marker_color = colors))
fig.update_layout(autosize = False, height = 750, title_text = 'Opponents Combined Win Pct - 162 Game Season', xaxis = dict(title = 'Win Pct'), title_x = 0.5)
st.plotly_chart(fig)


