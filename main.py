import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model

model = load_model("model/dr_cnn_model.h5")
st.title("🧠 Diabetic Retinopathy Classifier")

uploaded = st.file_uploader("Upload Retina Image", type=["jpg", "png", "jpeg"])
if uploaded:
    image = Image.open(uploaded).resize((224, 224))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.expand_dims(np.array(image)/255.0, axis=0)
    pred = model.predict(img_array)
    stage = ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"][np.argmax(pred)]

    st.subheader(f"Prediction: {stage}")

