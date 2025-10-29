import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.set_page_config(page_title="💧 WaterBuddy", page_icon="💧", layout="centered")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="color:#00BFFF;">💧 WaterBuddy</h1>
        <p style="font-size:18px;">Stay hydrated and track your water intake easily!</p>
    </div>
""", unsafe_allow_html=True)

# -------------------------------
# INITIALIZE SESSION STATE
# -------------------------------
if "water_intake" not in st.session_state:
    st.session_state["water_intake"] = 0
if "history" not in st.session_state:
    # History for past 7 days, start all zeros
    st.session_state["history"] = [0]*6 + [0]  # last value is today

# -------------------------------
# QUICK ACTIONS SECTION
# -------------------------------
st.subheader("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🥤 Add 250ml"):
        st.session_state["water_intake"] += 250

with col2:
    if st.button("🚰 Add 500ml"):
        st.session_state["water_intake"] += 500

with col3:
    if st.button("🔁 Reset"):
        st.session_state["water_intake"] = 0

# -------------------------------
# UPDATE HISTORY
# -------------------------------
st.session_state["history"][-1] = st.session_state["water_intake"]

# -------------------------------
# DISPLAY PROGRESS
# -------------------------------
intake = st.session_state["water_intake"]
goal = 2000
progress = min(intake / goal, 1.0)

st.progress(progress)
st.write(f"**Today's intake:** {intake} ml / {goal} ml")

# -------------------------------
# GRAPH SECTION (MATPLOTLIB)
# -------------------------------
st.subheader("📊 Water Intake - Past 7 Days")

dates = [(datetime.now() - timedelta(days=i)).strftime("%b %d") for i in range(6, -1, -1)]
values = st.session_state["history"]

fig, ax = plt.subplots()
ax.bar(dates, values, color="#00BFFF")
ax.set_title("Daily Water Intake (ml)", fontsize=14)
ax.set_ylabel("Water (ml)")
ax.set_xlabel("Date")
ax.set_ylim(0, 3000)
plt.xticks(rotation=30)

st.pyplot(fig)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
    <hr>
    <p style="text-align:center; color:gray; font-size:14px;">
        💙 WaterBuddy helps you stay hydrated every day!
    </p>
""", unsafe_allow_html=True)
