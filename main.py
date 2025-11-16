import pandas as pd

df = pd.read_csv(r"C:\Users\Owner\OneDrive\coding\what-makes-a-hit\data\top_10000_1950-now.csv")
print(df.columns)  # Step 1: check real column names

# Step 2: handle release_date or release_year properly
if 'Album Release Date' in df.columns:
    df['release_year'] = pd.to_datetime(df['Album Release Date'], errors='coerce').dt.year

# Step 3: convert to numeric
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# Step 4: filter 2020–2024
new_df = df[df['release_year'].between(2020, 2024)]
print(new_df.shape)
print(new_df.head())
