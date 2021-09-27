from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

from ..models import Post

register = template.Library()

COLORS_CLASSES = ['info', 'light']
POST_COUNT = 5

# Custom tags

@register.simple_tag
def total_posts():
  return Post.published.count()

@register.simple_tag
def rcolor(i):
  return COLORS_CLASSES[i%2]  # Striped pattern

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=POST_COUNT):
  latest_posts = Post.published.order_by('-publish')[:count]
  return {'latest_posts': latest_posts, 'post_count': count} 

# Custom filters

@register.filter(name='markdown')
def markdown_format(text):
  return mark_safe(markdown.markdown(text))
