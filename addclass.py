import requests
import time
import os
import json
class AddClass:
    #用于修改的类
    def __init__(self,cookie,post_url,sort_id,content_title):
        self.re = requests
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}
        self.cookie = cookie
        self.post_url = post_url
        self.sort_id = sort_id
        self.content_title = content_title
    #新增产品
    def user_login(self,upload_img):
        self.upload_img = upload_img
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.data = {'scode':self.sort_id,'title':self.content_title,'author':'admin','source':'本站','titlecolor':'#333333','date':date,'status':'1','content':f'<p style="text-align: center;"><img src="{self.upload_img}"/> </p>','ico':self.upload_img}
        return self.re.post(f'{self.post_url}/yncdwl.php?p=/Content/add/mcode/3',headers = self.header,data=self.data,cookies=self.cookie)

    def upload(self,url_img):
        #上传图片类
        self.url_img = url_img
        self.img_urls = []
        # 获取图片列表
        imgs = self.dir_list(self.url_img)
        for img in imgs:
            #循环拼接图片绝对地址
            img_url = f"{self.url_img}/{img}"
            #组合参数开始上传
            file_data =  {'upfile': open(img_url, 'rb')}
            jx = self.re.post(f'{self.post_url}/core/extend/ueditor/php/controller.php?action=uploadimage',files=file_data,headers=self.header)
            if jx.status_code == 200:
                jg = jx.json()
                #存入列表等待添加使用
                self.img_urls.append(jg['url'])
            else:
                print(jx.text)
        return self.img_urls

    #遍历文件夹下的所有图片，并返回一个列表
    def dir_list(self,dir_url):
        return os.listdir(dir_url)
