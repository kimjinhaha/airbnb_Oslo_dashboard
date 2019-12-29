import pandas as pd
import plotly.graph_objs as go

# let's extract date variables from date column
def extract_date(df, column):
    df[column] =  pd.to_datetime(df[column])
    df[column+'_year'] = df[column].apply(lambda x: x.year)
    df[column+'_month'] = df[column].apply(lambda x: x.month)
    df[column+'_day'] = df[column].apply(lambda x: x.day)
    df[column+'_dayofweek'] = df[column].apply(lambda x: x.strftime('%A'))
    return df

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart showing yearly growth in Oslo listing market
    reviews_raw = pd.read_csv('data/reviews.csv')
    reviews = extract_date(reviews_raw, 'date')
    df1 = pd.DataFrame(reviews['date_year'].value_counts())

    graph_one = []    
    graph_one.append(
        go.Scatter(
            x = df1.index.tolist(),
            y = df1.date_year.tolist(),
            mode = 'markers'            
        )
    )
    
    layout_one = dict(title = 'Yearly growth in Oslo listing market',
            xaxis = dict(title = 'Year'),
            yaxis = dict(title = 'The number of reviews'),
            )


# second chart plots monthly reviews   
    df2 = pd.DataFrame(reviews['date_month'].value_counts())

    graph_two = []

    graph_two.append(
      go.Bar(
          x = df2.index.tolist(),
          y = df2.date_month.tolist()
      )
    )

    layout_two = dict(title = 'Monthly number of reviews',
                xaxis = dict(title = 'Month',),
                yaxis = dict(title = 'The number of reviews'),
                )


# third chart plots the number of listings per neighborhood
    listings = pd.read_csv('data/listings.csv')
    df3 = pd.DataFrame(listings.neighbourhood.value_counts())
    
    graph_three = []
    graph_three.append(
      go.Bar(
          x = df3.index.tolist(),
          y = df3.neighbourhood.tolist(),
      )
    )

    layout_three = dict(title = 'The number of listings per neighborhood',
                xaxis = dict(automargin = True, title = 'Neighborhood'),
                yaxis = dict(title = 'The number of listings')
                       )
    
# fourth chart average price per neighbourhood
    df4 = pd.DataFrame(listings.groupby(['neighbourhood'])['price'].mean())
    
    graph_four = []
    
    graph_four.append(
      go.Bar(
          x = df4.index.tolist(),
          y = df4.price.tolist()
      )
    )

    layout_four = dict(title = 'Average price per neighborhood',
                xaxis = dict(automargin = True, title = 'Neighborhood'),
                yaxis = dict(title = 'Average price'),
                )
    

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures

