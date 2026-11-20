import subprocess
CSS='''*{margin:0;padding:0;box-sizing:border-box}body{width:1600px;height:H;background:#fff;font-family:'Noto Sans CJK KR';color:#2B2D31;overflow:hidden;padding:44px 56px}
h1{font-size:34px;font-weight:700;margin-bottom:6px}.sub{font-size:20px;color:#5F7388;margin-bottom:34px}
.row{display:flex;align-items:stretch;gap:0;justify-content:space-between}
.col{display:flex;flex-direction:column;gap:14px}
.lab{font-size:15px;letter-spacing:2px;color:#5F7388;margin-bottom:2px;font-weight:700}
.box{border-radius:12px;padding:16px 20px;font-size:21px;font-weight:700;line-height:1.35}
.dark{background:#2B2D31;color:#fff}.mid{background:#5F7388;color:#fff}.lt{background:#DDE4EB;color:#2B2D31}
.box small{display:block;font-size:16px;font-weight:400;opacity:.85;margin-top:4px}
.arr{width:70px;display:flex;align-items:center;justify-content:center;font-size:34px;color:#5F7388}
.grp{border:2px dashed #b9c5d1;border-radius:16px;padding:16px 18px}
.note{margin-top:30px;font-size:18px;color:#5F7388}
'''
def page(name,H,body):
    open(name+'.html','w').write(f'<!doctype html><meta charset=utf-8><style>{CSS.replace("height:H",f"height:{H}px")}</style>{body}')
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2',f'--window-size=1600,{H}',f'--screenshot=../../v37/{name}.png',f'{name}.html'],capture_output=True)



page('arch-p2',740,'''<h1>2차 시스템 구조</h1><div class=sub>모델은 미리 돌려 결과를 DB에 저장하고, 화면은 조회만 하는 구조</div>
<div class=row>
<div class=col><div class=lab>DATA</div><div class="box lt">전력사용량<small>17개 시도 · 월별 55개월</small></div><div class="box lt">기상 자료<small>시도 + 연도 + 월 기준으로 통일</small></div></div>
<div class=arr>→</div>
<div class=grp><div class=lab>PYTHON · 미리 실행</div><div class=col><div class="box mid">데이터 정리<small>pandas</small></div><div class="box mid">모델 학습 · 비교<small>시간순 분리<br>Random Forest(최종)<br>XGBoost · LightGBM 비교</small></div></div></div>
<div class=arr>→</div>
<div class=grp><div class=lab>MARIADB · MYBATIS</div><div class=col><div class="box dark">저장된 예측<small>forecast (앞으로 3개월)<br>backtest (검증 결과)</small></div><div class="box dark">실측 · 기준표<small>monthly_data (935행)<br>region (17개 시도)</small></div></div></div>
<div class=arr>→</div>
<div class=grp><div class=lab>SPRING BOOT · THYMELEAF</div><div class=col style="gap:10px">
<div class="box lt" style="padding:12px 18px">지도<small>시도별 증감률 · 클릭으로 지역 선택 (amCharts)</small></div>
<div class="box lt" style="padding:12px 18px">요약 카드 4개 · 앞으로 3개월 예측<small>최근 실적 · 예측 · 전년 대비 · 검증 오차</small></div>
<div class="box lt" style="padding:12px 18px">월별 추이 · 지역 특성 레이더<small>예측 구간은 점선 (Chart.js)</small></div>
<div class="box lt" style="padding:12px 18px">순위 표 · 상세 페이지<small>막대 · 계절 패턴 · 히트맵 · CSV</small></div>
</div></div>
</div><div class=note>※ 예시 초안입니다. 지역을 고르면 지도·순위·차트가 함께 바뀝니다(sessionStorage + 이벤트). 발표 자료(2차 PPT) 기준입니다.</div>''')

page('arch-p3',900,'''<h1>3차 시스템 구조</h1><div class=sub>머신러닝은 시험해 봤지만 쓰지 않고, API로 받은 예보에 위험점수를 매겨 A*로 길을 찾는 구조</div>
<div class=row>
<div class=col><div class=lab>EXTERNAL API</div><div class="box lt">MTIS<small>실시간 선박 · 사고위험 예보<br>10분 · 30분 주기로 수집</small></div><div class="box lt">Open-Meteo<small>항구 날씨 · 파고 · 풍속 예보</small></div></div>
<div class=arr>→</div>
<div class=grp><div class=lab>SPRING BOOT (JAVA)</div><div class=col><div class="box dark">위험도 조립<small>교통 0.5 · 사고예보 0.3 · 날씨 0.2<br>MTIS 칸 단위로 합쳐 0~1 점수</small></div><div class="box dark">A* 탐색 두 번<small>최소경로 · 안전경로 함께 반환<br>비용 = 거리 × (1 + α × 위험)</small></div><div class="box dark">항구 DB (MariaDB)<small>무역항 31곳 이름 · 좌표</small></div></div></div>
<div class=arr>→</div>
<div class=grp><div class=lab>BROWSER · THYMELEAF · LEAFLET</div><div class=col style="gap:10px">
<div class="box lt" style="padding:12px 18px">경로 탐색<small>출발 · 도착 항구 선택(자동완성)<br>최소경로와 안전경로를 한 지도에</small></div>
<div class="box lt" style="padding:12px 18px">교통현황<small>실시간 선박 수 · 밀집도<br>사고위험 칸 · 사고·좌초 지점 표시</small></div>
<div class="box lt" style="padding:12px 18px">안전진단<small>파고 · 풍속 72시간 그래프<br>출발지(실선)와 도착지(점선) 비교</small></div>
<div class="box lt" style="padding:12px 18px">출항 시각 선택 · 항만 CCTV<small>화면 전체가 같은 시각을 기준으로 표시</small></div>
</div></div>
</div>
<div class=grp style="margin-top:22px;display:flex;gap:28px;align-items:center"><div class=lab style="margin:0;white-space:nowrap">PYTHON · 미리 생성</div><div style="font-size:19px;line-height:1.5"><b>바다 격자 500m</b>　해안선을 500m 칸으로 나눠 칸마다 바다 비율을 저장 (numpy, 2.2MB) → 서버가 불러와 육지를 피하는 데 사용</div></div>
<div class=grp style="margin-top:14px;display:flex;gap:28px;align-items:center"><div class=lab style="margin:0;white-space:nowrap">ML 시험 · 미사용</div><div style="font-size:19px;line-height:1.5">날씨로 사고를 구분할 수 있는지 로지스틱 회귀 등으로 돌려 봤지만 AUC 0.549라 <b>서비스에는 쓰지 않았습니다</b><br>대신 날씨는 운항 한계 판정(파고 4m · 풍속 20m/s)에만 사용하고, 가중치 11조합은 MTIS 사고다발 26칸으로 채점해 골랐습니다</div></div>
<div class=note>※ 예시 초안입니다. 발표 자료(3차 PPT) 기준입니다.</div>''')
