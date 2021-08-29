from django.contrib import admin

from .models import Category, Genre, Review, Title, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    empty_value_display = '-пусто-'
    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    empty_value_display = '-пусто-'
    search_fields = ('name',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'category', 'description')
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    list_filter = ('category', 'year', 'genre')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'text',
                    'pub_date', 'score', 'title')
    search_fields = ('text',)
    list_filter = ('text',)
    empty_value_display = '-пусто-'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'review')
    search_fields = ('text',)
    list_filter = ('author', 'review',)
    empty_value_display = '-пусто-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentsAdmin)
