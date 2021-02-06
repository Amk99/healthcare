from django.contrib import admin
from .models import testimonies,contact,my_blog,SiteEditor
# Register your models here.

class SiteEditorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_object = self.model.objects.count()
        if num_object > 0:
            return False
        else:
            return True


admin.site.register(SiteEditor,SiteEditorAdmin)
admin.site.register(testimonies)
admin.site.register(contact)
admin.site.register(my_blog)

