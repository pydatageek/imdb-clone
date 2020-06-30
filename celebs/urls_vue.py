from django.urls import include, path

from .views import CelebDetailView, CelebListView, DutyDetailView, DutyListView

base_dir = 'vue/'

urlpatterns = [
    path('duty', include([
        path('<slug:slug>/', DutyDetailView.as_view(
            template_name=base_dir + 'celebs/duty_detail.html'
        ), name='duty-detail'),
        path('', DutyListView.as_view(
            template_name=base_dir + 'celebs/duty_list.html'
        ), name='duty-list')
    ])),
    path('', include([
        path('<slug:slug>/', CelebDetailView.as_view(
            template_name=base_dir + 'celebs/celeb_detail.html'
        ), name='celeb-detail'),
        path('', CelebListView.as_view(
            template_name=base_dir + 'celebs/celeb_list.html'
        ), name='celeb-list')
    ])),
]
