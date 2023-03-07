"""MyInsurance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyInsurance import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myhome),
    path('mysignup/',views.mysignup),
    path('custlogin/',views.custlogin),
    path('adminlogin/',views.adminlogin),
    path('contact/',views.contact),
    path('logout/',views.logout),
    path('leftpanel/',views.leftpanel),
    path('adminleftpanel/',views.adminleftpanel),
    path('viewcust/',views.viewcust),
    path('custupdate/',views.custupdate),
    path('custpendingpolicy/',views.custpendingpolicy),
    path('mycustupdate/',views.mycustupdate),
    path('custdelete/',views.custdelete),
    path('mycategary/',views.mycategary),
    path('addcat/',views.addcat),
    path('viewcat/',views.viewcat),
    path('catupdate/',views.catupdate),
    path('mycatupdate/',views.mycatupdate),
    path('delcat/',views.delcat),
    path('policydash/',views.policydash),
    path('addpolicy/',views.addpolicy),
    path('viewupdatepolicy/',views.viewupdatepolicy),
    path('updatepolicy/',views.updatepolicy),
    path('delpolicy/',views.delpolicy),
    path('viewpolicy/',views.viewpolicy),
    path('custviewpolicy/',views.custviewpolicy),
    path('applypolicy/',views.applypolicy),
    path('applypolicysave/',views.applypolicysave),
    path('askquestion/',views.askquestion),
    path('historypolicy/',views.historypolicy),
    path('adminviewpolicy/',views.adminviewpolicy),
    path('adminviewpolicyupdate/',views.adminviewpolicyupdate),
    path('adminapporvedpolicy/',views.adminapporvedpolicy),
    path('adminrejectedpolicy/',views.adminrejectedpolicy),
    path('adminpendingpolicy/',views.adminpendingpolicy),
    path('adminquestion/',views.adminquestion),
    path('adminquestionupdate/',views.adminquestionupdate),
    path('adminreplay/',views.adminreplay),
    path('custviewcat/',views.custviewcat),

]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

