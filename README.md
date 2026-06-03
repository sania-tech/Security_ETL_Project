Security Log Integration System with Power BI Reports (ETL + Dashboard)
License: MIT Python 3.8+ Status: Active

An automated security log processing and visualization system combining ETL pipelines with Power BI dashboards

📋 Project Overview
Security Log Integration System is a comprehensive solution designed to automate the collection, processing, analysis, and visualization of security log data. Built as an academic research project, this system addresses the critical challenge security administrators face: manually reviewing large volumes of logs to identify suspicious activities, failed login attempts, and potential security threats.

🎯 Problem Statement
System administrators often need to manually review large security logs, which is:

Time-consuming - Manual processes are slow and error-prone
Repetitive - Same tasks performed across multiple systems
Inefficient - Difficult to identify patterns and anomalies in massive datasets
✅ Solution
This project automates the entire workflow:

Collect - Raw security log data aggregation
Process - ETL pipeline for data transformation
Analyze - Generate meaningful insights and metrics
Visualize - Interactive dashboards for actionable intelligence
🏗️ Architecture
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
📊 Live Dashboards
Access the project dashboards here:

Dashboard	Purpose	Link
Power BI Report	Main security analytics dashboard	Security Log Integration Dashboard
Base44 UI	Design implementation & data visualization	Security Dashboard
Project Planning	Notion workspace with project details	Security Log Integration System
Key Features
- Data Processing
- Automated ETL pipeline for log aggregation
- Multi-format log file support
- Data validation and cleaning
- Real-time processing capabilities
- Analytics & Insights
- Failed login attempt detection
- Suspicious activity identification
- Trend analysis over time periods
- User activity patterns
- Threat severity classification
- Visualization
- Interactive Power BI dashboards
- Real-time metric updates
- Customizable reports
- Export functionality
- Historical trend tracking
- Security
- Data encryption support
- Access control mechanisms
- Audit logging
- Compliance-ready reporting
💻 Technology Stack
Component	Technology
Language	Python 3.8+
Database	SQLite
ETL	Custom Python scripts, Pandas
Visualization	Power BI, Base44 UI
Data Processing	NumPy, Pandas
Version Control	Git
📁 Project Structure
Security_ETL_Project/
│
├── README.md                 # Project documentation
├── .gitignore               # Git ignore rules
│
├── etl/                     # ETL Pipeline Module
│   ├── __init__.py
│   ├── extract.py           # Data extraction logic
│   ├── transform.py         # Data transformation logic
│   ├── load.py              # Data loading logic
│   └── queries.py           # Database queries
│
├── db/                      # Database
│   └── security_logs.db     # SQLite database (processed logs)
│
├── data/                    # Data Storage
│   ├── raw/                 # Raw log files
│   └── processed/           # Processed data files
│
└── reports/                 # Reports & Dashboards
    ├── dashboard.html       # HTML dashboard
    ├── dashboard.py         # Dashboard generation script
    └── power_bi_config.json # Power BI configuration
🚀 Getting Started
Prerequisites
Python 3.8 or higher
pip (Python package manager)
SQLite3
Power BI Desktop (for dashboard customization)
Installation
Clone the repository

git clone https://github.com/sania-tech/Security_ETL_Project.git
cd Security_ETL_Project
Install dependencies

pip install -r requirements.txt
Configure environment variables (if needed)

cp .env.example .env
# Edit .env with your configuration
Usage
Running the ETL Pipeline
python etl/extract.py          # Extract raw logs
python etl/transform.py        # Transform data
python etl/load.py             # Load to database
Querying Security Logs
python etl/queries.py          # Run analytics queries
Generating Reports
python reports/dashboard.py    # Generate HTML dashboard
Power BI Dashboard
Open Power BI Desktop
Load the connection to db/security_logs.db
Import or create visualizations
Publish to Power BI Service
📊 Dashboard Features
Power BI Dashboard Includes:
Login Analysis - Successful vs failed attempts by user/time
Threat Detection - High-risk activities and anomalies
Trend Analysis - Security events over time
User Behavior - Access patterns and unusual activities
System Health - Database and pipeline status
Base44 UI Includes:
Interactive security event visualization
Real-time data updates
Custom filtering and drill-down capabilities
Export options for reports
🔄 ETL Pipeline Details
Extract Phase
Reads security logs from multiple sources
Supports formats: .log, .csv, .json
Validates log format and integrity
Transform Phase
Parses timestamp and event data
Categorizes log entries (login, logout, access, error)
Identifies suspicious patterns
Enriches data with metadata
Load Phase
Stores processed data in SQLite database
Creates indexed tables for fast querying
Updates historical analytics
📈 Sample Metrics & KPIs
The system tracks:

Total failed login attempts
Unique users with suspicious activity
Peak hours for security events
Most frequently accessed resources
Failed authentication by user/time
Threat severity distribution
🔐 Security Considerations
- Encrypted database connections
- Role-based access control
- Audit trail of all system access
- GDPR-compliant data handling
- Regular backup and recovery procedures
Project Details
Detail	Value
Academic Institution	School of Computer Science & Technologies
Field of Study	Computer Science
Author	Sania Sohail
Student Index	47482
Supervisor	dr inż. Dominika Lisiak-Felicka
Location	Warsaw
Year	2026
Project Type	Academic Research Project
📚 Documentation
Notion Project Plan - Detailed project planning and research
Power BI Dashboard - Interactive analytics
Base44 Dashboard - UI/UX implementation
🤝 Contributing
This is an academic project. If you'd like to contribute improvements:

Fork the repository
Create a feature branch (git checkout -b feature/improvement)
Commit your changes (git commit -am 'Add improvement')
Push to the branch (git push origin feature/improvement)
Open a Pull Request
📧 Contact & Support
Author: Sania Sohail
Email: sania@tech.com
GitHub: @sania-tech
Project Issues: GitHub Issues
📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Supervisor: dr inż. Dominika Lisiak-Felicka for guidance and support
School of Computer Science & Technologies for resources and infrastructure
Power BI Community for documentation and best practices
📞 Future Enhancements
[ ] Machine learning anomaly detection
[ ] Real-time alert notifications
[ ] API endpoint for log ingestion
[ ] Multi-database support (PostgreSQL, MySQL)
[ ] Advanced SIEM integration
[ ] Mobile dashboard app
[ ] Automated report generation and scheduling
⭐ If you find this project useful, please consider giving it a star!

Made with ❤️ by Sania Sohail
