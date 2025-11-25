# Crop Yield Prediction Web Application for Pakistan 🇵🇰

[![Django](https://img.shields.io/badge/Django-5.2-brightgreen.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-RMSE%20964-9cf.svg)](https://xgboost.ai/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-success.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live-Demo-orange)](https://muneebtalks.pythonanywhere.com) <!-- update after deployment -->

> A full-stack Django web application that predicts crop yield (kg/ha) and total production (tonnes) for major Pakistani crops using official FAO data (1961–2023) and XGBoost machine learning model.


## Features
- Responsive Bootstrap 5 design (mobile-friendly)
- XGBoost Regressor model trained on FAO Pakistan crop data
- Predict yield for Wheat, Maize (corn), Potatoes, Sorghum
- Real-time total production calculation from land area
- Model performance: **RMSE 964 kg/ha** on test set
- Clean, professional UI with Pakistan green theme

## Tech Stack
- Backend: Django 5.2
- Machine Learning: XGBoost + scikit-learn + joblib
- Frontend: Bootstrap 5 + Django Templates
- Database: SQLite (production-ready with PostgreSQL possible)
- Data Source: FAO Official Crop Production Data (1961–2023)

## Data Source
- [Pakistan crop production analysis FAOSTAT_data](https://www.kaggle.com/code/datascientist97/pakistan-crop-production-analysis/)

![Screenshot_20-11-2025_105213_127 0 0 1](https://github.com/user-attachments/assets/059639be-afb7-4d68-b34c-af443e0b70bf)
![Screenshot_20-11-2025_105225_127 0 0 1](https://github.com/user-attachments/assets/f90f27e7-eec9-45db-ae2b-0ad4d7a9e0f8)
![Screenshot_20-11-2025_105240_127 0 0 1](https://github.com/user-attachments/assets/ad3d471d-fb28-49e0-a567-6c44edac5772)


## 🚀 Quick Start (Local) – Ready in 30 Seconds!

### One-command setup:

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/pakistan-crop-yield-predictor.git
cd pakistan-crop-yield-predictor

# 2. Create & activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations & start server
python manage.py migrate
python manage.py runserver


