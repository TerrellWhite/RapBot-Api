from __future__ import print_function
import io
import os

os.remove('./data.txt')

for entry in os.scandir('./clean'):
	with io.open(entry, 'r') as f:
		file = f.read()
		new_path = './data.txt'
		new_lyrics_file = open(new_path, 'a+')
		new_lyrics_file.write(file)
		new_lyrics_file.close()
