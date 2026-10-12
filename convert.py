import pandas as pd

# Load CSV
df = pd.read_csv("Martial arts world treasure list - Item list.csv")
# Standardize column names to camelCase
df = df.rename(columns={"realmid": "realmId", "iskey": "isKey", "isoffering": "isOffering"})
# Clean column headers (removes leading/trailing spaces from "realmId ", "name ", etc.)
df.columns = df.columns.str.strip()

# Clean string values in the 'name' column and drop empty rows
df["name"] = df["name"].astype(str).str.strip()
df = df[df["name"] != ""]
df = df.dropna(subset=["name"])

# Clean boolean columns if present
if "isOffering" in df.columns:
    df["isOffering"] = df["isOffering"].astype(str).str.upper().str.strip() == "TRUE"
if "isKey" in df.columns:
    df["isKey"] = df["isKey"].astype(str).str.upper().str.strip() == "TRUE"

# Export clean JSON
df.to_json("items.json", orient="records", indent=2)

print("Successfully converted items.json with clean keys!")