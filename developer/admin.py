from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Role)
admin.site.register(Developer_Status)
admin.site.register(Developer)
admin.site.register(Sprint)
admin.site.register(Sprint_Backlog)
admin.site.register(Backlog_allocation_Status)
admin.site.register(Sprint_Backlog_Allocations)
admin.site.register(Daily_Scrum)
admin.site.register(Review_Status)
admin.site.register(Sprint_Review)
admin.site.register(Sprint_Retrospective)
admin.site.register(Project)
admin.site.register(Feedback)
admin.site.register(Project_Phase)