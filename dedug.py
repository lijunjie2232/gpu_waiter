import subprocess

subprocess.run(
    ["python", "src/main.py", "-c", "ls -alh /usr/local", "-m", "23g", "-g", "2"]
)
