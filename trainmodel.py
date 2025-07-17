import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("cropds.csv")

# Encode labels
le = LabelEncoder()
data['label'] = le.fit_transform(data['label'])

# Features and target
X = data.iloc[:, :-1]
y = data['label']

# Split the data
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

# Train the model
model = SVC()
model.fit(xtrain, ytrain)

# Save the model and label encoder
joblib.dump(model, 'crop_model.pkl')
joblib.dump(le, 'label_encoder.pkl')
