import streamlit as st
import joblib
import pandas as pd

# Load model, vectorizer, and dataset
model = joblib.load('passmodel.pkl')
vectorizer = joblib.load('tfidfvectorizer.pkl')
df = pd.read_csv('drugsComTrain_raw.xls')

# Function to extract top 3 drugs
def top_drugs_extractor(condition, df):
    top_drugs = (
        df[df['condition'] == condition]
        .groupby('drugName')
        .agg({'rating': 'mean', 'usefulCount': 'sum'})
        .sort_values(['rating', 'usefulCount'], ascending=False)
        .head(3)
        .index.tolist()
    )
    return top_drugs

# Streamlit App UI
st.title("💊 Drug Review Analyzer")
st.markdown("This app predicts the medical condition based on your review and suggests the top 3 drugs.")

user_input = st.text_area("📝 Enter your drug review here:")

if st.button("🔍 Predict and Recommend"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")

        
    else:
        prediction = model.predict(vectorizer.transform([user_input]))[0]
        st.success(f"🩺 Predicted Condition: **{prediction}**")
        st.markdown("### ✅ Top 3 Recommended Drugs:")
        top_drugs = top_drugs_extractor(prediction, df)
        for i, drug in enumerate(top_drugs, 1):
            st.write(f"{i}. {drug}")