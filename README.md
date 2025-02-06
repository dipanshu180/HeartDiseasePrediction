# HeartDiseasePrediction
# Heart Disease Prediction Using Python

## 📌 Overview
This project predicts the likelihood of heart disease based on user input using a machine learning model trained on relevant medical data. The model is built using **Python** and deployed using **Flask** for web-based interaction.

## 🛠️ Technologies Used
- **Python**
- **Flask** (for web application)
- **Joblib** (for model loading)
- **Pandas** (for data processing)
- **Scikit-learn** (for training the model)
- **Git & GitHub** (for version control)

## 📂 Project Structure
```
📦 HeartDiseasePrediction
├── 📂 templates
│   ├── index.html  # Frontend UI
├── app.py  # Flask application
├── heart_disease_model.joblib  # Trained ML model
├── requirements.txt  # Required Python libraries
├── README.md  # Project documentation
└── .gitignore  # Files to ignore in Git
```

## 🚀 How to Run the Project
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/dipanshu180/HeartDiseasePrediction.git
cd HeartDiseasePrediction
```

### 2️⃣ Install Dependencies
Make sure you have Python installed. Then, install required packages:
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App
```sh
python app.py
```

### 4️⃣ Access the Web Application
Open your browser and go to:
```
http://127.0.0.1:5000/
```

## 🔍 How It Works
1. The user enters inputs like **age, chest pain type (cp), and maximum heart rate (thalach)**.
2. The trained **Machine Learning model** makes a prediction.
3. The app displays whether **Heart Disease is Present or Not**.

## 🏆 Model Details
- **Algorithm:** Logistic Regression (or any other used)
- **Training Data:** Kaggle Heart Disease Dataset (or mention your dataset)
- **Evaluation Metric:** Accuracy, Precision, Recall, F1-score

## 📜 License
This project is licensed under the MIT License.

---
Made with ❤️ by [Dipanshu]

