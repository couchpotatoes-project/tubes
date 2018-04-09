# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:55:35 2017

@author: Heena
"""
from django.shortcuts import tubes, render


def tubes(request, question_id):    
	result = [4,1,4,5,8,9,12,13,16]
	return render(request, 'tubes.html', {'rows': result})