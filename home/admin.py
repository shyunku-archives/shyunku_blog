from django.contrib import admin
from home.models import User_Info, Variables, Documents_Info, Comment

# Register your models here.


admin.site.register(User_Info)
admin.site.register(Variables)
admin.site.register(Documents_Info)
admin.site.register(Comment)