# 💊 Drug Review Analyzer

This Streamlit web application predicts a medical condition based on a user's drug review and suggests the top 3 most effective drugs for the predicted condition. It utilizes natural language processing (NLP) techniques and a machine learning model trained on the Drugs.com dataset.

---

## 🚀 Features

- 📝 Accepts user-written drug reviews.
- 🧠 Predicts the medical condition related to the review using a trained model.
- 💡 Recommends the top 3 drugs for that condition based on average ratings and usefulness scores.
- 🎯 User-friendly and interactive interface built with Streamlit.

---

## 📦 Tech Stack

- **Python**
- **Streamlit**
- **scikit-learn**
- **pandas**
- **joblib**
- **TF-IDF Vectorizer**
- **Drugs.com Dataset**

---

## 📁 Files in the Repo

| File/Folder             | Description |
|------------------------|-------------|
| `app.py`               | Main Streamlit app script |
| `passmodel.pkl`        | Trained ML model for condition prediction |
| `tfidfvectorizer.pkl`  | Saved TF-IDF vectorizer |
| `drugsComTrain_raw.xls`| Raw dataset containing drug reviews |
| `README.md`            | Project documentation |
| `requirements.txt`     | Python dependencies (you can generate this using `pip freeze > requirements.txt`) |

---
