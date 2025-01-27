

# **Consumer Complaint Analysis**

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Dataset](#dataset)
5. [How It Works](#how-it-works)
6. [Future Enhancements](#future-enhancements)

---

## **Project Overview**
The **Consumer Complaint Analysis** project is a Flask-based web application designed to classify consumer complaints and analyze credit reporting narratives.  
It uses **machine learning** techniques to:
- Classify complaints into product categories.
- Further cluster credit reporting complaints into specific themes.

The project aims to streamline complaint analysis for businesses, helping them identify trends and improve customer satisfaction.

---

## **Features**
- **Complaint Classification**: Classifies complaints into predefined categories (e.g., Credit Reporting, Debt Collection).
- **Clustering for Credit Reporting**: Groups credit reporting complaints into themes such as *Fraudulent Activity Reports* or *Identity Theft Claims*.
- **User-Friendly Interface**: Submit complaints via a simple web form.
- **Real-Time Results**: Displays classification and clustering results instantly.

---

## **Technologies Used**
- **Programming Language**: Python
- **Framework**: Flask
- **Machine Learning**:
  - Classification: Random Forest
  - Clustering: K-Means
- **NLP**:
  - TF-IDF for text vectorization
- **Frontend**:
  - HTML, CSS
- **Other Tools**:
  - Pickle for model serialization

---

## **Dataset**
- **Source**: Consumer Financial Protection Bureau (CFPB) Consumer Complaint Database. [https://www.consumerfinance.gov/complaint/]
- **Description**:
  - Contains thousands of consumer complaints with narrative descriptions.
  - Categories include Credit Reporting, Debt Collection, Loans, etc.

---

## **How It Works**
1. **Input**: Users submit a complaint narrative through the web interface.
2. **Classification**:
   - The complaint is classified into one of the predefined product categories.
3. **Clustering** (if applicable):
   - If the complaint is related to *Credit Reporting*, it is further clustered into specific themes using K-Means.
4. **Output**:
   - Displays the product category.
   - For credit reporting complaints, also shows the assigned cluster and its description.

---

## **Future Enhancements**
- **Improved Clustering**: Experiment with advanced clustering algorithms like DBSCAN.
- **Sentiment Analysis**: Analyze the tone of consumer complaints.
- **Dashboard**: Add a dashboard for visualizing trends and insights.
- **Multi-Language Support**: Extend the application to support complaints in multiple languages.

---
