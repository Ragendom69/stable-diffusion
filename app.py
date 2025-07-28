import gradio as gr
import subprocess

def generate(prompt):
    result = subprocess.run(
        ["python", "launch.py", "--prompt", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout

iface = gr.Interface(fn=generate, inputs="text", outputs="text")
iface.launch()
