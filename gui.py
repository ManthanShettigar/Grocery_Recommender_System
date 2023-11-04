import streamlit as st
import requests

st.title("Instacart Product Recommender")

# Define the API endpoint
api_url = 'http://localhost:5000/predict'  # Replace with your API endpoint

# Input form
st.header("User Input")
user_id = st.text_input("Enter User ID:")
order_number = st.number_input("Enter Order Number:")
days_since_prior_order = st.number_input("Enter Days Since Prior Order:")
order_dow = st.number_input("Enter Order Day of Week:")
order_hour_of_day = st.number_input("Enter Order Hour of Day:")
aisle = st.text_input("Enter Aisle:")
department = st.text_input("Enter Department:")
product_name = st.text_input("Enter Product Name:")

if st.button("Get Recommendations"):
    # Create a JSON input to send to the API
    input_data = {
        'user_id': [int(user_id)],
        'order_number': [int(order_number)],
        'days_since_prior_order': [float(days_since_prior_order)],
        'order_dow': [int(order_dow)],
        'order_hour_of_day': [int(order_hour_of_day)],
        'aisle': [aisle],
        'department': [department],
        'product_name': [product_name]
    }

    try:
        # Send a POST request to the API
        response = requests.post(api_url, json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.subheader(f"Will User {user_id} Reorder again ?")
            reorder = "Yes" if result.get('reorder_preds', 'N/A')==1 else 0
            st.write(reorder)
            st.subheader(f"Buying Same Product {product_name} again Probability :")
            st.write(result.get('same_preds', 'N/A'))

            recommended_products = result.get('recommended_products')
            if recommended_products:
                st.subheader("Recommendations:")
                st.write(recommended_products)
            else:
                st.info("No product recommendations available for this user.")
        else:
            st.error(f"API request failed with status code {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

