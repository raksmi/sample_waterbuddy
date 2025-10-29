import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

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
# QUICK ACTIONS SECTION
# -------------------------------
st.subheader("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🥤 Add 250ml"):
        st.session_state["water_intake"] = st.session_state.get("water_intake", 0) + 250

with col2:
    if st.button("🚰 Add 500ml"):
        st.session_state["water_intake"] = st.session_state.get("water_intake", 0) + 500

with col3:
    if st.button("🔁 Reset"):
        st.session_state["water_intake"] = 0

# Display intake
intake = st.session_state.get("water_intake", 0)
goal = 2000
progress = min(intake / goal, 1.0)

st.progress(progress)
st.write(f"**Today's intake:** {intake} ml / {goal} ml")

# -------------------------------
# GRAPH SECTION (MATPLOTLIB)
# -------------------------------
st.subheader("📊 Water Intake - Past 7 Days")

# Generate fake sample data (you can replace this with real data later)
dates = [(datetime.now() - timedelta(days=i)).strftime("%b %d") for i in range(6, -1, -1)]
values = [random.randint(1200, 2500) for _ in range(7)]
values[-1] = intake  # today's intake replaces last value

fig, ax = plt.subplots()
ax.bar(dates, values)
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
