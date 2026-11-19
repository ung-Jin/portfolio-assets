# C안 검토용: 이력서 사진(흰 배경 가정) 그대로 vs 보정안
exec(open('gen.py',encoding='utf-8').read().split("# A:")[0])
def idphoto(x,y,w,h,bg):
    # 실제 사진 대신 쓰는 단순한 형태(배경색 + 정장 실루엣 + 얼굴)
    return f'''<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};overflow:hidden">
<div class="abs" style="left:{int(w*.3)}px;top:{int(h*.16)}px;width:{int(w*.4)}px;height:{int(h*.36)}px;border-radius:50%;background:#E3D5C8"></div>
<div class="abs" style="left:{int(w*.08)}px;top:{int(h*.58)}px;width:{int(w*.84)}px;height:{int(h*.6)}px;border-radius:{int(w*.4)}px {int(w*.4)}px 0 0;background:#23293A"></div>
<div class="abs" style="left:{int(w*.44)}px;top:{int(h*.58)}px;width:{int(w*.12)}px;height:{int(h*.3)}px;background:#F2F2F2;clip-path:polygon(0 0,100% 0,50% 100%)"></div></div>'''
def stats(top0,gap):
    rows=[('3<small>개</small>','TEAM PROJECTS','한 팀으로 세 프로젝트 모두 팀장'),('9','TROUBLESHOOTING','막힌 문제와 해결 과정'),('46','WORK LOGS','작업일지')]
    return ''.join(f'<div class="stat" style="top:{top0+i*gap}px;padding-top:16px;display:flex;align-items:center;gap:28px"><div class="n serif" style="font-size:72px;width:150px">{n}</div><div><div class="l" style="margin:0">{l}</div><div class="s">{s}</div></div></div>' for i,(n,l,s) in enumerate(rows))
def left(name_px, role_px, head_px, top_name, top_role, top_rule):
    return f'''<div class="abs dash" style="left:72px;top:108px"></div><div class="abs eb" style="left:140px;top:96px">PORTFOLIO</div>
<div class="abs name" style="left:{72-int(name_px*.045)}px;top:{top_name}px;font-size:{name_px}px">이웅진</div>
<div class="abs role serif" style="left:72px;top:{top_role}px;font-size:{role_px}px">Full-Stack Developer · Java / Spring Boot / Python</div>
<div class="abs rule" style="left:72px;top:{top_rule}px;width:1096px"></div>
<div class="abs head" style="left:72px;top:{top_rule+34}px;width:1096px;font-size:{head_px}px">{HEAD}</div>
<div class="abs intro" style="left:72px;top:{top_rule+34+int(head_px*1.4)+18}px;width:960px">{INTRO}</div>'''
# C-1: 지금 C 그대로 + 흰 배경 이력서 사진
page('C1', left(224,44,34,170,430,510) + '<div class="panel"><div class="vert">PORTFOLIO &nbsp;·&nbsp; 2026</div>'+idphoto(80,84,240,300,'#FFFFFF')+stats(440,126)+'</div>'+FOOT)
# C-2: 사진 배경을 회색으로(촬영 시 회색 배경 선택 또는 배경만 어둡게), 이름 줄이고 한 줄 소개 키움
page('C2', left(184,46,42,176,392,474) + '<div class="panel"><div class="vert">PORTFOLIO &nbsp;·&nbsp; 2026</div>'+idphoto(80,84,240,300,'#8E959E').replace('background:#8E959E','background:#8E959E;outline:1px solid rgba(255,255,255,.25);outline-offset:8px')+stats(440,126)+'</div>'+FOOT)
print('ok')
