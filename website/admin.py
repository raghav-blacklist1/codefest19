from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(EventDetail)
admin.site.register(ValidReferral)
admin.site.register(Membership)
class EventDetailInline(admin.TabularInline):
    model=EventDetail


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('name','is_registration_on')
    inlines=[EventDetailInline]

class MembershipInline(admin.TabularInline):
    model=Membership

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('name','event','is_active')
    inlines=(MembershipInline,)