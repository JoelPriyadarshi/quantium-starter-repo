import pandas as pd
import glob

data_files = glob.glob("data/*.csv")

processed_dfs = []

for file in data_files:
    df = pd.read_csv(file)
    
    df = df[df['product'].str.lower() == 'pink morsel']

    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    df['sales'] = df['price'] * df['quantity']

    df = df[['sales', 'date', 'region']]
    
    processed_dfs.append(df)

final_df = pd.concat(processed_dfs)

final_df.to_csv("formatted_data.csv", index=False)

print("Complete! 'formatted_data.csv' is ready.")