import streamlit as st
import yfinance as fn
st.write(""" My first App  """)
st.title("Stock Market App with streamlit")
st.header("Simple data science web app")
st.sidebar.header("Bek Brace \n Code along with me...")
# This is a function that fetches the company's ticker 
def get_ticker(name):
	company=fn.Ticker(name)
	return company

c1=get_ticker("AAPL")
c2=get_ticker("MSFT")
c3=get_ticker("TSLA")

apple=fn.download("AAPL",start="2021-11-11",end="2022-11-11")
microsoft=fn.download("MSFT",start="2021-11-11",end="2022-11-11")
tesla=fn.download("TSLA",start="2021-11-11",end="2022-11-11")

data1=c1.history(period="3mo")
data2=c2.history(period="3mo")
data3=c3.history(period="3mo")

st.write("""## Apple""")
st.write(c1.info['longBusinessSummary'])
st.write(apple)
st.line_chart(data1.values)
st.write("""## Microsoft""")
st.write(c2.info['longBusinessSummary'])
st.write(microsoft)
st.line_chart(data2.values)
st.write("""## Tesla""")
st.write(c3.info['longBusinessSummary'])
st.write(tesla)
st.line_chart(data3.values)