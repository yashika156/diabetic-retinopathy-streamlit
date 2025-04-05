from keras.models import load_model
import gdown

# Download from public Google Drive link (shared with 'Anyone')
url = "https://drive.google.com/uc?id=1dCDPNXxSz3Kv9X5uS6iknfs01EU5tzQJ/view?usp=sharing"
output = "model/dr_cnn_model.h5"
gdown.download(url, output, quiet=False)

model = load_model(output)
