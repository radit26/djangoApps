from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	#return HttpResponse('<h1>Student IT Services - Home</h1>')
	#return render(request, 'itreporting/home.html')
	return render(request, 'itreporting/home.html', {'title': 'Home'})

def about(request):
	#return HttpResponse('<h1>Student IT Services - About')
	return render(request, 'itreporting/about.html', {'title': 'About Us'})

def contact(request):
	#return HttpResponse('<h1>Student IT Services - Contact Us')
	return render(request, 'itreporting/contact.html', {'title': 'Contact'})

def report(request):
	#return HttpResponse('<h1>Student IT Services - Contact Us')
	daily_report = {
		#'issues': issues
		'issues': Issue.objects.all()
	}
	return render(request, 'itreporting/report.html', daily_report)

class PostListView(ListView):
	model = Issue
	template_name = 'itreporting/report.html'
	context_object_name = 'issues'
	ordering = ['-date_submitted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Issue
	template_name = 'itreporting/user_issues.html'
	context_object_name = 'issues'
	paginate_by = 5
	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return Issue.objects.filter(author = user).order_by('-date_submitted')

class PostDetailView(DetailView):
	model = Issue

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Issue
	fields = ['type', 'room', 'details']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Issue
	fields = ['type', 'room', 'details']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		issue = self.get_object()
		if self.request.user == issue.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Issue
	success_url = '/report'
	def test_func(self):
		issue = self.get_object()
		if self.request.user == issue.author:
			return True
		return False
