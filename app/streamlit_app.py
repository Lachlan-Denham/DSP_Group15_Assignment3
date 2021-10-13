# To be filled by students
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import streamlit as st
import pandas as pd
from src.data import Dataset

#containers for each group members section

@st.cache(allow_output_mutation=True)
def load_csv(csv_file):
    df = Dataset(csv_file.name, pd.read_csv(csv_file))
    return df

def launchApp():
    
    #Initialising containers
    header = st.container()
    studentA = st.container()
    studentB = st.container()
    studentC = st.container()
    studentD = st.container()

    #Page title Container
    with header:
        st.title('DSP Assignment 3')

        #File uploader widget which is restricted to csv filetypes
        csv_file = st.file_uploader("Choose a CSV file", type=['csv'])

        #displaying uploaded file information
        if csv_file is not None:
            df = load_csv(csv_file)

    #1. 'Overall Information of the Dataset' Section
    with studentA:
        #overall information header
        st.header('Overall Information')
        st.subheader('Section by Lachlan Denham')

        if csv_file is not None:
            st.markdown('**Name of Table:** ' + df.get_name())
            st.markdown('**Number of Rows:** ' + str(df.get_n_rows()))
            st.markdown('**Number of Columns:** ' + str(df.get_n_cols()))
            st.markdown('**Number of Duplicated Rows:** ' + str(df.get_n_duplicates()))
            st.markdown('**Number of Rows with Missing Values:** ' + str(df.get_n_missing()))
            st.markdown('**List of Columns:** ')
            st.text(df.get_cols_list())
            st.markdown('**Type of Columns:** ')
            st.dataframe(df.get_cols_dtype().astype(str), 400, 500)
            rowNumberSlider = st.slider('Select the number of rows to be displayed')
            st.markdown('**Top Rows of Table**')
            st.dataframe(df.get_head(rowNumberSlider))
            st.markdown('**Bottom rows of Table**')
            st.dataframe(df.get_tail(rowNumberSlider))
            st.markdown('**Random Sample Rows of Table**')
            st.dataframe(df.get_sample(rowNumberSlider))
            conversionSelect = st.selectbox('Which columns do you want to convert to dates', df.get_cols_list())
            st.write('Current selection: ' + conversionSelect)
            convertButton = st.button('Convert Selected Column')
            if convertButton:
                df.df[conversionSelect] = pd.to_datetime(df.df[conversionSelect])
                st.experimental_rerun()
        else:
            st.markdown('**Name of Table:** ')
            st.markdown('**Number of Rows:** ')
            st.markdown('**Number of Columns:** ')
            st.markdown('**Number of Duplicated Rows:** ')
            st.markdown('**Number of Rows with Missing Values:** ')
            st.markdown('**List of Columns:** ')
            st.markdown('**Type of Columns:** ')
            st.slider('Select the number of rows to be displayed')
            st.markdown('**Top Rows of Table**')
            st.markdown('**Bottom rows of Table**')
            st.markdown('**Random Sample Rows of Table**')
            st.selectbox('Which columns do you want to convert to dates', ['N/A'])
            st.button('Convert Selected Column')

            
        

    with studentB:
        st.header('Information on each numeric column')

    with studentC:
        st.header('Information on each text column')

    with studentD:
        st.header('Information on each datetime column')
    
    return