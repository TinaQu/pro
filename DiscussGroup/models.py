from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    Department = models.CharField(max_length=30)
    isStudent = models.BooleanField(default=False)
    isStaff = models.BooleanField(default=False)
    isAdministrator = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

#class StudentProfile(models.Model):
 #   Student = models.OneToOneField(User)
    #Password = models.CharField(max_length=16)
    #Email = models.CharField(max_length=30)
  #  StartTime = models.DateField()
   # EndRime = models.DateField()

  #  def __unicode__(self):
   #     return self.user.username

#class StaffProfile(models.Model):
#    Staff = models.OneToOneField(User)
    #Password = models.CharField(max_length=16)
 #   Department = models.CharField(max_length=30)
    #Email = models.CharField(max_length=30)

 #   def __unicode__(self):
 #       return self.user.username

class DiscussionGroup(models.Model):
    GroupID = models.CharField(max_length=30)
    #MaxNum = models.IntegerField(max_length=3)
    #CreateUserId = models.IntegerField(max_length=20)
    CreateUserId = models.ForeignKey(User,related_name='+')
    Tag = models.CharField(max_length=100)
    Member = models.ManyToManyField(User,related_name='+u+')
    #StudentMember = models.ManyToManyField(StudentProfile)
    #StaffMember = models.ManyToManyField(StaffProfile)

    def __unicode__(self):
        return self.GroupID

class MessageDetails(models.Model):
    GroupID = models.OneToOneField(DiscussionGroup)
    PublishDate = models.DateTimeField()
    PublisherUserID = models.ForeignKey(User)
    #StaffUserID = models.ForeignKey(StaffProfile)
   # Comment = models.CharField(max_length=250)

    def __unicode__(self):
        return self.GroupID.GroupID

class Model(models.Model):
    ModelID = models.CharField(unique=True,max_length=30)
    CreateStaff = models.ForeignKey(User, related_name='+')
    Tag = models.CharField(max_length=100,null=True)
    Member = models.ManyToManyField(User, related_name='s+')

    def __unicode__(self):
        return self.ModelID

class ActivityDetails(models.Model):
    ModelID = models.OneToOneField(Model)
    PublishDate = models.DateTimeField()
    Comment = models.CharField(max_length=250)

    @property
    def __unicode__(self):
        return self.ModelID.ModelID

class AcceptRecord(models.Model):
    GroupID = models.ForeignKey(DiscussionGroup)
    UserID = models.ForeignKey(User)
    isAccept = models.BooleanField(default=False)
    isRefuse = models.BooleanField(default=False)



