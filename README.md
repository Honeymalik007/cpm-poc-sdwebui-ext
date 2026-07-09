# cpm-poc-sdwebui-ext

Research artifact — JHU EN.601.441/641 CPM study (Cross-Party Misdelegation).

Demonstrates the **XSS → extension install → RCE** chain in AUTOMATIC1111/stable-diffusion-webui.

When stable-diffusion-webui loads this extension at startup, `scripts/rce_poc.py` executes OS commands at module import time and writes proof output to `/tmp/sdwebui_cpm_rce_proof.txt`.

**Do not install outside an isolated research environment.**
