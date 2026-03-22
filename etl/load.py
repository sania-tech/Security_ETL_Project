import sqlite3
import os

def load(df):
    # Make sure db folder exists
    os.makedirs("db", exist_ok=True)

    db_path = "db/security_logs.db"
    conn = sqlite3.connect(db_path)

    # Save dataframe to SQL table - replace each time pipeline runs
    df.to_sql("security_logs", conn, if_exists="replace", index=False)

    # Verify it saved correctly
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM security_logs")
    count = cursor.fetchone()[0]

    conn.close()
    print(f"[LOAD] Saved {count} rows to {db_path}")
    print(f"[LOAD] Table name: security_logs")
