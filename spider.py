# -*- coding: utf-8 -*-  
# oratis  
import re  
import urllib  
import urllib2  
import os  
import socket
#抓取网页图片  
 
#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码  
def getHtml(url):  
    page = urllib.urlopen(url)  
    html = page.read()
    #print html  
    return html  
  
#创建保存图片的文件夹  
def mkdir(path):  
    path = path.strip()  
    # 判断路径是否存在  
    # 存在    True  
    # 不存在  Flase  
    isExists = os.path.exists(path)  
    if not isExists:  
        print u'新建了名字叫做',path,u'的文件夹'  
        # 创建目录操作函数  
        os.makedirs(path)  
        return True  
    else:  
        # 如果目录存在则不创建，并提示目录已经存在  
        print u'名为',path,u'的文件夹已经创建成功'  
        return False  
  
# 输入文件名，保存多张图片  
def saveImages(imglist,name):  
    number = 1  
    for imageURL in imglist:  
        splitPath = imageURL.split('.')  
        fTail = splitPath.pop()  
        if len(fTail) > 3:  
            fTail = 'jpg'  
        fileName = name + "/" + str(number) + "." + fTail  
        # 对于每张图片地址，进行保存  
        try:  
            u = urllib2.urlopen(imageURL)  
            data = u.read()  
            f = open(fileName,'wb+')  
            f.write(data)  
            print u'正在保存的一张图片为',fileName  
            f.close()  
        except urllib2.URLError as e:  
            print (e.reason)  
        number += 1  
  
  
#获取网页中所有图片的地址  
def getAllImg(html):  
    #利用正则表达式把源代码中的图片地址过滤出来  
    #reg = r'src="(.+?\.jpg)" pic_ext'  
    
    reg = r'data-original="(.+?\.jpg)" src='
    
    #<img pic_type="0" class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=294db374d462853592e0d229a0ee76f2/e732c895d143ad4b630e8f4683025aafa40f0611.jpg" pic_ext="bmp" height="328" width="560">
    #<img class="lazy" data-original="http://pic1.win4000.com/mobile/4/582bb8411bac3_200_300.jpg" src="http://pic1.win4000.com/mobile/4/582bb8411bac3_200_300.jpg" alt="简约卡通动漫美女手机锁屏壁纸" style="display: block;"> 
    print reg
    imgre = re.compile(reg)  
    imglist = imgre.findall(html) #表示在整个网页中过滤出所有图片的地址，放在imglist中  
    return imglist  
  
  
#创建本地保存文件夹，并下载保存图片  
if __name__ == '__main__':
	socket.setdefaulttimeout(100)
	pages = "http://www.win4000.com/mobile_0_0_0_"
	start_number = 228
	end_number = 326 
	for i in range(start_number,end_number):
		listurl = pages+str(i)+".html"
		print listurl
		for l in range(start_number,end_number):
			html = getHtml(listurl)#获取该网址网页详细信息，得到的html就是网页的源代码 
			path = u'wallpaper p'+str(i)  
    		mkdir(path) #创建本地文件夹  
    		imglist = getAllImg(html) #获取图片的地址列表  
    		saveImages(imglist,path) # 保存图片
	print u'已经结束了'
    
      
