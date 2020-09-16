import serializer_demo as sd

song = sd.Song("1", "Water of Love", "Dire Straits")
serializer = sd.SongSerializer()
print(serializer.serialize(song, "JSON"))
print("")
print(serializer.serialize(song, "XML"))
# serializer.serialize(song, "YAML")
