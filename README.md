# **Mortgage Default Risk Prediction**

Predicting mortgage default risk is a crucial task in the financial industry. It helps lenders identify high-risk customers and take preemptive measures to minimize losses. This project leverages advanced machine learning techniques to build predictive models, offering insights into the key factors driving mortgage defaults while ensuring the solution is scalable and interpretable.

The project encompasses:
- Data preprocessing and feature engineering to prepare the data.
- Training and evaluating multiple models, including Logistic Regression, Random Forest, and XGBoost.
- Model interpretability using SHAP for transparent decision-making.
- Deployment-ready code with a REST API and Docker for scalability.

This repository serves as a comprehensive example of applying machine learning to solve real-world financial challenges.

## **Overview**
This project demonstrates the development of a machine learning model to predict mortgage default risk. The workflow includes:
1. Data preprocessing.
2. Feature engineering.
3. Model training and evaluation.
4. Model interpretability using SHAP.
5. Risk scoring mechanism.

## Key Features

- **Model Implementation**: Logistic Regression, Random Forest, and XGBoost.
- **Threshold Adjustment**: Enhanced recall for high-risk categories.
- **Cross-Validation**: Ensuring model robustness.
- **Risk Scoring**: Providing actionable insights.
- **Interpretability**: Utilizing SHAP for feature importance.
- **Deployment**: Scalable solution with Docker.

## **Data Information**

This project uses a dataset to analyze mortgage default risk. Due to its size, the dataset is not included in this repository. You can download the data from the following source:

- [Kaggle - Home Credit Default Risk Dataset](https://www.kaggle.com/c/home-credit-default-risk/data)

### **Instructions to Set Up Data**

1. Download the following files from the data source:
   - `application_train.csv`
   - `application_test.csv`
2. Place the downloaded files in the `data/` directory within this repository:


---

## **Key Features**
- Implements Logistic Regression, Random Forest, and XGBoost models.
- Adjusted threshold for better recall in high-risk categories.
- Cross-validation for model robustness.
- Risk scoring system for actionable insights.
- Detailed visualizations and interpretability using SHAP.

---

### File Structure

- **Mortgage_Default_Risk_Prediction/**
  - `Dockerfile` - Docker configuration for deploying the application
  - **data/**
    - `application_train.csv` - Training dataset
    - `application_test.csv` - Testing dataset
  - **scripts/**
    - `mortgage_default_analysis.py` - Main script for analysis
  - **output/**
    - `xgboost_final_model.pkl` - Final trained model
    - `cross_validation_results.csv` - Cross-validation results
    - `risk_bucket_distribution.png` - Risk bucket visualization
    - `shap_feature_importance.png` - SHAP summary plot
    - `test_data_with_risk_scores.csv` - Risk-scored test dataset
  - `README.md`
  - `requirements.txt` - List of required libraries



## **Setup Instructions**

### **Prerequisites**
	Ensure you have the following installed:
	1. **Python** (>=3.8)
	2. Libraries:
	   - `pandas`
	   - `numpy`
	   - `matplotlib`
	   - `seaborn`
	   - `scikit-learn`
	   - `xgboost`
	   - `shap`
	   - `joblib`
	   - `imblearn`


### **Installation Steps**

Installation

	1. Clone this repository:

		1) git clone https://github.com/himanshu-dandle/Mortgage-Default-Risk-Prediction.git
	
		2) Install Dependencies

			pip install -r requirements.txt
			
		3) Place the dataset files (application_train.csv and application_test.csv) in the data/ directory.
	
	2. Running the Notebook
		1) Launch Jupyter Notebook:
				jupyter notebook
		2) Open mortgage_default_analysis.ipynb and execute the cells sequentially.
		
## Docker Deployment

### Prerequisites
	
	Install Docker from Docker's official website.
	
### Steps
		1) Build the Docker image:

			docker build -t mortgage-default-prediction .
		2) Run the Docker container:

			docker run -p 5000:5000 mortgage-default-prediction
		3) Access the API:
			The API will be accessible at http://localhost:5000.

# Key Insights
Model Performance: XGBoost achieved superior performance with an AUC of 0.85.
Feature Importance: EXT_SOURCE_3, DAYS_BIRTH, and AMT_CREDIT are significant predictors.
Risk Stratification: Implemented a risk scoring system categorizing applicants into low, medium, and high-risk groups.
