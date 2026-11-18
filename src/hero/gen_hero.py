# 첫 이미지 최종: C 배치 + 이름 184 / 한 줄 소개 42 + 검은 칸 사진 자리
# 사용법: python3 gen_hero.py [사진경로]  (사진이 없으면 빈 사진 칸)
import sys
exec(open('gen.py',encoding='utf-8').read().split("# A:")[0])
exec(open('gen2.py',encoding='utf-8').read().split("# C-1:")[0].split("exec(")[1].split("\n",1)[1])
photo = sys.argv[1] if len(sys.argv)>1 else None
X,Y,W,H = 80,84,240,300
frame = 'outline:1px solid rgba(255,255,255,.25);outline-offset:8px;'
if photo:
    ph_html = f'<div class="abs" style="left:{X}px;top:{Y}px;width:{W}px;height:{H}px;{frame}overflow:hidden"><img src="{photo}" style="width:100%;height:100%;object-fit:cover;object-position:center top;display:block"></div>'
else:
    ph_html = ph(X,Y,W,H,dark=True).replace('class="abs ph"','class="abs ph" data-x').replace('border-color:#4A4E55;','border-color:#4A4E55;'+frame)
page('hero-final', left(184,46,42,176,392,474) + '<div class="panel"><div class="vert">PORTFOLIO &nbsp;·&nbsp; 2026</div>'+ph_html+stats(440,126)+'</div>'+FOOT)
print('ok', bool(photo))
