# Task 3: Interactive Visualizations with Plotly

# Load the Plotly wind dataset
# Print the first and last 10 lines of the DataFrame.
# Clean the data. 
# Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
# Save and load the HTML file, as wind.html. Verify that the plot works correctly.

import plotly.express as px
import plotly.data as pldata


df = pldata.wind(return_type='pandas') 

print(df.head(10))
print(df.tail(10))

df['strength'] = df['strength'].str.replace(r'.*\-','',regex=True) #keep only the string after the -
df['strength'] = df['strength'].str.replace(r'\D','',regex=True) #keep only the digits


df['strength'] =df['strength'].astype('float')




fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Data", hover_data=["strength"])
fig.write_html("wind.html", auto_open=True)