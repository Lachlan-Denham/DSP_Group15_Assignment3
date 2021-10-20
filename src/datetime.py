# To be filled by students
import streamlit as st
import altair as alt
from dataclasses import dataclass
import pandas as pd


@dataclass
class DateColumn:
  col_name: str
  serie: pd.Series

  def get_series(self):
    return self.serie

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

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    df = self.serie.dt.dayofweek
    return df.isin([5,6]).sum()

  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    df = self.serie.dt.dayofweek
    return df.isin([0,1,2,3,4]).sum()
  
  def get_future(self):
    """
    The dates in the series are evaluated by the pandas function .to_datetime('today')
    to return a new series containing only dates which are greater than this date.
    the size of the series is then counted to get the output.

    Return number of cases with future dates (after today)
    """
    ds = self.serie
    df = ds[ds > pd.to_datetime("today")]
    return df.size

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    ds = self.serie
    df = ds[ds == pd.Timestamp(1900,1,1)]
    return df.size

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    ds = self.serie
    df = ds[ds == pd.Timestamp(1970,1,1)]
    return df.size

  def get_min(self):
    """
    Return the minimum date
    """
    return self.serie.min()

  def get_max(self):
    """
    Return the maximum date 
    """
    return self.serie.max()

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """

    df = self.serie.value_counts().reset_index()
    df.columns = ['Date', 'Number of Occurances']
    
    chart = alt.Chart(df).mark_bar().encode(
        x= alt.X('Date', title= self.col_name),
        y='Number of Occurances'
    )

    return st.altair_chart(chart, use_container_width=True)

  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    df = self.serie.value_counts().reset_index()
    df.columns = ['date', 'occurance']

    df['percentage'] = (df['occurance'] / df['occurance'].sum()) * 100
    return df