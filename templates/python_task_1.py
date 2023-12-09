import pandas as pd
df = pd.read_csv("dataset-1.csv")

# Create a new DataFrame with id_1 as index and id_2 as columns
result_df = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)

# Set diagonal values to 0
result_df.values[[range(len(result_df))]*2]

# Display the resulting DataFrame
print(result_df)

import pandas as pd
def get_type_count(df) -> dict:
    def categorize_car_type(value):
        if value <= 15:
            return 'low'
        elif value <= 25:
            return 'medium'
        else:
            return 'high'

    df['car_type'] = df['car'].apply(categorize_car_type)
    type_counts = dict(df['car_type'].value_counts())

    return type_counts

df = pd.read_csv("dataset-1.csv")
car_type_counts = get_type_count(df)
print(car_type_counts)

import pandas as pd
def get_bus_indexes(df):
    
    mean_bus = df['bus'].mean()
    indices = df.index[df['bus'] > 2 * mean_bus].tolist()
    indices.sort()
    return indices

df = pd.read_csv("dataset-1.csv")
result_indices = get_bus_indexes(df)
print(result_indices)

import pandas as pd
def filter_routes(df) -> list:

    mean_truck_by_route = df.groupby('route')['truck'].mean()
    filtered_routes = mean_truck_by_route[mean_truck_by_route > 7].index.tolist()
    filtered_routes.sort()

    return filtered_routes

df = pd.read_csv("dataset-1.csv")
result_routes = filter_routes(df)
print(result_routes)
