# chatbot.py

from cv_creator import CVCreatorAgent
from cv_reviewer import CVReviewerAgent


class MultiAgentChatbot:
    def __init__(self):
        self.creator = CVCreatorAgent()
        self.reviewer = CVReviewerAgent()

    def generate_and_review_cv(self, user_input):
        cv = self.creator.create_cv_section(user_input)
        feedback = self.reviewer.review_cv(cv)
        iteration = 1

        while iteration < 5 and not self.reviewer.is_satisfied(feedback):
            cv = self.creator.create_cv_section(
                f"{cv}\n\nFeedback: {feedback}\n\nRewrite the CV based on the feedback:"
            )
            feedback = self.reviewer.review_cv(cv)
            iteration += 1

        return cv, feedback
