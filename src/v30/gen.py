import subprocess
rows=[('01','1차','냉·난방 AS기사 스케줄 관리','2026.09.07 ~ 09.15',2,14),
('02','2차','시도별 전력사용량 예측 대시보드','2026.09.18 ~ 10.16',2,80),
('03','3차','해상교통 안전경로 예측 시스템','',4,80)]
import re
d=open('../v14/ph-03.html').read()
m=re.search(r'class="p">([^<]*)',d); rows[2]=rows[2][:3]+(m.group(1),)+rows[2][4:]
t=re.search(r'class="t">([^<]*)',d).group(1); rows[2]=rows[2][:2]+(t,)+rows[2][3:]
for n,s,title,date,c,gap in rows:
    H=gap+9+48+96+42+3
    html=f'''<!doctype html><meta charset=utf-8><style>*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1920px;height:{H}px;background:#fff;font-family:'Noto Sans CJK KR';color:#2B2D31;overflow:hidden}}
.r{{position:absolute;left:0;right:0;top:{gap}px;border-top:6px solid #2B2D31;border-bottom:2px solid #C9CED4;padding:28px 60px 24px;display:flex;align-items:center;gap:30px}}
.n{{font-family:'Noto Serif CJK KR';font-size:96px;font-weight:400;line-height:1;color:#5F7388}}
.t{{font-size:34px;font-weight:900;display:block}}.p{{font-size:17px;font-weight:700;letter-spacing:.1em;color:#5F7388;display:block;margin-top:6px}}
.b{{margin-left:auto;font-size:20px;font-weight:700;letter-spacing:.14em;border:3px solid #2B2D31;padding:10px 18px}}</style>
<div class=r><span class=n>{s}</span><div><b class=t>{title}</b><span class=p>{date}</span></div><span class=b>{c} CASES</span></div>'''
    open(f'ph-{n}.html','w').write(html)
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2',f'--window-size=1920,{H}',f'--screenshot=../../v30/ph-{n}.png',f'ph-{n}.html'],capture_output=True)
