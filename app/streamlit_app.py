# To be filled by students
import streamlit as st
import pandas as pd
from .. import src

#containers for each group members section

@st.cache(allow_output_mutation=True)
def load_csv(csv_file):
    df = pd.read_csv(csv_file)
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
            file_details = {"filename":csv_file.name, 
            "filetype":csv_file.type,
            "filesize":csv_file.size}
            st.write(file_details)

            df = load_csv(csv_file)

    #1. 'Overall Information of the Dataset' Section
    with studentA:
        #overall information header
        st.header('Overall Information')
        st.subheader('Section by Lachlan Denham')

        st.markdown('**Name of Table:** ')
        st.markdown('**Number of Rows:** ')
        st.markdown('**Number of Columns:** ')
        st.markdown('**Number of Duplicated Rows:** ')
        st.markdown('**Number of Rows with Missing Values:** ')
        st.markdown('**List of Columns:** ')
        if csv_file is not None:
            st.text(list(df.columns))
        st.markdown('**Type of Columns:** ')

    with studentB:
        st.header('Information on each numeric column')

    with studentC:
        st.header('Information on each text column')

    with studentD:
        st.header('Information on each datetime column')
    
    return