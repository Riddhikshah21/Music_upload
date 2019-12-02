from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'music'

urlpatterns = [
    path('',views.MusicHome.as_view(),name='musichome'),
    #path('form/',views.MusicView.as_view(),name='musicdetail'),
    #path('form/',views.MusicView,name='musicdetail'),
    path('form/',views.MusicView,name='musicview'),
    path('detail/',views.MusicDetailList.as_view(),name='musicdetaillist'),
    path('artist/<int:pk>/',views.MusicArtistList,name='musicartist'),
    path('artist/music/<int:pk>/',views.ArtistDetail,name='artistdetail')
]
