# -*- coding: utf-8 -*-
import html
exec(open('/home/claude/design/gen.py',encoding='utf-8').read().split("TOTAL = 5")[0])  # reuse CSS, page()
EXTRA = """
.band2 { position:absolute; left:0; top:0; width:1920px; height:230px; background:var(--ink); color:#fff }
.band2 .tag { position:absolute; left:120px; top:52px; width:56px; height:6px; background:var(--blue) }
.band2 .eb { position:absolute; left:196px; top:40px; font-size:19px; letter-spacing:.3em; color:rgba(255,255,255,.66); font-weight:500; white-space:nowrap }
.band2 .tt { position:absolute; left:116px; top:92px; width:1700px; font-size:__FS__px; line-height:1.2; font-weight:900; letter-spacing:-.02em; white-space:nowrap }
.info { position:absolute; left:120px; top:282px; width:1680px; display:flex }
.cell { padding-right:44px }
.cell + .cell { padding-left:44px; border-left:1px solid rgba(43,45,49,.22) }
.cell .l { font-size:16px; letter-spacing:.28em; color:var(--blue); font-weight:700 }
.cell .v { word-break:keep-all; margin-top:12px; font-size:27px; font-weight:700; line-height:1.45; letter-spacing:-.01em }
.cell .v.r { font-weight:500; font-size:24px }
"""
def render(name, eb, title, cells, fs=64, H=410):
    cs = ''.join(f'<div class="cell" style="width:{w}px"><div class="l">{l}</div><div class="v{" r" if r else ""}">{html.escape(v)}</div></div>' for l,v,w,r in cells)
    body = f'<div class="band2"><div class="tag"></div><div class="eb">{eb}</div><div class="tt">{html.escape(title)}</div></div><div class="info">{cs}</div>'
    css = (CSS + EXTRA.replace('__FS__', str(fs))).replace('__W__','1920').replace('__H__',str(H))
    open(f'/home/claude/design/{name}.html','w',encoding='utf-8').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>')

projects = [
 ('p1','냉·난방 AS기사 스케줄 관리','2026.09.07 – 09.15','4인 · 팀장','로그인 검사를 인터셉터 한 곳으로 일원화','Spring Boot · MyBatis · MariaDB · Thymeleaf'),
 ('p2','시도별 전력사용량 예측 대시보드','2026.09.18 – 10.16','4인 · 팀장','데이터 누수 발견, 강원도 오차 24.4% → 7.05%','Python · scikit-learn · FastAPI · Spring Boot · Chart.js'),
 ('p3','해상교통 안전경로 예측 시스템','2026.10.17 – 11.12','4인 · 팀장','경로의 육지 통과 3~16% → 0.136%','Spring Boot · Python · Leaflet'),
]
for i,(k,t,per,role,res,stack) in enumerate(projects,1):
    render(f'page-{k}', f'PROJECT &nbsp;{i:02d} / 03', t,
      [('PERIOD',per,340,False),('ROLE',role,260,False),('KEY RESULT',res,620,True),('STACK',stack,460,True)], fs=76)

ts = [
 (1,'1차 · AS 스케줄 관리','로그인 검사를 인터셉터 한 곳으로 모았습니다','보안·권한','Spring Boot','로그인 검사가 빠진 컨트롤러 5곳을 인터셉터 하나로 막았습니다'),
 (2,'1차 · AS 스케줄 관리','흩어진 SQL을 정본 하나로 합쳤습니다','협업·구조','SQL · Git','버전마다 달랐던 테이블 정의를 하나로 맞추고 PR 4건을 하나씩 병합했습니다'),
 (3,'2차 · 전력사용량 예측','좋은 점수의 원인은 데이터 누수였습니다','데이터·ML','Python · scikit-learn','검증 데이터 64%의 정답이 학습 데이터에 있던 것을 찾아 시간순 분리로 통일했습니다'),
 (4,'2차 · 전력사용량 예측','강원도 오차 24.4%를 추적했습니다','데이터·ML · 디버깅','Python · XGBoost','세대수 피처를 빼서 강원도 오차를 24.4%에서 7.05%로 낮췄습니다'),
 (5,'2차 · 전력사용량 예측','히트맵을 세 번 바꿔 만들었습니다','프론트엔드','JavaScript · Chart.js','칸 크기를 폭에 맞출 수 있는 산점도로 히트맵을 만들고, 데이터 가공은 서버로 옮겼습니다'),
 (6,'3차 · 해상교통 안전경로','위험 가중치를 채점해서 정했습니다','데이터·ML','Python','11가지 비중을 채점해 교통 0.5 · 사고예보 0.3 · 날씨 0.2를 골랐습니다'),
 (7,'3차 · 해상교통 안전경로','경로의 육지 통과를 0.136%로 줄였습니다','디버깅','—','격자를 500m로 줄여 경로의 육지 통과 비율을 3~16%에서 0.136%로 낮췄습니다'),
 (8,'3차 · 해상교통 안전경로','날씨 모델을 검증하고 설계를 바꿨습니다','데이터·ML','Python','날씨로는 사고를 구분하지 못한다는 것(AUC 0.549)을 확인하고 날씨의 역할을 바꿨습니다'),
 (9,'3차 · 해상교통 안전경로','영상 주소를 Git 이력에서 지웠습니다','보안·권한','Git','영상 주소와 DB 접속 정보를 .env로 분리하고 이력을 정리한 새 저장소로 옮겼습니다'),
]
for n,proj,t,cat,stack,res in ts:
    cells = [('CATEGORY',cat,300,False)]
    if stack != '—': cells.append(('STACK',stack,370,False))
    cells.append(('RESULT',res,1010 if stack!='—' else 1380,True))
    render(f'page-t{n}', f'TROUBLESHOOTING &nbsp;{n:02d} / 09 &nbsp;·&nbsp; {proj}', t, cells, fs=64)
print('ok')
