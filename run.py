import subprocess

subprocess.call(["pip", "install", "-r", "requirements.txt"])
subprocess.call(["docker", "compose", "up", "-d"])
subprocess.call(["python", "src/gui.py"])