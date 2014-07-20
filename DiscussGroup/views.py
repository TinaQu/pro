from DiscussGroup.models import UserProfile,DiscussionGroup,MessageDetails,Model,ActivityDetails,AcceptRecord,User
from django.template import RequestContext
from django.shortcuts import render_to_response
from DiscussGroup.forms import UserForm, UserProfileForm,DiscussionGroupForm,ModelForm,ActivityDetails,\
    AcceptRecordForm,MessageDetailsForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
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
                    return HttpResponseRedirect('/admin')
                if userprofile1.isStudent==True:
                    login(request, user)
                    return HttpResponseRedirect('/DiscussGroup/Login/IndexStudent')
                if userprofile1.isStaff==True:
                    login(request, user)
                    return HttpResponseRedirect('/DiscussGroup/Login/IndexStaff')
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
        return render_to_response('DiscussGroup/log_in.html', {}, context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/DiscussGroup')

########################################################################################################################
def IndexStudent(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    username1=request.user.username
    user1=User.objects.get(username=username1)
    userProfile=UserProfile.objects.filter(user=user1)
    result_list = []
    DiscussionGroup1=[]
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    try:

        DiscussionGroup1 = list(DiscussionGroup.objects.filter().exclude(CreateUserId =userProfile))
       # DiscussionGroup2=list(DiscussionGroup1)
        print(DiscussionGroup1)
        result_list = AcceptRecord.objects.filter(UserID=userProfile)

        if result_list and DiscussionGroup1 and userProfile:
          for AcceptRecord1 in result_list:
            for discussiongroup1 in  DiscussionGroup1:
                for user2 in userProfile:
                   if user2.user == AcceptRecord1.UserID.user:
                       if discussiongroup1.GroupID == AcceptRecord1.GroupID.GroupID:

                            DiscussionGroup1.remove(discussiongroup1)
    except User.DoesNotExist:
        pass
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('DiscussGroup/IndexStudent.html',{'DiscussionGroup1':DiscussionGroup1}, context)
#####################################################################################################################33

#######################################################################################################################
def IndexStaff(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    username1=request.user.username
    user1=User.objects.get(username=username1)
    userProfile=UserProfile.objects.filter(user=user1)
    result_list = []
    DiscussionGroup1=[]
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    try:

        DiscussionGroup1 = list(DiscussionGroup.objects.filter().exclude(CreateUserId =userProfile))
       # DiscussionGroup2=list(DiscussionGroup1)
        print(DiscussionGroup1)
        result_list = AcceptRecord.objects.filter(UserID=userProfile)

        if result_list and DiscussionGroup1 and userProfile:
          for AcceptRecord1 in result_list:
            for discussiongroup1 in  DiscussionGroup1:
                for user2 in userProfile:
                   if user2.user == AcceptRecord1.UserID.user:
                       if discussiongroup1.GroupID == AcceptRecord1.GroupID.GroupID:

                            DiscussionGroup1.remove(discussiongroup1)
    except User.DoesNotExist:
        pass
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('DiscussGroup/IndexStaff.html',{'DiscussionGroup1':DiscussionGroup1}, context)
#######################################################################################################################
def userHome(request):
    return render_to_response(
        'DiscussGroup/Login/userHome.html',)
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



           return render_to_response('DiscussGroup/SuccessfulMessage.html',{}, context)
        else:
           return IndexStudent(request)
    else:
        form=DiscussionGroupForm()
        return render_to_response('DiscussGroup/addNewGroup.html',{'form':form},context)
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
               Model.CreateStaff=userProfile
               Model.save()
           except User.DoesNotExist:
               return addNewModel(request)



           return render_to_response('DiscussGroup/SuccessfulMessage3.html',{}, context)
        else:
           return IndexStaff(request)
    else:
        form=ModelForm()
        return render_to_response('DiscussGroup/addNewModel.html',{'form':form},context)
########################################################################################################################
########################################################################################################################
def user_GroupListNow(request):
    context = RequestContext(request)
    username1 = request.user.username

    result_list1=[]
    result_list2=[]
    result_list3=[]

    try:
        user1= User.objects.get(username=username1)
        userProfile = UserProfile.objects.get(user=user1)
        result_list1= DiscussionGroup.objects.filter(CreateUserId=userProfile)
        result_list2= AcceptRecord.objects.filter(isAccept=True,isRefuse=False,UserID=userProfile)

    except User.DoesNotExist:
        pass

    return render_to_response('DiscussGroup/user_GroupListNow.html',{'result_list1': result_list1,'result_list2':result_list2},context)

################################################################################################################
def ModelNow(request):
    context = RequestContext(request)
    username1 = request.user.username

    result_list1=[]


    try:
        user1= User.objects.get(username=username1)
        userProfile = UserProfile.objects.get(user=user1)
        result_list1= Model.objects.filter(CreateStaff=userProfile)

    except User.DoesNotExist:
        pass
    return render_to_response('DiscussGroup/ModelNow.html',{'result_list1': result_list1},context)

####################################################################################################################

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
          DiscussionGroup2=DiscussionGroup.objects.get(id=offset)
          AcceptRecord1=AcceptRecord.objects.filter(GroupID=DiscussionGroup2,isAccept=True,isRefuse=False)
          AcceptRecord2=AcceptRecord.objects.filter(GroupID=DiscussionGroup2,isAccept=False,isRefuse=True)
          AcceptRecord3=AcceptRecord.objects.filter(GroupID=DiscussionGroup2,isAccept=False,isRefuse=False)
      except DiscussionGroup.DoesNotExist:
          pass

      return render_to_response('DiscussGroup/dealGroupApply.html',{'AcceptRecord1': AcceptRecord1,'AcceptRecord2': AcceptRecord2,
                                                              'AcceptRecord3': AcceptRecord3,
                                                              'DiscussionGroup2': DiscussionGroup2},context)
####################################################################################################################################3
def acceptApply(request,offset):
      context = RequestContext(request)
      acceptRecord1=[]
      try:
          offset=int(offset)
      except ValueError:
          raise Http404()
      try:
         acceptRecord1=AcceptRecord.objects.get(id=offset)
         AcceptRecord.objects.filter(id=offset,isRefuse=False).update(isAccept=True)
      except AcceptRecord.DoesNotExist:
          pass
      return render_to_response('DiscussGroup/SuccessfulAccept.html',{'applyRecord': acceptRecord1},context)

########################################################################################################################
def HistoryMessage(request,offset):
    context = RequestContext(request)
    result_list = []
    discussiongroup=[]
    result_list1=[]
    try:
          offset=int(offset)
    except ValueError:
          raise Http404()
    discussiongroup=DiscussionGroup.objects.filter(id=offset)
    result_list=MessageDetails.objects.filter(GroupID=discussiongroup)[:10]
    return render_to_response('DiscussGroup/HistoryMessage.html', {'result_list': result_list}, context)


########################################################################################################################
def SearchMessage(request,offset):
    context = RequestContext(request)
    result_list = []
    try:
          offset=int(offset)
    except ValueError:
          raise Http404()
    discussiongroup=DiscussionGroup.objects.filter(id=offset)
    for discussiongroup1 in discussiongroup:
       if request.method == 'POST':
           search = request.POST['field1']
           type1 = request.POST['field2']
           if type1 == 'PublisherID':
               result_list = MessageDetails.objects.filter(GroupID=discussiongroup1.GroupID,PublisherUserID_icontains=search)


    return render_to_response('DiscussGroup/HistoryMessage.html', {'result_list': result_list}, context)

#########################################################################################################################
def user_Apply(request):
      context = RequestContext(request)

      if request.method == 'POST':
        username = request.user.username
        GroupID = request.POST['GroupID']
      try:
        user1= User.objects.get(username=username)
        userProfile = UserProfile.objects.get(user=user1)
        DiscussionGroup1 = DiscussionGroup.objects.get(GroupID=GroupID)
        p =AcceptRecord(UserID=userProfile,GroupID=DiscussionGroup1)
        p.save()

        return render_to_response('DiscussGroup/SuccessfulApply.html',{}, context)
      except DiscussionGroup.DoesNotExist:
        return render_to_response('DiscussGroup/ErrorApply.html',{}, context)
#########################################################################################################################3
def GroupCharting(request,offset):
    context =RequestContext(request)

#    result_list1=[]

    #Grouresult_list1=[]pID1=request.DiscussionGroup.GroupID
    try:
          offset=int(offset)
    except ValueError:
          raise Http404()

    username1=request.user.username
    print(username1)


    user1=User.objects.filter(username=username1)
    userProfile=UserProfile.objects.filter(user=user1)
    print(userProfile)
#               DiscussionGroup1= DiscussionGroup.objects.get(GroupID=result_list1)
    result_list2= DiscussionGroup.objects.filter(id=offset)
#    print (result_list2+"@@@@@@@@@")

    if request.method=='POST':
        form=MessageDetailsForm(request.POST)

        if form.is_valid():

           MessageDetails=form.save(commit=False)
           try:
               MessageDetails.PublisherUserID=userProfile
               MessageDetails.GroupID=result_list2
               MessageDetails.save()
           except User.DoesNotExist:
               return GroupCharting(request)



           return render_to_response('DiscussGroup/SuccessfulMessage2..html',{}, context)
        else:
           return render_to_response('DiscussGroup/SuccessfulMessage2..html',{}, context)
    else:
        form=MessageDetailsForm()
        print("##############")
        return render_to_response('DiscussGroup/GroupCharting.html',{'form':form},context)
################################################################################################################
def AddGroupCharting(request):
    context = RequestContext(request)
    username= request.user.username
    user1= User.objects.get(username=username)
    if request.method == 'POST':

         GroupID = request.POST['GroupID']
    try:

        userProfile = UserProfile.objects.get(user=user1)
        DiscussionGroup1 = DiscussionGroup.objects.get(GroupID=GroupID)
        p =MessageDetails(PublisherUserID=userProfile,GroupID=DiscussionGroup1)
        p.save()
        return  render_to_response('DiscussGroup/GroupCharting.html',{},context)

    except DiscussionGroup.DoesNotExist:
        return render_to_response('DiscussGroup/ErrorApply.html',{}, context)

####################################################################################################################

def ShowTopicmessage(request,offset):
    context = RequestContext(request)
    username1 = request.user.username

    result_list1=[]
    result_list2=[]
    result_list3=[]
    try:
          offset=int(offset)
    except ValueError:
          raise Http404()

    try:
        user1= User.objects.get(username =username1)
        userProfile = UserProfile.objects.get(user=user1)
        result_list2= DiscussionGroup.objects.filter(id=offset)
        result_list1= MessageDetails.objects.filter(GroupID=result_list2)
        result_list3=AcceptRecord.objects.filter(isAccept=True,isRefuse=False,GroupID=result_list2)




    except User.DoesNotExist:
     pass


    return render_to_response('DiscussGroup/ShowTopicmessage.html',{'result_list1': result_list1,
                                                                     'result_list2':result_list2,
                                                                     'result_list3':result_list3
                                                                      },context)

##########################################################################################################################3
def SuccessfulMessage2(offset):
    result_list2=[]
    try:
          offset=int(offset)
    except ValueError:
          raise Http404()
    try:
        result_list2= DiscussionGroup.objects.filter(id=offset)

    except User.DoesNotExist:
     pass
    return render_to_response('DiscussGroup/SuccessfulMessage2.html',{'result_list2':result_list2},offset)
#######################################################################################################################
def SuccessfulMessage3(request):
    context =RequestContext(request)

#    result_list1=[]

    #Grouresult_list1=[]pID1=request.DiscussionGroup.GroupID


    username1=request.user.username
    print(username1)


    user1=User.objects.filter(username=username1)
    userProfile=UserProfile.objects.filter(user=user1)
    print(userProfile)
#               DiscussionGroup1= DiscussionGroup.objects.get(GroupID=result_list1)

#    print (result_list2+"@@@@@@@@@")

    if request.method=='POST':
        form=MessageDetailsForm(request.POST)

        if form.is_valid():

           MessageDetails=form.save(commit=False)
           try:
               MessageDetails.PublisherUserID=userProfile
               MessageDetails.save()
           except User.DoesNotExist:
               return GroupCharting(request)



           return render_to_response('DiscussGroup/SuccessfulMessage2..html',{}, context)
        else:
           return render_to_response('DiscussGroup/ErrorApply..html',{}, context)
    else:
        form=MessageDetailsForm()
        print("##############")
        return render_to_response('DiscussGroup/GroupCharting.html',{'form':form},context)
#####################################################################################################
def ShowTopicmessage1(request,offset):
    context = RequestContext(request)

    username1 = request.user.username
    user1= User.objects.get(username =username1)
    userProfile = UserProfile.objects.get(user=user1)

#    result_list1=[]
    result_list2=[]
#    result_list3=[]
    try:
          offset=int(offset)
    except ValueError:
          raise Http404()


    try:
        result_list2= DiscussionGroup.objects.filter(id=offset)
        print(result_list2)
#           result_list1= MessageDetails.objects.filter(GroupID=result_list2)
        result_list3=AcceptRecord.objects.filter(isAccept=True,isRefuse=False,GroupID=result_list2)
#

    except User.DoesNotExist:
     pass






   # discussiongroup1=DiscussionGroup.objects.get(GroupID=result_list2)

    if request.method=='POST':
        form=MessageDetailsForm(request.POST)

        if form.is_valid():

           MessageDetails=form.save(commit=False)

           try:
                    MessageDetails.PublisherUserID=userProfile
                    for DiscussionGroup1 in result_list2:
                      MessageDetails.GroupID=DiscussionGroup1
                      MessageDetails.save()
           except User.DoesNotExist:
               return addNewGroup(request)



           return render_to_response('DiscussGroup/SuccessfulMessage2.html',{}, context)
        else:
           return IndexStudent(request)
    else:
        form=MessageDetailsForm()




    return render_to_response('DiscussGroup/ShowTopicmessage1.html',{
                                                                     'result_list2':result_list2,
                                                                     'result_list3':result_list3,
                                                                     'form':form

                                                                     },context )

#####################################################################################################################
def dealQuit(request,offset):
    context = RequestContext(request)

    username1 = request.user.username
    user1= User.objects.get(username =username1)
    userProfile = UserProfile.objects.get(user=user1)

#    result_list1=[]
    result_list2=[]
#    result_list3=[]
    try:
          offset=int(offset)
    except ValueError:
          raise Http404()


    try:
        result_list2= DiscussionGroup.objects.filter(id=offset)
        print(result_list2)
#           result_list1= MessageDetails.objects.filter(GroupID=result_list2)
        result_list3=AcceptRecord.objects.filter(isAccept=True,isRefuse=False,GroupID=result_list2)
#

    except User.DoesNotExist:
     pass

    return render_to_response('DiscussGroup/dealQuit.html',{'result_list2': result_list2},context)

######################################################################################################################3#
def quit(request,offset):
     context = RequestContext(request)
     acceptRecord1=[]
     try:
          offset=int(offset)
     except ValueError:
          raise Http404()
     try:
         acceptRecord1=AcceptRecord.objects.get(id=offset)
         AcceptRecord.objects.filter(id=offset,isRefuse=False).update(isAccept=False)
     except AcceptRecord.DoesNotExist:
      pass

      return render_to_response('DiscussGroup/SuccessfulQuit.html',{'applyRecord': acceptRecord1},context_instance = RequestContext(request))
########################################################################################################################3