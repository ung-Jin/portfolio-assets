import subprocess,os
B="*{margin:0;padding:0;box-sizing:border-box}body{background:#fff;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden}"
n,t='09','경로의 육지 통과를 0.136%로 줄였습니다'
h=f'''<!doctype html><meta charset=utf-8><style>{B}
body{{width:1416px;height:170px}}.r{{position:absolute;left:0;right:0;bottom:0;height:140px;border-bottom:4px solid #2B2D31;display:flex;align-items:baseline;gap:28px;padding-bottom:26px}}
.n{{font-family:'Noto Serif CJK KR',serif;font-size:84px;font-weight:300;color:#5F7388;line-height:1}}
.t{{font-size:54px;font-weight:900;letter-spacing:-.015em;white-space:nowrap}}</style>
<div class="r"><span class="n">{n}</span><span class="t">{t}</span></div>'''
p=os.path.abspath('v34/case-09.html');open(p,'w',encoding='utf-8').write(h)
subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--window-size=1416,170','--screenshot='+os.path.abspath('../v34/case-09.png'),p],capture_output=True)
