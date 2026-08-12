"""Measure how bright a lesson's background pattern actually renders, and
whether body text still reads against it. Mechanical, so 'too dark' stops
being a matter of opinion.

usage: python3 /tmp/bgmeasure.py <lesson.html> [slide-index]
"""
import sys, asyncio, json
from PIL import Image
from playwright.async_api import async_playwright

def lum(rgb):
    o=[]
    for c in rgb[:3]:
        c/=255.0
        o.append(c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4)
    return 0.2126*o[0]+0.7152*o[1]+0.0722*o[2]

def ratio(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb)
    return (hi+0.05)/(lo+0.05)

async def main():
    f=sys.argv[1]; idx=int(sys.argv[2]) if len(sys.argv)>2 else 4
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        pg=await b.new_page(viewport={'width':1280,'height':720})
        await pg.goto('file://'+f)
        await pg.wait_for_timeout(1500)
        await pg.evaluate(f"""() => {{
          const s=[...document.querySelectorAll('.slide')];
          s.forEach(x=>x.classList.remove('is-active'));
          s[{idx}].classList.add('is-active');
          document.getElementById('stage').classList.remove('on-cover');
          const bg=s[{idx}].dataset.bg;
          document.getElementById('stage').style.setProperty('--hero', bg?`url('${{bg}}')`:'');
        }}""")
        await pg.wait_for_timeout(600)
        txt = await pg.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--text').trim()")
        await pg.screenshot(path='/tmp/bg.png')
        await b.close()
    im=Image.open('/tmp/bg.png').convert('RGB')
    W,H=im.size
    # sample bands that are background-only: far left/right margins + top/bottom strips
    pts=[]
    for y in range(60,H-60,7):
        for x in list(range(6,46,6))+list(range(W-46,W-6,6)):
            pts.append(im.getpixel((x,y)))
    for y in list(range(8,44,6))+list(range(H-70,H-40,6)):
        for x in range(60,W-60,11):
            pts.append(im.getpixel((x,y)))
    ls=sorted(lum(p) for p in pts)
    mean=sum(ls)/len(ls)
    t=txt.lstrip('#'); tc=tuple(int(t[i:i+2],16) for i in (0,2,4))
    # contrast of body text against the brightest 10% of the background
    bright=ls[int(len(ls)*0.90)]
    lt=lum(tc)
    cr=(max(lt,bright)+0.05)/(min(lt,bright)+0.05)
    print(json.dumps({
      'mean_bg_luminance': round(mean,4),
      'p10': round(ls[len(ls)//10],4),
      'p90': round(bright,4),
      'text': txt.strip(),
      'text_vs_brightest_bg': round(cr,2),
    }, indent=2))

asyncio.run(main())
