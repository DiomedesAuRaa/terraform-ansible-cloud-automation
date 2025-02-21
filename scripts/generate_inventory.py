import json
import os

with open("terraform/outputs.json") as f:
    outputs = json.load(f)

instance_ips = outputs["instance_ips"]["value"]

with open("ansible/inventory/hosts", "w") as f:
    f.write("[web]\n")
    for i, ip in enumerate(instance_ips):
        f.write(f"web-server-{i+1} ansible_host={ip}\n")
