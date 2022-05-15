from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from Accounts.models import User

#User =get_user_model


WORK_PLACE_TYPE = (
    ('onsite', 'On-site'),
    ('hybrid', 'Hybrid'),
    ('remote', 'Remote'),
)


EMPLOYMENT_TYPE = (
    ('full_time', 'Full time'),
    ('part_time', 'Part time'),
    ('contract', 'Contract'),
    ('temporary', 'Temporary'),
    ('volenteer', 'Volenteer'),
    ('internshp', 'Internship'),
)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, blank=True)
    #company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    company_description = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    workplace_type = models.CharField(
        max_length=32, choices=WORK_PLACE_TYPE, default='onsite')
    employment_type = models.CharField(
        max_length=25, choices=EMPLOYMENT_TYPE, default='full_time')
    experience = models.CharField(max_length=400)
    skills = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    job_function = models.CharField(max_length=200)
    tags = TaggableManager()
    def __str__(self):
        return '{} {} {}'.format(self.title, self.company_name, self.location)


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ['id']
        unique_together = ["user", "job"]

    def __strt__(self):
        return self.job.title

    @property
    def get_status(self):
        if self.status == 1:
            return "Panding"
        elif self.status == 2:
            return "Accepted"
        else:
            return "Rejected"
