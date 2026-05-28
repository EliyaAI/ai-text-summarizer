readme = """
# AI Text Summarizer

Simple NLP project using Hugging Face Transformers and Gradio.

## How it works
- Input text
- AI summarizes it
- Shows result in web UI

Model: distilbart-cnn-12-6
"""

with open("README.md", "w") as f:
    f.write(readme)
