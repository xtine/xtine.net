from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, Context
from django.http import Http404
from blog.models import Entry
import datetime


def index(request):
    entries = Entry.objects.all().order_by('-published')
    context = RequestContext(request)
    return render_to_response('blog/index.html', {'entries' : entries}, context_instance = context)


def detail(request, year, month, day, slug):
    entry = get_object_or_404(Entry,
        published__year=year,
        published__month=month,
        published__day=day,
        slug=slug)
    return render_to_response('blog/detail.html', { 'entry': entry })