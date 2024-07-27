import pandas as pd
from typing import List, Tuple

numeric_feat = [
    "pickup_weekday",
    "pickup_hour",
    'work_hours',
    "pickup_minute",
    "passenger_count",
    'trip_distance',
    'trip_time',
    'trip_speed'
]
categorical_feat = [
    "PULocationID",
    "DOLocationID",
    "RatecodeID",
]
FEATURES = numeric_feat + categorical_feat
EPS = 1e-7

def build_features(df: pd.DataFrame, target_col: str) -> pd.DataFrame:

   # Basic cleaning
    df = df[df['fare_amount'] > 0].reset_index(drop=True)  # avoid divide-by-zero
    # add target
    df['tip_fraction'] = df['tip_amount'] / df['fare_amount']
    df[target_col] = df['tip_fraction'] > 0.2

    # add features
    df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.weekday
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
    df['pickup_minute'] = df['tpep_pickup_datetime'].dt.minute
    df['work_hours'] = (df['pickup_weekday'] >= 0) & (df['pickup_weekday'] <= 4) & (df['pickup_hour'] >= 8) & (df['pickup_hour'] <= 18)
    df['trip_time'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.seconds
    df['trip_speed'] = df['trip_distance'] / (df['trip_time'] + EPS)

    # drop unused columns
    df = df[['tpep_dropoff_datetime'] + FEATURES + [target_col]]
    df[FEATURES + [target_col]] = df[FEATURES + [target_col]].astype("float32").fillna(-1.0)

    # convert target to int32 for efficiency (it's just 0s and 1s)
    df[target_col] = df[target_col].astype("int32")

    return df.reset_index(drop=True)


def compare_distributions(dfa: pd.DataFrame, dfb: pd.DataFrame) -> pd.DataFrame:
    """Compare the distributions of two datasets."""
    from scipy import stats
    statistics = []
    p_values = []

    for feature in FEATURES:
        statistic, p_value = stats.ks_2samp(dfa[feature], dfb[feature])
        statistics.append(statistic)
        p_values.append(p_value)
    
    comparison_df = pd.DataFrame(data={'feature': FEATURES, 'statistic': statistics, 'p_value': p_values})
    comparison_df.sort_values(by='p_value', ascending=True).head(11)

    return comparison_df