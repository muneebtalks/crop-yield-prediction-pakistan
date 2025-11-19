# Crop Yield Prediction Web Application for Pakistan 🇵🇰

[![Django](https://img.shields.io/badge/Django-5.2-brightgreen.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-RMSE%20964-9cf.svg)](https://xgboost.ai/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-success.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/Live-Demo-orange)](https://muneebtalks.pythonanywhere.com) <!-- update after deployment -->

> A full-stack Django web application that predicts crop yield (kg/ha) and total production (tonnes) for major Pakistani crops using official FAO data (1961–2023) and XGBoost machine learning model.

## Live Demo
https://muneebtalks.pythonanywhere.com 

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

## Quick Start (Local)

```bash
git clone https://github.com/muneebtalks/crop-yield-prediction-pakistan.git
cd crop-yield-prediction-pakistan/crop-yield-pk
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py          # trains & saves XGBoost model
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver