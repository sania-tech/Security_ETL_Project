import pandas as pd

df = pd.read_csv("data/raw_logs.csv")

print("=" * 40)
print("DATASET OVERVIEW")
print("=" * 40)
print(f"Total rows    : {len(df)}")
print(f"Total columns : {len(df.columns)}")
print(f"Columns       : {list(df.columns)}")

print("\n" + "=" * 40)
print("FIRST 5 ROWS")
print("=" * 40)
print(df.head())

print("\n" + "=" * 40)
print("MISSING VALUES")
print("=" * 40)
print(df.isnull().sum())

print("\n" + "=" * 40)
print("DUPLICATE ROWS")
print("=" * 40)
print(f"Duplicates found: {df.duplicated().sum()}")

print("\n" + "=" * 40)
print("STATUS COUNTS (success vs failed)")
print("=" * 40)
print(df["status"].value_counts())

print("\n" + "=" * 40)
print("TOP 5 USERS WITH FAILED LOGINS")
print("=" * 40)
failed = df[df["status"] == "failed"]
print(failed["user"].value_counts().head(5))

print("\n" + "=" * 40)
print("TOP 5 SUSPICIOUS IPs")
print("=" * 40)
print(failed["ip_address"].value_counts().head(5))

print("\n" + "=" * 40)
print("EVENT TYPE BREAKDOWN")
print("=" * 40)
print(df["event_type"].value_counts())
