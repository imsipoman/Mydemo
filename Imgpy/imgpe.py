from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageFilter
import time

ImgName = '01.jpg'
ImgSaveName = str(time.time())

def main():
    Img = Image.open(ImgName)
    w,h = Img.size
    ipx = Img.convert('L').filter(ImageFilter.BLUR)
    #ipx.thumbnail((w//2,h//2))
    ipx.save('oo','png')
    ImgC = Image.open('oo')
    ww,hh = ImgC.size
    ImgArray = ImgC.load()
    #black = []
    #white = []
    OutImg =  Image.new('RGB',ImgC.size,(255,255,255));
    for x in range(ww):
        for y in range(hh):
            if(y%20 == 0 and x%20 == 0):
                for a in range(10):
                    OutImg.putpixel((x+a,y+a),(0,0,0))        
    OutImg.save('ok','png')
    OutImg2 =  Image.new('RGB',ImgC.size,(255,255,255));            
    for x in range(ww):
        for y in range(hh):
            if(ImgArray[x,y] > 150):
                #black.append([x,y])
                OutImg2.putpixel((x,y),(255,255,255))
            elif (ImgArray[x,y] <= 150 and ImgArray[x,y] >= 40):
                #white.append([x,y])
                OutImg2.putpixel((x,y),(96,96,96))                
            else:
                OutImg2.putpixel((x,y),(0,0,0)) 
    OutImg2.save('kk','png')
    ImgOK = Image.open('ok')
    ImgKK = Image.open('kk')
    ImgEnd = Image.blend(ImgOK,ImgKK,0.4) 
    ImgEnd.save(ImgSaveName,'png')       

main()    