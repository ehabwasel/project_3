# Libraries
import pandas as pd

# Dataset cleanup
def dataset_cleanup(df):
    # Clean up the periods column to the correct years
    df["Periods"] = df["Periods"].str[:4].astype(int)
    df = df.rename(columns={"Periods": "Year"})

    # Add more if necessary
    #
    #
    #

    # Return cleaned up dataset
    return df

