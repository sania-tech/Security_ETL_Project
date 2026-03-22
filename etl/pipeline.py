from extract import extract
from transform import transform
from load import load

print("=" * 40)
print("SECURITY ETL PIPELINE STARTING")
print("=" * 40)

# Step 1 - Extract
raw_data = extract()

# Step 2 - Transform
clean_data = transform(raw_data)

# Step 3 - Load
load(clean_data)

# Save clean CSV to reports folder too
clean_data.to_csv("reports/clean_logs.csv", index=False)

print("=" * 40)
print("PIPELINE COMPLETE!")
print("=" * 40)
print("Output files:")
print("  db/security_logs.db    <- SQLite database")
print("  reports/clean_logs.csv <- Clean CSV for Power BI")
