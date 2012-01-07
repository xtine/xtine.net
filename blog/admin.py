from blog.models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'updated')
    list_display_links = ['title']
    prepopulated_fields = {'slug' : ('title',)}

    # TinyMCE
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


admin.site.register(Entry, EntryAdmin)
