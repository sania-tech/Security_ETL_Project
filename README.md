# Security Log Integration System with Power BI Reports (ETL + Dashboard)

An automated security log processing and visualization system combining ETL pipelines with Power BI dashboards.

---

## 📋 Project Overview

**Security Log Integration System** is a comprehensive solution designed to automate the collection, processing, analysis, and visualization of security log data. Built as an academic research project, this system addresses a critical challenge security administrators face: manually reviewing large volumes of logs to identify suspicious activities, failed login attempts, and potential security threats.

### 🎯 Problem Statement
System administrators often need to manually review large security logs, which is:
*   **Time-consuming:** Manual processes are slow and error-prone.
*   **Repetitive:** Same tasks are performed across multiple systems.
*   **Inefficient:** It is difficult to identify patterns and anomalies in massive datasets.

###  Solution
This project automates the entire workflow:
*   **Collect:** Raw security log data aggregation.
*   **Process:** ETL pipeline for data transformation.
*   **Analyze:** Generate meaningful insights and metrics.
*   **Visualize:** Interactive dashboards for actionable intelligence.

---

## 🏗️ Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    Raw Security Logs                        │
│                (Various Sources & Formats)                  │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │         ETL Pipeline         │
              │   • Extract                  │
              │   • Transform                │
              │   • Load                     │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │       SQLite Database        │
              │       security_logs.db       │
              └──────────────┬───────────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │      Power BI Dashboard      │
              │   • Real-time Metrics        │
              │   • Trend Analysis           │
              │   • Anomaly Detection        │
              └──────────────────────────────┘

## 📊 Live Dashboards

Access the project dashboards here:

| Dashboard | Purpose | Link |
| :--- | :--- | :--- |
| **Power BI Report** | Main security analytics dashboard | [Security Log Integration Dashboard](#) |
| **Base44 UI** | Design implementation & data visualization | [Security Dashboard](#) |
| **Project Planning** | Notion workspace with project details | [Security Log Integration System](#) |

---

## 🎨 Key Features

### 📈 Data Processing
*  Automated ETL pipeline for log aggregation
*  Multi-format log file support
*  Data validation and cleaning
*  Real-time processing capabilities

### 🔍 Analytics & Insights
*  Failed login attempt detection
*  Suspicious activity identification
*  Trend analysis over time periods
*  User activity patterns
*  Threat severity classification

### 📊 Visualization
*  Interactive Power BI dashboards
*  Real-time metric updates
*  Customizable reports
*  Export functionality
*  Historical trend tracking

### 🔐 Security
*  Data encryption support
*  Access control mechanisms
*  Audit logging
*  Compliance-ready reporting

---

## 💻 Technology Stack

| Component | Technology | Language |
| :--- | :--- | :--- |
| **Language** | Python 3.8+ | Python |
| **Database** | SQLite | SQL |
| **ETL** | Custom Python scripts, Pandas | Python |
| **Visualization** | Power BI, Base44 UI | Power BI Service / Desktop |
| **Data Processing** | NumPy, Pandas | Python |
| **Version Control** | Git | GitHub |

---

## 📁 Project Structure

```text
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

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher
* pip (Python package manager)
* SQLite3
* Power BI Desktop (for dashboard customization)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sania-tech/Security_ETL_Project.git](https://github.com/sania-tech/Security_ETL_Project.git)
   cd Security_ETL_Project

# 🔐 Security Logs ETL & Analytics System

An end-to-end **ETL pipeline and analytics dashboard system** for processing, analyzing, and visualizing security logs using Python, SQLite, Power BI, and Base44 UI.

---

### Install dependencies
```bash
pip install -r requirements.txt

