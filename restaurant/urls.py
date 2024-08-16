from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"booking", views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuListCreateAPIView.as_view(), name="menu-list-create"),
    path("menu/<int:pk>/", views.MenuDetailAPIView.as_view(), name="menu-detail"),
    path("", include(router.urls)),
    path("api-token-auth/", obtain_auth_token),
]
