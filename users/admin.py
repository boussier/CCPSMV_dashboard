from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, TimeWindow, VehicleType


class CustomUserAdmin(UserAdmin):    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
         ('Profil CCPSMV', {
          'fields': (
              'distanceToWork', 
              'travelDuration', 
              'averageCosumption', 
              'vehicleType', 
              'agendaRemoteWorking',
              'notation')}),
    )

    list_display = ['email']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TimeWindow)
admin.site.register(VehicleType)
