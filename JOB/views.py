from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from settings_app.models import (SeoSettings, SiteSettings, OneNavbar, TwoNavbar,
                                 FooterSettings, FooterLinks, SocialSettings)
from profile_app.models import Profile

from main_app.models import *
from job_app.models import Job, JobCategory, JobRegion

def base_page(view_func):
    def wrapper(request, *args, **kwargs):
        SEO_SETTINGS = SeoSettings.objects.last()
        SITE_SETTINGS = SiteSettings.objects.last()

        ONE_NAVBAR = OneNavbar.objects.all()
        TWO_NAVBAR = TwoNavbar.objects.all()

        FOOTER_SETTINGS = FooterSettings.objects.last()
        FOOTER_LINKS_1 = FooterLinks.objects.filter(is_useful=True)
        FOOTER_LINKS_2 = FooterLinks.objects.filter(is_useful=False)
        SOCIAL_SETTINGS = SocialSettings.objects.all()

        # Context
        base_context = {
            'SEO_SETTINGS': SEO_SETTINGS,
            'SITE_SETTINGS': SITE_SETTINGS,
            'ONE_NAVBAR': ONE_NAVBAR,
            'TWO_NAVBAR': TWO_NAVBAR,
            'FOOTER_SETTINGS': FOOTER_SETTINGS,
            'FOOTER_LINKS_1': FOOTER_LINKS_1,
            'FOOTER_LINKS_2': FOOTER_LINKS_2,
            'SOCIAL_SETTINGS': SOCIAL_SETTINGS
        }

        # Get child data
        main_context = view_func(request, *args, **kwargs)
        template = main_context.get('template', 'home.html')

        # Child data added to main data
        base_context.update(main_context)

        return render(request, template, base_context)

    return wrapper

@base_page
def home_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        region = request.POST.get('region')
        category_id = request.POST.get('category_id')

        # Filter jobs based on search parameters
        JOBS = Job.objects.filter(status="Aktiv")
        if title:
            JOBS = JOBS.filter(title__icontains=title)

        if region:
            JOBS = JOBS.filter(region__name__icontains=region)

        if category_id and category_id != '0':
            JOBS = JOBS.filter(category_id=int(category_id))

        # Pagination
        page_num = request.GET.get('page', 1)
        paginator = Paginator(JOBS, 16)

        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        # Child data
        main_context = {
            'template': 'all-jobs.html',
            'JOBS': page_obj,
            'page_num': page_num,
            'ALL_JOBS': JOBS,
        }

        return main_context

    home_search = HomeSearch.objects.last()
    home_search_counter = HomeSearchCounter.objects.all()
    job_categories = JobCategory.objects.all()

    home_steps = HomeStep.objects.all()

    aniq_ishlar = Job.objects.filter(is_none_price=False)[:10]
    noaniq_ishlar = Job.objects.filter(is_none_price=True)[:10]

    home_reklama = HomeReklama.objects.last()
    job_regions = JobRegion.objects.all()

    region_jobs = []
    for i in range(len(job_regions)):
        region_jobs.append(
            {
                'job': Job.objects.filter(region=job_regions[i]),
                'region': job_regions[i]
            }
        )
    sorted_region_jobs = sorted(region_jobs, key=lambda x: len(x['job']), reverse=True)

    home_resume = HomeResume.objects.last()
    home_app = HomeApp.objects.last()
    home_app_divs = HomeAppDivs.objects.all()

    # Child data
    main_context = {
        # Required
        'template': 'home.html',

        # Main
        'home_search': home_search,
        'home_search_counter': home_search_counter,
        'job_categories': job_categories,

        'home_steps': home_steps,

        'aniq_ishlar': aniq_ishlar,
        'noaniq_ishlar': noaniq_ishlar,

        'home_reklama': home_reklama,
        'job_regions': sorted_region_jobs[:4],
        'home_resume': home_resume,
        'home_app': home_app,
        'home_app_divs': home_app_divs,
    }

    return main_context

@base_page
def cabinet_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    # Child data
    main_context = {
        # Required
        'template': 'user-cabinet.html',

        # Main
        'profile': profile,
    }

    return main_context