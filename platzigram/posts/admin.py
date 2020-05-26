#Django
from django.contrib import admin
#Models

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'users', 'profile', 'title', 'photo')
    list_display_links = ('pk', 'users')

search_fields = ('users__username', 'title',)
list_filter = (
        'created',
        'modified',
        'users__is_active',
        'users__is_staff'
        )
readonly_fields = ('created', 'modified', 'users')

fieldsets = (
        ('Post', {
            'fields': (('title', 'photo'),)
        }),

        ('Metadata', {
            'fields': (
                ('users',),
                ('created', 'modified'),
            )
        })
    )