import streamlit as st
import pandas as pd
import plotly.express as px
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import os
os.environ["OPENAI_API_KEY"] = "ENTER API KEY HERE"

def load_data(file):
    # Load data
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file)
    else:
        st.error('Unsupported file format')
        return None
    return df

def generate_insights(df):
    # Set up the OpenAI LLM
    llm = OpenAI(temperature=0.7)

    # Define the prompt template
    prompt = PromptTemplate(
        input_variables=["data_description"],
        template="Provide insights and recommendations based on the following data description:\n\n{data_description}"
    )

    # Create the LLM chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Generate insights using the LLM
    data_description = df.describe().to_string()
    insights = chain.run(data_description)

    return insights

def main():
    st.title('AI-Powered Spreadsheet Data Visualizer')

    # File uploader
    st.sidebar.title('Upload Spreadsheet')
    file = st.sidebar.file_uploader('Upload your spreadsheet', type=['csv', 'xls', 'xlsx'])

    if file is not None:
        st.sidebar.success('File successfully uploaded')

        # Load data
        df = load_data(file)

        if df is not None:
            st.write('### Data Preview')
            st.write(df.head())

            st.write('### Data Visualization')
            st.sidebar.subheader('Select Visualization')
            visualization_type = st.sidebar.selectbox('Choose Visualization Type', ['Scatter Plot', 'Line Plot', 'Bar Chart'])

            if visualization_type == 'Scatter Plot':
                x_column = st.sidebar.selectbox('Choose X-axis data', df.columns)
                y_column = st.sidebar.selectbox('Choose Y-axis data', df.columns)
                fig = px.scatter(df, x=x_column, y=y_column, title='Scatter Plot')
                st.plotly_chart(fig)
            elif visualization_type == 'Line Plot':
                x_column = st.sidebar.selectbox('Choose X-axis data', df.columns)
                y_column = st.sidebar.selectbox('Choose Y-axis data', df.columns)
                fig = px.line(df, x=x_column, y=y_column, title='Line Plot')
                st.plotly_chart(fig)
            elif visualization_type == 'Bar Chart':
                x_column = st.sidebar.selectbox('Choose X-axis data', df.columns)
                y_column = st.sidebar.selectbox('Choose Y-axis data', df.columns)
                fig = px.bar(df, x=x_column, y=y_column, title='Bar Chart')
                st.plotly_chart(fig)

            st.write('### AI-Generated Insights')
            insights = generate_insights(df)
            st.write(insights)

if __name__ == "__main__":
    main()