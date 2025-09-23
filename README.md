# Sales Forecasting with Explainable AI: A Proof of Concept (PoC)

## Overview

- This project simulates a real-world data science proof of concept (PoC) aimed at forecasting daily retail sales using historical sales data and weather conditions. The primary goal is not only to build an accurate predictive model, but also to **interpret and explain** its behavior using Explainable AI (XAI) techniques.

- This is a project with case study: Sales Forecasting and Demand Prediction Using LightGBM and SHAP from AIO2025 Course, guided by Dr. Thai Ha Nguyen. 

## Objectives

- Build a reliable forecasting model for store-level, item-specific daily sales.
- Analyze the relationship between external features (e.g. weather, time, seasonality) and sales behavior.
- Use **Explainable AI** to interpret predictions and understand model decision-making.
- Present findings that can support data-driven decisions for stakeholders.

### 📁 Data Description

**1. Sales Data (2016 & 2017)**

- `date`, `province`, `store_id`, `store_name`
- `category`, `item_id`, `item_name`, `sales`

**2. Weather Data**

- `date`, `city`, `temperature`, `humidity`, `season`

---

## Proof of Concept

### 1. **Data Integration & Cleaning**

- Convert dates to time features (e.g., day of week, month, holiday).
- Handle missing values, incorrect types, and inconsistent entries.
- Handle outlier values.
- Merge sales and weather data by date and location.