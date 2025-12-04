import streamlit as st
import requests
import json

# Configuration
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
API_URL = os.getenv("BACKEND_URL") or "http://localhost:8000"

st.set_page_config(
    page_title="Audio Based Evaluator",
    page_icon="🎙️",
    layout="wide"
)

def main():
    st.title("🎙️ Audio Based Evaluator")
    st.markdown("### Question: What is the difference between `useEffect` and `useState` in React?")

    # Audio Input
    audio_value = st.audio_input("Record your answer")

    if audio_value:
        # Create a placeholder for status
        status_container = st.empty()
        
        # Add a button to explicitly trigger evaluation if desired, 
        # or just process automatically. Let's process automatically 
        # but show a spinner.
        
        # Actually, st.audio_input returns the value when recording stops.
        # It might be better to have a button to confirm sending to backend 
        # to avoid accidental sends, but the user request was simple.
        # Let's add a button for better UX.
        
        st.audio(audio_value)
        
        if st.button("Evaluate Answer", type="primary"):
            with st.spinner("Processing audio..."):
                try:
                    # Prepare the file for upload
                    # st.audio_input returns a BytesIO-like object
                    files = {"file": ("audio.wav", audio_value, "audio/wav")}
                    
                    response = requests.post(API_URL + "/process_audio" , files=files)
                    
                    if response.status_code != 200:
                        st.error(f"Error: {response.text}")
                    else:
                        data = response.json()
                        display_results(data)
                        
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

def display_results(data):
    transcription = data.get("transcription", "")
    transcription_cost = data.get("transcription_cost", 0.0)
    evaluations = data.get("evaluations", [])
    total_cost = data.get("total_cost", 0.0)
    
    # Layout for results
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Transcription")
        st.info(transcription)
        st.caption(f"**Transcription Cost:** ${transcription_cost:.5f}")
        
    with col2:
        st.subheader("Evaluations")
        for eval_item in evaluations:
            with st.expander(f"Model: {eval_item['model_name']}", expanded=True):
                st.markdown(eval_item['evaluation'])
                st.divider()
                st.caption(f"**Cost:** ${eval_item['cost']:.5f} | **Tokens:** In {eval_item['input_tokens']} / Out {eval_item['output_tokens']}")

    # Total Cost at the bottom
    st.divider()
    st.metric("Total Cost", f"${total_cost:.5f}")

    display_pricing_info()

def display_pricing_info():
    with st.expander("View Pricing Information"):
        st.markdown("""
        | Model | Provider | Input Price (per 1M tokens) | Output Price (per 1M tokens) | Notes |
        |---|---|---|---|---|
        | Gemini 2.5 Flash | Google | $0.30 | $2.50 | Optimized for high-throughput, low-latency, and multi-modal tasks. |
        | Gemini 2.5 Flash-Lite | Google | $0.10 | $0.40 | The cheapest tier, built for high-volume, cost-sensitive text workloads. |
        | GPT-5 (Standard) | OpenAI | $1.25 | $10.00 | The base model in the GPT-5 family. |
        | GPT-5 mini | OpenAI | $0.25 | $2.00 | A more cost-effective option than the standard GPT-5. |
        | GPT-5 nano | OpenAI | $0.05 | $0.40 | The lowest-cost option in the family, for ultra-cheap, latency-sensitive micro-tasks. |
        """)

if __name__ == "__main__":
    main()
