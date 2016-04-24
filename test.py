import ISS
import country
import song
import youtube

print("Looking for the ISS")
coord = ISS.coord()

print("Finding country from coordinates {}, {}".format(*coord))
country_name, country_code = country.info(coord)

print("Looking for songs in {} ({})".format(country_name, country_code))
song = song.grab(country_code)

filename = youtube.get_file(song)

print("Playing \"{}\" by {}".format(song.name, song.artist))
