import os
import subprocess

# Check for presence of 'output' folder
# Clear the existing folder if found
# Create folder if not found
if os.path.exists("output"):
    subprocess.Popen(["bash", "-c", "cd output && rm *"]).wait()
else:
    os.makedirs("output")


# Import IP address and URL from target file
target = {}
with open("target") as f:
    for line in f:
        if "=" in line:
            key,value = line.strip().split("=", 1)
            target[key] = value
IP = target["IP"]
URL = target["URL"]


print("Targets found from \"target\" file:")
print()
print("IP Address: " + IP)
print("URL: "+URL)
print()



# Run Scans and send their outputs to 'output' folder

print("Running whois scan on "+URL)
whois_process = subprocess.Popen(["bash", "-c", f"whois {URL} > output/whois.txt"])

print("Running nslookup on "+URL)
nslookup_process = subprocess.Popen(["bash", "-c", f"nslookup {URL} > output/nslookup.txt"])

print("Pinging "+IP)
ping_process = subprocess.Popen(["bash", "-c", f"ping {IP} -c 5 > output/ping.txt"])


whois_process.wait()
nslookup_process.wait()
ping_process.wait()




# Notify when all scans are done
print()
print()
print("Finished all scans")
print()

subprocess.run(["notify-send", "Recon Script", "Scan finished successfully!"])