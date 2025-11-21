# Bangalore Price Predictor

## Project Overview

The **Bangalore Price Predictor** is a web-based application designed to predict real estate prices in Bangalore using machine learning models. The project leverages data-driven insights and modern web technologies to provide accurate property price predictions.

---

## Features

* **Predict Property Prices:** Users can input property details and get predicted prices.
* **Multiple Regression Models:**

  * **Linear Regression**
  * **Ridge Regression**
  * **Lasso Regression**
* **Interactive Frontend:** Built using **HTML, CSS, and JavaScript**.
* **Backend:** Powered by **Flask** for handling predictions and serving the web application.

---

## Tools & Libraries

* **Python** for machine learning and data analysis
* **Pandas, NumPy, Scikit-Learn** for data preprocessing and modeling
* **Flask** for backend server
* **HTML/CSS/JS** for frontend interface
* **Jupyter Notebook** for model development and experimentation

---

## Folder Structure

```
BangalorePricePredictor/
│
├── .gitignore
├── README.md
├── requirements.txt
├── Cleaned_data.csv
├── Bengaluru_House_Data.csv
├── BangalorePriceModel.pkl
├── app.ipynb
├── main.py
├── templates/
└── static/
    ├── css/
    ├── js/
    └── images/
```

---

## Getting Started

### Installation

1. Clone the repository:

```bash
git clone <REPO_URL>
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

* Open your browser and navigate to `http://127.0.0.1:5000/` to use the app.

---

## Usage

* Enter property details such as location, area, BHK, etc.
* Click **Predict** to see the estimated price.

---

## Author

**Your Name**

---

## Notes

* The machine learning models are trained on historical Bangalore property data.
* Future improvements can include more features, data cleaning enhancements, and advanced modeling techniques.
