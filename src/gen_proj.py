# 프로젝트 섹션: 대표 프로젝트 3개 패널 (1920x640)
P=[
('01','4인 · 팀장','2026.09.07 – 09.15','냉·난방 AS기사 스케줄 관리','고객이 A/S를 신청하면 관리자가 기사를 배정하고, 기사가 방문 결과를 보고하는 흐름을 하나로 묶은 웹 시스템입니다.','로그인 검사가 빠진 곳','5곳 → 1곳','Spring Boot · MyBatis · MariaDB · Thymeleaf','shot-1.png'),
('02','4인 · 팀장','2026.09.18 – 10.16','시도별 전력사용량 예측 대시보드','17개 시도의 월별 전력사용량과 날씨로 향후 3개월을 예측하고, 지도와 차트로 보여주는 대시보드입니다.','강원도 예측 오차','24.4% → 7.05%','Python · scikit-learn · FastAPI · Spring Boot · Chart.js','shot-2.png'),
('03','4인 · 팀장','2026.10.17 – 11.12','해상교통 안전경로 예측 시스템','교통·사고위험·날씨를 반영한 안전경로를 거리만 보는 최소경로와 함께 보여주는 출항 전 항해 계획 도구입니다.','최소경로 대비 평균 위험점수','−22.6%','Spring Boot · Python · Leaflet','shot-3.png')]
CSS="""*{margin:0;padding:0;box-sizing:border-box}body{width:1920px;height:640px;background:#fff;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden;position:relative}
.rule{position:absolute;left:0;right:0;top:40px;border-top:3px solid #2B2D31}
.l{position:absolute;left:0;top:76px;width:700px}
.n{font-family:'Noto Serif CJK KR',serif;font-size:72px;font-weight:300;color:#5F7388;line-height:1}
.meta{margin-top:26px;font-size:17px;letter-spacing:.14em;font-weight:700;color:#5F7388}
.t{margin-top:14px;font-size:46px;font-weight:900;line-height:1.2;word-break:keep-all}
.d{margin-top:20px;font-size:21px;line-height:1.6;color:#4A5159;word-break:keep-all}
.k{position:absolute;left:0;top:440px;width:700px;border-top:1px solid #DDE4EB;padding-top:22px}
.kl{font-size:15px;letter-spacing:.2em;font-weight:700;color:#5F7388}
.kv{margin-top:8px;font-size:62px;font-weight:900;line-height:1.05;white-space:nowrap}
.s{position:absolute;left:0;top:590px;font-size:17px;color:#5F7388;font-weight:500}
.img{position:absolute;left:860px;top:76px;width:1060px;height:500px;border:1px solid #DDE4EB;border-radius:6px;overflow:hidden;background:#EEF1F4}
.img img{width:100%;height:100%;object-fit:cover;object-position:top left;display:block}
"""
for n,role,per,t,d,kl,kv,st,img in P:
    open(f'proj-{n}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{CSS}</style><div class="rule"></div><div class="l"><div class="n">{n}</div><div class="meta">{role}　·　{per}</div><div class="t">{t}</div><div class="d">{d}</div></div><div class="k"><div class="kl">KEY RESULT · {kl}</div><div class="kv">{kv}</div></div><div class="s">{st}</div><div class="img"><img src="{img}"></div>')
