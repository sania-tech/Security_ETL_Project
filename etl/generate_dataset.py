import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

users = [
    "admin", "sania", "john.doe", "jane.smith", "root",
    "guest", "ali.hassan", "sara.khan", "test_user", "backup_admin"
]

ip_pool = [
    "192.168.1.10", "192.168.1.22", "10.0.0.5", "10.0.0.18",
    "172.16.0.3",   "203.0.113.45", "198.51.100.7", "185.220.101.5",
    "45.33.32.156",  "192.168.1.99"
]

event_types = ["login", "login", "login", "logout", "password_change", "file_access"]

records = []
start_time = datetime(2026, 1, 1, 0, 0, 0)

for i in range(500):
    user      = random.choice(users)
    ip        = random.choice(ip_pool)
    event     = random.choice(event_types)
    timestamp = start_time + timedelta(minutes=random.randint(0, 43200))

    if user in ["admin", "root", "guest"]:
        status = random.choices(["success", "failed"], weights=[30, 70])[0]
    else:
        status = random.choices(["success", "failed"], weights=[80, 20])[0]

    records.append({
        "timestamp":  timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "user":       user,
        "ip_address": ip,
        "event_type": event,
        "status":     status
    })

df = pd.DataFrame(records)

duplicates = df.sample(20, random_state=1)
df = pd.concat([df, duplicates], ignore_index=True)

for idx in random.sample(range(len(df)), 10):
    df.at[idx, "user"] = None

df.to_csv("data/raw_logs.csv", index=False)
print(f"Dataset created! Total rows: {len(df)}")
print(df.head(10))
