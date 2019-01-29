from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from jobs import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('results/', views.ContractListView.as_view(), name='results'),
    path('create/new/', views.ContractCreateView.as_view(), name='contact-create'),
    path('contract/<int:pk>/update/', views.ContractUpdateView.as_view(), name='contract-update'),
    path('contract/<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract-delete'),
    path('contract/<int:pk>/', views.ContractDetailView.as_view(), name='contract-detail'),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name = "users/login.html"), name="login",),
    path('logout/', auth_views.LogoutView.as_view(template_name = "users/logout.html"), name="logout"),
]
