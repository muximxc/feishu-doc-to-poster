#!/usr/bin/env python3
import os, subprocess, sys
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
def render(html_path, out_png, width=1080, win_h=3400):
    os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"
    url = "file://" + os.path.abspath(html_path)
    cmd = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
           "--hide-scrollbars", "--force-device-scale-factor=2",
           f"--window-size={width},{win_h}",
           f"--screenshot={os.path.abspath(out_png)}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    if not os.path.exists(out_png):
        raise RuntimeError(f"Chrome render failed: {r.stderr[-500:]}")
    print("rendered:", out_png, os.path.getsize(out_png))
if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2],
           int(sys.argv[3]) if len(sys.argv)>3 else 1080,
           int(sys.argv[4]) if len(sys.argv)>4 else 3400)
