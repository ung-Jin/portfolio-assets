# 연락처 라벨 v18: 바탕 투명, 라벨만 (회색 상자 안에 들어감)
import subprocess
BASE="*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1120px;height:44px;font-family:'Noto Sans CJK KR',sans-serif;overflow:hidden}"
for k,l in (('email','EMAIL'),('github','GITHUB')):
    open(f'ct-lab-{k}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{BASE}</style><div style="padding-top:8px;font-size:26px;line-height:1;letter-spacing:.24em;font-weight:700;color:#5F7388">{l}</div>')
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--default-background-color=00000000','--window-size=1120,44',f'--screenshot=ct-lab-{k}.png',f'ct-lab-{k}.html'],capture_output=True)
print('ok')
