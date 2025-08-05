Approval Loop Detection App

 Overview

The Approval Loop Detection App is a Python-based application built to analyze approval audit logs for detecting suspicious activity like approval loops. It's designed with usability and extensibility in mind, providing both *web-based* and *desktop-based* interfaces.

# Key Features

- 🔄 Detects circular approval loops (e.g., A → B → A)
- 📊 Visualizes approval chains using graphs
- 📁 Supports file upload for audit logs
- 📈 Displays summary statistics of audit data
- 🔐 Configurable password protection
- 🧭 Dual interface: Streamlit (web) & Tkinter (desktop)


## 📁 Folder Structure

├── src/ # Main source code
├── data/ # Input audit logs (CSV/JSON/etc.)
├── archive/ # Output files and detected loops
├── configs/ # Settings and configurations
├── logs/ # Log files for application runs
├── assets/ # Icons, images for UI
└── docs/ # Documentation files

