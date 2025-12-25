# 🏥 Diabetes Prediction AI

A machine learning web application that predicts the likelihood of diabetes in patients based on medical diagnostic measurements. This project uses a **Random Forest Classifier** trained on the Pima Indians Diabetes Database and is deployed as a live web application using **Flask** and **Docker**.

**🔴 Live Demo:** [Link](https://pima-diabetes-prediction.onrender.com)

## ⚪ Project Overview

Early detection of diabetes can significantly improve patient outcomes. This application allows users to input specific health metrics (such as glucose level, BMI, and age) to receive an instant prediction on whether they are likely to be diabetic.

The system was built by training a machine learning model, wrapping it in a Flask API, containerizing it with Docker, and deploying it to the cloud via a CI/CD pipeline.

## ⚪ Tech Stack

* **Machine Learning:** Python, Scikit-Learn, Pandas, NumPy
* **Model:** Random Forest Classifier
* **Web Framework:** Flask
* **Containerization:** Docker
* **Deployment:** Render (PaaS) with CI/CD
* **Frontend:** HTML5, CSS3

## ⚪ Model Details

* **Dataset:** [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
* **Algorithm:** Random Forest Classifier
* **Training:** The model was trained on 8 diagnostic features including pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, and age.
* **Preprocessing:** Data cleaning and feature selection were performed to optimize model accuracy. No standard scaling was applied as Random Forest is a tree-based algorithm invariant to feature scaling.

## ⚪ Features

* **Real-time Prediction:** Users get instant results after submitting the form.
* **User-Friendly Interface:** Clean, responsive design for easy data entry.
* **Robust Backend:** Powered by Flask and Gunicorn for reliable performance.
* **Production Ready:** Dockerized environment ensures consistent behavior across different platforms.

## ⚪ How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Tharmeem1999/Pima_Diabetes_Prediction.git
    ```

2.  **Build the Docker Image**
    ```bash
    docker build -t diabetes-app .
    ```

3.  **Run the Container**
    ```bash
    docker run -p 5000:5000 diabetes-app
    ```

4.  **Access the App**
    Open your browser and go to `http://localhost:5000`

## 📂 Project Structure

```text
├── app.py 								# Flask application entry point
├── Pima_Indians_Diabetes_model.pickle 	# Serialized Machine Learning Model
├── Dockerfile 							# Docker configuration
├── requirements.txt 					# Python dependencies
├── Pima_Diabetes.ipynb 				# Model training notebook
├── diabetes.csv                        # The original dataset
├── Pima_Diabetes.ipynb                 # Jupyter Notebook (EDA, Preprocessing, Model Training)
├── README.md                           # Project Documentation
└── templates └── index.html 			# Frontend user interface
```
## ⚪ Screenshot

<img width="832" height="695" alt="Image" src="https://github.com/user-attachments/assets/189e6cf8-f08d-47c3-af87-b28628765029" />
