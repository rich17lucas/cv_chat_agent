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
        return cv, feedback
