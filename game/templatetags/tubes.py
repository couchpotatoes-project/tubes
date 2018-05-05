# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:55:35 2017

@author: Heena
"""
from django import template
from django.template.defaulttags import register
##from django.shortcuts import tubes, render

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)