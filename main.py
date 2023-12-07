from fastapi import FastAPI
import subprocess

app = FastAPI()

# root url
@app.get("/")
def get_container_ip():
	command="tail -1 /etc/hosts | awk '{print $1}'"
	ip = subprocess.run(command, shell=True, text=True, capture_output=True)
	ip_formatted = ip.stdout.strip()
	return f"Container IP is {ip_formatted}"

# healthcheck point
@app.get("/healthstatus")
def display_health_status():
    return {"status": "OK"}
