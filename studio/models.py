from django.db import models
from django.conf import settings
# Create your models here.
import uuid
from datetime import datetime
from django.shortcuts import redirect

class Task(models.Model):
    description = models.TextField()
    date_expired = models.DateTimeField('deadline date', default=datetime.now)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    is_complete = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    date_created = models.DateTimeField('created', blank = True, null =True, auto_now_add=True)
    date_finished = models.DateTimeField('finished', blank = True, null = True)
    name = models.CharField(max_length=45)
    in_progress = models.BooleanField(default=False)
    def __str__(self):
        return self.name + " " +  self.date_created.strftime("%Y-%m-%d %H:%M") +' - '+ self.date_expired.strftime("%Y-%m-%d %H:%M");
    def cancel(self):
        self.date_finished = datetime.now()
        self.is_cancelled = True;
        self.in_progress = False;
        super(Task,self).save();
    def reject(self):
        self.date_finished = datetime.now()
        self.is_rejected = True;
        self.in_progress = False;
        super(Task, self).save()
    def set_as_in_progress(self):
        self.in_progress = True;
        super(Task, self).save()
    def complete(self):
        self.date_finished =datetime.now()
        self.in_progress = False;
        self.is_complete = True;
        super(Task,self).save()
