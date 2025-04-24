
import streamlit as st

def sipoc_game():
    st.set_page_config(page_title="SIPOC Café – Interactive Game", layout="centered")
    st.title("☕ SIPOC Café – Interactive Lean Game")

    st.header("🎯 Your Goal:")
    st.markdown("""
Build a correct SIPOC diagram for the process of **making coffee**.
Then define:
- Two **Critical to Quality (CTQ)** elements for the customer
- One metric each for: Inputs, Process, Outputs
- A smart **Kaizen improvement**

Let's see how well you know your process!
    """)

    st.subheader("📋 Classify These Elements into SIPOC")
    elements = [
        "Ground Coffee", "Water", "Barista", "Clean Cup", "Boiling Water",
        "Putting moka on stove", "Hot Coffee in Cup", "Customer",
        "Grinder", "Lighting the stove", "Waiting at bar"
    ]
    correct = {
        "Ground Coffee": "Input",
        "Water": "Input",
        "Barista": "Supplier",
        "Clean Cup": "Input",
        "Boiling Water": "Process",
        "Putting moka on stove": "Process",
        "Hot Coffee in Cup": "Output",
        "Customer": "Customer",
        "Grinder": "Supplier",
        "Lighting the stove": "Process",
        "Waiting at bar": "Customer"
    }

    score = 0
    user_classifications = {}

    for item in elements:
        choice = st.selectbox(f"{item} →", ["Supplier", "Input", "Process", "Output", "Customer"], key=item)
        user_classifications[item] = choice
        if choice == correct[item]:
            score += 1

    st.markdown("---")
    st.subheader("🔍 CTQ and Metrics Challenge")
    ctq1 = st.text_input("CTQ #1 (e.g. 'Coffee temperature above 65°C')")
    ctq2 = st.text_input("CTQ #2 (e.g. 'Served in under 3 minutes')")

    metric_input = st.text_input("📊 Metric for Inputs (e.g. 'Coffee grind size')")
    metric_process = st.text_input("📊 Metric for Process (e.g. 'Brewing time')")
    metric_output = st.text_input("📊 Metric for Output (e.g. 'Serving temperature')")

    kaizen_idea = st.text_area("💡 Suggest one Kaizen improvement:")

    # Extra scoring
    if ctq1.strip():
        score += 1
    if ctq2.strip():
        score += 1
    if metric_input.strip():
        score += 1
    if metric_process.strip():
        score += 1
    if metric_output.strip():
        score += 1
    if kaizen_idea.strip():
        score += 2

    st.markdown("---")
    st.subheader("🏁 Final Score")

    st.markdown(f"### 🎯 Your total score is: **{score} / 18**")

    if score >= 15:
        st.success("🌟 Excellent! You're a Lean Coffee Master!")
    elif score >= 10:
        st.info("👍 Good job! A few tweaks and you're there.")
    else:
        st.warning("👀 Keep practicing your process awareness!")

sipoc_game()
