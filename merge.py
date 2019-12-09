import math
import glob
import os
filepath = './img/'
w = 0
h = 0

from PIL import Image

def find_png():
	if os.path.isfile("merge.png"):
		os.remove("merge.png")
	files = [f for f in glob.glob(filepath + "*.png")]	
	files.sort()
	return int(math.ceil(math.sqrt(len(files)))), files

number, files = find_png()
for index, file in enumerate(files):
  	img = Image.open(file)
	w,h = img.size

result = Image.new("RGBA", (w*number, h*number))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((w, h), Image.ANTIALIAS)
  x = (index % number) * w
  y = int(index/number) * h
  w, h = img.size
  '''print('pos {0},{1} size {2},{3}'.format(x, y, w, h))'''
  result.paste(img, (x, y, x + w, y + h))

result.save('merge.png')
