# Django Imports
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

# Local Imports
from cms.models import Page


def index(request):
    # Look for a Page by its related Title
    page = Page.objects.filter(title_set__title=settings.HOME_PAGE_TITLE).first()
    
    if page:
        # Use the page's reverse_id if you want named redirects
        if page.reverse_id:
            redirect_url = reverse(page.reverse_id)
        else:
            # fallback to the CMS home
            redirect_url = reverse("pages-root")
    else:
        redirect_url = reverse("workshop_app:index")
    
    return redirect(redirect_url)
