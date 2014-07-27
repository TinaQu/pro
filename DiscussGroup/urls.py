from django.conf.urls import patterns, url
from DiscussGroup import views


urlpatterns = patterns('',
        url(r'^$', views.user_login, name='log_in'),

 #       url(r'^Login/IndexStudent', views.IndexStudent, name='IndexStudent'),
        url(r'^Login/addNewGroup/$', views.addNewGroup, name='addNewGroup'),
        url(r'^Login/Index', views.Index, name='Index'),
 #       url(r'^Login/IndexAdministrator', views.IndexAdmin, name='IndexAdministrator'),
        url(r'^Login/ReturnIndex', views.ReIndex, name='ReturnIndex'),
        url(r'^Login/addNewModel/$', views.addNewModel, name='addNewGroup'),
        url(r'^Login/user_GroupListNow/$', views.user_GroupListNow, name='user_GroupListNow'),
        url(r'^Login/user_GroupListNow/ShowTopicmessage/(\d{1,4})', views.ShowTopicmessage1, name='ShowTopicmessage1'),
        url(r'^Login/user_GroupListNow/Quit/(\d{1,4})', views.quit, name='quit'),
        url(r'^Login/user_GroupListNow/Delete/(\d{1,4})', views.ShutDownGroup, name='ShutDownGroup'),
        url(r'^Login/user_GroupListNow/GroupCharting/$', views.AddGroupCharting, name='AddGroupCharting'),
        url(r'^Login/user_GroupListNow/HistoryMessasge/(\d{1,4})/$', views.History, name='HistoryMessage'),
        url(r'^Login/user_GroupListNow/search/(\d{1,4})',views.SearchMessage,name='SearchMessage'),
#        url(r'^Login/user_GroupListNow/GroupCharting/SuccessfulMessage', views.SuccessfulMessage3, name='SuccessfulMessage3'),
        url(r'^Login/apply', views.user_Apply, name='user_Apply'),
        url(r'^Login/offer/(\d{1,4})/$',views.acceptApply,name='acceptApply'),
        url(r'^Login/user_GroupListNow/Management/(\d{1,4})',views.dealGroupApply,name='dealGroupApply'),
        url(r'^Login/ModelNow/$', views.ModelNow, name='ModelNow'),
        url(r'^Login/ModelNow/AddActivity/(\d{1,4})', views.AddModelActivity, name='AddModelActivity'),
        url(r'^Login/StudentModelNow', views.studentModelNow, name='studentModelNow')
        

         )
