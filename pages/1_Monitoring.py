import streamlit as st
import sqlite3
import matplotlib.pyplot as plt
import datetime

st.title("📈 Daily Diabetes Monitoring")

# DB setup
conn = sqlite3.connect("monitor.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS sugar (date TEXT, fasting INTEGER, post_meal INTEGER)")

# Input form
with st.form("log_form"):
    fasting = st.number_input("Fasting Sugar", min_value=0)
    post_meal = st.number_input("Post-meal Sugar", min_value=0)
    submitted = st.form_submit_button("Log Entry")
    if submitted:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        c.execute("INSERT INTO sugar VALUES (?, ?, ?)", (date, fasting, post_meal))
        conn.commit()
        st.success("Logged successfully ✅")

# Fetch and plot
c.execute("SELECT * FROM sugar")
data = c.fetchall()

if data:
    df = { "date": [], "fasting": [], "post_meal": [] }
    for d in data:
        df["date"].append(d[0])
        df["fasting"].append(d[1])
        df["post_meal"].append(d[2])

    st.line_chart({
        "Fasting": df["fasting"],
        "Post-meal": df["post_meal"]
    })

    for i in range(len(df["date"])):
        st.write(f"{df['date'][i]} → Fasting: {df['fasting'][i]}, Post-meal: {df['post_meal'][i]}")
