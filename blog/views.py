from django.contrib.syndication.views import Feed
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from blog.models import Entry


def index(request):
    entries = Entry.objects.filter(hide=False).order_by('-published')[:5]
    archives = Entry.objects.filter(hide=False).dates('published', 'month', order='DESC')

    context = RequestContext(request)
    return render_to_response('blog/index.html', {'entries': entries, 'archives': archives}, context_instance=context)


def month(request, year, month):
    entries = Entry.objects.filter(hide=False, published__year=year, published__month=month)
    archives = Entry.objects.filter(hide=False).dates('published', 'month', order='DESC')

    if not entries:
        raise Http404

    return render_to_response('blog/index.html', {'entries': entries, 'archives': archives})


def year(request, year):
    entries = Entry.objects.filter(hide=False, published__year=year)
    archives = Entry.objects.filter(hide=False).dates('published', 'month', order='DESC')

    if not entries:
        raise Http404

    return render_to_response('blog/index.html', {'entries': entries, 'archives': archives})


def detail(request, year, month, day, slug):
    archives = Entry.objects.filter(hide=False).dates('published', 'month', order='DESC')

    entry = get_object_or_404(Entry,
        published__year=year,
        published__month=month,
        published__day=day,
        slug=slug)
    return render_to_response('blog/detail.html', {'entry': entry, 'archives': archives})


class LatestEntriesFeed(Feed):
    title = "xtine.net blog"
    link = "/blog/feed/"
    description = "xtine.net blog entries"

    def items(self):
        return Entry.objects.filter(hide=False).order_by('-published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_pubdate(self, item):
        return item.published
