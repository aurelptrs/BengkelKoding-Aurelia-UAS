import joblib
import streamlit as st

# Membaca model klasifikasi
churn_model = joblib.load('best_random_forest_model.joblib')

# Header
st.header('BENGKEL KODING')

# Title
st.title('Aplikasi Prediksi Churn Pelanggan Menggunakan Random Forest')

st.image('churn.png')

st.markdown('Churn pelanggan merupakan kondisi ketika seseorang berhenti berlangganan layanan.')
st.markdown('Aplikasi ini berfungsi untuk deteksi pelanggan mana yang memiliki potensi churn.')
st.markdown('Prediksi akan menghasilkan dua nilai, yaitu Yes (pelanggan berhenti berlangganan dan No (pelanggan tetap berlangganan.')

# Input data
col1, col2 = st.columns(2)

with col1 :
    gender = st.text_input ('Input jenis kelamin (ketik 0 = perempuan, 1 = laki-laki)')

with col2 :
    SeniorCitizen = st.text_input ('Status lansia (0 = tidak, 1 = iya)')

with col1 :
    Partner = st.text_input ('Apakah memiliki pelanggan (0 = tidak, 1 = iya)')

with col2 :
    Dependents = st.text_input ('Apakah memiliki tanggungan (0 = tidak, 1 = iya)')

with col1 :
    tenure = st.text_input ('Berapa lama berlangganan (bulan)')

with col2 :
    PhoneService = st.text_input ('Apakah menggunakan layanan telpon (0 = tidak, 1 = iya)')

with col1 :
    MultipleLines = st.text_input ('Apakah memiliki lebih dari satu jalur telepon (0 = tidak, 1 = iya, 2 = tidak ada layanan internet)')

with col2 :
    InternetService = st.text_input ('Internet Service (0 = tidak ada, 1 = DSL, 2 = Fiber optic)') 
    
with col1 :
    OnlineSecurity = st.text_input ('Input nilai Online Security (0 = tidak, 1 = iya, 2 = tidak ada layanan internet)')

with col2 :
    OnlineBackup = st.text_input ('Layanan Online Backup (0 = tidak, 1 = iya, 2 = tidak ada layanan internet)')

with col1 :
    DeviceProtection = st.text_input ('Proteksi perangkat (0 = tidak, 1 = iya, 2 = tidak ada layanan internet)') 

with col2 :
    TechSupport = st.text_input ('Dukungan teknik (0 = tidak, 1 = iya, 2 = tidak ada layanan internet)') 

with col1 :
    StreamingTV = st.text_input ('Apakah berlangganan TV streaming (0 = tidak, 1 = iya, 2 = tidak ada layanan internet)')

with col2 :
    StreamingMovies = st.text_input ('Apakah berlangganan Streaming Movies (0 = tidak, 1 = iya, 2 = tidak ada layanan internet)')

with col1 :
    Contract = st.text_input ('jenis kontrak pelanggan (0 = Month-to-month, 1 = One year, 2 = Two year)')

with col2 :
    PaperlessBilling = st.text_input ('Apakah memiliki tagihan tanpa kertas (0 = tidak, 1 = iya)')

with col1 :
    PaymentMethod = st.text_input ('Payment Method (0 = Electronic check, 1 = Mailed check, 2 = Bank transfer, 3 = Credit card)')

with col2 :
    MonthlyCharges = st.text_input ('Berapa biaya per bulan')

with col1 :
    TotalCharges = st.text_input ('Total biaya selama berlangganan')

# Prediksi
churn_diagnosis = ''

# Tombol prediksi
if st.button('Test prediksi churn'):
    churn_prediction = churn_model.predict([[gender, SeniorCitizen, Partner, Dependents, tenure, 
PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, 
StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges]])

    if(churn_prediction[0] == 1):
        churn_diagnosis = 'Ya, pelanggan berhenti berlangganan'
    else :
        churn_diagnosis = 'Tidak, pelanggan tetap berlangganan'
    
st.success(churn_diagnosis)