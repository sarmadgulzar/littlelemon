from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"booking", views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuListCreateAPIView.as_view(), name="menu-list-create"),
    path("menu/<int:pk>/", views.MenuDetailAPIView.as_view(), name="menu-detail"),
    path("booking/", include(router.urls)),
]
