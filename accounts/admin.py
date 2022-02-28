from django.contrib import admin
from .models import *
#from .forms omport UserAdminCreationForm, UserAdminChangeForm
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    
    model = User
 #      form = UserAdminCreationForm
  #     add_form = UserAdminChangeForm
    list_display = ['email', 'admin' ]
    list_filter = [ 'staff', 'active', 'admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin','staff', 'active', )}),
    )

class GuestEmailAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = GuestEmail

admin.site.register(User, UserAdmin)
admin.site.register(GuestEmail, GuestEmailAdmin)