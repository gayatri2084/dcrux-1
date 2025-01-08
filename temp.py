import streamlit as st
import pandas as pd
import datetime

# Store assessment data (in-memory for this example, use a database for production)
assessment_data = []

def calculate_risk_score(answers):
    score = 0
    if answers["feeling_down"] > 3:
        score += 2
    if answers["sleep_problems"] > 3:
        score += 1
    if answers["loss_of_interest"]:
        score += 3
    if answers["social_withdrawal"]:
        score += 2
    return score

def recommend_interventions(risk_score):
    if risk_score >= 6:
        return "High Risk: Immediate consultation with counselor recommended."
    elif risk_score >= 3:
        return "Medium Risk: Consider scheduling a check-in with counselor, explore self-help resources."
    else:
        return "Low Risk: Continue self-monitoring, utilize available resources."

st.title("Student Wellbeing Risk Assessment")

with st.expander("About this assessment"): # Added an expander for context
    st.write("""This is a simplified self-assessment tool designed to help you reflect on your wellbeing. 
             It is not a diagnostic tool and should not replace professional consultation. If you are 
             experiencing significant distress, please reach out to a counselor or mental health professional.""")

feeling_down = st.slider("How often have you been feeling down, depressed, or hopeless?", 1, 5, 3)
sleep_problems = st.slider("How often have you had trouble falling or staying asleep?", 1, 5, 2)
loss_of_interest = st.checkbox("Have you noticed a loss of interest or pleasure in things you usually enjoy?")
social_withdrawal = st.checkbox("Have you been withdrawing from social activities or isolating yourself?")

answers = {
    "feeling_down": feeling_down,
    "sleep_problems": sleep_problems,
    "loss_of_interest": loss_of_interest,
    "social_withdrawal": social_withdrawal,
}

risk_score = calculate_risk_score(answers)
st.write(f"Risk Score: {risk_score}")

recommendation = recommend_interventions(risk_score)
st.write(f"Recommendation: {recommendation}")

if risk_score >= 6:
    st.warning("A notification would be sent to the counselor in a real application. This is a simulation.")

    # Simulate data logging (replace with database interaction in production)
    assessment_data.append({
        "timestamp": datetime.datetime.now(),
        "risk_score": risk_score,
        "answers": answers
    })

    st.write("Assessment data logged (simulation).")

# Add a section to display past assessments (for the user)
if assessment_data:
    st.subheader("Your Assessment History (Simulated)")
    df = pd.DataFrame(assessment_data)
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S') # Format timestamp
    st.dataframe(df)
else:
    st.write("No assessment history yet.")

# Add resources section
st.subheader("Resources")
st.write("Here are some resources that may be helpful:")
st.markdown("* [Crisis Text Line](https://www.crisistextline.org/): Text HOME to 741741")
st.markdown("* [The National Suicide Prevention Lifeline](https://suicidepreventionlifeline.org/): 988")
st.markdown("* [MentalHealth.gov](https://www.mentalhealth.gov/)")


# Add a feedback section
st.subheader("Feedback")
feedback = st.text_area("Please provide any feedback on this tool:")
if st.button("Submit Feedback"):
    if feedback:
        st.success("Thank you for your feedback!")
        # In a real app, store this feedback
    else:
        st.warning("Please enter some feedback.")