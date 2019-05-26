from django.contrib import admin
from home.models import User_Info, Variables, Documents_Info, Comments

# Register your models here.


admin.site.register(User_Info)
admin.site.register(Variables)
admin.site.register(Documents_Info)
admin.site.register(Comments)