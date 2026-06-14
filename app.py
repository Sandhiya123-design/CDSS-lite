import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="CDSS-Lite", layout="wide")

# -------- RESET DEFAULT VALUES --------
defaults = {
    "name": "",
    "age": 30,
    "weight": 70,
    "height": 170,
    "gender": "Male",
    "blood_group": "A+",
    "temp": 36.5,
    "spo2": 98,
    "hr": 75,
    "duration": 1,
    "blood_pressure": "120/80",
    "allergies": "",
    "diabetes": False,
    "hypertension": False,
    "heart_disease": False,
    "chronic_respiratory": False,
    "chronic_kidney": False,
    "neuro_disorder": False,
    "alcohol": False,
    "smoking": False,
    "cancer": False,
    "immuno": False,
    "cold": "None",
    "cough": "None",
    "fever": "None",
    "headache": "None",
    "fatigue": "None",
    "sob": "None",
    "vomiting": "None",
    "wheezing": "None",
    "chest_pain": "None",
    "sore_throat": "None",
    "abdominal_pain": "None",
    "diarrhea": "None",
    "analyzed": False
}

for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp { background-color: #f0f4f8; }

.section { padding: 15px; border-radius: 12px; margin-bottom: 20px; }
.patient { background-color: #d0e1f9; }
.symptoms { background-color: #f9f0f9; }
.comorbid { background-color: #d0f9e1; }

.analysis-box { background-color: #ffffff; padding:10px; border-radius:8px; }
.risk-box { padding:10px; border-radius:8px; color:white; font-weight:bold; }

h3 { margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# ---------------- FILE SETUP ----------------
FILE_NAME = "patient_history.csv"
SEVERITY = ["None", "Mild", "Moderate", "High"]
sev_map = {s:i for i,s in enumerate(SEVERITY)}
risk_map = {"Low": 1, "Moderate": 2, "High": 3}

if not os.path.exists(FILE_NAME):
    pd.DataFrame(columns=[
        "Patient Name","Name","Age","Height","Weight","Gender","BloodGroup",
        "Temperature","SpO2","HeartRate","Duration","BloodPressure","Allergies",
        "Cold","Cough","Fever","Headache","Fatigue","ShortnessOfBreath",
        "Vomiting","Wheezing","ChestPain","SoreThroat","AbdominalPain","Diarrhea",
        "Diabetes","Hypertension","HeartDisease","ChronicRespiratory",
        "ChronicKidney","NeuroDisorder","Alcohol","Smoking","Cancer","Immuno",
        "RiskScore","RiskLevel","Condition"
    ]).to_csv(FILE_NAME,index=False)

# ---------------- TITLE ----------------
st.title("CDSS-Lite : Clinical Decision Support System")

# ---------------- PATIENT INFO ----------------
st.markdown("<div class='section patient'><h3>Patient Information</h3></div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    name = st.text_input("Patient Name", key="name")
    age = st.number_input("Age",0,120, st.session_state.age,key="age")
    height = st.number_input("Height (cm)",50,250, st.session_state.height,key="height")
with c2:
    temp = st.number_input("Temperature (°C)",30.0,45.0, st.session_state.temp,key="temp")
    spo2 = st.number_input("SpO₂ (%)",50,100, st.session_state.spo2,key="spo2")
    weight = st.number_input("Weight (kg)",1,300, st.session_state.weight,key="weight")
with c3:
    hr = st.number_input("Heart Rate (BPM)",30,200, st.session_state.hr,key="hr")
    duration = st.number_input("Duration of Symptoms (days)",1,30, st.session_state.duration,key="duration")
    blood_group = st.selectbox("Blood Group",["A+","A-","B+","B-","O+","O-","AB+","AB-"],
                               index=["A+","A-","B+","B-","O+","O-","AB+","AB-"].index(st.session_state.blood_group), key="blood_group")

# Row 4
c4_1, c4_2, c4_3 = st.columns(3)
with c4_1:
    gender = st.selectbox("Gender", ["Male","Female","Other"], key="gender")
with c4_2:
    blood_pressure = st.text_input("Blood Pressure", st.session_state.blood_pressure, key="blood_pressure")
with c4_3:
    allergies = st.text_input("Allergies", st.session_state.allergies, key="allergies")

# ---------------- SYMPTOMS ----------------
st.markdown("<div class='section symptoms'><h3>Symptoms Severity</h3></div>", unsafe_allow_html=True)
# 4x3 layout
s1, s2, s3 = st.columns(3)
with s1:
    cold = st.selectbox("Cold", SEVERITY,key="cold")
    cough = st.selectbox("Cough", SEVERITY,key="cough")
    fever = st.selectbox("Fever", SEVERITY,key="fever")
with s2:
    headache = st.selectbox("Headache",SEVERITY,key="headache")
    fatigue = st.selectbox("Fatigue",SEVERITY,key="fatigue")
    sob = st.selectbox("Shortness of Breath",SEVERITY,key="sob")
with s3:
    vomiting = st.selectbox("Vomiting",SEVERITY,key="vomiting")
    wheezing = st.selectbox("Wheezing",SEVERITY,key="wheezing")
    chest_pain = st.selectbox("Chest Pain",SEVERITY,key="chest_pain")

# 4th row
s4_1, s4_2, s4_3 = st.columns(3)
with s4_1:
    sore_throat = st.selectbox("Sore Throat",SEVERITY,key="sore_throat")
with s4_2:
    abdominal_pain = st.selectbox("Abdominal Pain",SEVERITY,key="abdominal_pain")
with s4_3:
    diarrhea = st.selectbox("Diarrhea",SEVERITY,key="diarrhea")

# ---------------- COMORBIDITIES ----------------
st.markdown("<div class='section comorbid'><h3>Comorbidities</h3></div>", unsafe_allow_html=True)
d1,d2,d3 = st.columns(3)
with d1:
    diabetes = st.checkbox("Diabetes",key="diabetes")
    hypertension = st.checkbox("Hypertension",key="hypertension")
    alcohol = st.checkbox("Alcohol Consumption History", key="alcohol")
with d2:
    heart_disease = st.checkbox("Heart Disease",key="heart_disease")
    chronic_respiratory = st.checkbox("Chronic Respiratory Disease",key="chronic_respiratory")
    smoking = st.checkbox("Smoking History", key="smoking")
with d3:
    chronic_kidney = st.checkbox("Chronic Kidney Disease",key="chronic_kidney")
    neuro_disorder = st.checkbox("Neurological Disorder (Stroke)",key="neuro_disorder")
    cancer = st.checkbox("Cancer", key="cancer")
    immuno = st.checkbox("Immunocompromised", key="immuno")

# ---------------- ANALYSIS FUNCTION ----------------
def analyze():
    patient_name = str(name).strip() if name else "Unknown"
    symptoms = {
        "Cold": cold,"Cough": cough,"Fever": fever,"Headache":headache,
        "Fatigue":fatigue,"Shortness of Breath":sob,"Vomiting":vomiting,
        "Wheezing":wheezing,"Chest Pain":chest_pain,"Sore Throat":sore_throat,
        "Abdominal Pain":abdominal_pain,"Diarrhea":diarrhea
    }

    # Risk score logic
    risk_score = sum(sev_map[v] for v in symptoms.values())
    if spo2 < 94: risk_score += 2
    if temp >= 38: risk_score += 1
    if diabetes or hypertension or heart_disease: risk_score += 1
    if alcohol or smoking or cancer or immuno: risk_score += 1

    if risk_score >= 12:
        risk_level = "High"
        condition = "Immediate Hospitalization Required"
        color="#FF4C4C"
    elif risk_score >= 8:
        risk_level = "Moderate"
        condition = "Consult Doctor Immediately"
        color="#FFD166"
    else:
        risk_level = "Low"
        condition = "Home Care & Observation"
        color="#06D6A0"

    df = pd.read_csv(FILE_NAME)
    df = pd.concat([df,pd.DataFrame([{
        "Patient Name":patient_name,"Name":patient_name,"Age":age,"Height":height,
        "Weight":weight,"Gender":gender,"BloodGroup":blood_group,"Temperature":temp,
        "SpO2":spo2,"HeartRate":hr,"Duration":duration,"BloodPressure":blood_pressure,
        "Allergies":allergies,
        "Cold":cold,"Cough":cough,"Fever":fever,"Headache":headache,"Fatigue":fatigue,
        "ShortnessOfBreath":sob,"Vomiting":vomiting,"Wheezing":wheezing,"ChestPain":chest_pain,
        "SoreThroat":sore_throat,"AbdominalPain":abdominal_pain,"Diarrhea":diarrhea,
        "Diabetes":diabetes,"Hypertension":hypertension,"HeartDisease":heart_disease,
        "ChronicRespiratory":chronic_respiratory,"ChronicKidney":chronic_kidney,
        "NeuroDisorder":neuro_disorder,"Alcohol":alcohol,"Smoking":smoking,
        "Cancer":cancer,"Immuno":immuno,
        "RiskScore":risk_score,"RiskLevel":risk_level,"Condition":condition
    }])],ignore_index=True)
    # ---- REORDER COLUMNS BEFORE SAVING ----
    order = [
        "Patient Name","Age","Height","Weight","Gender","BloodGroup",
        "Temperature","SpO2","HeartRate","Duration","BloodPressure","Allergies",
        "Cold","Cough","Fever","Headache","Fatigue",
        "ShortnessOfBreath","Vomiting","Wheezing","ChestPain",
        "SoreThroat","AbdominalPain","Diarrhea",
        "Diabetes","Hypertension","HeartDisease",
        "ChronicRespiratory","ChronicKidney","NeuroDisorder",
        "Alcohol","Smoking","Cancer","Immuno",
        "Name","RiskScore","RiskLevel","Condition"
    ]

    df = df[order]  # apply order to dataframe
    df.to_csv(FILE_NAME,index=False)

    # Display patient analysis
    st.subheader(f"Patient Analysis: {patient_name}")
    st.markdown(f"""
    <div class='analysis-box'>
    <b>Age:</b> {age} | <b>Height:</b> {height} cm | <b>Weight:</b> {weight} kg |
    <b>Gender:</b> {gender} | <b>Blood Group:</b> {blood_group} |
    <b>Temperature:</b> {temp}°C | <b>SpO₂:</b> {spo2}% | <b>HR:</b> {hr} BPM | <b>Duration:</b> {duration} days |
    <b>Blood Pressure:</b> {blood_pressure} | <b>Allergies:</b> {allergies}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='analysis-box'><b>Symptoms:</b></div>",unsafe_allow_html=True)
    st.markdown(f"<div class='analysis-box'>{'<br>'.join([f'{k}: {v}' for k,v in symptoms.items()])}</div>",unsafe_allow_html=True)

    alerts = []
    if temp>=38: alerts.append("High Body Temperature")
    if spo2<94: alerts.append("Low Oxygen Level")
    if hr<60 or hr>100: alerts.append("Abnormal Heart Rate")
    for s in ["Shortness of Breath","Vomiting","Wheezing","Chest Pain","Sore Throat","Abdominal Pain","Diarrhea"]:
        if symptoms[s] in ["Moderate","High"]:
            alerts.append(f"{s} Alert")
    st.markdown("<div class='analysis-box'><b>Alerts:</b></div>",unsafe_allow_html=True)
    st.markdown(f"<div class='analysis-box'>{'<br>'.join(alerts) if alerts else 'No critical alerts'}</div>",unsafe_allow_html=True)

    st.subheader("Patient Risk Level")
    st.markdown(f"<div class='risk-box' style='background-color:{color}'>Risk Level: {risk_level}<br>{condition}</div>",unsafe_allow_html=True)

    st.subheader("Patient History Table")
    st.dataframe(df)

    st.session_state.analyzed = True

# ---------------- BUTTONS ----------------
if st.button("Analyze Patient"):
    analyze()

if st.button("Reset"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# ---------------- GRAPHS ----------------
if st.session_state.analyzed:
    df = pd.read_csv(FILE_NAME)
    st.subheader("Graphs")
    g1,g2 = st.columns(2)
    # Symptoms Survivivity
    with g1:
        st.markdown("**Symptoms Survivivity**")
        symptoms_for_graph = {k:st.session_state[k] for k in ["cold","cough","fever","headache","fatigue","sob","vomiting",
                                                               "wheezing","chest_pain","sore_throat","abdominal_pain","diarrhea"]}
        symptoms_for_graph = {k:v for k,v in symptoms_for_graph.items() if v!="None"}
        if symptoms_for_graph:
            fig,ax=plt.subplots(figsize=(4.5,3))
            labels=list(symptoms_for_graph.keys())
            values=[sev_map[v] for v in symptoms_for_graph.values()]
            ax.bar(labels,values,color="#2e7d32")
            ax.set_ylim(0,3.5)
            ax.set_ylabel("Severity")
            plt.xticks(rotation=45,fontsize=8)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("No symptoms selected")

    # Risk Distribution
    with g2:
        st.markdown("**Risk Distribution Graph**")
        risk_level = df.iloc[-1]["RiskLevel"]
        fig,ax=plt.subplots(figsize=(4.5,3))
        levels=["Low","Moderate","High"]
        vals=[0,0,0]
        vals[levels.index(risk_level)] = 1
        ax.bar(levels,vals,color=["#06D6A0","#FFD166","#FF4C4C"])
        ax.set_ylim(0,1.5)
        ax.set_ylabel("Risk Presence")
        plt.tight_layout()
        st.pyplot(fig)

    # Risk Trend
    st.markdown("**Patient Risk Trend**")
    fig,ax=plt.subplots(figsize=(8,3))
    df_plot=df.copy()
    df_plot["RiskNum"]=df_plot["RiskLevel"].map(risk_map)
    x=np.arange(len(df_plot))
    y=df_plot["RiskNum"].values
    points=np.array([x,y]).T.reshape(-1,1,2)
    segments=np.concatenate([points[:-1],points[1:]],axis=1)
    color_map={"Low":"#06D6A0","Moderate":"#FFD166","High":"#FF4C4C"}
    lc=LineCollection(segments,colors=[color_map[r] for r in df_plot["RiskLevel"]],linewidths=2)
    ax.add_collection(lc)
    ax.set_xlim(x.min(),x.max())
    ax.set_ylim(0.5,3.5)
    ax.set_yticks([1,2,3])
    ax.set_yticklabels(["Low","Moderate","High"])
    ax.set_xticks([])
    ax.set_ylabel("Risk Level")
    plt.tight_layout()
    st.pyplot(fig)
