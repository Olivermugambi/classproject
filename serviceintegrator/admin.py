from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Service_Pipeline)
admin.site.register(Service_Pipeline_Item_Status)
admin.site.register(Service_Type)
admin.site.register(Service_Pipeline_Item)
admin.site.register(Service_Integration_Status)
admin.site.register(Service_Integration)
admin.site.register(Service_Integrator)
admin.site.register(Service_Integration_Item)
admin.site.register(Integration_Tool_Status)
admin.site.register(Integration_Tool_Type)
admin.site.register(Service_Integration_Tool)
admin.site.register(Tool_Allocation_Status)
admin.site.register(Integration_Tool_Allocation)
admin.site.register(Progress)
admin.site.register(Integration_Progress)
admin.site.register(Integration_Outcome)
admin.site.register(Recommended_Adaptations)