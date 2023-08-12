import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pandas as pd


#Author: SHAREN RAJENTHIRAN

# Import data
df = pd.read_csv('epa-sea-level.csv')

def draw_scatterplot():
    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],label='Data from epa sea level')
    # Create first best fit line
    line_A = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    Array_x_A = np.arange(df['Year'].min(),2050)
    Array_y_A = Array_x_A*line_A.slope + line_A.intercept
    plt.plot(Array_x_A,Array_y_A, color='Red', label='First best fit line')
    # Create second best fit line
    year_2000_above_data = df[df['Year']>=2000]
    line_B = linregress(year_2000_above_data['Year'], year_2000_above_data['CSIRO Adjusted Sea Level'])
    Array_x_B = np.arange(2000,2050)
    Array_y_B = Array_x_B*line_B.slope +line_B.intercept
    fig = plt.plot(Array_x_B,Array_y_B, color='Purple', label='Second best fit line')
    plt.title('Rise in Sea Level'), plt.ylabel('Sea Level (inches)'), plt.xlabel('Year')
    plt.legend(loc='upper left')
    plt.savefig('sea_level_plot.png')
    return fig

draw_scatterplot()