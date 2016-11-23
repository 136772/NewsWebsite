#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

from django import template
import datetime
from django.utils.timezone import LocalTimezone, UTC


register = template.Library()

@register.filter
def formatT(value):
    '''
    提交时间与现在时间的差
    :param value: 数据
    :return: 格式化后的时间
    '''
    value = value.replace(tzinfo=UTC())
    nowtime = datetime.datetime.today().replace(tzinfo=LocalTimezone())
    temp = (nowtime - value).days
    if temp >= 1:
        t = value
    else:
        t = (nowtime - value).seconds
        if t <= 3600:
            t = ('{} 分钟以前'.format(t // 60))
        else:
            t = ('{} 小时以前'.format(t // 3600))
    return t


@register.filter
def spli(value, value2):
    '''
    判断导航栏按钮 与 连接地址是否相同
    :param value: 链接地址
    :param value2: 导航栏地址
    :return: True/False
    '''
    flag = False
    value = value.split('/')[-2]
    if int(value) == int(value2):
        flag = True
    return flag
