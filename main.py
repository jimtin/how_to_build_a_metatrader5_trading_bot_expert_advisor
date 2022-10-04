import json
import os


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
    import_filepath = "C:/Users/james/PycharmProjects/how_to_build_a_metatrader5_trading_bot_expert_advisor/settings.json"
    project_settings = get_project_settings(import_filepath)

