# 하위 페이지(본문 폭 약 708px)용 이미지: 2배 크기(1416px)로 설계, 높이는 내용에 맞춰 자동
import re, html as H
src_cards=open('../gen_cards.py',encoding='utf-8').read()
CARDS={k:eval(v) for k,v in re.findall(r"C\['(t\d)'\]=card\('t\d',(\[.*?\]),\d+\)",src_cards,re.S)}
src_pages=open('../gen_pages.py',encoding='utf-8').read()
projects=eval(re.search(r"projects = (\[.*?\n\])",src_pages,re.S).group(1))
ts=eval(re.search(r"\nts = (\[.*?\n\])",src_pages,re.S).group(1))

SPLIT={1:'로그인 없이 관리자 화면에 들어가지던 문제를\n한 곳에서 막았습니다',
2:'서로 다른 DB 파일을 합치고,\n들어오는 수정은 하나씩 확인하며 병합했습니다',
3:'좋아 보이던 예측 점수가 부풀려진 것임을 확인하고\n검증 방식을 고쳤습니다',
4:'전체 평균에 가려져 있던 한 지역의 오류를\n찾아 해결했습니다',
5:'히트맵을 세 번 다시 만들어,\n직접 설명할 수 있는 방식으로 정했습니다',
6:'비율을 정한 이유를 숫자로 설명할 수 있도록,\n조합을 채점해 골랐습니다',
8:'날씨로 사고를 예측할 수 없다는 것을 확인하고,\n날씨의 쓰임을 바꿨습니다',
9:'공개하면 안 되는 주소와 비밀번호를 코드 밖으로 빼고,\n기록에서도 지웠습니다'}
ts=[(n,p,t,c,st,SPLIT[n]) for (n,p,t,c,st,r) in ts]
projects=[(k,t,per,role,res,stack.replace(' · FastAPI','')) for (k,t,per,role,res,stack) in projects]
BASE="""*{margin:0;padding:0;box-sizing:border-box}
body{width:1416px;background:#fff;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31}
.wrap{padding:8px 0 36px}
em{font-style:normal;color:#5F7388;font-weight:700}
"""
# ---------- 결과 카드 ----------
CCSS=BASE+""".top{display:flex;align-items:center;gap:16px;margin:20px 0 28px}
.top i{width:44px;height:5px;background:#5F7388}.top b{font-size:24px;letter-spacing:.3em;color:#5F7388;font-weight:700}
.m{padding:26px 0 30px;border-top:1px solid #DDE4EB}
.lab{font-size:27px;font-weight:700;color:#4A5159;margin-bottom:14px;word-break:keep-all}
.val{display:flex;align-items:baseline;gap:24px;font-weight:900;line-height:1.05;flex-wrap:wrap;letter-spacing:-.02em}
.b{color:#B9C4CF}.arrow{color:#5F7388;font-weight:400;font-size:.6em}
.cap{margin-top:16px;font-size:29px;line-height:1.55;word-break:keep-all}
.bars{display:flex;flex-direction:column;gap:20px;margin-top:6px}
.bar{display:flex;align-items:center;gap:24px}.bar .n{width:520px;flex-shrink:0;font-size:29px;word-break:keep-all}
.bar .t{flex:1;height:34px;background:#EEF1F4}.bar .t u{display:block;height:100%;background:#B9C4CF}
.bar.f .t u{background:#2B2D31}.bar.f .n{font-weight:700}
.bar .p{width:200px;flex-shrink:0;white-space:nowrap;text-align:right;padding-right:6px;box-sizing:border-box;font-size:40px;font-weight:900;color:#B9C4CF}.bar.f .p{color:#2B2D31}
"""
def metric(b):
    if b.get('bars'):
        bars=''.join(f'<div class="bar{" f" if f else ""}"><span class="n">{n}</span><span class="t"><u style="width:{p}%"></u></span><span class="p">{p}%</span></div>' for n,p,f in b['bars'])
        return f'<div class="m"><div class="lab">{b["label"]}</div><div class="bars">{bars}</div></div>'
    if 'after' in b:
        v=f'<div class="val" style="font-size:84px"><span class="b">{b["before"]}</span><span class="arrow">→</span><span>{b["after"]}</span></div>'
    else:
        v=f'<div class="val" style="font-size:96px"><span>{b["v"]}</span></div>'
    return f'<div class="m"><div class="lab">{b["label"]}</div>{v}<div class="cap">{b["cap"]}</div></div>'
for k,blocks in CARDS.items():
    if k=='t7': continue
    open(f'card-{k}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{CCSS}</style><div class="wrap"><div class="top"><i></i><b>RESULT</b></div>{"".join(metric(b) for b in blocks)}</div>')
# ---------- 페이지 제목 이미지 ----------
PCSS=BASE+""".band{background:#2B2D31;color:#fff;padding:46px 56px 52px}
.eb{display:flex;align-items:center;gap:18px;font-size:22px;letter-spacing:.24em;color:rgba(255,255,255,.66);font-weight:500}
.eb i{width:44px;height:5px;background:#5F7388}
.tt{margin-top:22px;font-size:62px;line-height:1.25;font-weight:900;letter-spacing:-.02em;word-break:keep-all}
.grid{display:grid;grid-template-columns:1fr 1fr;column-gap:56px;margin-top:30px}
.cell{border-top:1px solid #DDE4EB;padding:20px 0 24px}.cell.w{grid-column:1 / span 2}
.cell .l{font-size:20px;letter-spacing:.22em;color:#5F7388;font-weight:700}
.cell .v{margin-top:10px;font-size:31px;font-weight:700;line-height:1.45;word-break:keep-all}
"""
def banner(name, eb, title, cells):
    cs=''.join(f'<div class="cell{" w" if w else ""}"><div class="l">{l}</div><div class="v">{H.escape(v).replace(chr(10),'<br>')}</div></div>' for l,v,w in cells)
    open(f'{name}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{PCSS}</style><div class="wrap" style="padding-top:0"><div class="band"><div class="eb"><i></i>{eb}</div><div class="tt">{H.escape(title)}</div></div><div class="grid">{cs}</div></div>')
for i,(k,t,per,role,res,stack) in enumerate(projects,1):
    banner(f'page-{k}', f'PROJECT &nbsp;{i:02d} / 03', t, [('PERIOD',per,False),('ROLE',role,False),('KEY RESULT',res,True),('STACK',stack,True)])
KEY={1:'t1',2:'t2',3:'t3',4:'t4',5:'t5',6:'t6',8:'t8',9:'t9'}
for n,proj,t,cat,stack,res in ts:
    key=KEY[n]; m=n if n<7 else n-1
    cells=[('CATEGORY',cat,False)]+([('STACK',stack,False)] if stack!='—' else [])+[('RESULT',res,True)]
    banner(f'page-{key}', f'TROUBLESHOOTING &nbsp;{m:02d} / 08 &nbsp;·&nbsp; {proj}', t, cells)
print('cards', [k for k in CARDS if k!='t7'], 'banners', len(projects)+len(ts))
