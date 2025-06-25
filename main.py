import pandas as pd
from collections import Counter

# Load data
df = pd.read_csv('call_data.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Basic stats
print("\nTotal Calls:", len(df))
print("Unique Callers:", df['caller_id'].nunique())
print("Unique Receivers:", df['receiver_id'].nunique())

# Total call duration per caller
caller_durations = df.groupby('caller_id')['duration'].sum().sort_values(ascending=False)
print("\nTop Callers by Duration:\n", caller_durations.head())

# Most active caller
most_active = df['caller_id'].value_counts().idxmax()
print(f"\nMost Active Caller: {most_active}")

# Night call detector (calls between 10 PM to 6 AM)
df['hour'] = df['timestamp'].dt.hour
df['night_call'] = df['hour'].apply(lambda x: 1 if x >= 22 or x < 6 else 0)
night_calls = df[df['night_call'] == 1]

print(f"\nTotal Night Calls: {len(night_calls)}")
print("Users with repeated night calls:\n", night_calls['caller_id'].value_counts())

# Optional: Save night call data
night_calls.to_csv('night_calls.csv', index=False)

