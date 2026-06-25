import subprocess

result = subprocess.run(["lsusb"], capture_output=True, text=True)

print(result.stdout)
