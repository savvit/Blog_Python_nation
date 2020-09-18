# Модуль моего шаблонного тега
from django import template
from blog.models import Category, Tag, Post


register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu():
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('blog/tags.html')
def show_tags():
    tags = Tag.objects.all()
    return {'tags': tags}


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=4):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}
