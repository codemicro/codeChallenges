from PIL import Image
import imageio
import pygifsicle 
import os

OUTPUT = "./output.gif"

TEMP_FILE_LOCATION = "temp"

print("Loading source images")

IMAGE_ONE = Image.open("one.png")
IMAGE_TWO = Image.open("two.png")

transparent_frames = []

print("Building transparent frames")

for i in range(257):
    if i % 6 == 0:
        c = IMAGE_TWO.copy()
        c.putalpha(i)
        transparent_frames.append(c)

print("Building frames")

frames = []

for t_fr in transparent_frames:
    ni = IMAGE_ONE.copy()
    ni.paste(t_fr, (0, 0), t_fr)
    frames.append(ni)

del transparent_frames

print("Building GIF")

with imageio.get_writer(OUTPUT, mode="I") as writer:
    for fr in frames + list(reversed(frames)):
        fr.save(TEMP_FILE_LOCATION, "PNG")
        writer.append_data(imageio.imread(TEMP_FILE_LOCATION))

os.remove(TEMP_FILE_LOCATION)    

# See https://github.com/LucaCappelletti94/pygifsicle#how-do-i-install-this-package
# Uncomment the below line to compress the resultant GIF
# pygifsicle.optimize(OUTPUT)
