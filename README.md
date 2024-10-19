# Sentiment Analysis of RBI Monetary Policy Statements

## Project Overview

This project leverages **machine learning** to quantify the sentiment in **RBI monetary policy statements** and predict their impact on financial indices. The aim is to provide insights that help **risk-bearing individuals** make better investment decisions by interpreting central bank communications.

## Motivation

Central banks influence the economy through direct actions and communication, shaping market expectations. Our project focuses on analyzing **Monetary Policy Committee (MPC) minutes**, **Governor's statements**, and other key documents to extract sentiment and clarity, with the goal of assessing their impact on market behavior.

## Problem Statement

Experts believe that **RBI communications** impact the financial markets. Our project quantifies these communications into sentiment scores and evaluates their predictive power for market reactions, thus providing a useful tool for investors.

## Approach

We use **Natural Language Processing (NLP)** techniques combined with **financial sentiment dictionaries** to classify the tone of RBI statements. Specifically, we:

- Use **sentiment scoring** with pre-defined financial lexicons, including the **Loughran-McDonald Dictionary** and a custom-built dictionary.
- Perform **readability analysis** using the **Farr-Jenkins-Paterson (FJP) index**.
- Utilize **word embeddings** (Doc2Vec) to represent statements.
- Apply **LSTM** models to capture the long-term dependencies in the data for market prediction.

## Data

The dataset includes:

- **Bi-monthly MPC minutes** (FY 2014-15 to present)
- **Governor's statements** from quarterly monetary policy reviews (FY 2013-14 to FY 2005-06)
- **Annual Monetary and Credit Policy** & its mid-term reviews (FY 2004-05 to FY 2000-01)
- **FOMC minutes** (FY 2000 to present)

Key features extracted include **sentiment scores**, **readability indices**, and **financial metrics** from **NIFTY50** and other indices.

## Methodology

1. **Preprocessing**: Text cleaning, stopword removal, and lemmatization.
2. **Sentiment Analysis**: Using financial dictionaries to assign positive and negative scores.
3. **Readability Analysis**: Calculating FJP index for each statement to assess communication clarity.
4. **Word Embeddings**: Using **Doc2Vec** to create document-level vectors representing the entire statement.
5. **Modeling**:
   - **LSTM** (Long Short-Term Memory) models for time-series analysis.
   - Two approaches: breaking the text into clusters of 450 words and maintaining full document integrity.

## Results

We experimented with different modeling approaches:

- **Breaking sentences into clusters**: Precision: 0.518, Recall: 0.516, Test Accuracy: 0.516
- **Maintaining document integrity**: Precision: 0.667, Recall: 0.669, Balanced Accuracy: 0.639

By preserving document context, we achieved better results in sentiment classification and prediction.

## Challenges

1. **Class Imbalance**: We faced significant imbalance in the data and applied a thresholding technique to address it.
2. **Data Augmentation**: Used back translation to expand the training dataset.
3. **Noisy Target Variable**: The NIFTY50 index's annualized return of 12% was subtracted from the market returns to reduce noise.

## Real-World Applications

This solution can be extended with a richer dataset including other central bank communications to help investment firms get an edge in predicting market reactions and managing risk.

## Contributors

- **Ayush Bhatnagar, Abhiraaj Sharma, Tanushi Khandelwal**  
  Plaksha University | Data Science | Machine Learning & Pattern Recognition (MLPR)
