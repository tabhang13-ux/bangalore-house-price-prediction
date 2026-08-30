import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        # Case-insensitive location matching
        loc_index = next(
            i for i, col in enumerate(__data_columns)
            if col.lower() == location.lower()
        )
    except StopIteration:
        loc_index = -1

    input_data = np.zeros(len(__data_columns))

    input_data[0] = sqft
    input_data[1] = bath
    input_data[2] = bhk

    if loc_index >= 0:
        input_data[loc_index] = 1

    input_df = pd.DataFrame(
        [input_data],
        columns=__data_columns
    )

    return round(__model.predict(input_df)[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __data_columns
    global __locations
    global __model

    # Load model first
    with open("./artifacts/Bengaluru_House_Data.pickle", "rb") as f:
        __model = pickle.load(f)

    # Use the EXACT feature names used during model training
    __data_columns = list(__model.feature_names_in_)

    __locations = __data_columns[3:]

    print("loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()

    print(get_location_names())

    print(get_estimated_price("1st Phase JP Nagar", 1000, 3, 3))
    print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 2))
    print(get_estimated_price("Kalhalli", 1000, 2, 2))
    print(get_estimated_price("Ejipura", 1000, 2, 2))