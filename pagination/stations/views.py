from csv import DictReader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    bus_stations = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf8') as f:
        for row in DictReader(f):
            bus_stations.append(
                {'name': row.get('Name'),
                 'street': row.get('Street'),
                 'district': row.get('District')})
    # print(BUS_STATIONS)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    print(page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context=context)
