from django.contrib import admin
from .models import (
    User,
    Passenger,
    Driver,
    Profile,
    MaritalStatus,
    EdQual,
    Role,
    Gender,
    CarType,

)

# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display = ("user", "serialNumber",)


admin.site.register(User)
admin.site.register(Passenger)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Profile)
admin.site.register(MaritalStatus)
admin.site.register(EdQual)
admin.site.register(CarType)
admin.site.register(Gender)
admin.site.register(Role)
