import streamlit as st
from google import genai


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Learning Buddy Rabbit",
    page_icon="🎓"
)


# --------------------------------------------------
# GEMINI CONFIGURATION
# --------------------------------------------------

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

MODEL_NAME = "gemini-3.8-flash-lite"


# --------------------------------------------------
# UI
# --------------------------------------------------

st.title("🎓 AI Learning Buddy Rabbit")


topic = st.text_input("Enter a Topic")


option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)


# --------------------------------------------------
# GENERATE RESPONSE
# --------------------------------------------------

if st.button("Generate"):

    if not topic.strip():

        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":

            prompt = (
                f"Explain {topic} in simple language "
                "for a beginner."
            )

        elif option == "Real-Life Example":

            prompt = (
                f"Give one simple real-life example "
                f"of {topic}."
            )

        elif option == "Generate Quiz":

            prompt = (
                f"Create 5 MCQs on {topic} "
                "with answers."
            )

        else:

            prompt = topic

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            st.write(response.text)

        except Exception as e:

            st.error(
                "Unable to generate a response. "
                "Please try again."
            )

            st.caption(f"Error: {e}")
