# 트러블슈팅 갤러리용 표지 카드 (960x560)
D=[
('1','1차 · AS 스케줄 관리','로그인 검사를<br>인터셉터 한 곳으로 모았습니다','보안·권한','검사 위치','인터셉터 1곳'),
('2','1차 · AS 스케줄 관리','흩어진 SQL을<br>정본 하나로 합쳤습니다','협업·구조','SQL 파일','정본 1개'),
('3','2차 · 전력사용량 예측','좋은 점수의 원인은<br>데이터 누수였습니다','데이터·ML','정답이 학습 데이터에 있던 비율','64%'),
('4','2차 · 전력사용량 예측','강원도 오차 24.4%를<br>추적했습니다','데이터·ML','강원도 오차','24.4% → 7.05%'),
('5','2차 · 전력사용량 예측','히트맵을<br>세 번 바꿔 만들었습니다','프론트엔드','히트맵 구현 방식','3번 교체'),
('6','3차 · 해상교통 안전경로','위험 가중치를<br>채점해서 정했습니다','데이터·ML','사고다발 칸 구분 확률','85.6%'),
('7','3차 · 해상교통 안전경로','경로의 육지 통과를<br>0.136%로 줄였습니다','디버깅','육지를 지나는 경로 비율','0.136%'),
('8','3차 · 해상교통 안전경로','날씨 모델을 검증하고<br>설계를 바꿨습니다','데이터·ML','날씨 모델 AUC','0.549'),
('9','3차 · 해상교통 안전경로','영상 주소를<br>Git 이력에서 지웠습니다','보안·권한','새 저장소 검색 결과','0건'),
]
CSS="""*{margin:0;padding:0;box-sizing:border-box}
body{width:960px;height:560px;font-family:'Noto Sans CJK KR',sans-serif;background:#fff;color:#2B2D31;overflow:hidden}
.top{height:330px;background:#2B2D31;padding:40px 48px;color:#fff;position:relative}
.eb{display:flex;align-items:center;gap:14px;font-size:15px;letter-spacing:.28em;color:#DDE4EB;font-weight:500}
.eb i{display:block;width:34px;height:3px;background:#5F7388}
.t{margin-top:30px;font-size:42px;line-height:1.28;font-weight:900;word-break:keep-all}
.n{position:absolute;right:44px;bottom:18px;font-family:'Noto Serif CJK KR',serif;font-size:110px;font-weight:300;color:#5F7388;line-height:1}
.bot{padding:30px 48px}
.l{font-size:15px;letter-spacing:.18em;font-weight:700;color:#5F7388}
.v{margin-top:12px;font-size:60px;font-weight:900;line-height:1.1;white-space:nowrap}
.c{position:absolute;left:48px;bottom:30px;font-size:17px;color:#5F7388;font-weight:500}
"""
for n,p,t,c,l,v in D:
    open(f'cover-{n}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{CSS}</style><div class="top"><div class="eb"><i></i>{p}</div><div class="t">{t}</div><div class="n">0{n}</div></div><div class="bot"><div class="l">{l}</div><div class="v">{v}</div></div><div class="c">{c}</div>')
