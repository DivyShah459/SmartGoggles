from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os
from autocorrect import Speller
import pyttsx3
import subprocess
import librosa
from subprocess import TimeoutExpired
import vlc


st = time.time()

# Initialize Chrome options
service = Service(executable_path="/usr/bin/chromedriver")
options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_argument("--start-maximized")

chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images":2}
chrome_prefs["profile.maanged_default_content_settings"] = {"images": 2}

driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
driver.get('https://abcbraille.com')

upload_file = os.path.abspath('brailleimages/104classroom.jpg')
print(upload_file, end=':\n')

driver.find_element(By.ID, "file").send_keys(upload_file)

driver.find_element(By.NAME, "btnTranslate").click()

words = driver.find_element(By.XPATH, '//div[2]/div/ol')
print(words.text, end='\n\n')

spell = Speller(fast=True)

newtext = spell(words.text.lower())
print(newtext)

engine = pyttsx3.init()
engine.setProperty('volume', 1.0)  
voices = engine.getProperty('voices')
engine.setProperty('voice', 12)
engine.save_to_file(newtext, 'audio.mp3')

engine.runAndWait()

'''
my_audio = vlc.MediaPlayer("audio.mp3")
my_audio.play()
vlc.libvlc_media_player_set_time(my_audio, 2000)
my_audio.pause()
'''

'''
player = mpv.MPV()
player.play('audio.mp3')
player.wait_for_playback()
'''

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
#subprocess.Popen(['cvlc', '--start-time','--play-and-exit','audio.mp3']).wait(4)



'''
instance = vlc.Instance('--aout=alsa')
p = instance.media_player_new()
m = instance.media_new('audio.mp3')
p.set_media(m)
p.play()
p.pause()
vlc.libvlc_audio_set_volume(p,85)
'''

