from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from app.models import District
from app.models import Users
from PIL import Image
import time,os
# from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

# 首页
def index(request):
    return render(request, 'app/index.html')

# 多级联动
def cities(request):
    return render(request, 'app/cities.html')

# 访问地区的接口
def district(request, upid):
    dlist = District.objects.filter(upid=upid)
    list = []
    for ob in dlist:
        list.append({'id':ob.id,'name':ob.name})
    return JsonResponse({'data':list})

# 文件上传
def files(request):
    return render(request, 'app/file_upload.html')

# 文件上传接口
# @csrf_exempt
# 上面的装饰器可以取消form表单点的post验证
def upload(request):
    '''执行图片的上传'''
    file = request.FILES.get("pic", None)
    if not file:
        return HttpResponse("没有上传文件信息")
    filename = str(time.time())+"."+file.name.split('.').pop()
    # 开始写入文件
    destination = open("./static/pics/"+filename,"wb+")
    for chunk in file.chunks():    # 分块写入文件
        destination.write(chunk)  
    destination.close()

    # 执行图片缩放
    im = Image.open("./static/pics/"+filename)
    # 缩放到75*75(缩放后的宽高比例不变):
    im.thumbnail((75, 75))
    # 把缩放后的图像用jpeg格式保存:
    im.save("./static/pics/s_"+filename, None)

    #执行图片删除
    #os.remove("./static/pics/"+filename)

    return HttpResponse("上传成功！图片：" + filename)

# 分页页面
def page(request, pIndex):
    # list = Users.objects.filter(aParent__isnull=True)
    all = Users.objects.all()
    p = Paginator(all, 1) # 1条数据1页
    if pIndex == '':
        pIndex = '1'
    list = p.page(pIndex)
    pIndex = int(pIndex)
    list = p.page(pIndex)
    plist = p.page_range # 页码
    context = {'list': list, 'plist': plist, 'pIndex': pIndex}
    return render(request, 'app/page.html', context)

# ueditor 编辑器
def my_ueditor(request):
    return render(request, 'app/my_ueditor.html')

# session
def state(request):
    request.session['username'] = '张三'
    name = request.session.get('username', default=None)
    if name:
        return HttpResponse(name)
    return HttpResponse('Hello state')

# middleware
def middleware(request):
    return render(request, 'app/middleware.html')

# password
def password(request):
    import hashlib
    from django.contrib.auth.hashers import make_password, check_password
    
    # 第一种加密方式, 不适用于存数据库，每次刷新后都会变，而且太长
    pa = '123456' # 密码
    upass1 = make_password(pa, None, 'pbkdf2_sha256') # 加密后的密文
    checkpa1 = check_password(pa, upass1) # 对比明文和密文是否匹配

    # 第二种加密方式 2次 md5 加密, 推荐使用
    m = hashlib.md5()
    def enc(p):
        '''md5加密函数'''
        m.update(bytes(p, encoding="utf8"))
        return m.hexdigest()
    upass2 = enc(pa)
    upass2 = enc(upass2)

    context = {
        "pa": pa,
        "first": {"upass":upass1, "isRight":checkpa1},
        "second": {"upass":upass2}
    }
    return render(request, 'app/password.html', context)