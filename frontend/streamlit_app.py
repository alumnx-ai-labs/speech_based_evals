import streamlit as st
import requests
import json

# Configuration
API_URL = "http://localhost:8000/process_audio"

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
                    
                    response = requests.post(API_URL, files=files)
                    
                    if response.status_code != 200:
                        st.error(f"Error: {response.text}")
                    else:
                        data = response.json()
                        display_results(data)
                        
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

def display_results(data):
    transcription = data.get("transcription", "")
    evaluations = data.get("evaluations", [])
    total_cost = data.get("total_cost", 0.0)
    
    # Layout for results
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Transcription")
        st.info(transcription)
        
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

if __name__ == "__main__":
    main()
