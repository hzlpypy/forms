# -*- coding: utf-8 -*-
from verify import views, verification_code

__author__ = 'hzl'
__date__ = '202018/6/5 19:02'

from django.conf.urls import url

urlpatterns = [
    url('verify/',views.verify),
    url(r'^$',views.index,name='index'),
    url(r'login/',views.login,name='login'),
    url(r'login_hander',views.login_handle,name='login_handle'),
    url(r'logout',views.logout,name='logout'),
    url(r'verifycode',verification_code.verifycode),
    url(r'kk',verification_code.kk),
    url(r'judge/',verification_code.judge),

]