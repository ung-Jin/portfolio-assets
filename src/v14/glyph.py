import sys,numpy as np
from PIL import Image
# 지정한 세로 구간(1x 좌표)에서 글자가 시작하는 x(1x)
f,y0,y1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
a=np.asarray(Image.open(f).convert('RGB')).astype(int);s=a.shape[1]/1920
band=a[int(y0*s):int(y1*s)];m=np.abs(band-band[:,0:1]).sum(2)>60
xs=np.where(m.any(0))[0];print(f, 'start',xs[0]/s,'end',xs[-1]/s)
