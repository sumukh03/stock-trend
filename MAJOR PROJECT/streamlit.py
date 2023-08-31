import streamlit as st
import pandas as pd
from plotly import graph_objs as go
from prediction import make_prediction
from dates import generate_date_list
from datetime import date

tickers=["AAPL","GOOG","AMZN","WIT"]
selected_ticker=st.selectbox("Select Dataset for Prediction",tickers)

data_load_state=st.text("Load Data ...")
data=pd.read_csv(f"csv/{selected_ticker}")
data_load_state.text("Loading data Done!!")

st.subheader("Raw Data")
st.write(data.head())

def plot_raw_data(data):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"],y=data["Close"],name="stock_close"))
    # fig.layout.update(title_text="Time Series Data",xaxis_rangeslider_visible=True,yaxis_rangeslider_visible=True)
    fig.update_layout(
        dict(
            title="Time series with range slider and selectors",
            xaxis=dict(
                rangeselector=dict(
                    buttons=list(
                        [
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(count=6, label="6m", step="month", stepmode="backward"),
                            dict(count=1, label="YTD", step="year", stepmode="todate"),
                            dict(count=1, label="1y", step="year", stepmode="backward"),
                            dict(step="all"),
                        ]
                    )
                ),
                rangeslider=dict(visible=True),
                type="date",
            ),
        )
    )
    st.plotly_chart(fig)

plot_raw_data(data)

def plot_predicted(price,dates):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=dates,y=price,name="stock_close"))
    # fig.layout.update(title_text="Time Series Data",xaxis_rangeslider_visible=True,yaxis_rangeslider_visible=True)
    # fig.update_layout(
    #     dict(
    #         title="Time series with range slider and selectors",
    #         xaxis=dict(
    #             rangeselector=dict(
    #                 buttons=list(
    #                     [
    #                         dict(count=1, label="1m", step="month", stepmode="backward"),
    #                         dict(count=6, label="6m", step="month", stepmode="backward"),
    #                         dict(count=1, label="YTD", step="year", stepmode="todate"),
    #                         dict(count=1, label="1y", step="year", stepmode="backward"),
    #                         dict(step="all"),
    #                     ]
    #                 )
    #             ),
    #             rangeslider=dict(visible=True),
    #             type="date",
    #         ),
    #     )
    # )
    st.plotly_chart(fig)

#predicting 
number_of_days=365*5
last_100_values=pd.DataFrame(data["Close"]).tail(100)
print(last_100_values)
# predicted=make_prediction(selected_ticker,number_of_days=number_of_days,last_values=last_100_values)

TODAY=date.today().strftime("%Y-%m-%d")
print("today",TODAY)
dates=generate_date_list(TODAY,num_days=number_of_days)

plot_predicted(predicted,dates)


