import subprocess
ARW=lambda c,s,w=2.6:f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="square"><path d="M7 17L17 7M8 7h9v9"/></svg>'
RA=lambda c,s:f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.6" stroke-linecap="square"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
D=[('01','검사 위치','인터셉터 1곳'),('03','정답이 학습 데이터에<br>있던 비율','64%'),('04','강원도 오차','24.4% → 7.05%')]
BASE="""*{margin:0;padding:0;box-sizing:border-box}
body{width:600px;height:300px;background:#fff;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden;position:relative}
.safe{position:absolute;left:56px;top:34px;width:488px;height:232px;display:flex;flex-direction:column}
.bar{width:488px;height:5px;background:#2B2D31;margin-bottom:18px;flex:none}
.top{display:flex;align-items:flex-start;justify-content:space-between;gap:24px}
.lab{display:flex;align-items:baseline;gap:14px;min-width:0}
.n{font-family:'Noto Serif CJK KR',serif;font-size:34px;font-weight:500;color:#5F7388;line-height:1;flex:none}
.l{font-size:27px;font-weight:700;color:#4A5159;line-height:1.35;word-break:keep-all}
.v{margin-top:auto;font-size:56px;font-weight:900;line-height:1;letter-spacing:-.02em;white-space:nowrap}
"""
def go0(): return f'<div style="flex:none;display:flex;gap:8px;align-items:center;font-size:22px;font-weight:700;border-bottom:2px solid #2B2D31;padding-bottom:3px">자세히 {ARW("#2B2D31",20)}</div>'
def A(n,l,v): # 채운 버튼
    g=f'<div style="flex:none;display:flex;gap:8px;align-items:center;font-size:21px;font-weight:700;background:#2B2D31;color:#fff;padding:8px 14px;margin-top:-4px">자세히 보기 {ARW("#fff",18)}</div>'
    return f'<div class="safe"><div class="bar"></div><div class="top"><div class="lab"><span class="n">{n}</span><span class="l">{l}</span></div>{g}</div><div class="v">{v}</div></div>'
def B(n,l,v): # 우하단 원형 화살표
    c=f'<div style="position:absolute;right:0;bottom:0;width:52px;height:52px;border-radius:50%;background:#2B2D31;display:flex;align-items:center;justify-content:center">{RA("#fff",26)}</div>'
    return f'<div class="safe"><div class="bar"></div><div class="top"><div class="lab"><span class="n">{n}</span><span class="l">{l}</span></div></div><div class="v" style="font-size:52px">{v}</div>{c}</div>'
def C(n,l,v): # 하단 띠
    s=f'<div style="position:absolute;left:0;right:0;bottom:0;height:42px;background:#2B2D31;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 16px;font-size:21px;font-weight:700;letter-spacing:.02em"><span>눌러서 상세 보기</span>{RA("#fff",22)}</div>'
    return f'<div class="safe"><div class="bar"></div><div class="top"><div class="lab"><span class="n">{n}</span><span class="l">{l}</span></div></div><div class="v" style="font-size:46px;margin-bottom:56px">{v}</div>{s}</div>'
for k,f in [('A',A),('B',B),('C',C)]:
    for n,l,v in D:
        open(f'{k}{n}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{BASE}</style>'+f(n,l,v))
        subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=1','--window-size=600,300',f'--screenshot={k}{n}.png',f'{k}{n}.html'],capture_output=True)
rows=[('현재 — "자세히 ↗" 밑줄 글자만 (밑줄 글자가 버튼처럼 안 보임)',None),('A — "자세히 보기" 검은 버튼',"A"),('B — 우하단 동그란 화살표 버튼',"B"),('C — 하단 검은 띠 "눌러서 상세 보기"',"C")]
h='<!doctype html><meta charset=utf-8><style>body{margin:0;padding:24px;width:1000px;background:#fff;font-family:"Noto Sans CJK KR"}h4{margin:22px 0 10px;color:#c00;font-size:16px}.r{display:flex;gap:14px}.r img{width:300px;height:150px;object-fit:cover;border:1px solid #E6E6E6;border-radius:6px;box-shadow:0 1px 3px rgba(0,0,0,.08)}</style>'
for t,k in rows:
    h+=f'<h4>{t}</h4><div class="r">'
    for n,_,_ in D:
        src=f'../../portfolio-assets/v26/wc-{n}.png' if k is None else f'{k}{n}.png'
        h+=f'<img src="{src}">'
    h+='</div>'
open('sheet.html','w',encoding='utf-8').write(h)
subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--window-size=1050,860','--screenshot=sheet.png','sheet.html'],capture_output=True)
