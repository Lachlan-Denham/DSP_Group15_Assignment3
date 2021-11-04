import unittest

from pandas.core.frame import DataFrame
from .. import text
import pandas as pd



test_csv = "C:/Users/Declan/Downloads/food-consumption.csv"
df = pd.read_csv(test_csv)
ds = data.Dataset(test_csv,df)

class TextColumn(unittest.TestCase):

     def test_get_name(self):

         result = ds.get_name()
         expected = df.col_name

         self.assertEqual(result, expected)


     def test_get_unique(self):

         result = ds.get_unique()
         expected = df.serie.nunique()

         self.assertEqual(result, expected)

     def test_get_missing(self):

         result = ds.get_missing()
         expected = df.isna().sum()

         self.assertEqual(result, expected)

     def test_get_empty(self):

         result = ds.get_empty()
         expected = df.isnull().sum()

         self.assertEqual(result, expected)

     def test_get_whitespace(self):

         result = ds.get_whitespace()
         expected = df.str.isspace().sum()

         self.assertEqual(result, expected)

     def test_get_lowercase(self):

         result = ds.get_lowercaase()
         expected = df.str.islower().sum()

         self.assertEqual(result, expected)

     def test_get_uppercase(self):

         result = ds.get_uppercase()
         expected = df.str.isupper().sum()

         self.assertEqual(result, expected)

     def test_get_alphabet(self):

         result = ds.get_alphabet()
         expected = df.str.isalpha().sum()

         self.assertEqual(result, expected)

     def test_get_digit(self):

         result = ds.get_digit()
         expected = df.str.isdigit().sum()

         self.assertEqual(result, expected)


     def test_get_mode(self):

         result = df.get_mode()
         expected = ds.mode()

         self.assertEqual(result, expected)


     def test_get_barchart(self, col_name):

         result = str(type(get_barchart()))
         expected = str("<class 'altair.vegalite.v4.api.Chart'>")

         self.assertEqual(result, expected)

     def test_get_frequent(self):

        self.assertEqual(ds.get_head(), df.head())
