from django.conf.urls import url

from views import AssetList, AssetDetails, PlayMediaFile

urlpatterns = [

    url(r'^assets/$', AssetList.as_view(),
        name='asset-list'),

    url(r'^assets/(?P<pk>\w+)/$', AssetDetails.as_view(),
        name='asset-details'),

    url(r'^play/$',
        PlayMediaFile.as_view(),
        name='mediafile-play'),

]
