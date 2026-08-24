import sys
from PIL import Image
src, out, x0,y0,x1,y1, scale = sys.argv[1], sys.argv[2], *map(float, sys.argv[3:8])
im = Image.open(src)
W,H = im.size
box = (int(x0*W), int(y0*H), int(x1*W), int(y1*H))
c = im.crop(box)
c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(out)
print(out, c.size)
