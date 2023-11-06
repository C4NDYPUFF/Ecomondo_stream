import plotly_express as px
import pandas as pd

# Function to plot the top ten important items based on a column
def plot_ten_important(df, column):
    value_counts = df[column].value_counts()
    percentage = df[column].value_counts(normalize=True) * 100
    result = pd.DataFrame({'Counts': value_counts, 'Percentage': percentage}).reset_index()
    result.rename(columns={'index': column}, inplace=True)
    result = result.sort_values(by='Counts', ascending=False)
    result10 = result.head(10)
    return result10

# Function to create and display pie charts
def create_pie_chart(data, names, values, title, color_sequence):
    fig = px.pie(data, names=names, values=values, title=title, color_discrete_sequence=color_sequence)
    return fig

# Function to create and display bar charts
def create_bar_chart(data, x, y, text, color, title):
    fig = px.bar(data, y=y, x=x, text=text, color=color, title=title)
    fig.update_layout(xaxis_title='Registros', yaxis_title=y, yaxis=dict(showticklabels=False),
                      xaxis={'categoryorder':'total descending'}, uniformtext_minsize=8, uniformtext_mode='hide')
    return fig