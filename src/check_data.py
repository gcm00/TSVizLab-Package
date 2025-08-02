import pandas as pd

def check_data(df1: pd.DataFrame):
    while True:
        if not isinstance(df1, pd.DataFrame) :
            raise KeyError('You should include a DataFrame as an argument')

        if len(df1) <= 5:
            raise ValueError('Your Dataframe should contain at least 5 values')

        required_cols = ['close', 'high', 'low']
        if not all(col in df1.columns for col in required_cols):
            raise ValueError(f"DataFrame should contain the following columns : {required_cols}")

