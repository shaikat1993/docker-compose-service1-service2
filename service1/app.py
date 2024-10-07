import os
import json
import subprocess
from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_system_info():
    ip_address  = subprocess.getoutput("hostname -I").strip()
    processes   = subprocess.getoutput("ps -ax")
    disk_space  = subprocess.getoutput("df -h /")
    uptime      = subprocess.getoutput("uptime -p")
    return {
        "ip_address"    : ip_address,
        "processes"     : processes,
        "disk_space"    : disk_space,
        "uptime"        : uptime
    }

@app.route("/", methods=["GET"])
def system_info():
    service2_response = requests.get("http://service2:8200")
    service2_info = service2_response.json()

    service1_info = get_system_info()
    return jsonify({
        "Service1": service1_info,
        "Service2": service2_info
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8199)
