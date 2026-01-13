📊 Portuguese Bank Marketing – Machine Learning Classification Project

📌 Problem Statement

-The objective of this project is to predict whether a customer will subscribe to a term deposit based on their demographic details, banking history, and previous marketing interactions.
-This is a binary classification problem where the target variable indicates whether the client subscribed (yes) or not (no).
-The dataset is highly imbalanced, which makes accuracy an unreliable metric. Therefore, special attention was given to recall, precision, F1-score, and ROC-AUC.

📂 Dataset

The dataset is from a Portuguese banking institution and contains information such as:
-Customer age, job, marital status, education
-Contact type, previous campaign results
-Economic indicators
-Past campaign history

Target column:

y → Whether the client subscribed to a term deposit (yes or no)

Challenges Faced:
Highly imbalanced target variable
Large number of categorical features
Presence of highly correlated features
Features such as duration causing data leakage
Different models reacting differently to encoding and scaling

🛠️ Data Preprocessing

The following preprocessing steps were applied:

1️. Encoding
Two encoding techniques were tested:
-One-Hot Encoding
-Label Encoding

The impact of encoding on different models was carefully evaluated.

2️. Feature Scaling
Models sensitive to feature scale (Logistic Regression, KNN) were trained with standard scaling to improve performance.

3. Feature Selection

Highly correlated and leakage-prone features were removed, including:
One highly correlated economic feature

Models Trained:

Multiple classification models were trained and compared:
Hyperparameter Tuning
-GridSearchCV was used to tune important parameters such as:
-Number of trees and depth (Random Forest)
-Number of neighbors (KNN)

It was observed that hyperparameter tuning improved some models like KNN but slightly reduced performance in others due to overfitting

📈 Model Evaluation

Because the dataset is imbalanced, the following metrics were used:
-Recall
-Precision
-F1-Score
-Accuracy
-ROC-AUC

Confusion Matrix

-The focus was on maximizing recall to correctly identify customers likely to subscribe.

🏆 Final Outcome

After testing multiple preprocessing strategies and models, the final model was selected based on:
-Best balance between recall and precision

The project demonstrated how encoding, scaling, feature selection, and hyperparameter tuning significantly impact machine learning model performance.

💡 Business Insight

-The model helps the bank:
-Identify customers most likely to subscribe
-Reduce unnecessary marketing calls
-Improve campaign efficiency





