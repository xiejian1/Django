from django.contrib import admin

# Register your models here.
from DjangoApp.models import User,Contact,Tag
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')
# class ContactAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ['Main',{
#             'fields':('name','email'),
#         }],
#         ['Advance',{
#             'classes': ('collapse',), # CSS
#             'fields': ('age',),
#         }]
#     )
class TagInline(admin.TabularInline):
    model = Tag
# class ContactAdmin(admin.ModelAdmin):
#     inlines = [TagInline]  # Inline
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),
#             'fields': ('age',),
#         }]
#
#     )
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]
    )
admin.site.register(Contact,ContactAdmin)
admin.site.register([User])
