import streamlit as st
import plotly.graph_objects as go
import mt5_interface


# Function to define the CoPilot User Interface
def start_copilot_user_interface(symbol, timeframe):
    # Start the CoPilot
    try:
        # Get the historical data
        candles = get_historical_data(symbol=symbol, timeframe=timeframe, number_of_candles=1000)
    except Exception as exception:
        st.write(f"Error starting CoPilot. Error: {exception}")
        raise ConnectionAbortedError(f"Error starting CoPilot. Error: {exception}")
    # Construct the candlestick chart
    try:
        figure = construct_candlestick_chart(candles)
    except Exception as exception:
        st.write(f"Error constructing candlestick chart. Error: {exception}")
        raise ConnectionAbortedError(f"Error constructing candlestick chart. Error: {exception}")
    # Display the candlestick chart
    try:
        st.plotly_chart(figure)
    except Exception as exception:
        st.write(f"Error displaying candlestick chart. Error: {exception}")
        raise ConnectionAbortedError(f"Error displaying candlestick chart. Error: {exception}")
    # Return True if successful
    return True


# Function to Construct a Candlestick Chart
def construct_candlestick_chart(candles):
    # Construct the candlestick chart
    try:
        candlestick = go.Candlestick(
            x=candles.index,
            open=candles['open'],
            high=candles['high'],
            low=candles['low'],
            close=candles['close']
        )
    except Exception as exception:
        st.write(f"Error constructing candlestick chart. Error: {exception}")
        raise ConnectionAbortedError(f"Error constructing candlestick chart. Error: {exception}")
    # Construct the layout
    try:
        layout = go.Layout(
            title='Candlestick Chart',
            xaxis_title='Date',
            yaxis_title='Price'
        )
    except Exception as exception:
        st.write(f"Error constructing candlestick chart layout. Error: {exception}")
        raise ConnectionAbortedError(f"Error constructing candlestick chart layout. Error: {exception}")
    # Construct the figure
    try:
        figure = go.Figure(data=candlestick, layout=layout)
    except Exception as exception:
        st.write(f"Error constructing candlestick chart figure. Error: {exception}")
        raise ConnectionAbortedError(f"Error constructing candlestick chart figure. Error: {exception}")
    # Return the figure if successful
    return figure



# Retrieve the historical data
def get_historical_data(symbol, timeframe, number_of_candles):
    # Get the historical data
    try:
        candles = mt5_interface.query_historic_data(
            symbol=symbol,
            timeframe=timeframe,
            number_of_candles=number_of_candles
        )
    except Exception as exception:
        print(f"Error retrieving historical data. Error: {exception}")
        raise ConnectionError(f"Error retrieving historical data. Error: {exception}")
    # Return the candles
    return candles