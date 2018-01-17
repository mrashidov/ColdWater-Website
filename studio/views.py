from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect,reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from . import forms
from . import models

from studio.models import Task
class ShowTask(LoginRequiredMixin, generic.TemplateView):
    template_name = "studio/show_task.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            #Getting task
            task = get_object_or_404(models.Task, slug=slug)

        kwargs["task"] = task
        kwargs["user"] = self.request.user
        return super(ShowTask, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        slug = self.kwargs.get('slug')
        if slug:
            task = get_object_or_404(models.Task, slug=slug)
        POST = request.POST
        if POST.get('cancel')=='true':
            task.cancel()
        if POST.get('complete')=='true':
            task.complete()
        if POST.get('reject')=='true':
            task.reject()
        if POST.get('in_progress')=='true':
            task.set_as_in_progress()
        kwargs["task"] = task
        kwargs["user"] = request.user
        return super(ShowTask, self).get(request, *args, **kwargs)

    


class AddTask(LoginRequiredMixin, generic.TemplateView):
    template_name = 'studio/add_task.html'
    http_method_names = ['get','post']

    def get(self, request, *args, **kwargs):
        if "task_form" not in kwargs:
            kwargs["task_form"] = forms.TaskForm();
        return super(AddTask, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data['date_expired'])
        task = Task(name=data['name'],
            description=data['description'],
            date_expired=datetime.strptime(
                data['date_expired'], 
                "%Y-%m-%d").date(),
            client=request.user)
        task.save();
        print(task.slug)
        return redirect('studio:show',slug=task.slug)