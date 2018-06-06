# -*- coding: utf-8 -*-
# from django.forms import Form
from verify.models import Message

__author__ = 'hzl'
__date__ = '202018/6/5 19:02'

from django import forms
from django.forms import widgets, fields, models


class MessageForm(forms.Form):
    title = forms.CharField(max_length=32, error_messages={'required': '请输入标题'}, label='标题')
    phone = forms.CharField(label='电话', error_messages={'required': '请输入电话'}, max_length=222)
    content = forms.CharField(widget=forms.Textarea, label='信息', error_messages={'required': '请输入信息'}, min_length=6)

    def clean(self):
        try:
            content = self.cleaned_data['content']
        except Exception as a:
            print('except' + str(a))
            raise forms.ValidationError(u'信息过短,请重新输入')
        return self.cleaned_data


class Class_form(forms.Form):
    title = forms.RegexField('全栈\d+',
                             # initial='全栈', #设置input标签中的默认值
                             min_length=2,
                             required=True,
                             error_messages={'invalid': '必须以全栈开头',
                                             'min_length': '太短了',
                                             'required': '不能为空'})


class Students(forms.Form):
    name = forms.CharField(required=True)
    widgets = widgets.TextInput(attrs={'class': 'form-control'})
    error_message = {'required': '姓名不能为空'}
    sex = forms.CharField(required=True, error_messages={'required': '不能为空值'})


cls_id = fields.IntegerField(widget=widgets.Select(choices=Message.objects.values_list('id', 'title'),
                                                   attrs={'class': 'form-control'}))
