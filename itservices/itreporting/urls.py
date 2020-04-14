from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
	path('', views.home, name='itreporting-home'),
	path('about/', views.about, name='itreporting-about'),
	path('contact/', views.contact, name='itreporting-contact'),
	# path('report/', views.report, name='itreporting-report'),
	path('report/', PostListView.as_view(), name='itreporting-report'),
	path('issue/<int:pk>', PostDetailView.as_view(), name='issue-detail'),
	path('issue/new/', PostCreateView.as_view(), name='issue-create'),
	path('issue/<int:pk>/update/', PostUpdateView.as_view(), name='issue-update'),
	path('issue/<int:pk>/delete/', PostDeleteView.as_view(), name='issue-delete'),
	path('user/<str:username>', UserPostListView.as_view(), name='user-issues'),
]