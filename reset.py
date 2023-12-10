import subprocess
import shutil

subprocess.call(["docker", "compose", "down"])
shutil.rmtree("postgres",True)