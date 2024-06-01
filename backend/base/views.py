import datetime
from collections import Counter
from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.db.models import Sum, Count, F, ExpressionWrapper, FloatField
from django.db.models.functions import TruncYear, TruncMonth
from .models import (
    RealEstate,
    RoomsNumber,
    ProjectName,
    BuildingName
)
from .forms import (
    RealEstateForm
)


def is_valid_queryparam(param):
    return param != '' and param is not None


def reverse_order(param):
    return param.reverse()


def index(request):
    form = RealEstateForm()

    master_project = request.GET.get('master_project')
    project_name = request.GET.get('project_name')
    building_name = request.GET.get('building_name')
    property_type = request.GET.get('property_type')
    rooms_number = request.GET.get('rooms_number')
    time_period = request.GET.get('time_period')

    request.session['master_project'] = master_project
    request.session['project_name'] = project_name
    request.session['building_name'] = building_name
    request.session['property_type'] = property_type
    request.session['rooms_number'] = rooms_number
    request.session['time_period'] = time_period

    context = {
        'form': form,
        }
    return render(request, 'base/dashboard.html', context)


def all_transactions(request):
    qs = RealEstate.objects.all().order_by('-transaction_date')

    # start_time = datetime.datetime.now()
    # # Timeline filters
    # YTD_AGO = datetime.date(
    #     start_time.year,
    #     1, 1)
    # ONE_YEAR_AGO = datetime.date(
    #     start_time.year-1,
    #     start_time.month, 28)
    # FIVE_YEARS_AGO = datetime.date(
    #     start_time.year-5,
    #     start_time.month, 28)

    # # by default last year
    # period_filter = ONE_YEAR_AGO

    # time_period = request.session.get('time_period')
    # if is_valid_queryparam(time_period):
    #     if time_period == "YTD":
    #         period_filter = YTD_AGO
    #     elif time_period == "1Y":
    #         period_filter = ONE_YEAR_AGO
    #     elif time_period == "5Y":
    #         period_filter = FIVE_YEARS_AGO
    #     else:
    #         period_filter = "All"

    # # Decode => prefetch_related; objects.all().values for the dictionary
    # if period_filter != "All":
    #     qs = RealEstate.objects.all().filter(
    #         transaction_date__gte=period_filter).order_by('transaction_date')
    # else:
    #     qs = RealEstate.objects.all().order_by('transaction_date')

    # master_project = request.GET.get('master_project')
    # project_name = request.GET.get('project_name')
    # building_name = request.GET.get('building_name')
    # property_type = request.GET.get('property_type')
    # rooms_number = request.GET.get('rooms_number')

    master_project = request.session.get('master_project')
    project_name = request.session.get('project_name')
    building_name = request.session.get('building_name')
    property_type = request.session.get('property_type')
    rooms_number = request.session.get('rooms_number')

    # if not is_valid_queryparam(master_project):
    #     print('hi')
    #     messages.add_message(request, messages.INFO, "Hello world.")

    if is_valid_queryparam(master_project):
        qs = qs.filter(master_project=master_project)
    if is_valid_queryparam(project_name):
        qs = qs.filter(project_name=project_name)
    if is_valid_queryparam(building_name):
        qs = qs.filter(building_name=building_name)
    if is_valid_queryparam(property_type):
        qs = qs.filter(property_type=property_type)
    if is_valid_queryparam(rooms_number):
        qs = qs.filter(rooms_number=rooms_number)

    qs = (qs.annotate(price_per_sqm=ExpressionWrapper(
        F('object_price') / F('object_size'), output_field=FloatField())))

    context = {
        'qs': qs
        }

    return render(request, 'base/all_transactions.html', context)


def load_project_names(request):
    selected_project_name_id = request.session.get('project_name')
    if selected_project_name_id:
        selected_project_name = ProjectName.objects.get(
            id=selected_project_name_id)
    else:
        selected_project_name = None

    selected_master_project = request.GET.get('master_project')
    if is_valid_queryparam(selected_master_project):
        project_names = (ProjectName.objects.filter(
            realestate__master_project=selected_master_project)
            .distinct()
            .order_by('name'))
        if len(project_names.values()[0].get('name')) == 0:
            project_names = None
    else:
        project_names = None

    context = {
        'project_names': project_names,
        'selected_project_name': selected_project_name,
        'selected_master_project': selected_master_project
    }
    return render(request, 'base/project_names.html', context)


def load_building_names(request):
    selected_building_name_id = request.session.get('building_name')
    if selected_building_name_id:
        selected_building_name = BuildingName.objects.get(
            id=selected_building_name_id)
    else:
        selected_building_name = None

    selected_project_name = request.GET.get('project_name')
    if is_valid_queryparam(selected_project_name):
        building_names = (BuildingName.objects.filter(
            realestate__project_name=selected_project_name)
            .distinct()
            .order_by('name'))
        if len(building_names.values()[0].get('name')) == 0:
            building_names = None
    else:
        building_names = None

    context = {
        'building_names': building_names,
        'selected_project_name': selected_project_name,
        'selected_building_name': selected_building_name
    }
    return render(request, 'base/building_names.html', context)


def load_rooms_number(request):
    selected_property_type = request.GET.get('property_type')
    if is_valid_queryparam(selected_property_type):
        selected_rooms_number_id = request.session.get('rooms_number')
        if selected_rooms_number_id:
            selected_rooms_number = RoomsNumber.objects.get(
                id=selected_rooms_number_id)
        else:
            selected_rooms_number = None

        selected_property_type = request.GET.get('property_type')

        if is_valid_queryparam(selected_property_type):
            rooms_number = (
                RoomsNumber.objects.filter(
                    realestate__property_type=selected_property_type)
                .distinct()
                .order_by('name'))
            if len(rooms_number.values()[0].get('name')) == 0:
                rooms_number = None
        else:
            rooms_number = None

        context = {
            'rooms_number': rooms_number,
            'selected_property_type': selected_property_type,
            'selected_rooms_number': selected_rooms_number
        }
        return render(request, 'base/rooms_number.html', context)
    return render(request, 'base/rooms_number.html', {})


def line_data(request):
    start_time = datetime.datetime.now()
    # Timeline filters
    YTD_AGO = datetime.date(
        start_time.year,
        1, 1)
    ONE_YEAR_AGO = datetime.date(
        start_time.year-1,
        start_time.month, 28)
    FIVE_YEARS_AGO = datetime.date(
        start_time.year-5,
        start_time.month, 28)

    # by default last year
    period_filter = ONE_YEAR_AGO

    time_period = request.session.get('time_period')
    if is_valid_queryparam(time_period):
        if time_period == "YTD":
            period_filter = YTD_AGO
        elif time_period == "1Y":
            period_filter = ONE_YEAR_AGO
        elif time_period == "5Y":
            period_filter = FIVE_YEARS_AGO
        else:
            period_filter = "All"

    # Decode => prefetch_related; objects.all().values for the dictionary
    yearly_price_trend = {}
    monthly_price_trend = {}
    if period_filter != "All":
        qs = RealEstate.objects.all().filter(
            transaction_date__gte=period_filter).order_by('transaction_date')
    else:
        qs = RealEstate.objects.all().order_by('transaction_date')

    master_project = request.session.get('master_project')
    project_name = request.session.get('project_name')
    building_name = request.session.get('building_name')
    property_type = request.session.get('property_type')
    rooms_number = request.session.get('rooms_number')

    if is_valid_queryparam(master_project):
        qs = qs.filter(master_project=master_project)
    if is_valid_queryparam(project_name):
        qs = qs.filter(project_name=project_name)
    if is_valid_queryparam(building_name):
        qs = qs.filter(building_name=building_name)
    if is_valid_queryparam(property_type):
        qs = qs.filter(property_type=property_type)
    if is_valid_queryparam(rooms_number):
        qs = qs.filter(rooms_number=rooms_number)

    # Monthly Dynamics
    if (
      time_period == "YTD"
      or time_period == "1Y"
      or time_period == ''):
        monthly_sizes_items = (qs.annotate(
            month_year=TruncMonth('transaction_date'))
            .values('month_year')
            .annotate(total_monthly_size=Sum('object_size'),
                      transactions_number=Count('object_size'))
            .order_by('month_year'))
        monthly_sizes = {
            item.get('month_year').strftime("%b-%y"): item.get('total_monthly_size')
            for item in monthly_sizes_items}

        monthly_prices_items = (qs.annotate(
            month_year=TruncMonth('transaction_date'))
            .values('month_year')
            .annotate(total_monthly_price=Sum('object_price'))
            .order_by('month_year'))
        monthly_prices = {
            item.get('month_year').strftime("%b-%y"): item.get('total_monthly_price')
            for item in monthly_prices_items}

        for item in monthly_prices.keys():
            monthly_price_trend[item] = (round((monthly_prices.get(item)
                                         / monthly_sizes.get(item)), 0))

        dates = list(monthly_price_trend.keys())
        prices_per_sqm = list(monthly_price_trend.values())
        transactions_number = (
            [item.get('transactions_number') for item in monthly_sizes_items])
    else:
        # Yearly Dynamic
        yearly_sizes_items = (qs.annotate(
            year=TruncYear('transaction_date'))
            .values('year')
            .annotate(total_yearly_size=Sum('object_size'),
                      transactions_number=Count('object_size'))
            .order_by('year'))
        yearly_sizes = {
            item.get('year').year: item.get('total_yearly_size')
            for item in yearly_sizes_items}

        yearly_prices_items = (qs.annotate(
            year=TruncYear('transaction_date'))
            .values('year')
            .annotate(total_yearly_price=Sum('object_price'))
            .order_by('year'))
        yearly_prices = {
            item.get('year').year: item.get('total_yearly_price')
            for item in yearly_prices_items}

        for item in yearly_prices.keys():
            yearly_price_trend[item] = (round((yearly_prices.get(item)
                                        / yearly_sizes.get(item)), 0))

        dates = list(yearly_price_trend.keys())
        prices_per_sqm = list(yearly_price_trend.values())
        transactions_number = (
            [item.get('transactions_number') for item in yearly_sizes_items])


    end_time = datetime.datetime.now()
    process_time = end_time - start_time
    print(f'Time spent: {process_time}')
    # # decode
    # # items = RealEstate.objects.select_related('project_name').all().order_by('transaction_date')
    # # items = RealEstate.objects.prefetch_related('project_name').all().order_by('transaction_date')

    data = {
        'dates': dates,
        'prices_per_sqm': prices_per_sqm,
        'transactions_number': transactions_number
    }

    return JsonResponse(data)


def bar_data(request):
    start_time = datetime.datetime.now()
    # Decode => prefetch_related; objects.all().values for the dictionary
    qs = RealEstate.objects.all()

    master_project = request.session.get('master_project')
    project_name = request.session.get('project_name')
    building_name = request.session.get('building_name')
    property_type = request.session.get('property_type')
    rooms_number = request.session.get('rooms_number')

    if is_valid_queryparam(master_project):
        qs = qs.filter(master_project=master_project)
    if is_valid_queryparam(project_name):
        qs = qs.filter(project_name=project_name)
    if is_valid_queryparam(building_name):
        qs = qs.filter(building_name=building_name)
    if is_valid_queryparam(property_type):
        qs = qs.filter(property_type=property_type)
    if is_valid_queryparam(rooms_number):
        qs = qs.filter(rooms_number=rooms_number)

    # Displaying last 10 transactions
    qs = qs[:10]

    master_projects = list(
        reversed(qs.values_list('master_project__name', flat=True)))
    project_names = list(
        reversed(qs.values_list('project_name__name', flat=True)))
    building_names = list(
        reversed(qs.values_list('building_name__name', flat=True)))
    dates = list(
        reversed(qs.values_list('transaction_date', flat=True)))
    prices = list(
        reversed(qs.values_list('object_price', flat=True)))
    types = list(
        reversed(qs.values_list('property_type__name', flat=True)))
    sizes = list(
        reversed(qs.values_list('object_size', flat=True)))
    rooms_number = list(
        reversed(qs.values_list('rooms_number__name', flat=True)))

    data = {
        'master_projects': master_projects,
        'project_names': project_names,
        'building_names': building_names,
        'dates': dates,
        'prices': prices,
        'types': types,
        'sizes': sizes,
        'rooms_number': rooms_number
    }

    end_time = datetime.datetime.now()
    process_time = end_time - start_time
    print(f'Time spent: {process_time}')

    return JsonResponse(data)


class ajax_view(TemplateView):
    def get(self, request, *args, **kwargs):
        master_project = request.GET['master_project']
        project_name = request.GET['project_name']
        building_name = request.GET['building_name']
        property_type = request.GET['property_type']
        rooms_number = request.GET['rooms_number']
        time_period = request.GET['time_period']
        data_value = {'master_project': master_project,
                      'project_name': project_name,
                      'building_name': building_name,
                      'property_type': property_type,
                      'rooms_number': rooms_number,
                      'time_period': time_period}
        return JsonResponse(data_value)


### Review


# return JsonResponse(list(cities.values("id", "name")), safe=False)

# json_dict = {}
# for car_make in Make.objects.all():
#     json_dict[car_make] = Model.objects.filter(make=car_make)
# json_data = json.dumps(json_dict)