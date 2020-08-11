from django.db.models import Q
from django.shortcuts import render
from django_datatables_view.base_datatable_view import BaseDatatableView

from app.models import SocialUserSearch


def home_page(request):
    return render(request, 'pages/home.html')


class RecentSocialRunList(BaseDatatableView):
    model = SocialUserSearch
    columns = ['username', 'created_at', 'search_status',  'id']
    order_columns =['username', 'created_at', 'search_status',  'id']

    def filter_queryset(self, qs):

        qs = SocialUserSearch.objects.all().values('username', 'created_at', 'search_status',  'id').order_by(
            'id')
        #
        # sSearch = self.request.GET.get('sSearch', None)
        # if sSearch:
        #     qs = qs.filter(
        #         Q(user=sSearch) |
        #         Q(tester_name__icontains=sSearch) |
        #         Q(dataset_id__dataset_name__icontains=sSearch) |
        #         Q(run_status__icontains=sSearch) |
        #         Q(id__icontains=sSearch) |
        #         Q(start_time__icontains=sSearch)
        #     )
        return qs
