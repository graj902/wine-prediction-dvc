# Wine Quality Prediction - MLOps with DVC & AWS S3

This project demonstrates a professional MLOps workflow for versioning both code (via Git) and large-scale datasets (via DVC). By decoupling data from code, we ensure repository performance while maintaining 100% reproducibility.

## 🏗️ Architecture
- **Source Code:** Versioned in GitHub.
- **Data & Artifacts:** Versioned via DVC and stored in **AWS S3** (`mlops-bucket-for-myown-mlpos-project`).
- **Environment:** Isolated via Python Virtual Environments.



## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/graj902/wine-prediction-dvc.git](https://github.com/graj902/wine-prediction-dvc.git)
cd wine-prediction-dvc
2. Setup Environment
Bash

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. Pull the Data
Since the raw data is stored in S3, you need to pull it using DVC. Ensure you have AWS credentials configured.

Bash

dvc pull
🛠️ Tech Stack
DVC: Data Version Control for tracking datasets and model files.

AWS S3: Remote storage for large data artifacts.

Git: Version control for the codebase and DVC metadata pointers.

Python 3.10+: Core programming language.

📈 Data Lineage
Every version of the dataset is tracked by its MD5 hash in the .dvc files. This allows the team to:

Time-travel to previous data versions using git checkout + dvc checkout.

Ensure environment parity across development and production.

Prevent repository bloat by keeping binary files out of Git history.
