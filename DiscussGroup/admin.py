from django.contrib import admin
#from DiscussGroup.models import StaffProfile
#from DiscussGroup.models import StudentProfile
from DiscussGroup.models import UserProfile
from DiscussGroup.models import DiscussionGroup, MessageDetails,ModelMember, \
    Model, ActivityDetails, AcceptRecord


admin.site.register(UserProfile)
admin.site.register(DiscussionGroup)
admin.site.register(MessageDetails)
admin.site.register(Model)
admin.site.register(ModelMember)
admin.site.register(ActivityDetails)
admin.site.register(AcceptRecord)