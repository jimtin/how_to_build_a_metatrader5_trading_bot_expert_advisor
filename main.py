import mt5_interface
import copilot as metatrader5_copilot
import helper_functions

    
# Function to start Meta Trader 5 (MT5)
def start_mt5(project_settings):
    # Start MT5
    try:
        mt5_interface.start_mt5(project_settings["username"], project_settings["password"], project_settings["server"],
                                project_settings["mt5Pathway"])
    except Exception as exception:
        print(f"Error starting MetaTrader 5. Error: {exception}")
        raise ConnectionAbortedError(f"Error starting MetaTrader 5. Error: {exception}")
    # Initialize symbols
    try:
        mt5_interface.initialize_symbols(project_settings["symbols"])
    except Exception as exception:
        print(f"Error initializing symbols on MetaTrader 5. Error: {exception}")
        raise ConnectionAbortedError(f"Error initializing symbols on MetaTrader 5. Error: {exception}")
    # Return True if successful
    return True


# Function to start your MetaTrader 5 CoPilot
def start_copilot(symbol, timeframe):
    # Start the CoPilot
    try:
        metatrader5_copilot.start_copilot(symbol=symbol, timeframe=timeframe)
    except Exception as exception:
        print(f"Error starting CoPilot. Error: {exception}")
        raise ConnectionAbortedError(f"Error starting CoPilot. Error: {exception}")
    # Return True if successful
    return True


# Main function
if __name__ == '__main__':
    # Set up the import filepath
    import_filepath = "setting.json"
    # Import project settings
    project_settings = helper_functions.get_project_settings(import_filepath)
    # Start MT5
    try:
        if start_mt5(project_settings) is True:
            pass
        else:
            raise ConnectionError("Error starting MetaTrader 5")
    except Exception as exception:
        print(f"Error starting MetaTrader 5. Error: {exception}")
        raise ConnectionAbortedError(f"Error starting MetaTrader 5. Error: {exception}")
    # Start CoPilot
    try:
        if start_copilot(symbol=project_settings['symbols'][0], timeframe=project_settings['timeframe']) is True:
            pass
        else:
            raise ConnectionError("Error starting CoPilot")
    except Exception as exception:
        print(f"Error starting CoPilot. Error: {exception}")
        raise ConnectionAbortedError(f"Error starting CoPilot. Error: {exception}")
    