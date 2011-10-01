from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from blog.models import Entry

def index(request):
    entries = Entry.objects.all().order_by('-published')
    context = RequestContext(request)
    return render_to_response('blog/index.html', {'entries' : entries}, context_instance=context)