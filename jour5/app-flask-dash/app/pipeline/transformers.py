import pandas as pd
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import FunctionTransformer
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import StandardScaler

def extract_month(date_series):
    return pd.to_datetime(date_series).dt.month.values.reshape(-1,1)