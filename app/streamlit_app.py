# To be filled by students
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import streamlit as st
import pandas as pd
from src.data import Dataset
from src.text import TextColumn
from src.datetime import DateColumn
from src.numeric import NumericColumn


#Function for adding the uploaded dataset to the webpage cache
@st.cache(allow_output_mutation=True)
def load_csv(csv_file):
    ds = Dataset(csv_file.name, pd.read_csv(csv_file))
    return ds

def launchApp():




    #Initialising containers
    header = st.container()
    studentA = st.container()
    studentB = st.container()
    studentC = st.container()
    studentD = st.container()




    #Page title Container
    with header:
        st.title('Data Explorer Web Application')
        st.write('**Developed by Group 15 for Data Science Practice Assignment 3**')
        st.write('This web app is designed to perform exploratory data analysis on a dataset (CSV files only) provided by the user. The analyses produce information in four key sections; the overall dataset, numeric data, text data and datetime data.')
        st.write(' ')

        #File uploader widget which is restricted to csv filetypes
        csv_file = st.file_uploader("Choose a CSV file", type=['csv'])

        #displaying uploaded file information
        if csv_file is not None:
            ds = load_csv(csv_file)



    #1. 'Overall Information of the Dataset' Section
    with studentA:

        #Overall Information Header
        st.header('Overall Information')
        st.subheader('Section by Lachlan Denham')



        #Page display elements when a CSV file has been uploaded and is accessible
        if csv_file is not None:

            #Denotes overall dataset information using bold markdown text.
            #Also displays the corresponding answers in standard text format through calls to dataclass elements.
            st.markdown('**Name of Table:** ' + ds.get_name())
            st.markdown('**Number of Rows:** ' + str(ds.get_n_rows()))
            st.markdown('**Number of Columns:** ' + str(ds.get_n_cols()))
            st.markdown('**Number of Duplicated Rows:** ' + str(ds.get_n_duplicates()))
            st.markdown('**Number of Rows with Missing Values:** ' + str(ds.get_n_missing()))

            st.markdown('**List of Columns:** ')

            column_names = list(ds.get_cols_list())

            bracketless_column_names = (', '.join(repr(e) for e in column_names))
            column_names_clean = bracketless_column_names.replace("'", "")
            st.text(column_names_clean)

            #Denotes the column types and displays the relevant information in a dataframe visual element
            st.markdown('**Type of Columns:** ')
            st.dataframe(ds.get_cols_dtype().astype(str), 400, 500)

            #Displays Row samples taken from the beginning, end and randomly from each respective visual element.
            #Implements a slider to determine how many dataframe rows should be displayed in each element.
            rowNumberSlider = st.slider('Select the number of rows to be displayed', value=5)
            st.markdown('**Top Rows of Table**')
            st.dataframe(ds.get_head(rowNumberSlider))
            st.markdown('**Bottom rows of Table**')
            st.dataframe(ds.get_tail(rowNumberSlider))
            st.markdown('**Random Sample Rows of Table**')
            st.dataframe(ds.get_sample(rowNumberSlider))

            #Implements a streamlit selectbox to select a column to be converted into datetime format
            #Utilises a button element to confirm conversion, followed an element rerun to display the converted elements.
            conversionSelect = st.selectbox('Which columns do you want to convert to dates', ds.get_cols_list())
            st.write('Current selection: ' + conversionSelect)
            convertButton = st.button('Convert Selected Column')
            if convertButton:
                ds.df[conversionSelect] = pd.to_datetime(ds.df[conversionSelect].astype(str), infer_datetime_format=True)
                st.experimental_rerun()

        #Page display elements when no CSV file is accessible.
        #Largely repeats elements found in the above code without the necessary function calls to dataclass elements

        #else:
        #    st.markdown('**Name of Table:** ')
        #    st.markdown('**Number of Rows:** ')
        #    st.markdown('**Number of Columns:** ')
        #    st.markdown('**Number of Duplicated Rows:** ')
        #    st.markdown('**Number of Rows with Missing Values:** ')
        #    st.markdown('**List of Columns:** ')
        #    st.markdown('**Type of Columns:** ')
        #    st.slider('Select the number of rows to be displayed', value=5)
        #    st.markdown('**Top Rows of Table**')
        #    st.markdown('**Bottom rows of Table**')
        #    st.markdown('**Random Sample Rows of Table**')
        #    st.selectbox('Which columns do you want to convert to dates', ['N/A'])
        #    st.button('Convert Selected Column')
        else:
            st.write('No dataset provided, please input CSV file.')
            st.write(' ')



    with studentB:
        st.header('Information on each numeric column')
        st.subheader('Section by Amelia Craigie')

        if csv_file is not None:
            num_select = st.selectbox('Select a numeric column to explore:', ds.get_numeric_columns())

            if num_select is not None:
                st.markdown('')
                st.markdown('**Field Name: *' + num_select + '* **')

                num_serie = NumericColumn(num_select, ds.get_series(num_select))
                text_col1, text_col2 = st.columns(2)

                with text_col1:
                    st.write('Number of Unique Values:')
                    st.write('Number of Rows with Missing Values:')
                    st.write('Number of Rows with 0 Value:')
                    st.write('Number of Rows with Negative Value:')
                    st.write('Average Value:')
                    st.write('Std. Dev. Value:')
                    st.write('Minimum Value:')
                    st.write('Maximum Value:')

                with text_col2:
                    st.write(num_serie.get_unique())
                    st.write(num_serie.get_missing())
                    st.write(num_serie.get_zeros())
                    st.write(num_serie.get_negatives())
                    st.write(num_serie.get_mean())
                    st.write(num_serie.get_std())
                    st.write(num_serie.get_min())
                    st.write(num_serie.get_max())

                st.markdown('')
                st.markdown('**Histogram: **')
                num_serie.get_histogram()

                st.markdown('')
                st.markdown('**Top 20 Frequent Values**')
                st.table(num_serie.get_frequent())
        else:
            st.write('No dataset provided, please input CSV file.')
            st.write(' ')



    with studentC: # Declan
        st.header('3. Text Column Information')
        st.subheader('Section by Declan Stockdale')

        if csv_file is not None:

            '''
            Section allows for conversion of non string/text/object datatypes to string

            conversionSelect = st.selectbox('Which columns do you want to convert to text',ds.get_not_text_columns())
            st.write('Current selection: ' + conversionSelect)
            convertButton = st.button('Convert Selected Column to string')
            if convertButton:
                ds.df[conversionSelect] = ds.df[conversionSelect].apply(str)
                st.experimental_rerun()
            '''

            i = 0
            for col_name in ds.get_text_columns():
                st.markdown('')
                subheader_str = (f"3.{i} Field Name: _{col_name}_")
                st.subheader(subheader_str)

                txt_serie = TextColumn(col_name, ds.get_series(col_name))

                df1 = pd.DataFrame({'Value': [txt_serie.get_unique(),
                                              txt_serie.get_missing(),
                                              txt_serie.get_empty(),
                                              txt_serie.get_whitespace(),
                                              txt_serie.get_lowercase(),
                                              txt_serie.get_uppercase(),
                                              txt_serie.get_alphabet(),
                                              txt_serie.get_digit(),
                                              txt_serie.get_mode()[0]]},
                                  index=['Number of Unique Values',
                                         'Number of Rows with Missing Values',
                                         'Number of Empty rows',
                                         'Number of Rows with only whitespaces',
                                         'Number of Rows with only lower case characters',
                                         'Number of Rows with only upper case characters',
                                         'Number of Rows with only alphabet characters',
                                         'Number of rows with only numbers as characters',
                                         'Mode value'])

                df1 = df1.astype(str)
                st.dataframe(df1.style.set_properties(**{'text-align': 'right'}).hide_index())

                st.markdown('')
                st.markdown('**Bar Chart**')
                txt_serie.get_barchart(col_name)

                st.markdown('')
                st.markdown('**Most Frequent Values**')
                st.table(txt_serie.get_frequent())

                i = i+1
        else:
            st.write('No dataset provided, please input CSV file.')
            st.write(' ')

    with studentD:
        st.header('Information on each datetime column')
        st.subheader('Section by Ivan Cheung')
        #check if csv has been loaded. Only display this section if csv_file is not None.
        if csv_file is not None:

            option = st.selectbox('Select a <Datetime> column to explore:', ds.get_date_columns())

            #check if a datetime colum has been selected
            if option is not None:
                st.markdown('')
                st.markdown('**Field Name: *' + option + '* **')
                #create the data series from the selected option
                date_serie = DateColumn(option, ds.get_series(option))


                #print table of basic information for this column
                date_col1, date_col2 = st.columns(2)

                with date_col1:
                    st.write('Number of Unique Values:')
                    st.write('Number of Rows with Missing Values:')
                    st.write('Number of Weekend Dates:')
                    st.write('Number of Weekday Dates:')
                    st.write('Number of Dates in Future:')
                    st.write('Number of Rows with 1900-01-01:')
                    st.write('Number of Rows with 1970-01-01:')
                    st.write('Minimum Value:')
                    st.write('Maximum Value:')

                #call datetime information from datetime functions
                with date_col2:
                    st.write(date_serie.get_unique())
                    st.write(date_serie.get_missing())
                    st.write(date_serie.get_weekend())
                    st.write(date_serie.get_weekday())
                    st.write(date_serie.get_future())
                    st.write(date_serie.get_empty_1900())
                    st.write(date_serie.get_empty_1970())
                    st.write(date_serie.get_min())
                    st.write(date_serie.get_max())

                st.markdown('')
                st.markdown('**Bar Chart**')
                date_serie.get_barchart()


                st.markdown('')
                st.markdown('**Most Frequent Values**')
                st.table(date_serie.get_frequent())

        else:
            st.write('No dataset provided, please input CSV file.')
            st.write(' ')



    return
