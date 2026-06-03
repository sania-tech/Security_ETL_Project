# Security Log Integration System with Power BI Reports

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)](#)

An automated ETL and dashboard system for collecting, processing, analyzing, and visualizing security log data.

## Project Overview

Security Log Integration System helps reduce manual log review by automating the detection of failed login attempts, suspicious activity, and security trends. It processes raw logs through an ETL pipeline, stores results in SQLite, and presents insights through Power BI dashboards.

## Key Features

- Automated ETL pipeline for security logs
- Support for multiple log formats
- Data cleaning, validation, and transformation
- Failed login and suspicious activity detection
- Trend and user behavior analysis
- Interactive Power BI dashboards
- Historical reporting and export options

## Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    Raw Security Logs                        │
│                (Various Sources & Formats)                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────────────┐
        │      ETL Pipeline               │
        │  • Extract                      │
        │  • Transform                    │
        │  • Load                         │
        └────────────┬─────────────────────┘
                     │
        ┌────────────▼──────────────────┐
        │    SQLite Database             │
        │  security_logs.db              │
        └────────────┬─────────────────────┘
                     │
        ┌────────────▼──────────────────┐
        │  Power BI Dashboard            │
        │  • Real-time Metrics           │
        │  • Trend Analysis              │
        │  • Anomaly Detection           │
        └────────────────────────────────┘
```

## Technology Stack

| Component | Technology |
| --- | --- |
| Language | Python 3.8+ |
| Database | SQLite |
| ETL | Python scripts, Pandas |
| Visualization | Power BI, Base44 UI |
| Data Processing | NumPy, Pandas |
| Version Control | Git |

## Project Structure

```text
Security_ETL_Project/
├── etl/          # Extract, transform, load, and query scripts
├── db/           # SQLite database
├── data/         # Raw and processed log files
└── reports/      # Dashboards and report scripts
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip
- SQLite3
- Power BI Desktop

### Installation

```bash
git clone https://github.com/sania-tech/Security_ETL_Project.git
cd Security_ETL_Project
pip install -r requirements.txt
```

## Usage

Run the ETL pipeline:

```bash
python etl/extract.py
python etl/transform.py
python etl/load.py
```

Run analytics queries:

```bash
python etl/queries.py
```

Generate the HTML dashboard:

```bash
python reports/dashboard.py
```

## Dashboard Insights

The dashboard includes login analysis, threat detection, security event trends, user behavior, and system health metrics.

## Documentation

- [Power BI Dashboard](https://app.powerbi.com/groups/me/reports/cdfa1443-3223-4296-a04a-0e86c7ae1d1a)
- [Base44 Dashboard](https://security-dashboard.base44.app)
- [Notion Project Plan](https://app.notion.com/p/Security-Log-Integration-System-ETL-Power-BI-32375ec52b5c80abb1a5efd34fd69d11)

## Project Details

| Detail | Value |
| --- | --- |
| Author | Sania Sohail |
| Supervisor | dr inż. Dominika Lisiak-Felicka |
| Institution | School of Computer Science & Technologies |
| Location | Warsaw |
| Year | 2026 |
| Project Type | Academic Research Project |

## Future Enhancements

- Machine learning anomaly detection
- Real-time alert notifications
- API endpoint for log ingestion
- Multi-database support
- Automated report generation and scheduling

## License

This project is licensed under the MIT License.

---

Made with 🌻 by Sania Sohail
