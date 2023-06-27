import streamlit as st
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor as GBR
from catboost import CatBoostClassifier
import joblib
import pandas as pd
import numpy as np
import urllib.request
import boto3
from botocore.config import Config
from botocore import UNSIGNED
import io

st.title('Stroke Prediction')

st.text("""
This application uses various AI algorithms to indicate the risk of a stroke. If a stroke is suspected, a doctor must always be consulted. This is a medical emergency. This application is for demonstration purposes only.
""")

st.title('Contribution by Model')

st.text("""
At this point, you can check the risk contributions in percentage points for the individual models.
""")

URL = "https://strokemodels.s3.eu-central-1.amazonaws.com"
data_load_state = st.text('Loading models...')

# Load Sklearn models
@st.cache(allow_output_mutation=True)
def loadAllModels(url):
    models = []
    for c in ["svm1", "svm2", "logit1", "logit2", "nbc1", "nbc2", "rf1", "rf2", "errGBR"]:
        models.append(joblib.load(urllib.request.urlopen(url + "/" + "{}.pkl".format(c))))
    return models[0], models[1], models[2], models[3], models[4], models[5], models[6], models[7], models[8]

svm1, svm2, logit1, logit2, nbc1, nbc2, rf1, rf2, errGBR = loadAllModels(URL)

# Load CatBoost
@st.cache(allow_output_mutation=True)
def loadCatBoost():
    s3 = boto3.resource(
        service_name='s3',
        region_name='eu-central-1',
        config=Config(signature_version=UNSIGNED)
    )
    bucket = s3.Bucket('strokemodels')
    models = []
    for c in ["cb1", "cb2"]:
        obj = bucket.Object("%s" % (c))
        file_stream = io.BytesIO()
        obj.download_fileobj(file_stream)  # download to memory
        CB = CatBoostClassifier()
        models.append(CB.load_model(blob=file_stream.getvalue()))
    return models[0], models[1]

cb1, cb2 = loadCatBoost()

# Notify the reader that the data was successfully loaded.
data_load_state.text("AI Models Loaded")

############### SIDEBAR START ################

st.sidebar.title("Patient Data")

age = st.sidebar.slider('Age', 0, 100, 40)
bmi = st.sidebar.slider('BMI', 5, 45, 20)
agl = st.sidebar.slider('Average Glucose Level', 50, 400, 100)

smoking = st.sidebar.selectbox('Smoking Status', ["Never Smoked", "Formerly Smoked", "Smokes", "Unknown"])
if smoking == "Never Smoked":
    smoking_status_formerly_smoked = 0
    smoking_status_smokes = 0
    smoking_status_never_smoked = 1
    smoking_status = "never smoked"
elif smoking == "Formerly Smoked":
    smoking_status_formerly_smoked = 1
    smoking_status_smokes = 0
    smoking_status_never_smoked = 0
    smoking_status = "formerly smoked"
elif smoking == "Smokes":
    smoking_status_formerly_smoked = 0
    smoking_status_smokes = 1
    smoking_status_never_smoked = 0
    smoking_status = "smokes"
else:
    smoking_status_formerly_smoked = 0
    smoking_status_smokes = 0
    smoking_status_never_smoked = 0
    smoking_status = "unknown"

gender = st.sidebar.radio("Gender", ("Male", "Female"))

############### SIDEBAR END ################

st.title('AI model predictions')
st.text("""
Please remember: This is a medical emergency. In case of a suspected stroke, please consult a doctor immediately. This app is for demonstration purposes only.
""")

@st.cache
def compute_preds():
    data = {
        'age': [age],
        'bmi': [bmi],
        'avg_glucose_level': [agl],
        'smoking_status_formerly_smoked': [smoking_status_formerly_smoked],
        'smoking_status_smokes': [smoking_status_smokes],
        'smoking_status_never_smoked': [smoking_status_never_smoked],
        'gender_Male': [int(gender == "Male")],
        'gender_Female': [int(gender == "Female")]
    }

    df = pd.DataFrame(data)

    # Apply standard scaling to the input features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df)

    svm1_pred = svm1.predict(scaled_features)[0]
    svm2_pred = svm2.predict(scaled_features)[0]
    logit1_pred = logit1.predict(scaled_features)[0]
    logit2_pred = logit2.predict(scaled_features)[0]
    nbc1_pred = nbc1.predict(scaled_features)[0]
    nbc2_pred = nbc2.predict(scaled_features)[0]
    rf1_pred = rf1.predict(scaled_features)[0]
    rf2_pred = rf2.predict(scaled_features)[0]
    cb1_pred = cb1.predict_proba(df)[0][1]
    cb2_pred = cb2.predict_proba(df)[0][1]
    errGBR_pred = errGBR.predict(df)[0]

    preds = {
        'svm1': svm1_pred,
        'svm2': svm2_pred,
        'logit1': logit1_pred,
        'logit2': logit2_pred,
        'nbc1': nbc1_pred,
        'nbc2': nbc2_pred,
        'rf1': rf1_pred,
        'rf2': rf2_pred,
        'cb1': cb1_pred,
        'cb2': cb2_pred,
        'errGBR': errGBR_pred
    }

    return preds

predictions = compute_preds()

# Display prediction results
st.subheader('Stroke Risk Prediction Results')
for model, pred in predictions.items():
    st.write(f"{model}: {pred}")

st.subheader('Contribution by Model')
df_contribution = pd.DataFrame(predictions.items(), columns=['Model', 'Risk'])
df_contribution['Risk'] = df_contribution['Risk'].map(lambda x: round(x * 100, 2))
df_contribution = df_contribution.sort_values(by='Risk', ascending=False)

st.bar_chart(df_contribution.set_index('Model'))

