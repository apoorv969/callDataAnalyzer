import pandas as pd
import streamlit as st

df = pd.read_csv("call_data.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['night_call'] = df['hour'].apply(lambda x: 1 if x >= 22 or x < 6 else 0)

st.title("📞 Telecom Call Data Analyzer")

st.write("### 📊 Raw Call Data", df.head())

# Total stats
st.metric("📈 Total Calls", len(df))
st.metric("👤 Unique Callers", df['caller_id'].nunique())
st.metric("🌃 Night Calls", df['night_call'].sum())

# Night call fraud suspects
night_calls = df[df['night_call'] == 1]
suspects = night_calls['caller_id'].value_counts()
fraud_list = suspects[suspects >= 3].index.tolist()
st.write("🚨 **Suspected Fraud Callers (≥3 night calls):**", fraud_list)

# Visual chart
st.bar_chart(df['caller_id'].value_counts())
