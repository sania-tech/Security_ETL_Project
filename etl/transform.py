import pandas as pd

def transform(df):
    print(f"[TRANSFORM] Starting with {len(df)} rows")

    # Step 1 - remove duplicates
    df = df.drop_duplicates()
    print(f"[TRANSFORM] After removing duplicates: {len(df)} rows")

    # Step 2 - fill missing user values
    df["user"] = df["user"].fillna("unknown")
    print(f"[TRANSFORM] Missing users filled with 'unknown'")

    # Step 3 - convert timestamp to proper datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    print(f"[TRANSFORM] Timestamps converted to datetime")

    # Step 4 - count failed logins per user
    failed_counts = (
        df[df["status"] == "failed"]
        .groupby("user")
        .size()
        .reset_index(name="failed_count")
    )

    # Step 5 - merge failed counts back into main dataframe
    df = df.merge(failed_counts, on="user", how="left")
    df["failed_count"] = df["failed_count"].fillna(0)

    # Step 6 - assign risk_level based on your project rules
    def assign_risk(row):
        if row["status"] == "failed" and row["failed_count"] > 10:
            return "high"
        elif row["status"] == "failed" and row["failed_count"] > 3:
            return "medium"
        elif row["status"] == "failed":
            return "low"
        else:
            return "none"

    df["risk_level"] = df.apply(assign_risk, axis=1)

    # Step 7 - add log_id column
    df = df.reset_index(drop=True)
    df.insert(0, "log_id", df.index + 1)

    print(f"[TRANSFORM] Risk levels assigned")
    print(f"[TRANSFORM] Risk breakdown:")
    print(df["risk_level"].value_counts().to_string())
    print(f"[TRANSFORM] Done. Final rows: {len(df)}")

    return df
