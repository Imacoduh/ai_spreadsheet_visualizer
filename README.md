# AI-Powered Spreadsheet Data Visualizer

This is a Streamlit application that allows users to upload spreadsheet files (CSV, XLS, XLSX) and visualize the data using various plot types (scatter plot, line plot, and bar chart). Additionally, the application leverages the OpenAI language model to generate insights and recommendations based on the uploaded data.

## Features

- File uploader to load spreadsheet data (CSV, XLS, XLSX)
- Data preview and visualization options:
 - Scatter plot
 - Line plot
 - Bar chart
- AI-generated insights and recommendations using OpenAI's language model

## Technologies Used
- Python
- Streamlit
- OpenAI
- Pandas
- Langchain
- Plotly

## Installation

1. Clone the repository or download the source code.
2. Install the required Python packages: streamlit, pandas, plotly, langchain, openai
3. Set up your OpenAI API key as an environment variable:

## Usage

1. Run the Streamlit application: streamlit run app.py
2. Upload your spreadsheet file using the file uploader in the sidebar.
3. Select the desired visualization type (scatter plot, line plot, or bar chart) and choose the appropriate columns for the x and y axes.
4. The application will display the data preview, visualization plot, and AI-generated insights based on the uploaded data.

## Contributing

Contributions are welcome! If you find any issues or would like to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).