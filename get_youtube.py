#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script downloads information for each video in a YouTube playlist,
# downloads any videos it doesn't already have,
# and deletes any videos that are no longer in the playlist,
# then saves the list as playlist.dat for use with play_youtube.py

import subprocess
import collections
import os
import pickle
import ConfigParser

abs_path = os.path.dirname(os.path.abspath(__file__)) + "/"

config = ConfigParser.ConfigParser()
config.readfp(open(abs_path + 'config.txt', 'r'))
playlist_id = config.get('FluxVision Config', 'playlist_id')
video_format = config.get('FluxVision Config', 'video_format')

class videoinfo(object):
	def __init__(self, title, youtubeID, filename):
		self.title = title
		self.youtubeID = youtubeID
		self.filename = filename

def update(playlist_id):
	#"lock" file keeps more than one instance from running
	with open(abs_path + '.get_youtube_lck', 'w'):
		os.utime(abs_path + '.get_youtube_lck', None)

	#for each video in playlist, get title, YouTube ID, and (aspirational) local file name (media/ID.mp4)
	raw_output = subprocess.check_output(['yt-dlp', '-o', "media/%(id)s.%(ext)s", 'https://www.youtube.com/playlist?list=' + playlist_id, '--get-filename', '--get-title', '--get-id'])
	youtube_data = raw_output.splitlines()

	#parse into readable list of classes
	playlist = []
	i=0
	while i < len(youtube_data):
		playlist.append(videoinfo(youtube_data[i], youtube_data[i+1], youtube_data[i+2]))
		i += 3

	#save the list of classes so play_youtube.py can use it
        with open(abs_path + ".playlist_dat", "wb") as f:
                pickle.dump(playlist, f)

	#if there's a video in the list that isn't already saved, download it
	for video in playlist:
		if os.path.isfile(abs_path + video.filename) is False:
			subprocess.check_output(['yt-dlp', '-o', abs_path + video.filename, "https://www.youtube.com/watch?v=" + video.youtubeID, "-f", video_format])

	#if there's a video that has been previously saved that is no longer on the list, delete it
	for file in os.listdir(abs_path + "media"):
		match = False
		for video in playlist:
			if abs_path + video.filename == abs_path + "media/" + file:
				match = True
		if match is False:
			os.remove(abs_path + "media/" + file)

	#removes lock file
	os.remove(abs_path + '.get_youtube_lck')

update(playlist_id)
