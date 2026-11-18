# 트러블슈팅 카드 표지 v15 — 잘림 방지 안전 구역 버전
# 노션 갤러리(카드 크게): 표지 높이 180px 고정, 카드 폭은 화면에 따라 약 300~405px (비율 1.67~2.25)
# 캔버스 720x360(2:1). 가장 좁은 카드(1.67)에서 좌우 60씩, 가장 넓은 카드(2.25)에서 위아래 20씩 잘림
# → 모든 내용을 x 100~620, y 60~300 안에 둠 (잘린 뒤에도 최소 20px 여백)
import subprocess, sys
ARW=lambda c,s:f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="square"><path d="M7 17L17 7M8 7h9v9"/></svg>'
D8=[('01','검사 위치','인터셉터 1곳'),('02','SQL 파일','1개로 통일'),('03','정답이 학습 데이터에<br>있던 비율','64%'),('04','강원도 오차','24.4% → 7.05%'),('05','히트맵 구현 방식','3번 교체'),('06','사고다발 칸<br>구분 확률','85.6%'),('07','날씨 모델 AUC','0.549'),('08','새 저장소 검색 결과','0건')]
CSS="""*{margin:0;padding:0;box-sizing:border-box}
body{width:720px;height:360px;background:#F1F4F7;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden;position:relative}
.safe{position:absolute;left:100px;top:60px;width:520px;height:236px;display:flex;flex-direction:column}
.top{display:flex;align-items:flex-start;justify-content:space-between;gap:24px}
.lab{display:flex;align-items:baseline;gap:14px;min-width:0}
.n{font-family:'Noto Serif CJK KR',serif;font-size:40px;font-weight:500;color:#5F7388;line-height:1;flex:none}
.l{font-size:31px;font-weight:700;color:#4A5159;letter-spacing:-.01em;line-height:1.35;word-break:keep-all}
.go{flex:none;display:flex;align-items:center;gap:8px;font-size:26px;font-weight:700;color:#2B2D31;letter-spacing:.04em;border-bottom:3px solid #2B2D31;padding-bottom:3px;margin-top:2px}
.v{margin-top:auto;font-size:68px;font-weight:900;line-height:1;letter-spacing:-.02em;white-space:nowrap}
"""
GUIDE='<div style="position:absolute;left:100px;top:60px;width:520px;height:240px;outline:1px dashed red"></div>'
def card(n,l,v,guide=False):
    return f'<!doctype html><meta charset=utf-8><style>{CSS}</style><div class="safe"><div class="top"><div class="lab"><span class="n">{n}</span><span class="l">{l}</span></div><div class="go">자세히 {ARW("#2B2D31",23)}</div></div><div class="v">{v}</div></div>'+(GUIDE if guide else '')
for n,l,v in D8:
    open(f'wc-{n}.html','w',encoding='utf-8').write(card(n,l,v))
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--window-size=720,360',f'--screenshot=wc-{n}.png',f'wc-{n}.html'],capture_output=True)
print('ok')
