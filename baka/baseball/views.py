from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404 #does try/catch in one line
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Batter, Statline
from django.db.models import Q
from .forms import BatterForm, StatlineForm


def index(request):
#    all_batters = Batter.objects.all().order_by('rank')
    all_batters_list = Batter.objects.all().order_by('rank')

    query = request.GET.get("q")
    if query:
        all_batters_list = all_batters_list.filter(
            Q(player__icontains=query)|
            Q(pos__icontains=query)
                ).distinct()
    paginator = Paginator(all_batters_list, 20)
#    paginator = Paginator(all_batters_list, 30)  # Show 30 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        all_batters = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_batters = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_batters = paginator.page(paginator.num_pages)

    context = {
        'all_batters': all_batters,
        "page_request_var": page_request_var,
    }
    return render(request, 'baseball/index.html', context)#{'all_batters': all_batters})


def my_team(request):
#    renders basically the index page but only batters with my_team == True
    all_batters_list = Batter.objects.all().order_by('rank')

    query = request.GET.get("q")
    if query:
        all_batters_list = all_batters_list.filter(
            Q(player__icontains=query)|
            Q(pos__icontains=query)
                ).distinct()
    paginator = Paginator(all_batters_list, 20)
#    paginator = Paginator(all_batters_list, 30)  # Show 30 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        all_batters = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_batters = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_batters = paginator.page(paginator.num_pages)

    context = {
        'all_batters': all_batters,
        "page_request_var": page_request_var,
    }
    return render(request, 'baseball/my_team.html', context)#{'all_batters': all_batters})



def detail(request, batter_id):
    batter = get_object_or_404(Batter, pk=batter_id)  # replaces try/except statement
    return render(request, 'baseball/detail.html', {'batter': batter})



@login_required
def edit_batter(request, batter_id):
    batter = Batter.objects.get(id=batter_id)
    if request.method != 'POST': #no data submitted, create blank form
        form = BatterForm(instance=batter)
    else:
        form = BatterForm(instance=batter, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('baseball:detail', args=[batter.id]))

    context = {"batter": batter, "form": form}
    return render(request, 'baseball/edit_batter.html', context)

#set index as home page -- render list of batters on another page
@login_required
def new_batter(request): #add a new batter
    if request.method != 'POST': #no data submitted, create blank form
        form = BatterForm()
    else: #POST data submitted, process the data
        form = BatterForm(request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('baseball:batters'))
    context = {'form': form}
    return render(request, 'baseball/new_batter.html', context)
"""

@login_required
def new_batter((request):
	form = BatterForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print (form.cleaned_data.get("title"))
		instance.save()
		messages.success(request, "Successsfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "new_batter.html", context)


@login_required
def edit_statline(request, batter_id): #add a new statline
    batter = Batter.objects.get(pk=batter_id)
    statline = batter.statline


    if request.method != 'POST': #no data submitted, create blank form
        form = StatlineForm(instance=batter)
    else:
        form = StatlineForm(instance=batter, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('baseball:batters', args=[batter_id]))

    context = {'player': player, 'form': form, 'statline': statline}
    return render(request, 'baseball/edit_statline.html', context)





"""




@login_required
def new_statline(request, batter_id): #add a new statline
    batter = Batter.objects.get(pk=batter_id)

    if request.method != 'POST': #no data submitted, create blank form
        form = StatlineForm()
    else: #POST data submitted, process the data
        form = StatlineForm(data=request.POST)
        if form.is_valid():
            new_statline = form.save(commit=False)
            new_statline.batter = batter
            new_statline.save()
            return HttpResponseRedirect(reverse('baseball:batters', args=[batter_id]))

    context = {'batter': batter, 'form': form}
    return render(request, 'baseball/new_statline.html', context)





















