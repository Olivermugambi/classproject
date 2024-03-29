from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project_Manager)
admin.site.register(Priority)
admin.site.register(Plan_Status)
admin.site.register(Project_Plan)
admin.site.register(Risk_Status)
admin.site.register(Project_Plan_Risk)
admin.site.register(Development_Status)
admin.site.register(Project_Development)
admin.site.register(Team_Member_Role)
admin.site.register(Development_Team_Status)
admin.site.register(Development_Team)
admin.site.register(Team_Member_Status)
admin.site.register(Team_Member)
admin.site.register(Development_Rule)
admin.site.register(Development_Rule_Feedback)
admin.site.register(Release_Status)
admin.site.register(Release_Strategy)
admin.site.register(Release_Backlog)
admin.site.register(Product_Release)
admin.site.register(Release_Feature)