from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load models
with open('tfidf_classification.pkl', 'rb') as f:
    tfidf = pickle.load(f)

with open('model_classification.pkl', 'rb') as f:
    model = pickle.load(f)

with open('k_means_model.pkl', 'rb') as f:
    k_means = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

cluster_names = {
    0: 'Fraudulent Activity Reports',
    1: 'Credit Report Disputes',
    2: 'Identity Theft Claims',
    3: 'Debt Collection Compliance',
    4: 'Inaccurate Credit Reporting'
}
id_to_category = {
    0: "Credit reporting, repair, or other",
    1: "Debt collection",
    2: "Loan",
    3: "Credit card or prepaid card",
    4: "Checking or savings account",
    5: "Money transfer, virtual currency, or money service"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    new_complaint = request.form['complaint']
    X_new = tfidf.transform([new_complaint])
    predicted_category_id = model.predict(X_new)[0]
    category = id_to_category[predicted_category_id]

    if category == "Credit reporting, repair, or other":
        new_complaint_dtm = tfidf_vectorizer.transform([new_complaint])
        predicted_cluster = k_means.predict(new_complaint_dtm)[0]
        cluster_name = cluster_names[predicted_cluster]
        return render_template('result.html', category=category, cluster_name=cluster_name)
    
    return render_template('result.html', category=category)

if __name__ == '__main__':
    app.run(debug=True)
