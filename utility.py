# config/utility.py

import os
import json

class UtilityMethods:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "config", "test_data.json")

    @classmethod
    def get_data_by_keys(cls, key_name):
        print(f"Reading data from: {cls.data_path}")
        try:
            with open(cls.data_path, "r") as f:
                data = json.load(f)

            for item in data:
                if key_name in item:
                    return item[key_name]

            print(f"Warning: No matching data found for key: {key_name}")
            return None

        except FileNotFoundError:
            print("Error: test_data.json file not found.")
            return None
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON.")
            return None
