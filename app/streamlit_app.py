# To be filled by students
import streamlit as st

def launchApp():
    

    header = st.container()
    studentA = st.container()
    studentB = st.container()
    studentC = st.container()
    studentD = st.container()

    with header:
        st.title('DSP Assignment 3')

    with studentA:
        st.header('Overall Information')

    with studentB:
        st.header('Information on each numeric column')

    with studentC:
        st.header('Information on each text column')

    with studentD:
        st.header('Information on each datetime column')
    
    return