import streamlit as st
from textblob import TextBlob

# Page settings
st.set_page_config(page_title="Text Sentiment Analyzer", page_icon="🔍")
st.title("🔍 Text Sentiment Analyzer")

# Text input from user
text = st.text_area("Enter text to analyze:")

# Analyze button
if st.button("Analyze Sentiment"):
    if not text.strip():
        st.warning("Please enter some text!")
    else:
        # Perform sentiment analysis
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Determine sentiment
        if polarity > 0:
            sentiment = "Positive 😀"
        elif polarity < 0:
            sentiment = "Negative ☹️"
        else:
            sentiment = "Neutral 😐"

        # Display results
        st.subheader("Result")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Polarity:** {polarity:.2f}")
        st.write(f"**Subjectivity:** {subjectivity:.2f}")
