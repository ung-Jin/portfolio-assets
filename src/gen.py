# -*- coding: utf-8 -*-
CSS = """
@page { size: __W__px __H__px; margin: 0 }
:root { --ink:#2B2D31; --blue:#5F7388; --blue-l:#DDE4EB; --paper:#FFFFFF; }
* { box-sizing:border-box; margin:0; padding:0 }
html,body { width:__W__px; height:__H__px; background:var(--paper) }
body { font-family:'Noto Sans CJK KR','Noto Sans KR',sans-serif; color:var(--ink); position:relative; overflow:hidden }
.serif { font-family:'Noto Serif CJK KR','Noto Serif KR',serif }
.band { position:absolute; left:0; top:0; width:1920px; height:200px; background:var(--ink); color:#fff }
.band .tag { position:absolute; left:72px; top:46px; width:56px; height:6px; background:var(--blue) }
.band .t { position:absolute; left:64px; top:62px; font-size:104px; line-height:1; font-weight:900; letter-spacing:-.01em }
.band .idx { position:absolute; right:72px; top:44px; text-align:right }
.band .idx .n { font-size:72px; line-height:1; font-weight:300 }
.band .idx .n small { font-size:28px; color:rgba(255,255,255,.5); margin-left:6px }
.band .idx .s { margin-top:10px; font-size:19px; letter-spacing:.34em; color:rgba(255,255,255,.62); font-weight:500 }
.cols { position:absolute; left:72px; width:1776px; display:flex; align-items:stretch }
.col { width:456px; padding-right:48px; position:relative }
.col:last-child { padding-right:0 }
.col:first-child { width:408px }
.col + .col { padding-left:48px; border-left:1px solid rgba(43,45,49,.22) }
.num { font-size:76px; line-height:1; color:var(--blue); font-weight:300 }
.h { margin-top:20px; font-size:29px; letter-spacing:.2em; font-weight:700 }
.hr { margin-top:18px; height:3px; background:var(--ink) }
.item { padding:22px 0 22px; border-bottom:1px solid rgba(43,45,49,.18) }
.item .d { font-size:23px; letter-spacing:.06em; color:var(--blue); font-weight:700; font-variant-numeric:tabular-nums }
.item .n { margin-top:8px; font-size:35px; font-weight:700; line-height:1.3; letter-spacing:-.01em }
.item .o { margin-top:4px; font-size:25px; color:rgba(43,45,49,.68) }
.tech { padding:21px 0; border-bottom:1px solid rgba(43,45,49,.18); font-size:37px; font-weight:700; letter-spacing:-.005em }
.note { margin-top:24px; font-size:19px; line-height:1.7; color:rgba(43,45,49,.78) }
.foot { position:absolute; left:72px; right:0; bottom:0; height:76px }
.foot .line { position:absolute; left:0; width:1776px; top:0; height:1px; background:rgba(43,45,49,.28) }
.foot .tab { position:absolute; left:0; top:-1px; height:44px; width:170px; background:var(--ink); color:#fff; font-size:20px; letter-spacing:.14em; font-weight:500; display:flex; align-items:center; justify-content:center }
.foot .c { position:absolute; left:200px; top:8px; width:1576px; font-size:23px; letter-spacing:.02em; text-align:right; white-space:nowrap }
.foot .c i { font-style:normal; color:var(--blue); margin-right:10px; letter-spacing:.12em; font-size:18px; font-weight:700 }
.big { font-size:48px; font-weight:800; line-height:1.35; letter-spacing:-.02em; margin-top:26px }
.body { margin-top:22px; font-size:30px; line-height:1.75; color:rgba(43,45,49,.82) }
"""
def band(title, n, total, sub):
    return f'''<div class="band"><div class="tag"></div><div class="t">{title}</div>
    <div class="idx"><div class="n serif">{n}<small>/ {total}</small></div><div class="s">{sub}</div></div></div>'''
def page(name, W, H, body):
    css = CSS.replace('__W__', str(W)).replace('__H__', str(H))
    open(f'/home/claude/design/{name}.html','w',encoding='utf-8').write(
        f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>')

TOTAL = 5
foot = '''<div class="foot"><div class="line"></div><div class="tab">Portfolio</div></div>'''

# 01 PROFILE
def items(rows):
    return ''.join(f'<div class="item"><div class="d">{d}</div><div class="n">{n}</div><div class="o">{o}</div></div>' for d,n,o in rows)
def col(num, head, inner):
    return f'<div class="col"><div class="num serif">{num}</div><div class="h">{head}</div><div class="hr"></div>{inner}</div>'
cv = '<div class="cols" style="top:272px">' + \
  col('01','CERTIFICATE', items([('2026.09','정보처리기사','한국산업인력공단'),('2026.06','네트워크관리사 2급','정보통신자격협회'),('2026.11','ADsP','한국데이터산업진흥원'),('2026.12','SQLD','한국데이터산업진흥원')])) + \
  col('02','EDUCATION', items([('2026.06 – 2026.11','그린AI캠퍼스','풀스택 양성과정'),('2011.03 – 2016.07','동아대학교','컴퓨터공학과'),('2008.03 – 2011.02','한국게임과학고','프로그래밍과')])) + \
  col('03','EXPERIENCE', items([('2023.10 – 2025.07','현대자동차','의장-차체 생산직 / 제조'),('2020.11 – 2021.11','grit365','스마트스토어 운영'),('2017 – 2018.08','프로게이머','배틀그라운드')])) + \
  col('04','AWARDS', items([('2009','청소년 게임공모전 은상','전주정보영상진흥원'),('2008','청소년 게임대회 우승','전북디지털산업진흥위원회')]) ) + '</div>'
page('cv', 1920, 1260, band('PROFILE',1,TOTAL,'CERTIFICATE / EDUCATION / EXPERIENCE / AWARDS') + cv + foot)

# 02 SKILLS
def techs(l): return ''.join(f'<div class="tech">{t}</div>' for t in l)
sk = '<div class="cols" style="top:272px">' + \
  col('01','BACKEND', techs(['Java','Spring Boot','MyBatis','FastAPI'])) + \
  col('02','FRONTEND', techs(['Thymeleaf','JavaScript','Chart.js','Leaflet','React'])) + \
  col('03','DATA · AI', techs(['Python','pandas','scikit-learn','XGBoost','LightGBM'])) + \
  col('04','DB · TOOLS', techs(['MariaDB','ERDCloud','Git','GitHub','Notion'])) + '</div>'
page('skills', 1920, 1010, band('SKILLS',2,TOTAL,'BACKEND / FRONTEND / DATA · AI / DB · TOOLS') + sk)

# 03 / 04 banners
page('banner-projects', 1920, 200, band('PROJECTS',3,TOTAL,'3 TEAM PROJECTS · TEAM LEADER'))
page('banner-troubleshooting', 1920, 200, band('TROUBLESHOOTING',4,TOTAL,'8 CASES · SITUATION / CAUSE / FIX / RESULT'))

# 05 RETROSPECTIVE
def r(n, big, body):
    w = 544 if n=='01' else 616
    return f'<div class="col" style="width:{w}px"><div class="num serif">{n}</div><div class="hr" style="margin-top:22px"></div><div class="big">{big}</div><div class="body">{body}</div></div>'
retro = '<div class="cols" style="top:280px">' + \
  r('01','검증 조건을<br>먼저 의심합니다','좋은 점수가 누수일 수 있습니다.') + \
  r('02','기준선을<br>먼저 계산합니다','단순한 방법이 더 정확할 수 있습니다.') + \
  r('03','다른 기준으로<br>다시 잽니다','내 기준으로만 검증하면 항상 통과합니다.') + '</div>'
page('retro', 1920, 700, band('RETROSPECTIVE',5,TOTAL,'WHAT I LEARNED') + retro)
print('ok')
