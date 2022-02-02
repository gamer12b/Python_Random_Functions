d = "first.dll"

import subprocess
import sys
do = open(d, "r")
packages = [
    "requests",
    "pytube",
    "psutil",
    "pygame",
    "discord_webhook",
    "pyglet",
    "ursina",
    "gitpython",
    "googlemaps",
    "gtts",
    "speedtest_cli",
    "nmap",
    "nettools",
    "wifiinfo"
]
import time
if "0" in str(do.read()):
    do.close()
    print("Installing required packages..")
    do = open(d,"w")
    do.write("1")
    do.close()
    time.sleep(2)
    for package in reversed(packages):
        print("Installing "+package)
        time.sleep(0.3)
        subprocess.check_call([sys.executable,"-m","pip","install",package])
import time
import socket
import uuid
import random
import requests   # Download
import codecs
import pytube   # Download
import psutil   # Download
import pygame   # Download
import discord_webhook   # Download
import os
import pyglet   # Download
import tkinter
import googlemaps   # Download
import gtts   # Download
import speedtest_cli   # Download
import nmap   # Download python-nmap
import nettools    # Download
import wifiinfo   # Download
import configparser

from pytube import YouTube

def text_to_speech(text,language,name, slow):
    g = gtts.gTTS(text=text,lang=language,slow=slow, tld="com")
    g.save(name+".mp3")
def test_wifi():
    subprocess.check_call("speedtest-cli")
def random_number(nm1, nm2):
    print(random.randrange(int(nm1),int(nm2)))
def random_choice(list):
    print(random.choice(list))
def custom_command(command):
    subprocess.check_call(command)
def ip_host():
    print(socket.gethostbyname(socket.gethostname()))
    print(socket.gethostname())
def packages_available():
    for e in reversed(packages):
        print(e)
        time.sleep(0.4)
def encode(text, encoding):
    print(codecs.encode(bytes(text,encoding="utf8"), encoding))
def decode(text, decoding):
    print(codecs.decode(text, decoding))
def ls(dire):
    if dire == "here":
        l = os.listdir()
        print(l)
    else:
        l = os.listdir(dire)
        print(l)
def play(file):
    mixer = pygame.mixer
    music = mixer.music
    mixer.init()
    music.load(file)
    music.play(file)
def generate_uuid(type):
    if type == "4":
      print(str(uuid.uuid4()))
def video(link, resolution, title, desc, times):
  vid = YouTube(link)
  streams = vid.streams
  if title == "True":
    print(vid.title)
    print("")
  if desc == "True":
    print(f"{vid.description}\n\n")
  time.sleep(int(times))
  streams.filter(res=resolution).first().download()
def rm(file):
  os.remove(file)
def new(filename, extension):
  f = open(f"{filename}.{extension}","a")
  f.close()
def overwrite(amount):
  l = []
  for d in range(int(amount)):
    o = input("Enter file location: ")
    l.append(o)
  n = 0
  for i in l:
    print(i)
    n = n +1
    text = """
    ====== Virus ======
    This file has been taken over by
    the python pack virus, that will overwrite any files you specify, you cant undo it

    This file is gone
    /Killed by pack.py
    """
    e = open(i, "w")
    e.write(text)
    e.close()
    print("Success: "+str(n))
    time.sleep(0.25)
def rm_multiple(amount):
  e = []
  for i in range(amount):
    o = input("Enter file name: ")
    e.append(o)
  n = 0
  for s in e:
    n = n + 1
    os.remove(s)
    print("Successfully removed "+str(n) + " File(s)")

