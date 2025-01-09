from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView
from .forms import ContactForm
from .models import Facility, News, Product, Category, AboutUs
from django.contrib import messages
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


class About(ListView):
    model = AboutUs
    template_name = 'about_us.html'
    context_object_name = 'about_us'

    def get_queryset(self):
        return AboutUs.objects.filter(is_published=True)

class FacilityView(ListView):
    model = Facility
    template_name = 'our_facilities.html'
    context_object_name = 'facilities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FacilityDetailView(DetailView):
    model = Facility
    template_name = 'facility_detail.html'
    context_object_name = 'facility'
    slug_field = 'slug'  # This tells the view to use the `slug` field for lookups.
    slug_url_kwarg = 'facility_slug'  # Matches the <facility_slug> in the URL pattern.


class NewsUpdates(ListView):
    model = News
    template_name = 'news_updates.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'
    slug_url_kwarg = 'news_slug'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email or save the data to the database
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['khondamiras@gmail.com', 'info@saasteks.uz'],  # Replace with your own email or recipient list
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Replace 'contact' with the name of your URL pattern for this page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})




def our_products(request):
    return render(request, 'our_products.html')


# views.py
def product_details(request):
    knitted_products = Category.knitted.all()

    context = {
        'knitted_products': knitted_products,
    }

    return render(request, 'our_product_details.html', context)



def fabrics(request):
    fabric_products = Category.fabric.all()
    return render(request, 'fabrics.html', {'fabric_products': fabric_products})


