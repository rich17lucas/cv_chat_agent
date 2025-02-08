import base64

import streamlit as st

from chatbot import MultiAgentChatbot


def download_text(text, filename):
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">📥 Download {filename}</a>'
    return href


def main():
    st.set_page_config(page_title="Skippy's CV Agent", page_icon="🤖")
    st.title("Monkey approved CV Chatbot")
    st.write(
        "Generate and review your CV with the help of advanced (well, barely advanced) AI agents."
    )

    st.header("Generate and Review Your CV Section")
    user_input = st.text_area("Enter your CV prompt:", height=200)

    if st.button("🚀 Generate and Review CV"):
        if user_input:
            chatbot = MultiAgentChatbot()
            cv, feedback = chatbot.generate_and_review_cv(user_input)

            st.subheader("Initial CV")
            st.text(cv)
            st.subheader("Initial Feedback")
            st.text(feedback)

            iteration = 1
            while iteration < 5 and not chatbot.reviewer.is_satisfied(feedback):
                st.subheader(f"Iteration {iteration}")
                cv = chatbot.creator.create_cv_section(
                    f"{cv}\n\nFeedback: {feedback}\n\nRewrite the CV based on the feedback:"
                )
                feedback = chatbot.reviewer.review_cv(cv)
                st.text(cv)
                st.text(feedback)

                iteration += 1

            st.subheader("Final CV")
            st.text(cv)
            st.subheader("Final Feedback")
            st.text(feedback)
            st.markdown(download_text(cv, "final_cv.txt"), unsafe_allow_html=True)
    else:
        st.warning("Please enter a CV prompt.")


if __name__ == "__main__":
    main()
