# Shows artist info for a URN or URL

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint

username = sys.argv[1] if len(sys.argv) > 1 else 'plamere'
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
sp.trace = True
user = sp.user(username)
pprint.pprint(user)
