from src.utils.logger import Logger
import json

class JsonReader:

    @staticmethod
    def get_test_file(filename: str) -> dict:
        json_file_path = f"test_data/{filename}"
        try:
            # Open the JSON file in read mode
            with open(json_file_path, 'r') as file:
                # Use json.load() to parse the JSON content into a Python object
                # The resulting object will typically be a dictionary or a list,
                # depending on the top-level structure of your JSON.
                python_object = json.load(file)
        except FileNotFoundError:
            Logger.error_msg(f"Error: The file '{json_file_path}' was not found.")
        except json.JSONDecodeError:
            Logger.error_msg(f"Error: Could not decode JSON from '{json_file_path}'. Check if it's valid JSON.")
        except Exception as e:
            Logger.error_msg(f"An unexpected error occurred: {e}")
        return python_object