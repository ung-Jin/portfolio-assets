# 연락처 띠 v17: 바탕 투명 → 라이트/다크 테마 모두 자연스럽게
# 구분선 = 차콜 1px + 바로 아래 흰색 반투명 1px (흰 바탕에선 안 보이고, 어두운 바탕에선 밝은 선으로 보임)
import subprocess
BASE="*{margin:0;padding:0;box-sizing:border-box}html,body{background:transparent}body{width:1120px;font-family:'Noto Sans CJK KR',sans-serif;color:#2B2D31;overflow:hidden}"
RULE="border-top:1px solid #2B2D31;box-shadow:0 1px 0 rgba(255,255,255,.26)"
def shot(name,html,h):
    open(f'{name}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{BASE}body{{height:{h}px}}</style>{html}')
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=2','--default-background-color=00000000',f'--window-size=1120,{h}',f'--screenshot={name}.png',f'{name}.html'],capture_output=True)
for k,l in (('email','EMAIL'),('github','GITHUB')):
    shot(f'ct-top-{k}',f'<div style="margin-top:6px;{RULE};padding-top:16px;font-size:22px;letter-spacing:.24em;font-weight:700;color:#5F7388">{l}</div>',58)
shot('ct-bottom',f'<div style="margin-top:2px;{RULE}"></div>',14)
print('ok')
