import songs
import serializers
import yaml_serializer

song = songs.Song("1", "Water of Love", "Dire Straits")
serializer = serializers.ObjectSerializer()

print(serializer.serialize(song, "JSON"))
print("")
print(serializer.serialize(song, "XML"))
print("")
print(serializer.serialize(song, "YAML"))
