
import imageio
import os
pnglist=[]
filenames=[ a for a in os.listdir()]
for file in filenames:
    if file.endswith(".png"):
        pnglist.append(file)



images = []
for filename in pnglist:
    images.append(imageio.imread(filename))
imageio.mimsave('MSE.gif', images)