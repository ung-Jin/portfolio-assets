# 링크 컴포넌트 시안: 프로젝트 패널 하단 CTA + 연락처 타일
import re
src=open('gen_proj.py',encoding='utf-8').read()
P=eval(re.search(r"P=(\[.*?\])\nCSS",src,re.S).group(1))
CSS=re.search(r'CSS="""(.*?)"""',src,re.S).group(1).replace('height:640px','height:__H__px')
INSIDE={'01':'내 담당 · 문제 해결 2건 · 설계(ERD) · 기술 스택 · 남은 한계',
        '02':'내 담당 · 문제 해결 3건 · 모델 비교 · 구조 · 남은 한계',
        '03':'내 담당 · 문제 해결 3건 · 구조 · 기술 스택 · 남은 한계'}
VAR={
'a':""".cta{position:absolute;left:0;right:0;top:644px;height:92px;border:2px solid #2B2D31;display:flex}
.ci{flex:1;display:flex;align-items:center;gap:28px;padding:0 34px}
.cl{font-size:18px;letter-spacing:.24em;font-weight:700;color:#5F7388}
.cv{font-size:26px;font-weight:500;color:#2B2D31}
.cb{width:400px;background:#2B2D31;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 34px;font-size:27px;font-weight:700}
.cb b{font-size:36px;font-weight:400}""",
'b':""".cta{position:absolute;left:0;right:0;top:644px;height:92px;border-top:1px solid #2B2D31;border-bottom:1px solid #2B2D31;display:flex}
.ci{flex:1;display:flex;align-items:center;gap:28px;padding:0 0}
.cl{font-size:18px;letter-spacing:.24em;font-weight:700;color:#5F7388}
.cv{font-size:26px;font-weight:500;color:#2B2D31}
.cb{display:flex;align-items:center;gap:22px;font-size:27px;font-weight:700;color:#2B2D31}
.cb b{width:58px;height:58px;border-radius:50%;background:#2B2D31;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:400}"""}
for v,vcss in [('b',VAR['b'])]:
  for n,role,per,t,d,kl,kv,st,img in P:
    H=760
    open(f'link/proj-{n}-{v}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{CSS.replace("__H__",str(H))}{vcss}</style><div class="rule"></div><div class="l"><div class="n">{n}</div><div class="meta">{role}　·　{per}</div><div class="t">{t}</div><div class="d">{d}</div></div><div class="k"><div class="kl">KEY RESULT · {kl}</div><div class="kv">{kv}</div></div><div class="s">{st}</div><div class="img"><img src="../{img}"></div><div class="cta"><div class="ci"><span class="cl">INSIDE</span><span class="cv">{INSIDE[n]}</span></div><div class="cb">프로젝트 자세히 보기<b>→</b></div></div>')
# 연락처 타일 (반쪽 칸에 들어갈 크기)
TC="""*{margin:0;padding:0;box-sizing:border-box}body{width:1120px;height:150px;background:#fff;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden}
.t{position:absolute;inset:2px;border:2px solid #2B2D31;display:flex}
.i{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 40px}
.l{font-size:22px;letter-spacing:.24em;font-weight:700;color:#5F7388}
.v{margin-top:8px;font-size:40px;font-weight:700;letter-spacing:-.005em}
.b{width:260px;background:#2B2D31;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 36px;font-size:30px;font-weight:700}
.b i{font-style:normal;font-size:40px;font-weight:400}"""
for k,l,v,b in [('email','EMAIL','leeungjin@gmail.com','메일 쓰기'),('github','GITHUB','github.com/ung-Jin','GitHub 열기')]:
    open(f'link/ct-{k}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{TC}</style><div class="t"><div class="i"><div class="l">{l}</div><div class="v">{v}</div></div><div class="b">{b}<i>↗</i></div></div>')
print('ok')
