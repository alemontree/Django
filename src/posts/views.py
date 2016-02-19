from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post


def post_create(request):
  form = PostForm(request.POST or None)
  if form.is_valid():
    instance = form.save(commit=False)
    print form.cleaned_data.get("title")
    instance.save()


  # if request.method == "POST":
  #   print request.POST.get("content")
  #   print request.POST.get("title")
  #   #Post.objects.create(title=title)

  context = {
    "form": form,
  }

  return render(request, "post_form.html", context)

def post_detail(request, id):
  #instance = Post.objects.get(id=10)
  instance = get_object_or_404(Post, id=id);
  context = {
    "title": instance.title,
    "instance": instance
  }
  return render(request, "post_form.html", context)

def post_list(request):
  queryset = Post.objects.all()
  if request.user.is_authenticated():
    context = {
      "object_list": queryset,
      "title": "My User List"
    }
  else:
    context = {
      "title": "List"
    }

  return render(request, "index.html", context)
  # return HttpResponse("<h1>List</h1>")

def post_update(request, id=None):
  instance = get_object_or_404(Post, id=id);
  form = PostForm(request.POST or None)

  if form.is_valid():
    instance = form.save(commit=False)

    instance.save()
  context = {
    "title": instance.title,
    "instance": instance,
    "form": form,
  }
  return render(request, "post_form.html", context)

def post_delete(request):
  context = {
    "title": "Delete"
  }
  return render(request, "index.html", context)

