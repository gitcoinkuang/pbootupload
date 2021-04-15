import time
from addclass import AddClass

#定义参数
#网站地址
url = 'http://localhost'
#后台cookie
cookie = {'PbootSystem':'q09i19rhpvmdnfrsfjd6k7pioe'}
#要新增产品的栏目
sort_id = '23'
#文章标题
content_title = '镀锌管'
#实例化addclass类
add_all = AddClass(cookie,url,sort_id,content_title)
num = 0
#循环上传文件夹的图片
print('正在上传图片……')
img_url = add_all.upload('/home/wgr/下载/钢材2021/镀锌管')
#循环新增产品
for value in img_url:
    a = add_all.user_login(f"{img_url[num]}")
    if a.status_code == 200:
        print(f'新增成功{num+1}')
        time.sleep(0.1)
    num += 1


