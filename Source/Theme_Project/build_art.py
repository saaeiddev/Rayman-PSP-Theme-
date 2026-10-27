from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
from pathlib import Path
import json, shutil
R=Path('/workspace/scratch/3881f31d12e8/Rayman-Raving-Rabbids-PSP-Theme'); P=R/'Source/Theme_Project'; S=Path('/workspace/scratch/3881f31d12e8/ptf-studio/samples/PTF_STUDIO_SAMPLE_THEME/index.json')
ix=json.loads(S.read_text()); ix.update(name='Rayman Raving Rabbids',file_name='RABBIDS_UNIVERSAL',version='1.0',psp_version='6.20'); ix['background_mode']=8
ix['categories']['2']['5']={'file_type':5,'file_name':'2_0005.gim','file_comp':2}
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
cats={1:'Settings',2:'Photo',3:'Music',4:'Video',5:'Video',6:'Game',7:'Network',8:'Extras'}
def quant(im, path, colors=256):
 im.convert('RGBA').quantize(colors=colors,method=Image.Quantize.FASTOCTREE).save(path)
def fit(im,sz):
 im=im.copy();im.thumbnail(sz,Image.Resampling.LANCZOS); out=Image.new('RGBA',sz);out.alpha_composite(im,((sz[0]-im.width)//2,(sz[1]-im.height)//2));return out
wall=Image.open(R/'Wallpapers/Main_Wallpaper.png').convert('RGB'); wall.save(P/'1_0000.png'); wall.resize((300,170),Image.Resampling.LANCZOS).convert('RGBA').save(P/'0_0001.png')
category={k:Image.open(R/'Icons/Category'/f'{v}.png').convert('RGBA') for k,v in cats.items()}
quant(fit(category[6],(16,16)),P/'0_0000.png')
for k,im in category.items(): quant(im,P/f'2_{k:04}.png')
# A distinct labeled badge is paired with a semantically related illustration for each native slot.
slots={2:('MS','Game','Memory Stick'),4:('DISC','Video','UMD'),6:('CAM','Photo','Camera'),8:('PLAY','Game','Game Sharing'),10:('SAVE','Game','Saved Data Utility'),12:('UP','Game','UMD Update'),14:('UP','Network','Network Update'),16:('USB','Settings','USB Connection'),18:('VID','Video','Video Settings'),20:('PIC','Photo','Photo Settings'),22:('SYS','Settings','System Settings'),24:('ART','Extras','Theme Settings'),26:('TIME','Settings','Date and Time Settings'),28:('PWR','Settings','Power Save Settings'),30:('TV','Video','External Display Settings'),32:('SND','Music','Sound Settings'),34:('LOCK','Settings','Security Settings'),36:('RSS','Network','RSS Channel Settings'),38:('NET','Network','Network Settings'),40:('HELP','Extras','Online Instruction Manuals'),42:('LINK','Game','Remote Play'),44:('FM','Music','Internet Radio'),46:('RSS','Network','RSS Channel'),48:('WEB','Network','Internet Browser'),50:('FIND','Network','Internet Search'),52:('ID','Extras','Account Management'),54:('PSP','Game','Default Fallback'),56:('BT','Network','Bluetooth Settings'),58:('SENS','Music','SensMe Channels')}
namecat={v:k for k,v in cats.items()}; namecat['Video']=4

def body(label,category_name,size=48):
 # Supersampled composition: illustration plus legible navy-and-yellow identification tab.
 S=4; canvas=Image.new('RGBA',(size*S,size*S)); icon=fit(category[namecat[category_name]], (size,size)).resize((size*S,size*S),Image.Resampling.LANCZOS); canvas.alpha_composite(icon,(0,0))
 d=ImageDraw.Draw(canvas); h=12*S; y=size*S-h; d.rounded_rectangle((2*S,y,(size-2)*S,size*S-1),radius=4*S,fill=(4,20,58,238),outline=(255,215,30,255),width=S)
 f=ImageFont.truetype(font,(7 if len(label)>3 else 8)*S); box=d.textbbox((0,0),label,font=f); d.text(((size*S-(box[2]-box[0]))/2,y+(h-(box[3]-box[1]))/2-box[1]-S/2),label,font=f,fill='white')
 return canvas.resize((size,size),Image.Resampling.LANCZOS)
def focus(im,sz):
 a=Image.new('L',(sz,sz));a.paste(im.getchannel('A'),((sz-im.width)//2,(sz-im.height)//2)); glow=a.filter(ImageFilter.GaussianBlur(3)); glow=ImageChops.subtract(glow,a).point(lambda x:round(x*0.9/4)*4); o=Image.new('RGBA',(sz,sz),(255,255,255,0));o.putalpha(glow);return o
for n,(label,cat,desc) in slots.items():
 im=body(label,cat); im.save(R/'Icons/First_Level'/f'{n:02}_{desc.replace(" ","_")}.png'); quant(im,P/f'3_{n:04}.png'); fo=focus(im,64);fo.save(R/'Icons/Focus'/f'{n+1:02}_focus.png');quant(fo,P/f'3_{n+1:04}.png',64)
for n,lab,cat in [(0,'ON','Settings'),(2,'OFF','Settings')]:
 im=body(lab,cat,32);im.save(R/'Icons/Second_Level'/f'{n:02}_icon.png');quant(im,P/f'4_{n:04}.png');fo=focus(im,48);fo.save(R/'Icons/Focus'/f'second_{n+1:02}_focus.png');quant(fo,P/f'4_{n+1:04}.png',64)
shutil.copy(R/'Icons/First_Level/54_Default_Fallback.png',R/'Icons/PSP_Go/Standard_Fallback.png')
(P/'index.json').write_text(json.dumps(ix,indent=2))
# conceptual XMB navigation previews, not screenshots or an emulator
f=ImageFont.truetype(font,11);fs=ImageFont.truetype(font,9)
for title,sub,cat in [('Settings',22,1),('Game',54,6),('Music',2,3)]:
 im=wall.convert('RGBA'); d=ImageDraw.Draw(im); centers=[-54,28,110,192,274,356,438]; ids=[1,2,3,4,6,7,8]; selected=ids.index(cat)
 for j,id in enumerate(ids):
  x=110+(j-selected)*82; icon=category[id].copy()
  if id!=cat: icon.putalpha(icon.getchannel('A').point(lambda p:p//2))
  im.alpha_composite(icon,(x-32,48))
 d.text((110,101),title,font=f,fill='white',stroke_width=1,stroke_fill=(3,12,30),anchor='ma'); ic=Image.open(R/'Icons/First_Level'/f'{sub:02}_{slots[sub][2].replace(" ","_")}.png');im.alpha_composite(ic,(86,126));d.text((148,143),slots[sub][2],font=f,fill='white',stroke_width=1,stroke_fill=(3,12,30));d.text((380,13),'12:00   100%',font=fs,fill='white',stroke_width=1,stroke_fill=(3,12,30))
 im.convert('RGB').save(R/'Previews'/f'{title}_Preview.png')
shutil.copy(R/'Previews/Game_Preview.png',R/'Previews/PSP_Go_Preview.png');shutil.copy(R/'Previews/Game_Preview.png',R/'Previews/PSP_3000_Preview.png')
