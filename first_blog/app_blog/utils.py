from django.db.models import Count
from .models import *

auth_menu = [{'title': "Add review", 'url_name': 'add_review'}

             ]
menu = [{'title': "About us", 'url_name': 'about'},
        {'title': "Contact us", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('filmreview'))
        user_menu_auth = auth_menu.copy() + menu.copy()
        user_menu_info = menu.copy()
        context['auth_menu'] = user_menu_auth
        context['menu'] = user_menu_info
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


