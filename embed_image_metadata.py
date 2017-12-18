import subprocess
import os

for root, dirs, files in os.walk('/Path/to/image/directory'):
	
	for name in files:
		filepath = os.path.join(root,name)
		
		###this example writes "Primary" to the IPTC Keywords field and overwrites the original file###
		metadata_write = subprocess.run(["exiftool", "-IPTC:Keywords=Primary", "-P","-overwrite_original", filepath])