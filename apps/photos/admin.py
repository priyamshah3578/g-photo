# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


class PhotoAdmin(admin.ModelAdmin):
    """Photos admin views.
    """
    list_display = ('thumb_tag', 'name',)
    readonly_fields = ('image_tag', 'concepts_chart')

    def get_form(self, request, obj=None, **kwargs):
        """Set update fields on photo edit.
        """
        if obj and obj.pk:
            self.fields = ('image_tag', 'name', 'image', 'concepts_chart')
        else:
            self.fields = ('name', 'image')
        return super(PhotoAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(models.Photo, PhotoAdmin)
