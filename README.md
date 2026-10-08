# JP Managats Development Game

This project runs the browser games from a local Python Flask web server.
Sky Hopper's background track uses the locally supplied MP3 and loops only the
1:21–2:11 section while that game is active and sound is enabled.

## Run on Windows

Open PowerShell in this folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py app.py
```

Then open <http://127.0.0.1:5000> in your browser. Press `Ctrl+C` in PowerShell to stop the server.

If PowerShell blocks virtual-environment activation, run the commands without activating it:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

## Android APK

The `android-app` folder contains an Android WebView wrapper for
`https://jpmanagats.com/`. The website must be publicly hosted with working DNS
and a valid HTTPS certificate, and the phone needs internet access. See
[android-app/README.md](./android-app/README.md) for APK build instructions.
