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

### ✅ Solution
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
