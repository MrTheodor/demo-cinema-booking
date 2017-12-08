from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'get_screening/(?P<screening_id>[0-9]+)/$', views.get_screening),
    url(r'history/$', views.get_history, name='history'),
    url(r'^api/', include(router.urls)),
]