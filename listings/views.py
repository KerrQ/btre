from django.views.generic import ListView, DetailView
from .models import Listing
from django.core.paginator import Paginator
from .choises import bedroom_choices, state_choices, price_choices
from django.db.models import Q
from realtors.models import Realtor
# Create your views here.


class Home(ListView):
    template_name = 'index.html'
    context_object_name = 'listings'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context["bedroom_choices"] = bedroom_choices
        context["state_choices"] = state_choices
        context["price_choices"] = price_choices
        return context

    def get_queryset(self):
        qs = Listing.objects.all().order_by('-list_date')[:3]
        return qs


class About(ListView):
    template_name = "about.html"
    model = Realtor
    context_object_name = 'realtors'


class ListingDetail(DetailView):
    model = Listing
    template_name = 'listing.html'
    context_object_name = 'listing'


class Listings(ListView):
    template_name = 'listings.html'
    context_object_name = 'listings'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("keywords")
        queryset_list = Listing.objects.all()
        if query:
            queryset_list = queryset_list.filter(title__icontains=query).distinct()
        return queryset_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Listings, self).get_context_data(**kwargs)
        queryset_list = Listing.objects.all()
        paginator = Paginator(queryset_list, 6)
        context['pages'] = range(1, paginator.num_pages + 1)
        return context


class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'listings'
    paginate_by = 6

    def get_queryset(self):
        keywords = self.request.GET.get("keywords")
        city = self.request.GET.get("city")
        bedrooms = self.request.GET.get("bedrooms")
        price = self.request.GET.get("price")
        state = self.request.GET.get("state")
        queryset_list = Listing.objects.all().order_by('-list_date')
        if keywords:
            queryset_list = queryset_list.filter(
                Q(title__icontains=keywords) |
                Q(description__icontains=keywords)
            ).distinct()

        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms).distinct()

        if price:
            queryset_list = queryset_list.filter(price__lte=price).distinct()

        if city:
            queryset_list = queryset_list.filter(city__iexact=city).distinct()

        if state:
            queryset_list = queryset_list.filter(state__iexact=state).distinct()
            print(state)

        return queryset_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        queryset_list = Listing.objects.all()
        paginator = Paginator(queryset_list, 6)
        context['pages'] = range(1, paginator.num_pages + 1)
        context["bedroom_choices"] = bedroom_choices
        context["state_choices"] = state_choices
        context["price_choices"] = price_choices
        return context
