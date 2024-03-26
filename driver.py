import subprocess

script_list = ["smartgoggles.py", "audioplaying1.py"]

for script in script_list:
	
	subprocess.run(["python", script])

