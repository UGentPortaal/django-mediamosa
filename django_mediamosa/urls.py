from django.conf.urls.defaults import url, patterns

from views import AssetList, AssetDetails, PlayMediaFile

urlpatterns = patterns('',

    url(r'^/assets/$', AssetList.as_view(),
        name='asset-list'),

    url(r'^/assets/(?P<pk>\w+)/$', AssetDetails.as_view(),
        name='asset-details'),

    url(r'^/play/$',
        PlayMediaFile.as_view(),
        name='mediafile-play'),

)
