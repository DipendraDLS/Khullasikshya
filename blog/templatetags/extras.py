# Creating the custom template tags for using in blog_details.py

from django import template

register = template.Library()


@register.filter(name="get_val")     #yo chai templatetag ko name ho which is used in blog_details.py
def get_val(dict, key):     #Yo function le yeuta dictonary lincha ani key lincha ra key ko adhar ma dictionary bata value fetchout gardincha.
    return dict.get(key)
