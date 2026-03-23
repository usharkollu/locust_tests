# 🚀 Locust Performance Testing Suite
This repository contains a professional-grade load testing framework using Locust, fully integrated into Azure DevOps CI/CD. It provides a scalable way to execute performance tests, manage multiple environments, and visualize results through automated reporting.

## 🌟 Project Achievements
* **Automated CI/CD Pipeline:** Integrated directly into azure-pipelines.yml using standard Python execution for full control over the testing lifecycle and environment. 

* **Dynamic Environment Logic:** Supports seamless switching between prod, stg, and other environments via the LOCUST_ENV variable and a centralized configuration loader for each env that will pass or fail the test run.

* **Automated Results Artifacts:** Every execution automatically generates and publishes a visual HTML report as a Pipeline Artifact for immediate performance analysis.



## 📂 Project Structure
locustfile.py: The primary test suite entry point.

tests/: Modularized test scenarios (e.g., get_AllBookingIds.py).

utils/: Reusable helper functions for configuration and data parsing.

utils/base.py: Core logic for environment setup and HTTP client configuration.

utils/load_config: load configuration for each environment.

envs/: Environment-specific .env configuration files.

## 🚀 Quick Start
To run the tests locally with the same configuration as the CI/CD pipeline:

<pre>
Bash
LOCUST_ENV=prod locust -f locustfile.py --headless --html locust_report.html
</pre>

### 📊 How to Access Results in Azure

1. Navigate to your Pipeline Run Summary.
2. Click the **Published Artifacts** link in the **Related** section.
3. Download `locust_report.html` from the **LocustReport** folder.
