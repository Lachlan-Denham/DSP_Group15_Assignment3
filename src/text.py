import streamlit as st
from dataclasses import dataclass
import pandas as pd
import altair as alt


@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series

  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name

  def get_unique(self):
    """
    Return number of unique values for selected column
    """
    return self.serie.nunique()

  def get_missing(self):
    """
    Return number of missing values for selected column
    """
    return self.serie.isna().sum()

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """
    return self.serie.isnull().sum()

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    return self.serie.str.isspace().sum()

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    return self.serie.str.islower().sum()

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    return self.serie.str.isupper().sum()

  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    return self.serie.str.isalpha().sum()

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    return self.serie.str.isdigit().sum()

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    return self.serie.mode()[0]


  def get_barchart(self):
    """
    Return the generated bar chart for selected column  - bar chart is sorted
    """

    df = self.serie.value_counts().reset_index() # works
    df.columns = ['Value', 'Number of Occurances']

    chart = alt.Chart(df).mark_bar().encode(
        x = alt.X('Value', sort=alt.EncodingSortField(field="Number of Occurances", op="count", order='ascending')),
        y = alt.Y('Number of Occurances',axis=alt.Axis(tickMinStep=1)) # added tick
        )
    return st.altair_chart(chart, use_container_width=True)

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    n = 20
    df = self.serie.value_counts().reset_index()
    df.columns = ['Value', 'Occurance']

    df['Percentage %'] = (df['Occurance'] / df['Occurance'].sum()) * 100
    return df.head(n)