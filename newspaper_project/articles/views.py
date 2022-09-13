from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import CommentCreateForm


# Create your views here.
@login_required
def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)     # get the article using the `primary_key`
    if request.method == 'POST':        # if the comment form is submitted i.e POST request
        form = CommentCreateForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)       # save the form but not commited in order to set the article and the user field
            comment.article = article
            comment.author = request.user
            comment.save()      # finally save the comment
        return redirect('article_detail', pk=pk)        # redirect the user to the detail page of the article after successfully saving the form
    else:       # if the request is not POST
        form = CommentCreateForm()      # create and empty form to be sent to be rendered to
    return render(request, 'article_detail.html', {'form': form, 'article': article})


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "article_list"
    login_url = "login"
    fields = ('comment',)


# class ArticleDetailView(LoginRequiredMixin, DetailView, CreateView):
    # model = Article
    # template_name = "article_detail.html"
    # context_object_name = "article"
    # login_url = "login"

    # def post(self, request):
        # self.model = Comment
        # return super().post(request)

    # def form_valid(self, form):
        # form.instance.author = self.request.user
        # form.instance.article = self.request.article
        # return super().form_valid(form)
    

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ("title", "body")
    template_name = "article_edit.html"
    login_url = "login"

    def test_func(self):
        # returns True if the author of the article is the same as the current user
        return self.get_object().author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    login_url = "login"

    def test_func(self):
        # returns True if the author of the article is the same as the current user
        return self.get_object().author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
