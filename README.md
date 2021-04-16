# pbootcms批量上传
python批量上传图片到pbootcms并自动生成文章，目前仅写了批量上传到产品，后续可能添加批量上传到案例和新闻
## 使用方法
### 1、解除pbootcms验证
`apps\common\AdminController.php` 里增加不验证字段：`Content`
```php
// 不进行表单检验的控制器
$nocheck = array(
    'Upgrade',
    'Content'
);
```
`core\extend\ueditor\php\controller.php` 里注释权限不足的代码
```php
// 启动会话
// if (! session('sid')) {
//     die('权限不足');
// }
```

### 2、添加cookie
手动在浏览器中登录pboot后台，然后获取到`cookie`，填入`index.py`中，将要上传的同类型图片放到文件夹中，获取文件夹的绝对路径填入，以及要生成的文章标题
```python
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
```
windows的文件夹绝对路径要修改下代码，将上传部分修改为
```python
img_url = add_all.upload(r'c:\xxxxxx\xxxxx')
```
接下来直接运行就好了
```python
python3 index.py
```
