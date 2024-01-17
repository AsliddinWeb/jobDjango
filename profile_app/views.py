from django.contrib.auth.decorators import login_required
from JOB.views import base_page
from django.shortcuts import render, redirect

from .forms import ProfileForm
from .models import Profile

@login_required
@base_page
def profile_create_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    if profile is None:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                # Child data
                main_context = {
                    # Required
                    'template': 'user-cabinet.html',

                    # Main
                    'form': form,
                }

                return main_context
        else:
            form = ProfileForm()

        # Child data
        main_context = {
            # Required
            'template': 'profile/create.html',

            # Main
            'form': form,
            'value': 'add',
        }

        return main_context
    else:
        # Child data
        main_context = {
            # Required
            'template': 'user-cabinet.html',

            # Main
            'profile': profile,
        }

        return main_context

@login_required
@base_page
def profile_update_page(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            main_context = {
                # Required
                'template': 'user-cabinet.html',

                # Main
                'form': form,
                'profile': profile
            }

            return main_context
    else:
        form = ProfileForm(instance=profile)

    # Child data
    main_context = {
        # Required
        'template': 'profile/create.html',

        # Main
        'form': form,
        'value': 'add',
        'profile': profile,
    }

    return main_context