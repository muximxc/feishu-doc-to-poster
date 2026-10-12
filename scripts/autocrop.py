#!/usr/bin/env python3
import sys
from PIL import Image
def crop(in_path, out_path, pad=90):
    im = Image.open(in_path).convert("RGB")
    w, h = im.size; px = im.load(); last = h-1
    for y in range(h-1, 0, -1):
        hit = False
        for x in range(0, w, 4):
            r,g,b = px[x,y]
            if r<150 and g<120 and b<160: hit=True; break
            if r>150 and g<100 and b>120: hit=True; break
        if hit: last=y; break
    im.crop((0,0,w,min(h,last+pad))).save(out_path)
    print("cropped:", out_path, Image.open(out_path).size)
if __name__ == "__main__":
    crop(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv)>3 else 90)
