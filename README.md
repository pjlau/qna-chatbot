# Q&A Chatbot with FastAPI and Local LLM

A simple web application that displays a set of Q&As and allows users to ask questions via a textbox. The backend uses FastAPI, and a local LLM (e.g., Phi-3 via Ollama) generates answers based on the Q&As or its knowledge.

## Features
- Displays predefined Q&As on a clean HTML page.
- User can submit questions via a textbox.
- Local LLM (Phi-3) matches questions to Q&As or generates answers.
- FastAPI backend for high performance.

## Prerequisites
- Python 3.8+
- Ollama installed (https://ollama.com/)
- Git

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/pjlau/qna-chatbot.git
   cd qna-chatbot
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
3. Pull a free LLM model (e.g., `phi3` for efficiency and `llama3` as alternative):
   ```bash
   ollama pull phi3
4. Run the server command.
    ```bash
    python main.py
5. Try out the Q&A bot at `http://localhost:8000`. 

6. Finish the server process by pressing `Ctrl+C`. 