import user_interface



# Function to run the CoPilot
def start_copilot(symbol, timeframe):
    # Start the CoPilot
    try:
        user_interface.start_copilot_user_interface()
    except Exception as exception:
        print(f"Error starting CoPilot. Error: {exception}")
        raise ConnectionAbortedError(f"Error starting CoPilot. Error: {exception}")
    # Return True if successful
    return True



    
        
