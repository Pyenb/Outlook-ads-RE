import psutil, time

blocked_exe = "msedgewebview2.exe"
blocked_args = ["--renderer-client-id=7", "--webview-exe-name=olk.exe"]
suspended_pids = []

while True:
    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'exe']):
        if blocked_exe in proc.info['name'] and all(arg in proc.info['cmdline'] for arg in blocked_args):
            if proc.pid not in suspended_pids:
                try: 
                    proc.suspend()
                    suspended_pids.append(proc.pid)
                    print(f"Blocked {proc.pid} {proc.info['name']}")
                except: pass
    for pid in suspended_pids:
        if not psutil.pid_exists(pid):
            suspended_pids.remove(pid)
    time.sleep(0.1)