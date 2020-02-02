ueditor 富文本编辑器 使用简介
---

Django集成UEditor (封装成应用) 百度富文本编辑器

http://ueditor.baidu.com/website/

### 概要

该ueditor版本是基于python2.x的, 后来修改为3的版本

### 测试环境

ubuntu 16.04
python3.5.2
django1.11.7

### 目前测试解决了出现的以下两个问题,都是python版本问题

1 ) **error1**

```python
# name 'file' is not defined
 controller.py  68行

 # jsonfile = file(config_path)
 jsonfile = open(config_path)
```

2 ) **error2**

```python
File "ueditor/controller.py", line 45, 
in buildFileName
for key, value in texts.iteritems():
AttributeError: 'dict' object has no attribute 'iteritems'

controller.py  45行

# for key, value in texts.iteritems():
for key, value in texts.items():
```

### 配置方法

- 下载解压ueditor文件包,放置在项目中,作为一个应用目录

- 打开settings.py，给INSTALLED_APPS加入应用ueditor
    ```python
    INSTALLED_APPS = [
            'ueditor',
        ]
    ```

- 检查一下settings.py是否设置好static静态目录，可参考如下设置
    ```python
    STATIC_URL = '/static/'
    #静态目录
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
    ```

- 打开django项目的urls.py文件，添加ueditor的url路由配置

    ```python
    myproject/myproject/urls.py:

    from django.conf.urls import url,include
    from django.contrib import admin

    urlpatterns = [
        url(r'^ueditor/', include('ueditor.urls')),
        url(r'^admin/',include('myadmin.urls')),
        url(r'^',include('myweb.urls')),
    ]
    ```

- 上面步骤配置完成之后，基本可以使用了, 可以在自己的项目中如下使用
    ```html
    <link rel="stylesheet" type="text/css" href="/ueditor/UE/third-party/SyntaxHighlighter/shCoreDefault.css">
        <script type="text/javascript" src="/ueditor/UE/third-party/SyntaxHighlighter/shCore.js"></script>
        <script type="text/javascript" src="/ueditor/UE/ueditor.config.js"></script>
        <script type="text/javascript" src="/ueditor/UE/ueditor.all.min.js"></script>
        <script type="text/javascript" src="/ueditor/UE/lang/zh-cn/zh-cn.js"></script>

        <div class="am-form-group">
            <label for="user-intro" class="am-u-sm-3 am-form-label">商品简介</label>
            <div class="am-u-sm-9">
                <!-- <textarea name="descr" class="" rows="10" id="user-intro" placeholder="请输入商品简介"></textarea> -->
                <!-- <script id="editor" type="text/plain" style="width:100%;height:500px;"></script> -->
                <script id="editor" name="content" type="text/plain" style="height:500px;"></script>
            </div>
        </div>


        <script type="text/javascript">
            var ue = UE.getEditor('editor');
            SyntaxHighlighter.all();
        </script>
    ```

### 水印功能

- 上传图片自动加水印 该功能默认没开启。
- 上传图片加水印功能需要安装PIL $ `pip3 install pillow`
- 水印相关设置在ueconfig.json末尾：
    ```json
    "openWaterMark": false,  //是否开启
    "waterMarkText": "我的水印\nhttp://xxxxx.com", //水印内容，建议一行文本
    "waterMarkFont": "msyhbd.ttf",  //字体，中文需要字体支持才不会出错
    "waterMarkSize": 15,    //字体大小
    "waterMarkBottom": 45,  //下边距
    "waterMarkRight": 155   //右边距
    ```

### 其它问题

- ueditor配置可能需要根据你的项目具体情况修改
- ueditor前端配置文件，在ueditor/UE/ueditor.config.js
- ueditor后端配置文件，在ueditor/ueconfig.json 具体配置可参考ueditor官网