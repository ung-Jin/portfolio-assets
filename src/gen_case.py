# 프로젝트 페이지용: 사례 머리 이미지 + GitHub/작업일지 링크 타일 (본문 폭 약 708px, 2배 크기로 설계)
B="*{margin:0;padding:0;box-sizing:border-box}body{background:#fff;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden}"
T=[('01','로그인 검사를 인터셉터 한 곳으로 모았습니다'),('02','흩어진 SQL을 정본 하나로 합쳤습니다'),('03','좋은 점수의 원인은 데이터 누수였습니다'),('04','강원도 오차 24.4%를 추적했습니다'),('05','히트맵을 세 번 바꿔 만들었습니다'),('06','위험 가중치를 채점해서 정했습니다'),('07','경로의 육지 통과를 0.136%로 줄였습니다'),('08','날씨 모델을 검증하고 설계를 바꿨습니다'),('09','영상 주소를 Git 이력에서 지웠습니다')]
for n,t in T:
    open(f'case-{n}.html','w',encoding='utf-8').write(f'''<!doctype html><meta charset=utf-8><style>{B}
body{{width:1416px;height:170px}}.r{{position:absolute;left:0;right:0;bottom:0;height:140px;border-bottom:4px solid #2B2D31;display:flex;align-items:baseline;gap:28px;padding-bottom:26px}}
.n{{font-family:'Noto Serif CJK KR',serif;font-size:84px;font-weight:300;color:#5F7388;line-height:1}}
.t{{font-size:54px;font-weight:900;letter-spacing:-.015em;white-space:nowrap}}</style>
<div class="r"><span class="n">{n}</span><span class="t">{t}</span></div>''')
TC=B+"""body{width:680px;height:120px}
.t{position:absolute;left:0;right:0;top:4px;bottom:4px;border-top:1px solid #2B2D31;border-bottom:1px solid #2B2D31;display:flex;align-items:center}
.i{flex:1}.l{font-size:20px;letter-spacing:.22em;font-weight:700;color:#5F7388}
.v{margin-top:6px;font-size:31px;font-weight:700;white-space:nowrap}
.b{width:60px;height:60px;border-radius:50%;background:#2B2D31;color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px}"""
for p,repo,nth in [('p1','Schedule','1차'),('p2','Predict','2차'),('p3','Navigate','3차')]:
    for k,l,v,a in [('gh','GITHUB',f'ung-Jin/{repo}','↗'),('log','WORK LOG',f'{nth} 프로젝트 작업일지','→')]:
        open(f'{k}-{p}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{TC}</style><div class="t"><div class="i"><div class="l">{l}</div><div class="v">{v}</div></div><div class="b">{a}</div></div>')
