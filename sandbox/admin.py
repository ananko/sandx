from django.contrib import admin

from sandbox.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created', 'modified')

admin.site.register(Note, NoteAdmin)

