import requests



data = {'add_to_cart_order': [2],
 'product_name': ["Bulgarian Yogurt"],
 'user_id': [199120],
 
 'order_number': [49],
 'order_dow': [3],
 'order_hour_of_day': [20],
 'days_since_prior_order': [7.0],
 'aisle': ["yogurt"],
 'department': ["dairy eggs"]}

response = requests.post('http://127.0.0.1:5000/predict', json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print('API request failed')
