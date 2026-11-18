# 트러블슈팅 섹션: 프로젝트 구분 이미지 + 흰색 카드 표지
CSS="*{margin:0;padding:0;box-sizing:border-box}body{background:#fff;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden}"
PH=[('01','1차 · 냉·난방 AS기사 스케줄 관리','2026.09.07 ~ 09.15'),('02','2차 · 시도별 전력사용량 예측 대시보드','2026.09.18 ~ 10.16'),('03','3차 · 해상교통 안전경로 예측 시스템','2026.10.17 ~ 11.12')]
for n,t,p in PH:
    open(f'ph-{n}.html','w',encoding='utf-8').write(f'''<!doctype html><meta charset=utf-8><style>{CSS}
body{{width:1920px;height:130px}}.r{{position:absolute;left:120px;right:120px;bottom:0;height:104px;border-bottom:3px solid #2B2D31;display:flex;align-items:baseline;gap:30px;padding-bottom:20px}}
.n{{font-family:'Noto Serif CJK KR',serif;font-size:64px;font-weight:300;color:#5F7388;line-height:1}}
.t{{font-size:38px;font-weight:900}}.p{{margin-left:auto;font-size:20px;letter-spacing:.16em;font-weight:700;color:#5F7388}}</style>
<div class="r"><span class="n">{n}</span><span class="t">{t}</span><span class="p">{p}</span></div>''')
D=[('01','검사 위치','인터셉터 1곳'),('02','SQL 파일','정본 1개'),('03','정답이 학습 데이터에 있던 비율','64%'),('04','강원도 오차','24.4% → 7.05%'),('05','히트맵 구현 방식','3번 교체'),('06','사고다발 칸 구분 확률','85.6%'),('07','육지를 지나는 경로 비율','0.136%'),('08','날씨 모델 AUC','0.549'),('09','새 저장소 검색 결과','0건')]
for n,l,v in D:
    open(f'wc-{n}.html','w',encoding='utf-8').write(f'''<!doctype html><meta charset=utf-8><style>{CSS}
body{{width:1000px;height:483px;padding:56px 60px}}
.no{{font-family:'Noto Serif CJK KR',serif;font-size:46px;font-weight:300;color:#5F7388;line-height:1}}
.l{{margin-top:62px;font-size:19px;letter-spacing:.16em;font-weight:700;color:#5F7388}}
.v{{margin-top:14px;font-size:84px;font-weight:900;line-height:1.05;white-space:nowrap}}</style>
<div class="no">{n}</div><div class="l">{l}</div><div class="v">{v}</div>''')
