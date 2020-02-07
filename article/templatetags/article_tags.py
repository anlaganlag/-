from django import template
register = template.Library()
from article.models import ArticlePost
from django.db.models import Count


@register.simple_tag
def most_commented_articles(n=3):
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by("-total_comments")[:n]

@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()

@register.simple_tag
def author_total_articles(user):
    return user.article.count()


@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by('-created')[:n]
    return {"latest_articles":latest_articles}

@register.simple_tag
def most_commented_articles(n=3):
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:n]
    #annotate就是做好標記yong Count('comments')
#得到是..Aritcles對象關聯的comment對象的個數
#標注到artcles所對應ArticlesPosst對象上


