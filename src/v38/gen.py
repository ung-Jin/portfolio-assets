import subprocess
CSS='''*{margin:0;padding:0;box-sizing:border-box}
body{width:1920px;height:HHpx;background:#fff;font-family:'Noto Sans CJK KR';color:#2B2D31;overflow:hidden}
.top{height:6px;background:#2B2D31}
.head{display:flex;align-items:flex-end;padding:34px 72px 30px;gap:30px}
.n{font-family:'Noto Serif CJK KR';font-size:92px;font-weight:400;line-height:1;color:#5F7388}
.t{flex:1;padding-bottom:6px}.t h1{font-size:44px;font-weight:700;line-height:1.1}.t p{font-size:22px;color:#5F7388;margin-top:10px;font-weight:500}
.tag{border:3px solid #2B2D31;padding:10px 20px;font-size:20px;font-weight:700;letter-spacing:3px;margin-bottom:10px}
.line{height:2px;background:#2B2D31;margin:0 72px}
.flow{display:flex;padding:40px 72px 0;align-items:stretch;gap:44px}
.col:not(:last-child) .ch{clip-path:polygon(0 0,calc(100% - 34px) 0,100% 50%,calc(100% - 34px) 100%,0 100%)}
.col{flex:1;min-width:0;display:flex;flex-direction:column;border-bottom:2px solid #2B2D31}
.ch{height:95px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #2B2D31}
.ch .num{font-family:'Noto Serif CJK KR';font-size:46px;color:#5F7388;line-height:1;width:58px}
.ch .k{font-size:14px;letter-spacing:3px;color:#5F7388;font-weight:700}
.ch .h{font-size:28px;font-weight:700;margin-top:2px;line-height:1.2}
.it{padding:16px 0 15px}
.it+.it{border-top:1px solid #d3dae1}
.it b{display:block;font-size:23px;font-weight:700;line-height:1.35}
.it span{display:block;font-size:18px;color:#5F7388;margin-top:3px;line-height:1.5}
.ar{width:70px;height:95px;margin-top:3px;display:flex;align-items:center;justify-content:center;flex:none}
.ar svg{width:34px;height:18px}
.ch{background:#2B2D31;border-bottom-color:#2B2D31;padding:0 18px}
.ch .num{color:#9fb0c1}.ch .k{color:#9fb0c1}.ch .h{color:#fff}
.it{padding-left:18px;padding-right:14px}
.strip{display:flex;margin:0 72px;border-top:1px solid #2B2D31;padding:18px 0;gap:30px;align-items:baseline}
.strip .k{width:210px;font-size:18px;letter-spacing:1px;color:#5F7388;font-weight:700;flex:none}
.strip .v{font-size:21px;line-height:1.6}.strip .v b{font-weight:700}
.end{margin-top:26px;border-top:6px solid #2B2D31}
'''
AR=''
def page(name,H,body):
    open(name+'.html','w').write(f'<!doctype html><meta charset=utf-8><style>{CSS.replace("HH",str(H))}</style>{body}')
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2',f'--window-size=1920,{H}',f'--screenshot=../../v38/{name}.png',f'{name}.html'],capture_output=True)
def it(b,s=''): return f'<div class=it><b>{b}</b>'+(f'<span>{s}</span>' if s else '')+'</div>'
def col(n,k,h,items,cls=''): return f'<div class="col {cls}"><div class=ch><div class=num>{n}</div><div><div class=k>{k}</div><div class=h>{h}</div></div></div>{"".join(items)}</div>'

page('arch-p2',900,f'''<div class=top></div>
<div class=head><div class=n>2차</div><div class=t><h1>시스템 구조</h1><p>모델은 미리 돌려 결과를 DB에 저장하고, 화면은 조회만 합니다</p></div><div class=tag>PRE-COMPUTED</div></div><div class=line></div>
<div class=flow>
{col('01','DATA','자료',[it('전력사용량','17개 시도 · 월별 55개월'),it('기상 자료','시도 + 연도 + 월 기준으로 통일')])}{AR}
{col('02','PYTHON','학습 · 비교',[it('데이터 정리','pandas'),it('모델 학습 · 비교','시간순 분리<br>Random Forest(최종)<br>XGBoost · LightGBM')])}{AR}
{col('03','MARIADB','저장',[it('forecast','앞으로 3개월 예측'),it('backtest','모델 검증 결과'),it('monthly_data · region','과거 실측 935행<br>17개 시도 기준표')],'key')}{AR}
{col('04','SPRING BOOT','화면 조회',[it('지도','시도별 증감률 · 클릭으로 지역 선택'),it('요약 카드 · 3개월 예측','최근 실적 · 예측 · 전년 대비 · 검증 오차'),it('월별 추이 · 지역 특성 레이더','예측 구간은 점선'),it('순위 표 · 상세 페이지','막대 · 계절 패턴 · 히트맵 · CSV')])}
</div>
<div style="height:34px"></div>
<div class=strip><div class=k>한 번 클릭하면</div><div class=v>지역을 고르면 <b>지도 · 순위 · 도넛 · 레이더</b>가 함께 바뀝니다. 선택은 sessionStorage에 두고, 바뀌었다는 알림을 이벤트로 전파합니다.</div></div>
<div class=strip><div class=k>화면 기술</div><div class=v>Thymeleaf · Chart.js(차트) · amCharts(지도) · axios</div></div>
<div class=end></div>''')

page('arch-p3',895,f'''<div class=top></div>
<div class=head><div class=n>3차</div><div class=t><h1>시스템 구조</h1><p>예보에 위험점수를 매기고 A*로 길을 찾습니다. 머신러닝은 시험만 하고 쓰지 않았습니다</p></div><div class=tag>NO ML IN SERVICE</div></div><div class=line></div>
<div class=flow>
{col('01','EXTERNAL API','수집',[it('MTIS','실시간 선박 · 사고위험 예보<br>10분 · 30분 주기'),it('Open-Meteo','항구 날씨 · 파고 · 풍속 예보')])}{AR}
{col('02','SPRING BOOT','계산',[it('위험도 조립','교통 0.5 · 사고예보 0.3 · 날씨 0.2<br>MTIS 칸 단위로 합쳐 0~1 점수'),it('A* 탐색 두 번','최소경로 · 안전경로 함께 반환<br>비용 = 거리 × (1 + α × 위험)'),it('항구 DB (MariaDB)','무역항 31곳 이름 · 좌표')],'key')}{AR}
{col('03','BROWSER','화면',[it('경로 탐색','출발 · 도착 항구 선택 · 두 경로를 한 지도에'),it('교통현황','선박 수 · 밀집도 · 사고위험 칸 · 사고 · 좌초 지점'),it('안전진단','파고 · 풍속 72시간 그래프<br>출발지(실선)와 도착지(점선) 비교'),it('출항 시각 · 항만 CCTV','화면 전체가 같은 시각을 기준으로 표시')])}
</div>
<div style="height:34px"></div>
<div class=strip><div class=k>시험 후 미사용</div><div class=v><b>날씨로 사고 구분</b>　로지스틱 회귀 등으로 돌려 봤지만 AUC 0.549라 서비스에는 쓰지 않았습니다. 날씨는 운항 한계 판정(파고 4m · 풍속 20m/s)에만 쓰고, 가중치 11조합은 MTIS 사고다발 26칸으로 채점해 골랐습니다.</div></div>
<div class=end></div>''')
