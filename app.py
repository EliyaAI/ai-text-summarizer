code = """
import gradio as gr
from transformers import pipeline

summarizer = pipeline(
    \"summarization\",
    model=\"sshleifer/distilbart-cnn-12-6\"
)

def summarize_text(text):
    result = summarizer(
        text,
        max_length=80,
        min_length=20,
        do_sample=False
    )
    return result[0]['summary_text']

demo = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=12),
    outputs=\"text\",
    title=\"AI Text Summarizer\"
)

demo.launch()
"""

with open("app.py", "w") as f:
    f.write(code)
