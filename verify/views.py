from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

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
