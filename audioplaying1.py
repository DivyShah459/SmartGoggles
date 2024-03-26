import subprocess


try:
	subprocess.Popen(['cvlc', '--start-time','--play-and-exit','audio.mp3']).wait(4)
except subprocess.TimeoutExpired:
	pass

	
