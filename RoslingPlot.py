# -*- coding: utf-8 -*-

# Modules

import plotly.express as px


# DataFrame

df = px.data.gapminder()


# Data Viz

# Emulation of Hans Rosling's most famous plot using plotly.

px.scatter(data_frame = df,
           x = 'gdpPercap',
           y= 'lifeExp',
           size = 'pop',
           color = 'continent',
           title = 'Global trend in terms of health and economics',
           # Meaningful labels
           labels = {'gdpPercap': 'per-capita GDP',
                     'lifeExp': 'life expectations'},
           # Log scale in x axis
           log_x = True,
           range_y = [25,95],
           # Country when hover over points
           hover_name = 'country',
           # Animation based on years
           animation_frame = 'year',
           height = 600,
           size_max = 100)

