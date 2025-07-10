#### Django provides high-level and low-level ways to help you manage paginated data – that is, data that’s split across several pages, with “Previous/Next” links.

# %%
from django.core.paginator import Paginator

objects = ["john", "paul", "george", "ringo"]
p = Paginator(objects, 2)
print(p.count)
print(p.num_pages)
print(p.page_range)
print(type(p.page_range))

page1 = p.page(1)
print(page1)
print(page1.object_list)
print("has_next ", page1.has_next())
print("has_previous ", page1.has_previous())
print("has_other_pages ", page1.has_other_pages())
print("next_page_number ", page1.next_page_number())

# %%
#### django.views.generic.list.ListView provides a builtin way to paginate the displayed list. You can do this by adding a paginate_by attribute to your view class, for example
from django.views.generic import ListView
from mocks.models import Contact

class ContactListView(ListView):
    paginate_by = 2
    model = Contact
# %%
#### Here’s an example using Paginator in a view function to paginate a queryset
from django.core.paginator import Paginator
from django.shortcuts import render

from mocks.models import Contact


def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})
# %%
