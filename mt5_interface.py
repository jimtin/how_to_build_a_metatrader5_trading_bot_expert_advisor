import MetaTrader5


# Function to start Meta Trader 5 (MT5)
def start_mt5(username, password, server, path):
    # Ensure that all variables are the correct type
    uname = int(username) # Username must be an int
    pword = str(password) # Password must be a string
    trading_server = str(server) # Server must be a string
    filepath = str(path) # Filepath must be a string

    # Attempt to start MT5
    if MetaTrader5.initialize(login=uname, password=pword, server=trading_server, path=filepath):
        print("Trading Bot Starting")
        # Login to MT5
        if MetaTrader5.login(login=uname, password=pword, server=trading_server):
            print("Trading Bot Logged in and Ready to Go!")
            return True
        else:
            print("Login Fail")
            quit()
            return PermissionError
    else:
        print("MT5 Initialization Failed")
        quit()
        return ConnectionAbortedError


# Function to initialize a symbol on MT5
def initialize_symbols(symbol_array):
    # Get a list of all symbols supported in MT5
    all_symbols = MetaTrader5.symbols_get()
    # Create an array to store all the symbols
    symbol_names = []
    # Add the retrieved symbols to the array
    for symbol in all_symbols:
        symbol_names.append(symbol.name)

    # Check each symbol in symbol_array to ensure it exists
    for provided_symbol in symbol_array:
        if provided_symbol in symbol_names:
            # If it exists, enable
            if MetaTrader5.symbol_select(provided_symbol, True):
                print(f"Sybmol {provided_symbol} enabled")
            else:
                return ValueError
        else:
            return SyntaxError

    # Return true when all symbols enabled
    return True


# Function to place a trade on MT5
def place_order(order_type, symbol, volume, price, stop_loss, take_profit, comment):
    # If order type SELL_STOP
    if order_type == "SELL_STOP":
        order_type = MetaTrader5.ORDER_TYPE_SELL_STOP
    elif order_type == "BUY_STOP":
        order_type = MetaTrader5.ORDER_TYPE_BUY_STOP
    # Create the request
    request = {
        "action": MetaTrader5.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": round(price, 3),
        "sl": round(stop_loss, 3),
        "tp": round(take_profit, 3),
        "type_filling": MetaTrader5.ORDER_FILLING_RETURN,
        "type_time": MetaTrader5.ORDER_TIME_GTC,
        "comment": comment
    }
    # Send the order to MT5
    order_result = MetaTrader5.order_send(request)
    # Notify based on return outcomes
    if order_result[0] == 10009:
        print(f"Order for {symbol} successful")
    else:
        print(f"Error placing order. ErrorCode {order_result[0]}, Error Details: {order_result}")
    return order_result


# Function to cancel an order
def cancel_order(order_number):
    # Create the request
    request = {
        "action": MetaTrader5.TRADE_ACTION_REMOVE,
        "order": order_number,
        "comment": "Order Removed"
    }
    # Send order to MT5
    order_result = MetaTrader5.order_send(request)
    return order_result


# Function to modify an open position
def modify_position(order_number, symbol, new_stop_loss, new_take_profit):
    # Create the request
    request = {
        "action": MetaTrader5.TRADE_ACTION_SLTP,
        "symbol": symbol,
        "sl": new_stop_loss,
        "tp": new_take_profit,
        "position": order_number
    }
    # Send order to MT5
    order_result = MetaTrader5.order_send(request)
    if order_result[0] == 10009:
        return True
    else:
        return False


# Function to convert a timeframe string in MetaTrader 5 friendly format
def set_query_timeframe(timeframe):
    # Implement a Pseudo Switch statement. Note that Python 3.10 implements match / case but have kept it this way for
    # backwards integration
    if timeframe == "M1":
        return MetaTrader5.TIMEFRAME_M1
    elif timeframe == "M2":
        return MetaTrader5.TIMEFRAME_M2
    elif timeframe == "M3":
        return MetaTrader5.TIMEFRAME_M3
    elif timeframe == "M4":
        return MetaTrader5.TIMEFRAME_M4
    elif timeframe == "M5":
        return MetaTrader5.TIMEFRAME_M5
    elif timeframe == "M6":
        return MetaTrader5.TIMEFRAME_M6
    elif timeframe == "M10":
        return MetaTrader5.TIMEFRAME_M10
    elif timeframe == "M12":
        return MetaTrader5.TIMEFRAME_M12
    elif timeframe == "M15":
        return MetaTrader5.TIMEFRAME_M15
    elif timeframe == "M20":
        return MetaTrader5.TIMEFRAME_M20
    elif timeframe == "M30":
        return MetaTrader5.TIMEFRAME_M30
    elif timeframe == "H1":
        return MetaTrader5.TIMEFRAME_H1
    elif timeframe == "H2":
        return MetaTrader5.TIMEFRAME_H2
    elif timeframe == "H3":
        return MetaTrader5.TIMEFRAME_H3
    elif timeframe == "H4":
        return MetaTrader5.TIMEFRAME_H4
    elif timeframe == "H6":
        return MetaTrader5.TIMEFRAME_H6
    elif timeframe == "H8":
        return MetaTrader5.TIMEFRAME_H8
    elif timeframe == "H12":
        return MetaTrader5.TIMEFRAME_H12
    elif timeframe == "D1":
        return MetaTrader5.TIMEFRAME_D1
    elif timeframe == "W1":
        return MetaTrader5.TIMEFRAME_W1
    elif timeframe == "MN1":
        return MetaTrader5.TIMEFRAME_MN1


# Function to query previous candlestick data from MT5
def query_historic_data(symbol, timeframe, number_of_candles):
    # Convert the timeframe into an MT5 friendly format
    mt5_timeframe = set_query_timeframe(timeframe)
    # Retrieve data from MT5
    rates = MetaTrader5.copy_rates_from_pos(symbol, mt5_timeframe, 1, number_of_candles)
    return rates


# Function to retrieve all open orders from MT5
def get_open_orders():
    orders = MetaTrader5.orders_get()
    order_array = []
    for order in orders:
        order_array.append(order[0])
    return order_array


# Function to retrieve all open positions
def get_open_positions():
    # Get position objects
    positions = MetaTrader5.positions_get()
    # Return position objects
    return positions
