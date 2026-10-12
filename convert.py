import pandas as pd

# Load CSV downloaded from Google Sheets
df = pd.read_csv("Item list - Item list example.csv")

# 1. Drop empty rows where 'name' is missing
df = df.dropna(subset=["name"])

# 2. Fill empty formula cells if needed
df["baseGift"] = pd.to_numeric(df["baseGift"], errors="coerce").fillna(0)
df["baseStats"] = pd.to_numeric(df["baseStats"], errors="coerce").fillna(0)

# 3. Export clean JSON
df.to_json("items.json", orient="records", indent=2)

print(f"Successfully generated items.json with {len(df)} items!")