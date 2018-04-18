# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:55:35 2017

@author: Heena
"""
from django import template
##from django.shortcuts import tubes, render

register = template.Library()


@register.simple_tag
def squares(value):
    squares = value
    return squares


@register.simple_tag
def points(values):
    points = [1,4,5,8,9,12,13,16]
    return {points: points}
	
@register.simple_tag
def count():
    iterator=itertools.count()
    return iterator
	

def tubes(request, question_id):    
	result = [4,1,4,5,8,9,12,13,16]
	return render(request, 'tubes.html', {'rows': result})
