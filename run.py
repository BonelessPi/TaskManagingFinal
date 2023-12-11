import subprocess
import sys
from time import sleep


# Update if the requirements.txt file changes!
# Note that I didn't have this script open requirements.txt because "psycopg[binary]" isn't listed in `pip list`
REQUIRED_MODULES = [b'psycopg', b'psycopg-binary', b'dotenv']

# Check what modules are installed and skip install if possible
# This control flow was chosen since it will still display the output of `pip install`
pip_list_result = subprocess.run([sys.executable, "-m", "pip", "list"], capture_output=True)
# Note that `pip list` sends data to stdout
all_installed = all([m in pip_list_result.stdout for m in REQUIRED_MODULES])
if not all_installed:
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Run docker compose and wait a little extra if starting up (attempting to avoid a connection failure in the dbmanager)
docker_compose_result = subprocess.run(["docker", "compose", "up", "-d"], capture_output=True)
# Note that `docker compose up -d` sends data to stderr
containers_just_created = b'Created' in docker_compose_result.stderr
if containers_just_created:
    print("Waiting 10 seconds for the docker containers to finish setup")
    for _ in range(10):
        sleep(1)
        print('.',end='',flush=True)
    print()

subprocess.run([sys.executable, "src/gui.py"])