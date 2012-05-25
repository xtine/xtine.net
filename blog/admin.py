from blog.models import Entry
from django.contrib import admin


class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'updated')
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Entry, EntryAdmin)
