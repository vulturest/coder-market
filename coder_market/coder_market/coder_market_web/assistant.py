# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 22:28:59 2016

@author: novice
3"""
import re

def is_vaild_username(usrinput):#tested
    '''
        要求:
            1.长度小于20位
            2.必须由数字字母(包括大小写)组成
            3.由字母打头
    '''
    flag = 0    
    first_alp = usrinput[0]
    if len(usrinput)>20 :
        flag = 1
    if first_alp.isalpha() == False:
        flag = 1
    if usrinput.isalnum() == False:
        flag = 1
    if flag == 0:
        return True
    else:
        return False
def is_vaild_password(usrinput):#tested
    '''
        要求:
        
            1.长度小于16位
            2.必须由数字、字母(包括大小写)、下划线组成
    '''
    flag = 0
    if len(usrinput) > 16:
        flag = 1
    result=re.match("[0-9\a-zA-Z\_]+$",usrinput)
    if str(result) == 'None' :
        flag = 1
    if flag == 0:
        return True
    else:
        return False
        
        
def is_vaild_email(usrinput):#tested
    '''
        要求:
            符合合法的email标准，网上有很多现成的，要求改造成这种函数形式
    '''
    result=re.match(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b',usrinput)
    if str(result) !='None':
        return True
    else:
        return False
def is_vaild_receiver(usrinput):#tested
    '''
        要求:
            1.要求是数字
            2.大于1小于等于100
    '''
    for i in usrinput:
        if i.isdigit() == False:
            return False
    num = int(usrinput)  
    if num > 1 and num <= 100:
        return True
    else:
        return False
def is_vaild_tag(usrinput):#tested
    '''
        要求:
            长度小于40位
    '''
    if len(usrinput) < 40:
        return True
    else:
        return False
        
