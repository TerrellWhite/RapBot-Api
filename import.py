from __future__ import print_function
import lyricsgenius as genius

rappers = [
	'J Cole',
	'Logic',
	'Kendrick Lamar',
]

api = genius.Genius('tZuQfFrwOfhBeNqz7CKzdurOGjz-X88Sukpfr8CFQbCU1acd3iR66MxbgoKtLY8V')

for rapper in rappers:
	artist = api.search_artist(rapper, max_songs=15, get_full_song_info=False)
	print(artist)
	artist.save_lyrics(format_='txt', overwrite=False, binary_encoding=True)  # Save lyrics to txt file
