from django import forms
from DiscussGroup.models import UserProfile
from DiscussGroup.models import DiscussionGroup, MessageDetails, \
    Model, ActivityDetails, AcceptRecord
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password','first_name','last_name')


class UserProfileForm(forms.ModelForm):
    Department = forms.CharField(max_length=100,required=False)
    StartTime = forms.DateField(help_text='The start date')
    EndTime = forms.DateField(help_text='The end date')
    isStudent = forms.BooleanField()
    isStaff = forms.BooleanField()
    isAdministrator = forms.BooleanField()
    class Meta:
        model = UserProfile
        fields = ('Department','StartTime','EndTime','isStudent','isStaff','isAdministrator')

class DiscussionGroupForm(forms.ModelForm):
    GroupID = forms.CharField(max_length=100,help_text='Please enter a group name')
    Tag = forms.CharField(max_length=100,help_text='Please add some tags to the group')

    class Meta:
        model = DiscussionGroup
        fields = ('GroupID','Tag')

class MessageDetailsForm(forms.ModelForm):
    Comment = forms.CharField(max_length=250,help_text='The max length is 250')

    class Meta:
        model = MessageDetails
        fields = ('Comment')

class ModelForm(forms.ModelForm):
    ModelID = forms.CharField(max_length=50)
    Tag = forms.CharField(max_length=250)

    class Meta:
        model = Model
        fields = ('ModelID','Tag')


class ActivityDetails(forms.ModelForm):
    Comment = forms.CharField(max_length=250)

    class Meta:
        model = ActivityDetails
        fields =( 'Comment' )

class AcceptRecordForm(forms.ModelForm):
    class Meta:
        model = AcceptRecord
        fields = ('GroupID','UserID','isAccept','isRefuse')







