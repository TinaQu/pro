from DiscussGroup.models import UserProfile,DiscussionGroup,MessageDetails,Model,ActivityDetails,AcceptRecord,User,ModelMember
from django.template import RequestContext
from django.shortcuts import render_to_response
from DiscussGroup.forms import UserForm, UserProfileForm,DiscussionGroupForm,ModelForm,ActivityDetailsform,\
    AcceptRecordForm,MessageDetailsForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
import datetime
from django.core.mail import send_mail
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
<<<<<<< HEAD
                #if userprofile1.isAdministrator==True:
                login(request, user)
                return HttpResponseRedirect('/DiscussGroup/Login/Index')
                #elif userprofile1.isStaff==True:
                #    login(request, user)
                  #  return HttpResponseRedirect('/DiscussGroup/Login/Index')
                #elif userprofile1.isStudent==True:
                #    login(request, user)
                  #  return HttpResponseRedirect('/DiscussGroup/Login/Index')
=======
                if userprofile1.isAdministrator==True:
                    login(request, user)
                    return HttpResponseRedirect('/DiscussGroup/Login/IndexAdministrator')
                elif userprofile1.isStaff==True:
                    login(request, user)
                    return HttpResponseRedirect('/DiscussGroup/Login/IndexStudent')
                elif userprofile1.isStudent==True:
                    login(request, user)
                    return HttpResponseRedirect('/DiscussGroup/Login/IndexStaff')
>>>>>>> 97bad6ee39054c2f8026e2d09af2703481ce9a83
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your forum account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.

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
def Index(request):
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
    return render_to_response('DiscussGroup/Index.html',{'DiscussionGroup1':DiscussionGroup1,'userProfile':userProfile}, context)
#####################################################################################################################33

#######################################################################################################################
<<<<<<< HEAD
=======
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
def IndexAdmin(request):
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
    return render_to_response('DiscussGroup/IndexAdministrator.html',{'DiscussionGroup1':DiscussionGroup1}, context)
#######################################################################################################################
>>>>>>> 97bad6ee39054c2f8026e2d09af2703481ce9a83
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
              # print(username1)
               user1=User.objects.get(username=username1)
               userProfile=UserProfile.objects.get(user=user1)
               #print(userProfile)
               DiscussionGroup.CreateUserId=userProfile
               DiscussionGroup.save()
#               if DiscussionGroup.DoesNotExist:
#                   return render_to_response('DiscussGroup/SuccessfulMessage.html',{}, context)


           except User.DoesNotExist:
               return addNewGroup(request)



           return render_to_response('DiscussGroup/SuccessfulMessage.html',{}, context)
        else:
            return render_to_response('DiscussGroup/FailMessage.html',{},)
          # return Index(request)
    else:
        form=DiscussionGroupForm()
        return render_to_response('DiscussGroup/addNewGroup.html',{'form':form,},context)

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



           return render_to_response('DiscussGroup/SuccessfulMessage.html',{}, context)
        else:
           return render_to_response('DiscussGroup/FailMessage.html',{},)
    else:
        form=ModelForm()
        return render_to_response('DiscussGroup/addNewModel.html',{'form':form},context)
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
    result_list2=[]

    result_list1=[]


    try:
        user1= User.objects.get(username=username1)
        userProfile = UserProfile.objects.get(user=user1)
        result_list1= Model.objects.filter(CreateStaff=userProfile)
        result_list2= ActivityDetails.objects.filter(ModelID=result_list1)

        #####################################
    except User.DoesNotExist:
        pass
    return render_to_response('DiscussGroup/ModelNow.html',{'result_list1': result_list1,'result_list2': result_list2},context)
####################################################################################################################
def studentModelNow(request):
    context = RequestContext(request)
    username1 = request.user.username
    result_list2=[]

    result_list1=[]
    result_list3=[]

    try:
        user1= User.objects.get(username=username1)
        userProfile = UserProfile.objects.get(user=user1)
        result_list3= ModelMember.objects.filter(Member=userProfile)
        result_list2= ActivityDetails.objects.filter(ModelID=result_list3)
        for model in result_list3:
              result_list1= Model.objects.filter(ModelID=model.ModelID)
        #####################################d
    except User.DoesNotExist:
        pass
    return render_to_response('DiscussGroup/studentModelNow.html',{'result_list3': result_list3,'result_list1': result_list1,'result_list2': result_list2},context)

####################################################################################################################
def AddModelActivity(request,offset):
    context=RequestContext(request)
    model=[]
    try:
         offset=int(offset)
    except ValueError:
          raise Http404()

    username1 = request.user.username
    user1= User.objects.filter(username =username1)

    userProfile = UserProfile.objects.get(user=user1)

    if request.method=='POST':
        form=ActivityDetailsform(request.POST)

        if form.is_valid():

           ActivityDetails=form.save(commit=False)

           try:
                    model= Model.objects.filter(id=offset)
                    for model1 in model:
                        ActivityDetails.ModelID=model1

                        ActivityDetails.save()
           except User.DoesNotExist:
               return AddModelActivity(request)
#           message=ActivityDetailsform.CommentAD
#           for useremail in user1:
#               fromemail=useremail.Email

#           send_mail('New Activity', message, fromemail ,['to@example.com'], fail_silently=False)
           return render_to_response('DiscussGroup/SuccessfulMessage3.html',{}, context)
        else:
           return Index(request)

<<<<<<< HEAD
=======
           return render_to_response('DiscussGroup/SuccessfulMessage2.html',{}, context)
        else:
           return IndexStaff(request)

>>>>>>> 97bad6ee39054c2f8026e2d09af2703481ce9a83
    else:

         form=ActivityDetailsform()



    return render_to_response('DiscussGroup/AddModelActivity.html',{'form':form},context)




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
def ShutDownGroup(request,offset):
     context = RequestContext(request)
     username1 = request.user.username
     user1= User.objects.get(username =username1)
     userProfile = UserProfile.objects.get(user=user1)
     acceptRecord1=[]
     try:
          offset=int(offset)
     except ValueError:
          raise Http404()
     try:
<<<<<<< HEAD
         acceptRecord1=AcceptRecord.objects.filter(id=offset)
         if acceptRecord1.none():
               DiscussionGroup.objects.filter(id=offset,CreateUserId=userProfile).delete()
               return render_to_response('DiscussGroup/SuccessfulShutDown.html',{},context)
         else:
               AcceptRecord.objects.filter(id=offset,isRefuse=False).delete()
               DiscussionGroup.objects.filter(id=offset,CreateUserId=userProfile).delete()
               return render_to_response('DiscussGroup/SuccessfulShutDown.html',{},context)

     except DiscussionGroup.DoesNotExist:
=======
         acceptRecord1=AcceptRecord.objects.get(id=offset)
         AcceptRecord.objects.filter(id=offset,isRefuse=False).delete()
         DiscussionGroup.objects.filter(id=offset,CreateUserId=userProfile).delete()
         return render_to_response('DiscussGroup/SuccessfulQuit.html',{},context)

     except AcceptRecord.DoesNotExist:
>>>>>>> 97bad6ee39054c2f8026e2d09af2703481ce9a83
      pass

      #return HttpResponseRedirect('/DiscussGroup/Login/user_GroupListNow')
     # return render_to_response('DiscussGroup/SuccessfulAccept.html',{'applyRecord': acceptRecord1},context)
      return render_to_response('DiscussGroup/SuccessfulShutDown.html',{},context)
##################################################################################################################################
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
         return render_to_response('DiscussGroup/SuccessfulAccept.html',{'applyRecord': acceptRecord1},context)
      except AcceptRecord.DoesNotExist:
          pass


########################################################################################################################
def History(request, offset):
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
    discussiongroup=DiscussionGroup.objects.filter(pk=offset)
    for discussiongroup1 in discussiongroup:
       if request.method == 'POST':
           username = request.POST['field1']
           type1 = request.POST['field2']
           if type1 == 'PublisherID':
               print("")
               user1=User.objects.get(username=username)
               userProfile=UserProfile.objects.filter(user=user1)

               result_list = MessageDetails.objects.filter(GroupID=discussiongroup1,PublisherUserID=userProfile)


    return render_to_response('DiscussGroup/SearchResult.html', {'result_list': result_list}, context)

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
           return Index(request)
    else:
        form=MessageDetailsForm()




    return render_to_response('DiscussGroup/ShowTopicmessage1.html',{
                                                                     'result_list2':result_list2,
                                                                     'result_list3':result_list3,
                                                                     'form':form

                                                                     },context )

#####################################################################################################################
######################################################################################################################3#
def quit(request,offset):
     context = RequestContext(request)
     username1 = request.user.username
     user1= User.objects.get(username =username1)
     userProfile = UserProfile.objects.get(user=user1)
     acceptRecord1=[]
     try:
          offset=int(offset)
     except ValueError:
          raise Http404()
     try:
         acceptRecord1=AcceptRecord.objects.get(id=offset)
         AcceptRecord.objects.filter(id=offset,isRefuse=False,UserID=userProfile).delete()
         return render_to_response('DiscussGroup/SuccessfulQuit.html',{},context)
     except AcceptRecord.DoesNotExist:
      print "Does not exist."

      #return HttpResponseRedirect('/DiscussGroup/Login/user_GroupListNow')
     # return render_to_response('DiscussGroup/SuccessfulAccept.html',{'applyRecord': acceptRecord1},context)
      return render_to_response('DiscussGroup/SuccessfulQuit.html',{},context)
########################################################################################################################
def ReIndex(request):
    context = RequestContext(request)
    username1 = request.user.username
    user1= User.objects.get(username =username1)
    userprofile1 = UserProfile.objects.get(user=user1)
    return HttpResponseRedirect('/DiscussGroup/Login/Index')




