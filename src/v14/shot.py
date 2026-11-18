# 고정 크기 2배 렌더: python3 shot.py in.html out.png W H
import subprocess,sys
i,o,W,H=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2',f'--window-size={W},{H}',f'--screenshot={o}',i],capture_output=True)
