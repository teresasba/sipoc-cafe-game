
import streamlit as st
import pandas as pd
from datetime import datetime

def sipoc_metrics_game():
    st.set_page_config(page_title="SIPOC & Metrics Lean Game", layout="centered")
    st.title("🚀 SIPOC & Metrics – Lean Thinking Game")

    st.header("🎯 Your Mission:")
    st.markdown("""
Understand the full flow of your process.
Classify elements correctly into SIPOC.
Identify the right type of metrics.
Recognize Leading vs Lagging indicators.
Discover the real impact of your work on Customers and Colleagues.
    """)

    player_name = st.text_input("👤 Enter your name or team:", key="player_name")

    with st.expander("📘 Glossary – Click to expand"):
        st.markdown("""
        ### 🧩 SIPOC Elements
        - **Supplier:** Person, group, or organization that provides inputs (internal or external).
        - **Input:** Resources needed to start the process (materials, information, data).
        - **Process:** Actions that transform inputs into outputs.
        - **Output:** Product or service resulting from the process.
        - **Customer:** Person, group, or organization receiving the output (internal or external).

        ### 📊 Types of Metrics
        - **Input Metrics:** Measure the quality or availability of inputs (e.g., % complete customer data).
        - **Process Metrics:** Measure activities inside the process (e.g., call handling time).
        - **Output Metrics:** Measure immediate results of the process (e.g., delivery time).
        - **Outcome Metrics:** Measure final impact on customers (e.g., NPS score).

        ### ⚡ Leading vs Lagging Indicators
        - **Leading Indicators:** Based on Inputs and Processes. Allow proactive action.
        - **Lagging Indicators:** Based on Outputs and Outcomes. Measure results after the fact.

        ---
        Remember:
        - Leading = Early warning → You can act NOW.
        - Lagging = After the fact → Only reactive corrections.
        """)

    scenario = st.radio("Select your scenario:", ["☕ Make a Coffee", "📞 Handle a Customer Call"])

    # Scenario data
    if scenario == "☕ Make a Coffee":
        elements = {
            "Ground Coffee": "Input",
            "Water": "Input",
            "Barista": "Supplier",
            "Clean Cup": "Input",
            "Putting moka on stove": "Process",
            "Boiling water": "Process",
            "Hot coffee in cup": "Output",
            "Customer": "Customer",
            "Grinder": "Supplier",
            "Lighting the stove": "Process"
        }
    else:
        elements = {
            "Client’s phone number": "Input",
            "CRM customer history data": "Input",
            "Internal Data Entry Team": "Supplier",
            "Customer’s request (information)": "Input",
            "Access CRM system": "Process",
            "Answer call and verify customer": "Process",
            "Problem solved": "Output",
            "Ticket updated in CRM": "Output",
            "Client (caller)": "Customer",
            "Supervisor (escalation)": "Customer"
        }

    st.subheader("🧩 Classify each element into SIPOC")
    total_score = 0
    results = []

    for item, correct_category in elements.items():
        guess = st.selectbox(f"What is '{item}'?", ["Supplier", "Input", "Process", "Output", "Customer"], key=item)
        explanation = ""
        if guess == correct_category:
            total_score += 2
        else:
            explanation = f"❌ Oops! Correct answer: **{correct_category}**. Remember: {item} serves as {correct_category.lower()} in the process."

        st.markdown(f"✅ You chose: {guess}")
        if explanation:
            st.info(explanation)

        results.append({
            "Player": player_name,
            "Element": item,
            "Your Choice": guess,
            "Correct Category": correct_category,
            "Correct": guess == correct_category
        })

    st.markdown("---")
    st.subheader("📊 Metrics Challenge: Leading or Lagging?")

    metrics = {
        "Brewing water temperature stability": "Leading",
        "Final coffee taste rating": "Lagging",
        "CRM Access Time": "Leading",
        "First Call Resolution Rate": "Lagging",
        "Customer Satisfaction (CSAT)": "Lagging",
        "Average Handle Time (AHT)": "Leading"
    }

    for metric, correct_type in metrics.items():
        guess_metric = st.radio(f"Classify the metric: {metric}", ["Leading", "Lagging"], key=metric)
        if guess_metric == correct_type:
            total_score += 1
        else:
            st.warning(f"Correct answer: {correct_type}. Remember, Leading = early action; Lagging = after the fact.")

        results.append({
            "Player": player_name,
            "Element": metric,
            "Your Choice": guess_metric,
            "Correct Category": correct_type,
            "Correct": guess_metric == correct_type
        })

    st.markdown("---")
    st.subheader("🏁 Final Score")
    st.markdown(f"### 🎯 Your total score is: **{total_score}** points!")

    # Inspirational Closing
    st.markdown("---")
    st.subheader("🌟 Final Reflection: The True Power of SIPOC")
    st.markdown("""
    In just one simple page, a SIPOC diagram gives you a complete, structured view of your process:

    - **It identifies all your Customers** — internal and external — and reminds you that every action you take impacts someone's experience.
    - **It maps the true start and end of your work** — showing that you're part of a greater value chain.
    - **It highlights the Inputs and Outputs** that sustain quality.
    - **It connects you to the right Metrics** — to proactively guide performance.

    💡 You're not just completing tasks — you are **creating value** for others: your colleagues, your customers, your team, your entire organization.

    💡 By understanding the flow, the needs, and the metrics, you are empowered to **build better outcomes**, today and tomorrow.

    **SIPOC is not just a tool.**  
    It is a way to see **the purpose behind the process, and the people behind the purpose**.

    ✨ Now, ask yourself:

    > **Do you know who all your Customers are?**  
    > **Do you truly know the impact your work has on them?**

    ➡️ Start asking these questions.  
    ➡️ Start seeing beyond the task.  
    ➡️ Start building value — with awareness, with purpose, with heart. 💖
    """)

    if player_name.strip():
        df = pd.DataFrame(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sipoc_metrics_results_{player_name}_{timestamp}.csv"
        st.success("📥 Your results were saved!")
        st.download_button("⬇ Download your results", data=df.to_csv(index=False), file_name=filename, mime="text/csv")

sipoc_metrics_game()
