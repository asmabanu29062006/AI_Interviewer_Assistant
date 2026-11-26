
import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Interview Assistant", layout="centered")

st.title("AI Interview Assistant")
st.caption("Practice interviews with AI-generated questions and constructive feedback.")
st.caption("Launched By Asma Banu")
st.write("Department of AI & DS")

# Connect to Groq API
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    st.success("API connected successfully!")

except (KeyError, FileNotFoundError):
    st.error("GROQ_API_KEY is missing. Add it to Streamlit Cloud → App settings → Secrets.")
    st.stop()

# Select Job Role
role = st.selectbox(
    "Select Job Role",
    [
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Machine Learning Engineer",
        "Software Engineer",
        "HR Executive"
    ]
)

# Generate Interview Questions
if st.button("Generate Interview Questions"):

    prompt = "Generate 5 interview questions for the role of " + role

    try:
        with st.spinner("Generating interview questions..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert technical interviewer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            output = response.choices[0].message.content

            st.subheader("Generated Interview Questions")
            st.write(output)

    except Exception as e:
        st.error(f"Error generating questions: {e}")


  
