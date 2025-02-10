# CV Chat Agent

## Overview

The CV Chat Agent is a simple application that uses large language models (LLMs) to generate and refine CV sections based on user input. It leverages the power of OpenAI's models to create professional CV sections and provide detailed feedback for improvement.

## Features

- **CV Generation**: Uses OpenAI's models to create well-structured and professional CV sections.
- **CV Review**: Provides constructive feedback on the generated CV sections.
- **Feedback Loop**: Iteratively improves the CV based on feedback up to 5 times or until the reviewer is satisfied.
- **Streamlit Interface**: A user-friendly web interface for interacting with the CV Chat Agent.

## Setup

### Prerequisites

- Python 3.13 or later
- OpenAI API key

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/cv-chat-agent.git
    cd cv-chat-agent
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```
    
3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**

    Create a `secrets.toml` file in the `.streamlit` directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Running the Application

1. **Start the Streamlit app:**

    ```sh
    streamlit run streamlit_app.py
    ```

2. **Access the application:**

    Open your web browser and navigate to `http://localhost:8501` to use the CV Chat Agent.

## Usage

1. **Enter a CV Prompt:**
   - In the text area, enter the details or sections you want to include in your CV.

2. **Generate and Review CV:**
   - Click the "Generate and Review CV" button to start the process.
   - The application will display the initial CV and feedback.
   - The feedback loop will run up to 5 iterations, displaying each revised CV and the corresponding feedback.
   - The final CV and feedback will be shown, and you can download the final CV.

## Project Structure

- `.gitignore`: Specifies intentionally untracked files to ignore.
- `.python-version`: Specifies the Python version to use.
- `launch.json`: Configuration for debugging.
- `chatbot.py`: Defines the `MultiAgentChatbot` class.
- `cv_creator.py`: Defines the `CVCreatorAgent` class.
- `cv_reviewer.py`: Defines the `CVReviewerAgent` class.
- `hello.py`: A simple script to test the setup.
- `pyproject.toml`: Project metadata and dependencies.
- `streamlit_app.py`: The main Streamlit application file.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.