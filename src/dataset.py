import pandas as pd

def load_data(year: int, month: int) -> pd.DataFrame:
    """Read the data for a given year and month."""
    filename = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02}.parquet"
    return pd.read_parquet(filename)