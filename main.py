import json
import os
import mt5_interface
import strategy
import time


# Function to import settings from settings.json
def get_project_settings(importFilepath):
    # Test the filepath to sure it exists
    if os.path.exists(importFilepath):
        # Open the file
        f = open(importFilepath, "r")
        # Get the information from file
        project_settings = json.load(f)
        # Close the file
        f.close()
        # Return project settings to program
        return project_settings
    else:
        return ImportError


# Main function
if __name__ == '__main__':
    # Set up the import filepath
    import_filepath = "C:/Users/james/PycharmProjects/how_to_build_a_metatrader5_trading_bot_expert_advisor/settings.json"
    # Import project settings
    project_settings = get_project_settings(import_filepath)
    # Start MT5
    mt5_interface.start_mt5(project_settings["username"], project_settings["password"], project_settings["server"],
                            project_settings["mt5Pathway"])
    # Initialize symbols
    mt5_interface.initialize_symbols(project_settings["symbols"])
    # Select symbol to run strategy on
    symbol_for_strategy = project_settings['symbols'][0]
    # Set up a previous time variable
    previous_time = 0
    # Set up a current time variable
    current_time = 0
    # Start a while loop to poll MT5
    while True:
        # Retrieve the current candle data
        candle_data = mt5_interface.query_historic_data(symbol=symbol_for_strategy,
                                                        timeframe=project_settings['timeframe'], number_of_candles=1)
        # Extract the timedata
        current_time = candle_data[0][0]
        # Compare against previous time
        if current_time != previous_time:
            # Notify user
            print("New Candle")
            # Update previous time
            previous_time = current_time
            # Retrieve previous orders
            orders = mt5_interface.get_open_orders()
            # Cancel orders
            for order in orders:
                mt5_interface.cancel_order(order)
            # Start strategy one on selected symbol
            strategy.strategy_one(symbol=symbol_for_strategy, timeframe=project_settings['timeframe'],
                                  pip_size=project_settings['pip_size'])
        else:
            # Get positions
            positions = mt5_interface.get_open_positions()
            # Pass positions to update_trailing_stop
            for position in positions:
                strategy.update_trailing_stop(order=position, trailing_stop_pips=10,
                                              pip_size=project_settings['pip_size'])
        time.sleep(0.1)


