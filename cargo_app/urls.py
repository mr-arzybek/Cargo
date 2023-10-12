from django.urls import path

from cargo_app import views

urlpatterns = [
    path('trackcode/create/', views.TrackCodeCreate.as_view(), name='create TrackCode'),
    path('trackcode/get/all/', views.TrackCodeList.as_view(), name='create TrackCode'),
    path('trackcode/get/<int:id>/', views.TrackCodeGet.as_view(), name='get TrackCode'),
    path('trackcode/update/<int:id>/', views.TrackCodeUpdate.as_view(), name='update TrackCode'),
    path('trackcode/delete/<int:id>/', views.TrackCodeDelete.as_view(), name='delete TrackCode')

]
