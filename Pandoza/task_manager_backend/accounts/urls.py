from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import Logout, EmployeeView, AccountsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('employees', EmployeeView,  basename='employees_api')
router.register('manage', AccountsView,  basename='manage')

urlpatterns = [
    path('login/',TokenObtainPairView.as_view(),name='access_token'),
    path('logout/',Logout.as_view(),name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include(router.urls))
]
