from email import message
from multiprocessing import context
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy



from Accounts.models import User
from Job.forms import *
from Job.models import *
from Job.permission import *
User = get_user_model()


def home_view(request):
    published_jobs = Job.objects.all().order_by('date')
    jobs = published_jobs
    total_candidates = User.objects.filter(role='user').count()
    total_companies = User.objects.filter(role='company').count()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        job_lists = []
        job_objects_list = page_obj.object_list.values()
        for job_list in job_objects_list:
            job_lists.append(job_list)

        next_page_number = None
        if page_obj.has_next():
            next_page_number = page_obj.next_page_number()

        prev_page_number = None
        if page_obj.has_previous():
            prev_page_number = page_obj.previous_page_number()
        data = {
            'job_lists': job_lists,
            'current_page_number': page_obj.number,
            'next_page_number': next_page_number,
            'no_of_page': paginator.num_pages,
            'prev_page_number': prev_page_number,
        }
        return JsonResponse(data)
    context = {
        'total_candidates': total_candidates,
        'total_companies': total_companies,
        'total_jobs': len(jobs),
        'page_obj': page_obj
    }
    print('ok')
    return render(request, 'job/index.html', context)


def job_list_View(request):

    job_list = Job.objects.all().order_by('-date')
    paginator = Paginator(job_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'job/job_list.html', context)


@login_required(login_url=reverse_lazy('Accounts:login'))
@is_user
def create_job_view(request):
    form = JobForm(request.POST or None)

    user = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            form.save_m2m()
            message.success(
                request, 'You are successfully posted your job! please wait for review.')
            return redirect(reverse("job:single-job", kwargs={
                'id': instance.id
            }))
    context = {
        'form' : form
        }

    return render(request,'job/post-job.html',context)

def single_job_view(request,id):

    job=get_object_or_404(Job,id=id)
    related_job_list=job.tags.similar_objects()

    paginator =Paginator(related_job_list,5)
    page_number=request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    
    context={
        'job':job,
        'page_obj':page_obj,
        'total':len(related_job_list)
    }
    return render(request,'job/job-single.html',context)

def search_result_view(request):

    job_list=Job.objects.order_by('-date')
    if 'job_title_or_company_name' in request.GET:
        job_title_or_company_name = request.GET['job_title_or_company_name']

        if job_title_or_company_name:
            job_list = job_list.filter(title__icontains=job_title_or_company_name) | job_list.filter(
                company_name__icontains=job_title_or_company_name)

    # location
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            job_list = job_list.filter(location__icontains=location)

    # Job Type
    if 'job_type' in request.GET:
        job_type = request.GET['job_type']
        if job_type:
            job_list = job_list.filter(job_type__iexact=job_type)

    # job_title_or_company_name = request.GET.get('text')
    # location = request.GET.get('location')
    # job_type = request.GET.get('type')

    #     job_list = Job.objects.all()
    #     job_list = job_list.filter(
    #         Q(job_type__iexact=job_type) |
    #         Q(title__icontains=job_title_or_company_name) |
    #         Q(location__icontains=location)
    #     ).distinct()

    # job_list = Job.objects.filter(job_type__iexact=job_type) | Job.objects.filter(
    #     location__icontains=location) | Job.objects.filter(title__icontains=text) | Job.objects.filter(company_name__icontains=text)

    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {

        'page_obj': page_obj,

    }
    return render(request, 'jobapp/result.html', context)
