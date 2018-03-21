# Creating a plotly world visualisation for the books and countries I have read so far. 
# colour scales from http://colorbrewer2.org

import pandas as pd
import plotly.plotly as py


# Import book data
df = pd.read_csv('book_count_rec.csv', dtype = {'country_name': str, \
'book_count': int, 'iso_code': str, 'recommended_author': str, \
'recommended_title': str})

# Specify text to be displayed when hovering over a country I have read
df['text'] = df['country_name'] + '<br>' + 'Author: ' + df['recommended_author'] +\
'<br>' + 'Title: ' + df['recommended_title']

# Specify data properties 
data = [ dict(
        type = 'choropleth',
        locations = df['iso_code'],
        z = df['book_count'],
        text = df['text'],
        colorscale = [[0,"rgb(247,251,255)"],[0.01,"rgb(198,219,239)"],\
        [0.05,"rgb(158,202,225)"], [0.10,"rgb(107,174,214)"],\
        [0.20,"rgb(66,146,198)"],[0.50,"rgb(33,113,181)"],[1,"rgb(8,48,107)"]],
        autocolorscale = False,
        reversescale = False,
        marker = dict(
            line = dict (
                color = 'rgb(127,127,127)',
                width = 0.5
            ) ),
      ) ]

# Specify layout properties
layout = dict(
    title = 'Number of books read per country',
    geo = dict(
        showframe = False,
        showcoastlines = True,
        coastlinecolor = 'rgb(180,180,180)',
        coastlinewidth = 0.5,
        showland = True,
        landcolor = "rgb(247,251,255)",
        showcountries = True,
        countrycolor = "rgb(247,251,255)",
        countrywidth = 0.5,
        projection = dict(
            type = 'orthographic'
        )
    )
)

# define plot source
fig = dict( data=data, layout=layout )

# plot directly to plotly 
py.plot( fig, validate=False, filename='book-world-map' )
