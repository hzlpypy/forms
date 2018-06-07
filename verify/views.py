from datetime import timedelta

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from forms import settings
from verify import models
from verify.forms import MessageForm


# Create your views here.

def verify(request):
    if request.method == 'POST':
        f = MessageForm(request.POST)
        if f.is_valid():
            title = f.cleaned_data['title']
            phone = f.cleaned_data['phone']
            content = f.cleaned_data['content']
            message = models.Message()
            message.title = title
            message.phone = phone
            message.content = content
            message.save()
            # request.session['title'] = title
            success = '留言发送成功'
            return render(request, 'verify.html', {'form': f, 'success': success})

    else:
        f = MessageForm()
        return render(request, 'verify.html', {'form': f})


def index(request):
    uname = request.session.get('uname')
    return render(request, 'booktest/index.html', {'uname': uname})


def login(request):
    return render(request, 'booktest/login.html')


def login_handle(request):
    request.session['uname'] = request.POST.get('uname')
    return redirect(reverse('main:index'))


def logout(request):
    # request.session['uanme'] = None
    # del request.session['uname'] 删除会话
    # request.session.clear()  清楚所有对话
    """
    set_expiry(value):设置会话额超过时间
    如果没有指定，则两个星期后过期
    如果value是一个整数，会话将在values秒没有活动后过期
    若果value是一个imedelta对象，会话将在当前时间加上这个指定的日期/时间过期
    如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期
    如果value为None，那么会话永不过期
    修改视图中login_handle函数，查看效果
    """
    # request.session.set_expiry(10) # 10秒内没有活动过期
    # request.session.set_expiry(timedelta(days=5)) # 5天后过期
    request.session.set_expiry(0) # 在浏览器关闭时过期
    # request.session.set_expiry(None) # 永不过期
    # request.session.flush()
    return redirect(reverse('main:login'))

def email(request):
    msg = "<div>抠脚倩,点击下面有惊喜</div>" \
          "<a href='http://xyq.163.com/'>点击进入梦幻世界</a></br>" \
          "<a href='http://qnm.163.com/#index'>点击进入倩女幽魂</a>" \
          "<a href='https://user.qzone.qq.com/1761784585?ADUIN=1761784585&ADSESSION=1528351054&ADTAG=CLIENT.QQ.5563_MyTip.0&ADPUBNO=26785&source=namecardhoverstar' target='_blank'>点击来到我的空间<a/>"
    send_mail('标题','内容','hzl5201314159@163.com',
              ['yqq520131459@163.com'],
              html_message=msg)
    return HttpResponse('OK')