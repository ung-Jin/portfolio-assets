# 첫 이미지 배치 시안 3종 (1920x860, 여백 72px 기준)
BASE = """
:root{--ink:#2B2D31;--blue:#5F7388;--blue-l:#DDE4EB}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1920px;height:860px;background:#fff}
body{font-family:'Noto Sans CJK KR',sans-serif;color:var(--ink);position:relative;overflow:hidden}
.serif{font-family:'Noto Serif CJK KR',serif}
.abs{position:absolute}
.ph{background:#EEF1F4;border:1px solid var(--blue-l);overflow:hidden;display:flex;flex-direction:column;align-items:center;justify-content:flex-end}
.ph i{display:block;border-radius:50%;border:2px solid #C3CDD7}
.ph b{display:block;border:2px solid #C3CDD7;border-bottom:none;border-radius:999px 999px 0 0}
.dash{width:44px;height:6px;background:var(--ink)}
.eb{font-size:22px;letter-spacing:.38em;font-weight:700}
.name{line-height:1;font-weight:900;letter-spacing:-.045em}
.role{font-style:italic;color:var(--blue)}
.rule{height:2px;background:var(--ink)}
.head{font-size:34px;line-height:1.4;font-weight:800;letter-spacing:-.02em}
.intro{text-wrap:balance;font-size:24px;line-height:1.7;color:rgba(43,45,49,.8);word-break:keep-all}
.foot{position:absolute;left:72px;bottom:0;height:76px;width:1168px;border-top:1px solid rgba(43,45,49,.28)}
.foot .tab{position:absolute;left:0;top:-1px;height:44px;width:170px;background:var(--ink);color:#fff;font-size:20px;letter-spacing:.14em;font-weight:500;display:flex;align-items:center;justify-content:center}
.panel{position:absolute;left:1240px;top:0;width:680px;height:860px;background:var(--ink);color:#fff}
.panel .tag{position:absolute;left:80px;top:84px;width:56px;height:6px;background:var(--blue)}
.panel .vert{position:absolute;right:40px;top:84px;writing-mode:vertical-rl;font-size:17px;letter-spacing:.42em;color:rgba(255,255,255,.55);font-weight:500}
.stat{position:absolute;left:80px;right:120px;border-top:1px solid rgba(255,255,255,.22);padding-top:18px}
.stat .n{font-size:104px;line-height:1;font-weight:300;letter-spacing:-.02em}
.stat .n small{font-size:38px;margin-left:8px;color:var(--blue-l)}
.stat .l{margin-top:8px;font-size:20px;letter-spacing:.2em;font-weight:500;color:rgba(255,255,255,.88)}
.stat .s{margin-top:4px;font-size:18px;color:rgba(255,255,255,.55)}
"""
HEAD='좋아 보이는 결과일수록 한 번 더 확인합니다.'
INTRO='점수가 좋은 이유를 따져 데이터 누수를 찾았고, 평균에 묻힌 강원도 오차를 지역별로 나눠 추적했습니다.'
PANEL='''<div class="panel"><div class="tag"></div><div class="vert">PORTFOLIO &nbsp;·&nbsp; 2026</div>
<div class="stat" style="top:150px"><div class="n serif">3<small>팀</small></div><div class="l">TEAM PROJECTS</div><div class="s">세 프로젝트 모두 팀장</div></div>
<div class="stat" style="top:372px"><div class="n serif">8</div><div class="l">TROUBLESHOOTING</div><div class="s">막힌 문제와 해결 과정</div></div>
<div class="stat" style="top:594px"><div class="n serif">36<small>+</small></div><div class="l">WORK LOGS</div><div class="s">작업일지</div></div></div>'''
FOOT='<div class="foot"><div class="tab">Portfolio</div></div>'
def ph(x,y,w,h,round_=False,dark=False):
    hd=int(w*.34); bw=int(w*.62); bh=int(h*.26)
    st=f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;'+('border-radius:50%;' if round_ else '')+('background:#3A3D42;border-color:#4A4E55;' if dark else '')
    col='#5E646C' if dark else '#C3CDD7'
    return f'<div class="abs ph" style="{st}"><i style="width:{hd}px;height:{hd}px;border-color:{col};margin-bottom:{int(h*.04)}px"></i><b style="width:{bw}px;height:{bh}px;border-color:{col}"></b></div>'
def page(name, body):
    open(f'{name}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{BASE}</style>{body}')

# A: 작은 사진을 이름 옆에, 소개는 아래 전체 폭
page('A', ph(72,96,240,300) + f'''
<div class="abs dash" style="left:352px;top:108px"></div><div class="abs eb" style="left:420px;top:96px">PORTFOLIO</div>
<div class="abs name" style="left:344px;top:150px;font-size:190px">이웅진</div>
<div class="abs role serif" style="left:352px;top:358px;font-size:40px">Full-Stack Developer</div>
<div class="abs rule" style="left:72px;top:446px;width:1096px"></div>
<div class="abs head" style="left:72px;top:480px;width:1096px">{HEAD}</div>
<div class="abs intro" style="left:72px;top:540px;width:960px">{INTRO}</div>''' + PANEL + FOOT)

# B: 동그란 사진을 이름 앞에 (작게), 이름도 한 단계 작게
page('B', f'''<div class="abs dash" style="left:72px;top:108px"></div><div class="abs eb" style="left:140px;top:96px">PORTFOLIO</div>''' + ph(72,176,176,176,round_=True) + f'''
<div class="abs name" style="left:280px;top:178px;font-size:168px">이웅진</div>
<div class="abs role serif" style="left:286px;top:362px;font-size:38px">Full-Stack Developer</div>
<div class="abs rule" style="left:72px;top:446px;width:1096px"></div>
<div class="abs head" style="left:72px;top:480px;width:1096px">{HEAD}</div>
<div class="abs intro" style="left:72px;top:540px;width:960px">{INTRO}</div>''' + PANEL + FOOT)

# C: 사진을 오른쪽 차콜 칸 위쪽에 넣고, 왼쪽은 이름 중심 그대로
PANEL_C = '''<div class="panel"><div class="vert">PORTFOLIO &nbsp;·&nbsp; 2026</div>''' + ph(1320-1240,84,240,300,dark=True).replace('class="abs ph"','class="abs ph" data-x') + '''
<div class="stat" style="top:440px;padding-top:16px;display:flex;align-items:center;gap:28px"><div class="n serif" style="font-size:72px;width:150px">3<small>팀</small></div><div><div class="l" style="margin:0">TEAM PROJECTS</div><div class="s">세 프로젝트 모두 팀장</div></div></div>
<div class="stat" style="top:566px;padding-top:16px;display:flex;align-items:center;gap:28px"><div class="n serif" style="font-size:72px;width:150px">8</div><div><div class="l" style="margin:0">TROUBLESHOOTING</div><div class="s">막힌 문제와 해결 과정</div></div></div>
<div class="stat" style="top:692px;padding-top:16px;display:flex;align-items:center;gap:28px"><div class="n serif" style="font-size:72px;width:150px">36<small>+</small></div><div><div class="l" style="margin:0">WORK LOGS</div><div class="s">작업일지</div></div></div></div>'''
page('C', f'''<div class="abs dash" style="left:72px;top:108px"></div><div class="abs eb" style="left:140px;top:96px">PORTFOLIO</div>
<div class="abs name" style="left:62px;top:170px;font-size:224px">이웅진</div>
<div class="abs role serif" style="left:72px;top:430px;font-size:44px">Full-Stack Developer</div>
<div class="abs rule" style="left:72px;top:510px;width:1096px"></div>
<div class="abs head" style="left:72px;top:544px;width:1096px">{HEAD}</div>
<div class="abs intro" style="left:72px;top:604px;width:960px">{INTRO}</div>''' + PANEL_C + FOOT)
print('ok')
