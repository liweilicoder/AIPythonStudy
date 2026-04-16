import csv
import pandas as pd
from IPython.display import display, HTML

def display_table(data):
    df = pd.DataFrame(data)

    # Display the DataFrame as an HTML table
    display(HTML(df.to_html(index=False)))
