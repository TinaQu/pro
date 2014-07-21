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
    CreateUserId = models.ForeignKey(UserProfile)
    Tag = models.CharField(max_length=100)

    #StudentMember = models.ManyToManyField(StudentProfile)
    #StaffMember = models.ManyToManyField(StaffProfile)

    def __unicode__(self):
        return self.GroupID



class MessageDetails(models.Model):
    GroupID = models.ForeignKey(DiscussionGroup)
    PublishDate = models.DateTimeField(auto_now_add=True)
    PublisherUserID = models.ForeignKey(UserProfile)
    #StaffUserID = models.ForeignKey(StaffProfile)
    CommentMDF = models.CharField(max_length=250)

    def __unicode__(self):
        return self.GroupID.GroupID

class Model(models.Model):
    ModelID = models.CharField(unique=True,max_length=30)
    CreateStaff = models.ForeignKey(UserProfile)
    Tag = models.CharField(max_length=100,null=True)

    def __unicode__(self):
        return self.ModelID

class ModelMember(models.Model):
    ModelID= models.ForeignKey(Model)
    Member = models.ForeignKey(User)

    def __unicode__(self):
        return self.ID

class ActivityDetails(models.Model):
    ModelID = models.ForeignKey(Model)
    PublishDate = models.DateTimeField(auto_now_add=True)
    CommentAD = models.CharField(max_length=250)


    def __unicode__(self):
        return self.ModelID.ModelID

class AcceptRecord(models.Model):
    GroupID = models.ForeignKey(DiscussionGroup)
    UserID = models.ForeignKey(UserProfile)
    isAccept = models.BooleanField(default=False)
    isRefuse = models.BooleanField(default=False)



