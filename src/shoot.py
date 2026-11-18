# 긴 창으로 찍은 뒤 내용 끝에서 잘라 높이를 자동으로 맞춤 (잘림 방지)
import subprocess, glob
from PIL import Image
for f in sorted(glob.glob('card-*.html')+glob.glob('page-*.html')):
    out=f.replace('.html','.png')
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--window-size=1416,1400',f'--screenshot={out}',f],capture_output=True)
    im=Image.open(out).convert('RGB'); w,h=im.size
    px=im.load(); last=0
    for y in range(h-1,-1,-1):
        if any(sum(px[x,y])<740 for x in range(0,w,4)): last=y; break
    if last>=h-4: print('!! 창 높이 부족', f)
    c=im.crop((0,0,w,min(h,last+1+48))); c.save(out); print(out, c.size)
