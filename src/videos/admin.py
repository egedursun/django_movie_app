from django.contrib import admin

# Register your models here.
from .models import VideoPublishedProxy
from .models import VideoAllProxy


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['active']
    readonly_fields = ['id', 'is_published']
    class Meta:
        model = VideoAllProxy

    #implement it in the model
    """
    def published(self, obj, *args, **kwargs):
        return obj.active
    """

class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    #list_filter = ['video_id']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)


admin.site.register(VideoAllProxy, VideoAllAdmin)
admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)