from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    list_display = ('title', 'id', 'slug', 'created', 'get_img', 'views',)
    list_filter = ('category', 'tags',)
    fields = ('title', 'slug', 'category', 'tags', 'content', 'time_to_read', 'img', 'get_img', 'views', 'created')
    readonly_fields = ('views', 'get_img', 'created')
    search_fields = ('title',)
    save_as = True

    def get_img(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="50">')
        return '-'
    get_img.short_description = 'Image'
