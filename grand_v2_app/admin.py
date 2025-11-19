from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import Page, Media

class SortedMediaFormSet(BaseInlineFormSet):
    def get_queryset(self):
        # Get the original queryset
        queryset = super().get_queryset()
        # Sort it by numeric value of 'path'
        sorted_queryset = sorted(queryset, key=lambda media: int(media.path) if media.path.isdigit() else float('inf'))
        # Return the sorted queryset, now as a list of objects
        return sorted_queryset

class MediaInline(admin.TabularInline):
    model = Media
    extra = 0
    formset = SortedMediaFormSet  # Use the custom formset
    fields = ('title', 'phase', 'path', 'get_custom_type_display')  # Added 'path' back here

    readonly_fields = ('get_custom_type_display',)

    def get_custom_type_display(self, obj):
        # If the media is linked to the 'stills' page, display 'Still'
        if obj.page.name == 'stills' and obj.type == 'image':
            return 'Still'
        return obj.get_type_display()

    get_custom_type_display.short_description = 'Type'

class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'phase', 'page', 'path', 'get_custom_type_display')  # Also added 'path' here

    def get_custom_type_display(self, obj):
        # If the media is linked to the 'stills' page, display 'Still'
        if obj.page.name == 'stills' and obj.type == 'image':
            return 'Still'
        return obj.get_type_display()

    get_custom_type_display.short_description = 'Type'

class PageAdmin(admin.ModelAdmin):
    inlines = [MediaInline]

admin.site.register(Page, PageAdmin)
admin.site.register(Media, MediaAdmin)
