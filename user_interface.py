import streamlit as st
import plotly.graph_objects as go
import mt5_interface


current_symbol = "USDJPY"
current_timeframe = "M1"

# Function to define the CoPilot User Interface
def start_copilot_user_interface(symbol, timeframe):
    """
    Function to start the CoPilot User Interface
    :param symbol: The symbol to be used
    :param timeframe: The timeframe to be used
    :return: True if successful
    """
    try:
        # Get the candlesticks
        candlesticks = update_candlesticks(selected_symbol=symbol, selected_timeframe=timeframe)
    except Exception as exception:
        st.write(f"Error updating candlesticks. Error: {exception}")
        raise ConnectionAbortedError(f"Error updating candlesticks. Error: {exception}")
    # Get a list of all the available symbols
    try:
        symbols = get_symbols()
    except Exception as exception:
        st.write(f"Error retrieving symbols. Error: {exception}")
        raise ConnectionAbortedError(f"Error retrieving symbols. Error: {exception}")
    # Create a Side Bar
    with st.sidebar:
        st.title("CoPilot Settings")
        st.write("Select a symbol and timeframe")
        # Define what happens when the symbol changes
        def on_symbol_change():
            selected_symbol = st.session_state['selected_symbol']
            print(f"Selected Symbol: {selected_symbol}")
        symbol = st.selectbox("Symbol", symbols, key='selected_symbol', on_change=on_symbol_change)
        # Define what happens when the timeframe changes
        def on_timeframe_change():
            selected_timeframe = st.session_state['selected_timeframe']
            print(f"Selected Timeframe: {selected_timeframe}")
        timeframe = st.selectbox("Timeframe", ["M1", "M5", "M15", "M30", "H1", "H4", "H6", "H8", "H12", "D1", "W1", "MN1"], key='selected_timeframe', on_change=on_timeframe_change)
    # Return True if successful
    return True


# Function to Construct a Candlestick Chart
def construct_candlestick_chart(candles):
    """
    Function to construct a candlestick chart
    :param candles: The candlestick data
    :return: The candlestick chart
    """
    # Construct the candlestick chart
    try:
        candlestick = go.Candlestick(
            x=candles['human_time'],
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
    """
    Function to retrieve the historical data
    :param symbol: The symbol to be used
    :param timeframe: The timeframe to be used
    :param number_of_candles: The number of candles to be retrieved
    :return: The candles
    """
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


# Get a list of all the available symbols for this MT5
def get_symbols():
    """
    Function to get a list of all the available symbols for this MT5
    :return: The symbols
    """
    # Get the symbols
    try:
        symbols = mt5_interface.get_symbols()
    except Exception as exception:
        print(f"Error retrieving symbols. Error: {exception}")
        raise ConnectionError(f"Error retrieving symbols. Error: {exception}")
    # Iterate through the symbols and construct a list of the name 
    symbol_names = []
    for symbol in symbols:
        symbol_names.append(symbol.name)
    # Return the symbols
    return symbol_names


# Function to check if new candlesticks are required
def check_for_new_candlesticks(selected_symbol, selected_timeframe):
    """
    Function to check if new candlesticks need to be retrieved from MT5
    :param selected_symbol: The selected symbol
    :param selected_timeframe: The selected timeframe
    :return: True if new candlesticks are required
    """
    # Compare the selected symbol and timeframe with the current symbol and timeframe
    if selected_symbol != current_symbol:
        try:
            # Make sure the new symbol is enabled on MT5
            symbols = mt5_interface.initialize_symbol(selected_symbol)
        except Exception as exception:
            print(f"Error initializing symbol. Error: {exception}")
            raise ConnectionError(f"Error initializing symbol. Error: {exception}")
        # Update the current symbol
        current_symbol = selected_symbol
        return True
    if selected_timeframe != current_timeframe:
        # Update the current timeframe
        current_timeframe = selected_timeframe
        return True
    return False
    

# Function to update the chart
def update_candlesticks(selected_symbol, selected_timeframe):
    """
    Function to update the candlestick chart
    :param selected_symbol: The selected symbol
    :param selected_timeframe: The selected timeframe
    :return: True if successful
    """
    # Check if new candlesticks are required
    new_candlesticks_required = True #check_for_new_candlesticks(selected_symbol, selected_timeframe)
    # If new candlesticks are required, retrieve the new candlesticks
    if new_candlesticks_required is True:
        try:
            # Get the historical data
            candles = get_historical_data(symbol=selected_symbol, timeframe=selected_timeframe, number_of_candles=1000)
        except Exception as exception:
            st.write(f"Error updating candlesticks. Error: {exception}")
            raise ConnectionAbortedError(f"Error updating candlesticks. Error: {exception}")
        try:
            # Construct the candlestick chart
            figure = construct_candlestick_chart(candles)
        except Exception as exception:
            st.write(f"Error updating candlesticks. Error: {exception}")
            raise ConnectionAbortedError(f"Error updating candlesticks. Error: {exception}")
        # Display the candlestick chart
        try:
            st.plotly_chart(figure)
        except Exception as exception:
            st.write(f"Error updating candlesticks. Error: {exception}")
            raise ConnectionAbortedError(f"Error updating candlesticks. Error: {exception}")
    # Return True if successful
    return True