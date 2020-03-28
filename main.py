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
        pct_games_over_500 = (df[df >= 0.5].count()) / (len(df))
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


games_500_82_season = pd.DataFrame(games_500[0])
games_500_82_season = games_500_82_season.sort_values(by = 'Games', ascending = False).reset_index()