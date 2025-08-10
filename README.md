# Spam-Ham Classifier: Real-Time SMS Classification Dashboard
An interactive Streamlit-based web application that classifies text messages as Spam or Ham (non-spam) using a trained machine learning model. Built for quick, reliable, and user-friendly spam detection.

## Tech Stack
The project was built using the following tools and technologies:
- 🐍 Python – Programming language used for model building and app logic.
- 📊 Scikit-learn – ML library used for model training and evaluation.
- 📝 Pandas & NumPy – Data cleaning, preprocessing, and manipulation.
- 🔤 NLTK (Natural Language Toolkit) – Text preprocessing (tokenization, stopwords removal, stemming).
- 📂 Google Colab – Development and training environment.
- 🌐 Streamlit – Web framework for building the interactive UI.
- 📁 Source Control – Dataset and code sourced from GitHub.

## Data Source
Source: Public dataset from GitHub containing labeled SMS messages (Spam or Ham).
The dataset includes:
📩 Message text – Raw SMS content.
🏷 Labels – “spam” or “ham” tags for supervised learning.
Preprocessed version used for model training to improve classification accuracy.

## Features / Highlights
Business Problem
Spam messages cause inconvenience, waste time, and can lead to financial loss through scams and phishing attacks. Manually identifying them is inefficient and unreliable.

## Goal of the Dashboard
To create a real-time, browser-based spam detection tool that:
Accurately classifies messages as spam or ham.
Helps individuals and organizations filter unwanted content.
Demonstrates the application of NLP and ML in real-world use cases.

## Walkthrough of Key Components
- Text Input Box – Users can type or paste a message for classification.
- Prediction Output Panel – Displays classification result (“Spam” or “Ham”) instantly.
- Model Confidence Score – Shows prediction probability.
- Data Preprocessing Pipeline – Automatic cleaning, tokenizing, stopword removal, and stemming before classification.
- Interactive Streamlit Interface – No coding required for the user; everything runs in-browser.

## Business Impact & Insights
Email & SMS Filtering – Can be adapted for large-scale spam filtering systems.
Cybersecurity – Early detection of phishing or scam messages.
Productivity – Reduces distractions by filtering irrelevant content.
ML Demonstration – Great example of applying NLP techniques to a real-world dataset.

## App Preview
![App Preview](https://github.com/souravjha127/Spam-Ham-Classifier/blob/main/Spam_detection.png)
