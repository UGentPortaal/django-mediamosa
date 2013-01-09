from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from base import api


class AssetList(ListView):
    template_name = 'django_mediamosa/index.html'
    paginate_by = 10

    def get_queryset(self):
        asset_list = api.asset_list()
        return asset_list


class AssetDetails(DetailView):
    template_name = 'django_mediamosa/asset_detail.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        return api.asset(asset_id=pk)


class PlayMediaFile(DetailView):

    def get_object(self, queryset=None):
        # asset_id = self.request.GET.get('asset_id', '')
        mediafile_id = self.request.GET.get('mediafile_id', '')

        return api.mediafile(mediafile_id=mediafile_id)

    def render_to_response(self, context, **response_kwargs):
        output = self.object.play()
        return HttpResponse(output)
