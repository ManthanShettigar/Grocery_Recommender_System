
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load your models and encoder here
xgb_model = joblib.load('./model/xgb_model.pkl') 
same_prod_model = joblib.load('./model/same_prod_model.pkl')
encoder = joblib.load('./model/target_encoder.pkl')
df = pd.read_csv('data/recommend_products.csv')


# Define recommend_products_for_user function
def recommend_products_for_user(user_id, num_recommendations=5):
    user_data = df[df['user_id'] == user_id]
    user_products = user_data['product_name'].unique()

    # Calculate product scores based on user behavior or other criteria
    # In this simplified example, we recommend the most popular products
    product_scores = df['product_name'].value_counts().reset_index()
    product_scores.columns = ['product_name', 'popularity']

    # Filter out products the user has already purchased
    product_scores = product_scores[~product_scores['product_name'].isin(user_products)]

    # Sort products by popularity and recommend the top N products
    recommended_products = product_scores.nlargest(num_recommendations, 'popularity')['product_name']

    return recommended_products.tolist()

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict customer re-order probability and recommend products.
    """
    
    try:
        data = request.get_json()
        test_input = pd.DataFrame(data)

        # Transform the input data
        test_input[['product_name', 'aisle', 'department']] = encoder.transform(test_input[['product_name', 'aisle', 'department']])

        input1 = test_input[['order_number', 'days_since_prior_order', 'order_dow', 'order_hour_of_day', 'aisle', 'department', 'product_name']]
        reorder_preds = xgb_model.predict(input1).item()

        input2 = test_input[['user_id', 'product_name', 'order_number', 'days_since_prior_order', 'order_dow', 'order_hour_of_day']]
        same_preds = np.max(same_prod_model.predict_proba(input2)).item()

        # Get product recommendations for the user
        user_id_to_recommend = test_input['user_id'].iloc[0]
        recommended_products = recommend_products_for_user(user_id_to_recommend)

        return jsonify({'reorder_preds': reorder_preds, 'same_preds': same_preds, 'recommended_products': recommended_products})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


