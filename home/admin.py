from django.contrib import admin
from .models import *
# Register your models here.

class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status','note','message','email','ip',]
    list_editable = ['status','note']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']

admin.site.register(Setting,SettingtAdmin)
admin.site.register(Slider,)
admin.site.register(Pay,)
admin.site.register(Gallrey,)


admin.site.register(ContactMessage,ContactMessageAdmin)