from django.contrib import admin
from .models import (
    Trip,
    Start,
    End,
)
# Register your models here.

admin.site.register(Trip)
admin.site.register(Start)
admin.site.register(End)