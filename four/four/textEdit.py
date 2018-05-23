__author__ = 'tian'
from four.settings import LOCATION
import requests
import re

class textEdit(object):
    def dealWithAll(self,response,classname='',id=''):

        text = self.getText(response,classname,id)
        files = ''
        if classname:
            classname_ = '\"'+classname+'\"'
            text_ = response.xpath('//*[@class=%s]'%classname_)
            dict_file,files = self.dealWithText(text_,response)
            print('dict_file:%s'%dict_file)
            _text = self.textReedit(text,dict_file)
            return _text,files
        elif id:
            id = '\"'+id+'\"'
            text_ = response.xpath('//*[@id=%s]'%id)
            dict_file,files = self.dealWithText(text_,response)
            print('dict_file:%s'%dict_file)
            _text = self.textReedit(text,dict_file)
            return _text,files

    def getText(self,response,classname='',id=''):
        connected = True
        while response.status != 200:
            print('...%s'%response.status)
            connected = False
        if connected:
            if classname:
                classname = '\"'+classname+'\"'
                text = response.xpath('//*[@class=%s]'%classname).extract()
                text = ' '.join(text)
                return text
            elif id:
                id = '\"'+id+'\"'
                text = response.xpath('//*[@id=%s]'%id).extract()
                text = ' '.join(text)
                return text
            else:
                return None

    def downloadFile(self,url,filename):
        r = requests.get(url)
        with open(LOCATION+filename,'wb') as f:
            f.write(r.content)

    def dealWithText(self,textXpath,response):
        #处理以a标签开头的图片或者附件
        urls = textXpath.xpath('.//a')
        dict_file = {}
        files = []
        if urls:
            for url in urls:
                url =  url.xpath('./@href').extract_first()
                if url:
                    url = url.strip()
                    if url.endswith('jpg') or url.endswith('JPG') or url.endswith('png') or url.endswith('PNG'):
                        imgName = url[(url.rindex('/')+1):]
                        if not imgName:
                            imgName = url
                        dict_file[url] = LOCATION+imgName
                        if not url.startswith('http'):
                            url = response.urljoin(url)
                        self.downloadFile(url,imgName)
                    if url.endswith('doc') or url.endswith('zip') or url.endswith('docx') or url.endswith('pdf') or \
                        url.endswith('xls') or url.endswith('csv') or url.endswith('xlsx') or url.endswith('rar'):
                        fileName = url[(url.rindex('/')+1):]
                        if not fileName:
                            fileName = url
                        files.append(fileName)
                        dict_file[url] = LOCATION+fileName
                        if not url.startswith('http'):
                            url = response.urljoin(url)
                        self.downloadFile(url,fileName)
        files = ';'.join(files)
        #处理以img标签开头的图片
        urls_img = textXpath.xpath('.//img')
        if urls_img:
            for url_img in urls_img:
                url_img = url_img.xpath('./@src').extract_first()
                if url_img:
                    url_img = url_img.strip()
                    imgName = url_img[(url_img.rindex('/')+1):]
                    dict_file[url_img] = LOCATION+imgName
                    url_img = response.urljoin(url_img)
                    print('图片地址:%s'%url_img)
                    self.downloadFile(url_img,imgName)


        return  dict_file,files

    def textReedit(self,text,dict_file):
        text_ = text
        for k in dict_file.keys():
            text_ = re.sub(k,dict_file.get(k),text)
            text = text_
        return text_