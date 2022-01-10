from django.urls import path
from . import views

app_name = 'lettings'


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('lettings/', views.index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
    path('sentry-debug/', trigger_error),
]
