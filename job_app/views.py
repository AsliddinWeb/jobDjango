from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from phone_auth.models import PhoneNumber

from JOB.views import base_page

from .forms import JobForm
from .models import JobRegion, JobCategory, Job

@login_required
@base_page
def add_job_page(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            # Retrieve form data
            title = request.POST.get('title')
            description = request.POST.get('description')
            file = request.FILES.get('files')  # Use request.FILES for file uploads
            region_id = request.POST.get('region')
            district = request.POST.get('district')
            price = request.POST.get('price')
            is_none_price = request.POST.get('is_none_price') == 'on'
            deadline = request.POST.get('deadline')
            is_none_deadline = request.POST.get('is_none_deadline') == 'on'
            category_id = request.POST.get('category')

            # Create JobCategory and JobRegion instances
            category = JobCategory.objects.get(pk=category_id)
            region = JobRegion.objects.get(pk=region_id)

            # Create Job instance
            job = Job(
                user=request.user,
                category=category,
                title=title,
                description=description,
                file=file,
                region=region,
                district=district,
                price=price if not is_none_price else None,
                is_none_price=is_none_price,
                deadline=deadline if not is_none_deadline else None,
                is_none_deadline=is_none_deadline,
                status='Kutishda'
            )

            # Save the instance
            job.save()
            main_context = {
                # Required
                'template': 'add-job-success.html',

                # Main
            }

            return main_context

    JOB_REGIONS = JobRegion.objects.all()
    JOB_CATEGORY = JobCategory.objects.all()

    # Child data
    main_context = {
        # Required
        'template': 'add-job.html',

        # Main
        'form': form,
        'JOB_REGIONS': JOB_REGIONS,
        'JOB_CATEGORY': JOB_CATEGORY,
    }

    return main_context

@login_required
@base_page
def add_job_success(request):
    # Child data
    main_context = {
        # Required
        'template': 'add-job-success.html',

        # Main
    }

    return main_context

@base_page
def all_jobs(request):
    JOBS = Job.objects.filter(status="Aktiv")

    page_num = request.GET.get('page', 1)
    paginator = Paginator(JOBS, 16)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)


    # Child data
    main_context = {
        # Required
        'template': 'all-jobs.html',

        # Main
        'JOBS': page_obj,
        'page_num': page_num,
        'ALL_JOBS': JOBS,
    }

    return main_context

@base_page
def job_detail(request, pk):
    # Child data
    job = get_object_or_404(Job, pk=pk)
    phone_number = PhoneNumber.objects.filter(user=job.user).order_by('-id')[0]
    last_jobs = Job.objects.filter(status="Aktiv")[:3]

    main_context = {
        # Required
        'template': 'job-detail.html',

        # Main
        'job': job,
        'phone_number': phone_number,
        'last_jobs': last_jobs,
    }

    return main_context

@base_page
def job_region(request, pk):
    JOBS = Job.objects.filter(status="Aktiv", region=pk)

    page_num = request.GET.get('page', 1)
    paginator = Paginator(JOBS, 16)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    # Child data
    main_context = {
        # Required
        'template': 'all-jobs.html',

        # Main
        'JOBS': page_obj,
        'page_num': page_num,
        'ALL_JOBS': JOBS,
    }

    return main_context