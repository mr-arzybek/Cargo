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
    path('group-track-codes/', views.GroupTrackCodeAddView.as_view(), name='group-track-code-add'),
    path('group-track-codes/delete/<int:id>/', views.GroupTrackCodeDeleteApiView.as_view(),
         name='group-track-code-delete'),
    path('group-track-codes/update/<int:id>/', views.GroupTrackCodeUpdateApiView.as_view(),
         name='group-track-code-update'),
    path('group-track-codes/<int:id>/', views.GroupTrackCodeGetApiView.as_view(), name='group-track-code-get'),
    path('status/create/', views.StatusListCreateView.as_view(), name='status-list-create'),
    path('status/delete/<int:id>/', views.StatusDelete.as_view(), name='status-delete'),

]
