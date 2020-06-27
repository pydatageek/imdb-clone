from django.urls import include, path

from .views import CelebDetail, CelebList, DutyDetail, DutyList

base_dir = 'html/lte/'

urlpatterns = [
    path('duty', include([
        path('<slug:slug>/', DutyDetail.as_view(
            template_name=base_dir + 'celebs/duty_detail.html'
        ), name='duty-detail'),
        path('', DutyList.as_view(
            template_name=base_dir + 'celebs/duty_list.html'
        ), name='duty-list')
    ])),
    path('', include([
        path('<slug:slug>/', CelebDetail.as_view(
            template_name=base_dir + 'celebs/celeb_detail.html'
        ), name='celeb-detail'),
        path('', CelebList.as_view(
            template_name=base_dir + 'celebs/celeb_list.html'
        ), name='celeb-list')
    ])),
]
