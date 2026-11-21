from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W=H=1024
BG=(11,18,32)
CARD=(22,32,54)
ACCENT=(255,196,0)
WHITE=(255,255,255)
MUTED=(176,190,210)

def font(name, size):
    paths=[
        f"/home/hatch/.local/share/fonts/poppins/{name}",
        f"/usr/share/fonts/truetype/dejavu/{name}",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: pass
    return ImageFont.load_default()

f_title=font("Poppins-ExtraBold.ttf", 58)
f_date=font("Poppins-Bold.ttf", 26)
f_head=font("Poppins-Bold.ttf", 27)
f_body=font("Poppins-Regular.ttf", 22)
f_small=font("Poppins-Regular.ttf", 20)
f_num=font("Poppins-ExtraBold.ttf", 34)

img=Image.new("RGB",(W,H),BG)
d=ImageDraw.Draw(img)
# top accent bar
d.rectangle([0,0,W,10], fill=ACCENT)
d.text((48,28),"WORLD NEWS", font=f_title, fill=WHITE)
d.text((48,96),"20 NOVEMBER 2026  •  FRIDAY", font=f_date, fill=ACCENT)
d.text((48,132),"Six stories that defined the day — in one picture", font=f_small, fill=MUTED)

stories=[
 ("1","WORLD COURT","Myanmar guilty of genocide","ICJ rules 9–6: Myanmar committed genocide against the Rohingya minority.", (255,90,90)),
 ("2","SUMMIT","Trump, Xi & Putin meet","First three-way summit in Shenzhen ends with a joint peace declaration.", (90,180,255)),
 ("3","MARKETS","Anthropic's big Nasdaq debut","Shares close +17% at ~$97. Stocks fall a 5th day; Nikkei drops 4.8%.", (255,196,0)),
 ("4","WAR IN UKRAINE","Russian strikes hit Kyiv","Overnight strikes hit Kyiv bridges; 8 people killed, 28 injured.", (255,140,90)),
 ("5","MIDDLE EAST","Missile hits Riyadh tower","Houthi missile damages the PIF tower in Riyadh's financial district.", (120,220,160)),
 ("6","GAMING","GTA 6 launch: $2.3bn","Grand Theft Auto VI tops $2.3 billion in launch sales.", (200,140,255)),
]

x0,y0=48,180
cw,ch=452,238
gx,gy=24,20
for i,(num,tag,title,body,color) in enumerate(stories):
    col=i%2; row=i//2
    x=x0+col*(cw+gx); y=y0+row*(ch+gy)
    d.rounded_rectangle([x,y,x+cw,y+ch], radius=18, fill=CARD)
    d.rectangle([x,y,x+8,y+ch], fill=color)
    d.text((x+28,y+18), num, font=f_num, fill=color)
    d.text((x+72,y+26), tag, font=f_head, fill=color)
    # title wrapped
    lines=textwrap.wrap(title, width=20)
    yy=y+72
    for ln in lines:
        d.text((x+28,yy), ln, font=f_head, fill=WHITE)
        yy+=32
    blines=textwrap.wrap(body, width=29)
    yy+=6
    for ln in blines:
        d.text((x+28,yy), ln, font=f_body, fill=MUTED)
        yy+=28

d.text((48,962),"Sources: ICJ • Shenzhen summit • Nasdaq • Kyiv • Riyadh • Rockstar  •  20 Nov 2026", font=f_small, fill=MUTED)
img.save("/home/hatch/workspace/makefun-news-20261120/entry.png", optimize=True)
print("saved", img.size, os.path.getsize("/home/hatch/workspace/makefun-news-20261120/entry.png"))
