from django.conf.urls.defaults import url, patterns

from views import AssetList, AssetDetails, PlayMediaFile,\
    TinyMceAssetSelectionDialog

urlpatterns = patterns('',

    url(r'^/assets/$', AssetList.as_view(),
        name='asset-list'),

    url(r'^/assets/(?P<pk>\w+)/$', AssetDetails.as_view(),
        name='asset-details'),

    url(r'^/assets/(?P<asset_id>\w+)/mediafiles/(?P<pk>\w+)/play/$',
        PlayMediaFile.as_view(),
        name='mediafile-play'),

    # TinyMCE dialogs

    url(r'^/tinymce/assets/$', TinyMceAssetSelectionDialog.as_view(),
        name='tinymce-asset-select'),

)
