import sys,numpy as np
from PIL import Image
for f in sys.argv[1:]:
    a=np.asarray(Image.open(f).convert('RGB')).astype(int);h,w,_=a.shape
    L=np.abs(a-a[:,0:1]).sum(2)>60;R=np.abs(a-a[:,-1:]).sum(2)>60
    l=np.where(L.any(0))[0];r=np.where(R.any(0))[0]
    print(f"{f:28s} {w}x{h} left {l[0]*1920/w if len(l) else -1:6.1f} right {(w-1-r[-1])*1920/w if len(r) else -1:6.1f}  (/1920)")
