import mt5_interface
import pandas
import numpy


# Function to articulate strategy_one
def strategy_one(symbol, timeframe, pip_size):
    # Retrieve the required data from get_and_transform_mt5_data
    data_df = get_and_transform_mt5_data(symbol=symbol, timeframe=timeframe, number_of_candles=2, pip_size=pip_size)
    print(data_df)
    # Pass this to make_decision
    decision = make_decision(data_df)
    print(decision)
    # Pass the decision and dataframe to create_new_order
    create_new_order(decision_outcome=decision, candle_dataframe=data_df, pip_size=pip_size, symbol=symbol)
    return "Completed"


# Function to query last two candles in MetaTrader 5 based upon timeframe
def get_and_transform_mt5_data(symbol, timeframe, number_of_candles, pip_size):
    # Retrieve the raw data from MT5 platform
    raw_data = mt5_interface.query_historic_data(symbol, timeframe, number_of_candles)
    # Transform raw data into Pandas DataFrame
    df_data = pandas.DataFrame(raw_data)
    # Convert the time in seconds into a human readable datetime format
    df_data['time'] = pandas.to_datetime(df_data['time'], unit='s')
    # Calculate if red or green
    df_data['RedOrGreen'] = numpy.where((df_data['open'] < df_data['close']), 'Green', 'Red')
    # Calculate trade_high (high price + 1 pip)
    df_data['trade_high'] = df_data['high'] + pip_size
    # Calculate trade_low (low price - 1 pip)
    df_data['trade_low'] = df_data['low'] - pip_size
    # Calculate the number of pips between trade_high and trade_low
    df_data['pip_distance'] = (df_data['trade_high'] - df_data['trade_low'])/pip_size
    # Return the data frame to the user
    return df_data


# Function to make decisions based on presented dataframe
def make_decision(candle_dataframe):
    # Test if they are both the same
    if(candle_dataframe.iloc[0]['RedOrGreen'] != candle_dataframe.iloc[1]['RedOrGreen']):
        return "DoNothing"
    # Test if both are Green
    elif(candle_dataframe.iloc[0]['RedOrGreen'] == "Green" and candle_dataframe.iloc[0]['RedOrGreen'] == "Green"):
        return "Green"
    # Test if both are Red
    elif (candle_dataframe.iloc[0]['RedOrGreen'] == "Red" and candle_dataframe.iloc[0]['RedOrGreen'] == "Red"):
        return "Red"
    # Default outcome in case of unforseen error
    else:
        return "DoNothing"


# Function to create a new order based upon previous analysis
def create_new_order(decision_outcome, candle_dataframe, pip_size, symbol):
    # Extract the first row of the dataframe
    first_row = candle_dataframe.iloc[1]
    # Do nothing if outcome is "DoNothing
    if decision_outcome == "DoNothing":
        return
    elif decision_outcome == "Green":
        # Calculate the order stop_loss (trade_low of previous candle)
        stop_loss = first_row['trade_low']
        # Calculate the order buy_stop (trade_high of previous candle)
        buy_stop = first_row['trade_high']
        # Calculate the order take_profit (2 times the pip distance, added to the buy_stop)
        num_pips = first_row["pip_distance"] * 2 * pip_size # Convert pip_distance back into pips
        take_profit = buy_stop + num_pips
        # Add in an order comment
        comment = "Green Order"
        # Send order to place_order function in mt5_interface.py
        mt5_interface.place_order("BUY_STOP", symbol, 0.1, buy_stop, stop_loss, take_profit, comment)
        return
    elif decision_outcome == "Red":
        # Calculate the order stop_loss (trade_high of previous candle)
        stop_loss = first_row['trade_high']
        # Calculate the order buy_stop (trade_low of previous candle)
        buy_stop = first_row['trade_low']
        # Calculate the order take_profit (2 times the pip distance, subtracted from the buy_stop)
        num_pips = first_row["pip_distance"] * 2 * pip_size  # Convert pip_distance back into pips
        take_profit = buy_stop - num_pips
        # Add in an order comment
        comment = "Red Order"
        # Send order to place_order function in mt5_interface.py
        mt5_interface.place_order("SELL_STOP", symbol, 0.1, buy_stop, stop_loss, take_profit, comment)
        return


# Function to update trailing stop if needed
def update_trailing_stop(order, trailing_stop_pips, pip_size):
    # Convert trailing_stop_pips into pips
    trailing_stop_pips = trailing_stop_pips * pip_size
    # Determine if Red or Green
    # A Green Position will have a take_profit > stop_loss
    if order[12] > order[11]:
        # If Green, new_stop_loss = current_price - trailing_stop_pips
        new_stop_loss = order[13] - trailing_stop_pips
        # Test to see if new_stop_loss > current_stop_loss
        if new_stop_loss > order[11]:
            print("Update Stop Loss")
            # Create updated values for order
            order_number = order[0]
            symbol = order[16]
            # New take_profit will be the difference between new_stop_loss and old_stop_loss added to take profit
            new_take_profit = order[12] + new_stop_loss - order[11]
            print(new_take_profit)
            # Send order to modify_position
            mt5_interface.modify_position(order_number=order_number, symbol=symbol, new_stop_loss=new_stop_loss,
                                          new_take_profit=new_take_profit)
    elif order[12] < order[11]:
        # If Red, new_stop_loss = current_price + trailing_stop_pips
        new_stop_loss = order[13] + trailing_stop_pips
        # Test to see if new_stop_loss < current_stop_loss
        if new_stop_loss < order[11]:
            print("Update Stop Loss")
            # Create updated values for order
            order_number = order[0]
            symbol = order[16]
            # New take_profit will be the difference between new_stop_loss and old_stop_loss subtracted from old take_profit
            new_take_profit = order[12] - new_stop_loss + order[11]
            print(new_take_profit)
            # Send order to modify_position
            mt5_interface.modify_position(order_number=order_number, symbol=symbol, new_stop_loss=new_stop_loss,
                                          new_take_profit=new_take_profit)
