# 트러블슈팅 카드 표지 시안: 실제 표시 크기(373x180)의 2배로 설계
D={'01':('검사 위치','인터셉터 1곳'),'03':('정답이 학습 데이터에 있던 비율','64%'),'04':('강원도 오차','24.4% → 7.05%')}
def card(n,l,v,bg):
    return f'''<!doctype html><meta charset=utf-8><style>*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:746px;height:360px;background:{bg};font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden;padding:38px 42px 40px;display:flex;flex-direction:column}}
.top{{display:flex;align-items:baseline;gap:14px}}
.n{{font-family:'Noto Serif CJK KR',serif;font-size:36px;font-weight:500;color:#5F7388;line-height:1}}
.l{{font-size:27px;font-weight:700;color:#4A5159;letter-spacing:-.01em}}
.v{{margin-top:auto;font-size:80px;font-weight:900;line-height:1;letter-spacing:-.02em;white-space:nowrap}}</style>
<div class="top"><span class="n">{n}</span><span class="l">{l}</span></div><div class="v">{v}</div>'''
for n,(l,v) in D.items():
    open(f'o1-{n}.html','w',encoding='utf-8').write(card(n,l,v,'#FFFFFF'))
    open(f'o2-{n}.html','w',encoding='utf-8').write(card(n,l,v,'#F1F4F7'))
