import pandas as pd
import numpy as np
import plotly.offline as plt
import plotly.graph_objs as go

data = pd.read_csv('../data/athlete_events.csv')


def male_female_participants():
    gender_participants = data.groupby(by=['Year', 'Sex'], sort=True, as_index=False).size()
    male_participants = gender_participants.loc[:, 'M']
    female_participants = gender_participants.loc[:, 'F']

    plot_figure = go.Figure(data=[
        go.Scatter(x=male_participants.index, y=male_participants.values, name='Male Participants', mode='lines+markers',
                   marker={'color': '#FFFFFF'}),
        go.Scatter(x=female_participants.index, y=female_participants.values, name='Female Participants', mode='lines+markers',
                   marker={'color': '#FFB300'})],
        layout=go.Layout(plot_bgcolor='#212121', paper_bgcolor='#212121'))

    plt.plot(plot_figure, filename='../plots/male_female_participants.html')


def country_medals():
    medal_df = data.groupby(by=['Medal', 'NOC']).size()

    fig = go.Figure([
        go.Choropleth(locations=medal_df.loc['Gold'].index, z=medal_df.loc['Gold'].values, colorscale='YlOrRd',
                      geo='geo3', showscale=False, name='Gold Medals', reversescale=True),
        go.Choropleth(locations=medal_df.loc['Silver'].index, z=medal_df.loc['Silver'].values, colorscale='Blues',
                      geo='geo2', showscale=False, name='Silver Medals', reversescale=True),
        go.Choropleth(locations=medal_df.loc['Bronze'].index, z=medal_df.loc['Bronze'].values, colorscale='Reds',
                      geo='geo1', showscale=False, name='Bronze Medals')
    ])

    fig.layout.update(
        height=2000,
        title='Gold, Silver and Bronze Medals',
        paper_bgcolor='#212121',
        font=dict(color='#FFFFFF'),
        geo1=dict(bgcolor='#212121'),
        geo2=dict(bgcolor='#212121'),
        geo3=dict(bgcolor='#212121'),
    )

    plt.plot(fig, filename='../plots/country_medals.html')


def sports_highest_participants():
    participants = data.groupby(by=['Year', 'Sport']).size().groupby(level=0).nlargest(5).droplevel(0).to_frame().reset_index()
    years = ['Year ' + str(yr) for yr in participants['Year'].unique()]

    participants = participants.groupby(by='Year')

    colors = ['#004D40', '#00897B', '#4DB6AC', '#B2DFDB', '#E0F2F1']

    fig = go.Figure(
        [go.Barpolar(r=participants.nth(i)[0], name='', text=participants.nth(i)['Sport'], marker_color=colors[i], theta=years)
         for i in range(4, -1, -1)],
        go.Layout(height=1000, title='Top 5 popular sports in Olympic History',
                  polar_bgcolor='#212121', paper_bgcolor='#212121',
                  font_size=15, font_color='#FFFFFF',
                  polar=dict(radialaxis=dict(visible=False)))
    )

    plt.plot(fig, filename='../plots/highest_participants.html')
