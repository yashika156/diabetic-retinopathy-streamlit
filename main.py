from keras.models import load_model
import gdown
import os

# Ensure 'model' directory exists
os.makedirs("model", exist_ok=True)
# Download from public Google Drive link (shared with 'Anyone')
url = url = "https://drive.google.com/uc?export=download&id=1dCDPNXxSz3Kv9X5uS6iknfs01EU5tzQJ"
output = "model/dr_cnn_model.h5"
gdown.download(url, output, quiet=False)

model = load_model(output)
