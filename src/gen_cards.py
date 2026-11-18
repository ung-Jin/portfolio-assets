# 결과 숫자 카드 생성기 (트러블슈팅 페이지용)
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1920px;background:#fff;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31}
.wrap{padding:56px 120px 60px}
.top{display:flex;align-items:center;gap:20px;margin-bottom:40px}
.top i{display:block;width:56px;height:4px;background:#5F7388}
.top b{font-size:22px;letter-spacing:.34em;color:#5F7388;font-weight:700}
.row{display:flex;align-items:stretch}
.m{padding:0 56px;border-left:2px solid #DDE4EB}
.m:first-child{padding-left:0;border-left:0}
.lab{font-size:20px;letter-spacing:.2em;font-weight:700;color:#5F7388;margin-bottom:22px}
.val{display:flex;align-items:baseline;gap:28px;font-weight:900;line-height:1.05;white-space:nowrap}
.b{color:#B9C4CF}.a{color:#2B2D31}.arrow{color:#5F7388;font-weight:400;font-size:.6em}
.cap{margin-top:20px;font-size:23px;line-height:1.5;color:#2B2D31;word-break:keep-all}
.cap em{font-style:normal;color:#5F7388;font-weight:700}
.bars{display:flex;flex-direction:column;gap:18px;width:1100px}
.bar{display:flex;align-items:center;gap:24px}
.bar .n{width:420px;font-size:23px;word-break:keep-all}
.bar .t{flex:1;height:34px;background:#EEF1F4}
.bar .t u{display:block;height:100%;background:#B9C4CF}
.bar.f .t u{background:#2B2D31}.bar.f .n{font-weight:700}
.bar .p{width:130px;font-size:34px;font-weight:900;color:#B9C4CF}.bar.f .p{color:#2B2D31}
"""
def val(b, size):
    if 'after' in b:
        return f'<div class="val" style="font-size:{size}px"><span class="b">{b["before"]}</span><span class="arrow">→</span><span class="a">{b["after"]}</span></div>'
    return f'<div class="val" style="font-size:{size}px"><span class="a">{b["v"]}</span></div>'
def card(name, blocks, H=380):
    inner=''
    for b in blocks:
        if b.get('bars'):
            bars=''.join(f'<div class="bar{" f" if f else ""}"><span class="n">{n}</span><span class="t"><u style="width:{p}%"></u></span><span class="p">{p}%</span></div>' for n,p,f in b['bars'])
            inner+=f'<div class="m"><div class="lab">{b["label"]}</div><div class="bars">{bars}</div></div>'
        else:
            inner+=f'<div class="m" style="width:{b.get("w","auto")}"><div class="lab">{b["label"]}</div>{val(b,b.get("size",120))}<div class="cap">{b["cap"]}</div></div>'
    html=f'<!doctype html><meta charset=utf-8><style>{CSS}</style><div class="wrap"><div class="top"><i></i><b>RESULT</b></div><div class="row">{inner}</div></div>'
    open(f'card-{name}.html','w',encoding='utf-8').write(html)
    return H
C={}
C['t1']=card('t1',[
 dict(label='검사 위치',before='컨트롤러별',after='인터셉터 1곳',size=72,cap='검사 코드를 <em>한 곳</em>에 모았습니다',w='900px'),
 dict(label='검사가 빠진 곳',before='6곳 중 5곳',after='전 요청 검사',size=72,cap='새 화면은 주소 규칙 <em>한 줄</em>만 추가합니다')],330)
C['t2']=card('t2',[
 dict(label='SQL 파일',v='정본 1개',size=96,cap='버전마다 달랐던 테이블 정의를 하나로 맞췄습니다',w='800px'),
 dict(label='발표 당일 PR',v='4건 순차 병합',size=96,cap='한꺼번에 받지 않고 <em>하나씩</em> 병합하며 매번 화면을 확인했습니다')],330)
C['t3']=card('t3',[
 dict(label='검증 데이터 중 정답이 학습 데이터에 있던 비율',v='64%',size=150,cap='검증 187행 중 <em>119행</em>이 학습 데이터에 답이 들어 있었습니다',w='820px'),
 dict(label='검증 오차 (MAPE)',before='3.52%',after='4.11%',size=110,cap='무작위 분리 → <em>시간순 분리</em> · 검증 행 수가 달라 같은 모델의 악화는 아닙니다')],400)
C['t4']=card('t4',[
 dict(label='강원도 오차',before='24.4%',after='7.05%',size=120,cap='세대수 피처를 빼서 낮췄습니다',w='860px'),
 dict(label='XGBoost 전체 오차',before='10.26%',after='4.66%',size=120,cap='평균에 묻혔던 문제를 <em>지역별</em>로 나눠 찾았습니다')],380)
C['t6']=card('t6',[
 dict(label='사고다발 칸이 다른 칸보다 위험도가 높게 나올 확률',bars=[('교통만 사용',64.9,False),('세 요소 비슷하게 (35 : 35 : 30)',79.8,False),('교통 0.5 · 사고예보 0.3 · 날씨 0.2',85.6,True)])],430)
C['t7']=card('t7',[
 dict(label='육지를 지나는 경로 비율 (110m 해안선 기준)',before='3~16%',after='0.136%',size=120,cap='격자를 2.5km에서 <em>500m</em>로 줄였습니다',w='1000px'),
 dict(label='격자 크기',before='2.5km',after='500m',size=72,cap='바다 비율 80% 이상인 칸만 통과')],380)
C['t8']=card('t8',[
 dict(label='날씨 모델 AUC',v='0.549',size=150,cap='0.5가 무작위입니다. 날씨만으로는 사고를 거의 구분하지 못했습니다',w='900px'),
 dict(label='정확도',v='77.3%',size=96,cap='전부 "무사고"로 찍어도 나오는 값이라 <em>AUC</em>로 판단했습니다')],400)
C['t9']=card('t9',[
 dict(label='새 저장소에서 영상 주소 · 비밀번호 검색',v='0건',size=150,cap='로그인하지 않은 상태로 새 저장소를 받아 확인했습니다',w='1100px'),
 dict(label='분리한 값',v='.env',size=96,cap='영상 주소와 DB 접속 정보를 <em>저장소 밖</em>에 두었습니다')],380)
import json;json.dump(C,open('cards.json','w'))
