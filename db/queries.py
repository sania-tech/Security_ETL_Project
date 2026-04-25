import sqlite3
import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, "db", "security_logs.db")
reports_path = os.path.join(base_dir, "reports")

conn = sqlite3.connect(db_path)

print("=" * 40)
print("QUERY 1 - Failed logins per user")
print("=" * 40)
query1 = """
    SELECT user, COUNT(*) as failed_count
    FROM security_logs
    WHERE status = 'failed'
    GROUP BY user
    ORDER BY failed_count DESC
"""
df1 = pd.read_sql_query(query1, conn)
print(df1)
df1.to_csv(f"{reports_path}/failed_logins.csv", index=False)
print("Saved to reports/failed_logins.csv ✅")

print()
print("=" * 40)
print("QUERY 2 - Suspicious IP addresses")
print("=" * 40)
query2 = """
    SELECT ip_address, COUNT(*) as failed_count
    FROM security_logs
    WHERE status = 'failed'
    GROUP BY ip_address
    ORDER BY failed_count DESC
"""
df2 = pd.read_sql_query(query2, conn)
print(df2)
df2.to_csv(f"{reports_path}/suspicious_ips.csv", index=False)
print("Saved to reports/suspicious_ips.csv ✅")

print()
print("=" * 40)
print("QUERY 3 - Risk level summary")
print("=" * 40)
query3 = """
    SELECT risk_level, COUNT(*) as total
    FROM security_logs
    GROUP BY risk_level
    ORDER BY total DESC
"""
df3 = pd.read_sql_query(query3, conn)
print(df3)
df3.to_csv(f"{reports_path}/risk_summary.csv", index=False)
print("Saved to reports/risk_summary.csv ✅")

print()
print("=" * 40)
print("QUERY 4 - Login activity over time")
print("=" * 40)
query4 = """
    SELECT 
        DATE(timestamp) as date,
        COUNT(*) as total_logins,
        SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed_logins,
        SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as success_logins
    FROM security_logs
    GROUP BY DATE(timestamp)
    ORDER BY date
"""
df4 = pd.read_sql_query(query4, conn)
print(df4.head(10))
df4.to_csv(f"{reports_path}/login_activity.csv", index=False)
print("Saved to reports/login_activity.csv ✅")

print()
print("=" * 40)
print("QUERY 5 - KPI summary cards")
print("=" * 40)
query5 = """
    SELECT
        COUNT(*) as total_events,
        SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as total_failed,
        SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) as total_success,
        SUM(CASE WHEN risk_level = 'high' THEN 1 ELSE 0 END) as high_risk_events
    FROM security_logs
"""
df5 = pd.read_sql_query(query5, conn)
print(df5)
df5.to_csv(f"{reports_path}/kpi_summary.csv", index=False)
print("Saved to reports/kpi_summary.csv ✅")

conn.close()
print()
print("=" * 40)
print("ALL QUERIES COMPLETE!")
print("=" * 40)
print("Files saved in reports/ folder:")
print("  failed_logins.csv")
print("  suspicious_ips.csv")
print("  risk_summary.csv")
print("  login_activity.csv")
print("  kpi_summary.csv")
