from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
    "form": form,
    }

    return render(request, "post_form.html", context)

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id);
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)

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

    return render(request, "post_list.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id);
    form = PostForm(request.POST or None, instance = instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated", extra_tags='some-tag')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,

        "instance": instance,
        
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id);
    messages.success(request, "Successfully Deleted")
    instance.delete()

    return redirect("posts:list")

