

from DiscussGroup.models import UserProfile,DiscussionGroup,MessageDetails,Model,ActivityDetails,AcceptRecord,User
from django.template import RequestContext
from django.shortcuts import render_to_response
from DiscussGroup.forms import UserForm, UserProfileForm,DiscussionGroupForm,ModelForm,ActivityDetails,\
    AcceptRecordForm,MessageDetailsForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
########################################################################################################################
def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                user1= User.objects.get(username=username)
                userprofile1 = UserProfile.objects.get(user=user1)
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                if userprofile1.isAdministrator==True:
                    login(request, user)
                    return HttpResponseRedirect('/admin/')
                if userprofile1.isStudent==True:
                    login(request, user)
                    return HttpResponseRedirect('/DiscussGroup/Login/indexStudent')
                if userprofile1.isStaff==True:
                    login(request, user)
                    return HttpResponseRedirect('/DiscussGroup/Login/indexStaff')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your forum account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('DiscussionGroup/log_in.html', {}, context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/DiscussionGroup')

########################################################################################################################
def IndexStudent(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict = {}


    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    try:
        DiscussionGroup1 = DiscussionGroup.objects.all()

    except DiscussionGroup1.DoesNotExist:
        pass
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('DiscussGroup/Login/IndexStudent.html', context_dict, context)
#####################################################################################################################33

#######################################################################################################################
def IndexStafft(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    context_dict = {}


    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    try:
        DiscussionGroup1 = DiscussionGroup.objects.order_by('-GroupID')

    except DiscussionGroup1.DoesNotExist:
        pass
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('DiscussionGroup/Login/indexStaff.html', context_dict, context)
#######################################################################################################################
def userHome(request):
    return render_to_response(
        'DiscussionGroup/Login/userHome.html',)
##########################################################################################################################
def addNewGroup(request):
    context =RequestContext(request)
    if request.method=='POST':
        form=DiscussionGroupForm(request.POST)

        if form.is_valid():

           DiscussionGroup=form.save(commit=False)
           try:
               username1=request.user.username
               print(username1)
               user1=User.objects.get(username=username1)
               userProfile=UserProfile.objects.get(user=user1)
               print(userProfile)
               DiscussionGroup.CreateUserId=userProfile
               DiscussionGroup.save()
           except User.DoesNotExist:
               return addNewGroup(request)



           return IndexStudent(request)
        else:
           return IndexStudent(request)
    else:
        form=DiscussionGroupForm()
        return render_to_response('DiscussionGroup/Login/addNewGroup.html',{'form':form},context)
#########################################################################################################################
def addNewModel(request):
    context =RequestContext(request)
    if request.method=='POST':
        form=ModelForm(request.POST)

        if form.is_valid():

           Model=form.save(commit=False)
           try:
               username1=request.user.username
               print(username1)
               user1=User.objects.get(username=username1)
               userProfile=UserProfile.objects.get(user=user1)
               print(userProfile)
               Model.CreateUserId=userProfile
               Model.save()
           except User.DoesNotExist:
               return addNewModel(request)



           return IndexStafft(request)
        else:
           return IndexStafft(request)
    else:
        form=ModelForm()
        return render_to_response('DiscussionGroup/Login/addNewModel.html',{'form':form},context)
##########################################################################################################################
def apply_new_group(request,offset):
      context = RequestContext(request)
      try:
          offset=int(offset)
      except ValueError:
          raise Http404()
      try:
           result_list=DiscussionGroup.objects.get(pk=offset)
           UserId = User.objects.get(username=result_list.userId).UserId
          # SecondName = User.objects.get(username=result_list.userId).last_name
      except DiscussionGroup.DoesNotExist:
           pass

      return render_to_response('DiscussionGroup/Login/apply_new_group.html', {'result_list': result_list,'UserId': UserId,}, context)
#########################################################################################################################################
def user_GroupListNow(request):
    context = RequestContext(request)
    username1 = request.user.username
    result_list1=[]

    try:
        user1= User.objects.get(username=username1)
        userProfile = UserProfile.objects.get(user=user1)
        result_list1= DiscussionGroup.objects.filter(userId=userProfile)


    except User.DoesNotExist:
        pass
    return render_to_response('DiscussionGroup/Login/user_GroupListNow.html',{'result_list1': result_list1},context)

################################################################################################################
#############????????????????????????????????????????????#############
################################################################################################################
def addGroupCharting(request):
    context =RequestContext(request)
    if request.method=='POST':
        form=MessageDetailsForm(request.POST)

        if form.is_valid():

           MessageDetails=form.save(commit=False)
           try:
               username1=request.user.username

               print(username1)
               user1=User.objects.get(username=username1)
               userProfile=UserProfile.objects.get(user=user1)
              # group1 = DiscussionGroup.objects.get(group1= GroupID)
               print(userProfile)
               MessageDetails.PublisherUserID=userProfile
               MessageDetails.save()
           except User.DoesNotExist:
               return addGroupCharting(request)



           return IndexStudent(request)
        else:
           return IndexStudent(request)
    else:
        form=MessageDetailsForm()
        return render_to_response('DiscussionGroup/Login/enterGroup.html',{'form':form},context)
################################################################################################################

def dealGroupApply(request,offset):
      context = RequestContext(request)
      AcceptRecord1=[]
      AcceptRecord2=[]
      AcceptRecord3=[]
      DiscussionGroup2=[]
      try:
          offset=int(offset)
      except ValueError:
          raise Http404()
      try:
          experiment1=DiscussionGroup.objects.get(id=offset)
          AcceptRecord1=AcceptRecord.objects.filter(GroupID=DiscussionGroup2,isAccept=True,isRefuse=False)
          AcceptRecord2=AcceptRecord.objects.filter(GroupID=DiscussionGroup2,isAccept=False,isRefuse=True)
          AcceptRecord3=AcceptRecord.objects.filter(GroupID=DiscussionGroup2,isAccept=False,isRefuse=False)
      except DiscussionGroup.DoesNotExist:
          pass

      return render_to_response('dragon/dealExperiment.html',{'AcceptRecord1': AcceptRecord1,'AcceptRecord2': AcceptRecord2,
                                                              'AcceptRecord3': AcceptRecord3,
                                                              'DiscussionGroup2': DiscussionGroup2},context)
########################################################################################################################
#def MessageSearch(request):
#    context = RequestContext(request)
#    result_list = []
#    if request.method == 'POST':
#        search = request.POST['field1']
#        type1 = request.POST['field2']
#        if type1 == 'PublishID':
#            result_list = MessageDetails.objects.filter(title__icontains=search).order_by(
#                '-payment')[:5]
#        elif type1 == 'StartTime':
#            result_list = Experiment.objects.filter(isOverdue=True,title__icontains=search).order_by(
#                '-startTime')[:5]
#        elif type1 == 'EndTime':
#            result_list = Experiment.objects.filter(isOverdue=True, title__icontains=search).order_by(
#                '-endTime').reverse()[:5]
#
#    return render_to_response('dragon/search.html', {'result_list': result_list}, context)
#
########################################################################################################################