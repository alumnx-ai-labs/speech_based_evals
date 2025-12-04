import gradio as gr
import requests
import json
import os

API_URL = "http://localhost:8000/process_audio"

def process_audio(audio_path):
    if not audio_path:
        return "No audio recorded", "", ""
    
    try:
        with open(audio_path, "rb") as f:
            files = {"file": f}
            response = requests.post(API_URL, files=files)
        
        if response.status_code != 200:
            return f"Error: {response.text}", "", ""
        
        data = response.json()
        
        transcription = data.get("transcription", "")
        evaluations = data.get("evaluations", [])
        total_cost = data.get("total_cost", 0.0)
        
        # Format evaluations
        eval_md = "## Evaluations\n\n"
        for eval_item in evaluations:
            eval_md += f"### {eval_item['model_name']}\n"
            eval_md += f"**Cost:** ${eval_item['cost']:.5f}\n"
            eval_md += f"**Tokens:** Input {eval_item['input_tokens']} / Output {eval_item['output_tokens']}\n\n"
            eval_md += f"{eval_item['evaluation']}\n\n"
            eval_md += "---\n\n"
            
        cost_md = f"## Total Cost: ${total_cost:.5f}"
        
        return transcription, eval_md, cost_md
        
    except Exception as e:
        return f"Error: {str(e)}", "", ""

with gr.Blocks(title="Audio Based Evaluator") as demo:
    gr.Markdown("# Audio Based Evaluator")
    gr.Markdown("### Question: What is the difference between `useEffect` and `useState` in React?")
    
    with gr.Row():
        audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Record Answer")
        
    submit_btn = gr.Button("Evaluate", variant="primary")
    
    with gr.Row():
        transcription_output = gr.Textbox(label="Transcription", lines=5)
    
    with gr.Row():
        evaluations_output = gr.Markdown(label="Evaluations")
        
    with gr.Row():
        cost_output = gr.Markdown(label="Total Cost")
        
    submit_btn.click(
        fn=process_audio,
        inputs=[audio_input],
        outputs=[transcription_output, evaluations_output, cost_output]
    )

if __name__ == "__main__":
    demo.launch()
