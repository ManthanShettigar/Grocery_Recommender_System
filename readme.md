# Grocery Store Recommender System

This project aims to build a recommender system for a grocery store that predicts whether a user will reorder a product and provides product recommendations. It includes a machine learning model for reorder prediction, product popularity-based recommendations, and a Flask API for making real-time predictions.

## Objectives

- Predict if a user reorders from the grocery store.
- Predict if the user reorders the same product based on their purchase history.
- Recommend the most popular products to users based on purchase history.
- Deploy a Flask API  using streamlit for users to interact with the system.

## Tech Stack
- Python
- Pandas
- NumPy
- Streamlit
- Scikit-learn
- XGBoost
- Flask
```
# No code changes needed to initialize a git repo in this context
```



## Model Building

### Reorder Prediction Model

 Built a machine learning model for reorder prediction. The following steps were taken:

#### Data Preprocessing

- Performed feature engineering to create relevant features for reorder prediction.
- Encoded categorical features using `TargetEncoder`
- Split the data into training and testing sets.

#### Model Selection

For reorder prediction and buying the same product again prediction, we used a gradient boosted decision tree model (XGBoost) since it typically performs well for classification problems with stratified kfold with 5 splits cross validation to reduce the imbalance of the target variable in the dataset.

#### Model Results

The model was evaluated using ROC AUC as the primary evaluation metric. Here are the ROC AUC results for each fold and the mean ROC AUC:

- Fold 0: ROC AUC = 0.7575
- Fold 1: ROC AUC = 0.7559
- Fold 2: ROC AUC = 0.7574
- Fold 3: ROC AUC = 0.7597
- Fold 4: ROC AUC = 0.7559
- Mean ROC AUC = 0.7573

The results indicate that the model is effective in predicting whether a user will reorder a specific product.

### Same Product Reordered Prediction Model

 built a model to predict whether a user will reorder the same product. Here are the ROC AUC results for each fold and the mean ROC AUC:

- Fold 0: ROC AUC = 0.7555
- Fold 1: ROC AUC = 0.7576
- Fold 2: ROC AUC = 0.7597
- Fold 3: ROC AUC = 0.7564
- Fold 4: ROC AUC = 0.7569
- Mean ROC AUC = 0.7572

These results suggest that the model is reasonably effective in predicting whether a user will reorder the same product.

### Popularity-Based Recommendation

roduct recommendations based on popularity:

1. Calculate the popularity of each product.
2. Filter out products the user has already purchased.
3. Sort products by popularity.
4. Recommend the top N products.

## API Usage

Install the venv and dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


To run the Flask API, execute the following command:

```bash
python api.py
```

A Streamlit web app is available for users to explore the recommender system interactively. It can be run using the following command:

```bash
streamlit run gui.py
```

It will open up a web browser where users can input their purchase history and receive reorder predictions and product recommendations.

here is the democode for the API usage:

![GitHub Octocat](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnQzajM2bzliaTd1eW83NHA0c2JxeDd6OGczdW1kc256cHRzd2g5dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dxicSPeffatKoJzA7p/giphy.gif)

