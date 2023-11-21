from django.urls import path

from api.cargo_app import views

urlpatterns = [
    path('trackcode/create/', views.TrackCodeCreate.as_view(), name='create TrackCode'),
    path('trackcode/get/all/', views.TrackCodeList.as_view(), name='create TrackCode'),
    path('trackcode/get/<int:id>/', views.TrackCodeGet.as_view(), name='get TrackCode'),
    path('trackcode/update/<int:id>/', views.TrackCodeUpdate.as_view(), name='update TrackCode'),
    path('trackcode/delete/<int:id>/', views.TrackCodeDelete.as_view(), name='delete TrackCode'),
    path('status/delete/<int:id>/', views.StatusDelete.as_view(), name='delete status'),
    path('status/list/', views.StatusList.as_view(), name='List Status'),
    path('check/trackcode/', views.CheckTrackCodeView.as_view(), name='check TrackCode'),
    path('group/add/trackcode/', views.GroupTrackCodeAddView.as_view(), name='Add TrackCode'),
    path('group/delete/trackode/', views.GroupTrackCodeDeleteApiView.as_view(), name='Delete TrackCode'),
    path('group/all/', views.GroupTrackCodeGetApiView.as_view(), name='Get TrackCode'),
    path('group/put/trackcode/', views.GroupTrackCodePutApiView.as_view(), name='Put TrackCode'),
]
