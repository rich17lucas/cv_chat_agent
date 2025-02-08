""" Streamlit app for the CV Chat Agent. """

import streamlit as st

from chatbot import MultiAgentChatbot

# Initialize the chatbot
chatbot = MultiAgentChatbot()
st.set_page_config(page_title="Skippy's CV Agent", page_icon="🤖")

# App title and description
st.title("Monkey approved CV Chatbot")
st.write(
    """
Generate and review your CV with the help of advanced (well, barely advanced) AI agents.
"""
)

# User Input Section
st.header("Generate and Review Your CV Section")
user_prompt = st.text_input(
    "Enter your CV prompt: (the more skills you add the better!)",
    "Generate a summary for a software engineer CV.",
)

# Generate and Review Button
if st.button("🚀 Generate and Review CV"):
    if user_prompt.strip():
        with st.spinner("🔮 Generating your CV..."):
            try:
                cv, feedback = chatbot.generate_and_review_cv(user_prompt)

                # Display Generated CV
                st.subheader("📄 Generated CV Section:")
                st.text_area("🖊 CV Content:", cv, height=200)

                # Display Reviewer Feedback
                st.subheader("📝 Reviewer Feedback:")
                st.text_area("💬 Feedback:", feedback, height=150)

                # Optional: Download Buttons
                import base64

                def download_text(text, filename):
                    b64 = base64.b64encode(text.encode()).decode()
                    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download {filename}</a>'
                    return href

                st.markdown(
                    download_text(cv, "generated_cv.txt"), unsafe_allow_html=True
                )
                st.markdown(
                    download_text(feedback, "feedback.txt"), unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"⚠️ An error occurred: {e}")
    else:
        st.error("🐵 Come on, you monkeys! Enter a prompt before hitting the button.")
