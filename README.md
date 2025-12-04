# Audio Based Evaluator

This project captures voice input, transcribes it using OpenAI Whisper, and evaluates the transcription against a specific technical question using Gemini-2.5-Flash and GPT-5.

## Features

- **Voice Input**: Capture audio directly from the browser.
- **Transcription**: High-accuracy transcription using OpenAI Whisper.
- **Parallel Evaluation**: Uses LangGraph to run Gemini and GPT-4 evaluations in parallel.
- **Cost Tracking**: Displays token usage and estimated cost for each step (Whisper + LLMs).
- **LangSmith Tracing**: Integrated tracing for debugging and monitoring.

## Prerequisites

- Python 3.9+
- ffmpeg (required for audio processing)
  - Linux: `sudo apt-get install ffmpeg`
  - Mac: `brew install ffmpeg`
  - Windows: Download and add to PATH.

## Setup

1.  **Clone the repository** (if applicable) or navigate to the project folder.

2.  **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**:
    Copy `.env.template` to `.env` and fill in your API keys.

    ```bash
    cp .env.template .env
    ```

    Required Keys:

    - `OPENAI_API_KEY`: For Whisper and GPT-4.
    - `GOOGLE_API_KEY`: For Gemini.
    - `LANGCHAIN_API_KEY`: For LangSmith tracing.
    - `LANGCHAIN_TRACING_V2=true`
    - `LANGCHAIN_PROJECT`: Project name for LangSmith.

## Usage

1.  **Start the Backend**:

    ```bash
    uvicorn backend.main:app --reload
    ```

    The backend will run at `http://localhost:8000`.

2.  **Start the Frontend** (in a new terminal):

    ```bash
    python frontend/app.py
    ```

    The Gradio interface will open in your browser (usually `http://127.0.0.1:7860`).

3.  **Evaluate**:
    - Click the microphone icon to record your answer to: _"What is the difference between `useEffect` and `useState` in React?"_
    - Click "Evaluate".
    - View the transcription, evaluations from both models, and the total cost.

## Project Structure

- `backend/`: FastAPI app and LangGraph workflow.
- `frontend/`: Gradio application.
- `requirements.txt`: Python dependencies.
