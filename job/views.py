from django.db.models.query import InstanceCheckMeta
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from job.models import Category, Company, Job
from job.decorators import *
from job.forms import JobForm, CompanyForm
from user.models import Profile


def index(request):
    category_qs = Category.objects.all()
    jobs = Job.objects.all()[:4]
    context = {
        'categories': category_qs,
        'jobs': jobs,
    }
    return render(request, 'index.html', context)


@allow_user
def post_listing(request, slug=None):
    if slug:
        jobs = Job.objects.filter(category__slug=slug)
    else:
        jobs = Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'job/job_listing.html', context)


@login_required
def post_detail(request, slug):
    job = Job.objects.filter(slug=slug).first()
    context = {
        'job': job,
    }
    return render(request, 'job/job_details.html', context)


@login_required
@allow_company
def add_job(request, slug=None):
    if slug:
        job = Job.objects.get(slug=slug)
        form = JobForm(request.POST or None, request.FILES or None, instance=job, request=request)
    else:
        form = JobForm(request.POST or None, request.FILES or None, request=request)
    jobs = Job.objects.filter(company__profile=request.user.profile)
    if request.method == "POST":
	    if form.is_valid():
		    form.save()
		    return redirect("job:add-job")
    context = {
        'form': form,
        'jobs': jobs,
    }
    return render(request, 'job/add_job.html', context)


@login_required
@allow_company
def add_company(request, pk=None):
    if pk:
        company = Company.objects.get(pk=pk)
        form = CompanyForm(request.POST or None, request.FILES or None, instance=company)
    else:
        form = CompanyForm(request.POST or None, request.FILES or None)
    companies = request.user.profile.company_set.all()
    if request.method == "POST":
        if form.is_valid():
            company = form.save(commit=False)
            company.profile = request.user.profile
            company.save()
            return redirect("job:add-company")
    context = {
        'form': form,
        'companies': companies,
    }
    return render(request, 'job/add_company.html', context)


@login_required
@allow_company
def company_detail(request):
    profile = Profile.objects.get(user=request.user)
    companies = Company.objects.filter(profile=profile)
    context = {
        'companies': companies,
        'profile': profile,
    }
    return render(request, 'job/company_details.html', context)
