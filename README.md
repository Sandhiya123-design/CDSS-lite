CDSS-Lite: Clinical Decision Support System
🏥 Overview

CDSS-Lite is a Streamlit-based Clinical Decision Support System designed to assist in basic patient risk assessment using vital signs, symptoms, and comorbidities. It provides a simple, rule-based risk classification to support medical decision-making.

⚠️ Disclaimer: This tool is for educational purposes only and is NOT a medical diagnostic system.

🚀 Live Demo

🔗 https://cdss-lite-j6fs6xqfs7jiix7shuptkm.streamlit.app/

🧠 Features
Patient information input (age, weight, height, BP, etc.)
Vital signs monitoring (Temperature, SpO₂, Heart Rate)
Symptom severity-based evaluation
Comorbidity analysis (diabetes, hypertension, etc.)
Rule-based risk scoring system
Risk classification:
Low
Moderate
High
Patient history stored in CSV file
Data visualization:
Symptom severity graph
Risk distribution chart
Risk trend analysis
🛠️ Technologies Used
Python
Streamlit
Pandas
NumPy
Matplotlib
📂 Project Structure
CDSS_Project/
│
├── app.py                 # Main Streamlit application
├── requirements.txt      # Dependencies
├── patient_history.csv   # Patient data storage
└── README.md             # Project documentation
⚙️ Installation & Run Locally
1. Clone the repository
git clone https://github.com/your-username/CDSS-Lite.git
cd CDSS-Lite
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run app.py
📊 How It Works
Enter patient details
Select symptoms and severity levels
System calculates a risk score
Output shows:
Risk level (Low / Moderate / High)
Recommended action
Visual graphs
Data is stored for history tracking
📌 Risk Logic (Simplified)
Symptoms severity → score (0–3)
Low SpO₂ (<94) → +2
Fever (≥38°C) → +1
Comorbidities → +1 to +2
Final score determines risk category
📈 Future Improvements
AI/ML-based prediction model
Doctor login system
PDF patient report generation
Database integration (MySQL / Firebase)
Mobile-friendly UI
👨‍💻 Author
Developed by: SANDHIYA K
