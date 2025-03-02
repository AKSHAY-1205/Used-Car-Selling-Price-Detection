# 🚗 Used Car Selling Price Prediction

This project is a **Machine Learning-powered web application** that predicts the selling price of a used car based on various factors such as year of purchase, kilometers driven, fuel type, seller type, transmission, and owner history.

## 📌 Features
- 🔍 **Predicts selling price** of a used car based on user inputs
- 📊 **Trained using a Random Forest Regressor**
- 🖥️ **Interactive UI with Streamlit**
- ☁ **Deployed on Streamlit Cloud**
  
## 🛠️ Technologies Used
- **Python**
- **Streamlit** (for UI)
- **Scikit-Learn** (for ML model)
- **Pandas & NumPy** (for data preprocessing)
- **Pickle** (for model saving/loading)

## 📂 Project Structure
📂 user_car_price_prediction/
   ├── 📂 models/
   │   ├── random_forest_model.pkl  # Trained ML model
   ├── 📂 data/
   │   ├── car_data.csv             # Dataset for training
   ├── app.py                        # Streamlit app
   ├── train_model.py                 # Script to train and save model
   ├── requirements.txt               # Dependencies for deployment  
   ├── README.md                      # (Optional) Project description



## 🚀 How to Run Locally
1. **Clone the repository**:
   git clone https://github.com/AKSHAY-1205/Used-Car-Selling-Price-Detection.git
   cd Used-Car-Selling-Price-Detection

2.Install dependencies:
  pip install -r requirements.txt

3.Train the model:
  python train_model.py

4.Run the streamlit app:
  streamlit run app.py

5.Visit http://localhost:8501/ in your browser to use the app.



📡 Deployment
The app is deployed on Streamlit Cloud.
🔗 https://used-car-selling-price-detection.streamlit.app/



📬 Contact
Akshay J
📧 Email - akshayjagadeesh05@gmail.com

