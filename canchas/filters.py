import django_filters
from .models import Cancha

import operator
from django.db.models import Q
from functools import reduce



class CanchaFilter(django_filters.FilterSet):
    servicios = django_filters.MultipleChoiceFilter(choices=Cancha.SERVICIOS_CHOICES, method='services_filter')
    class Meta:
        model = Cancha
        fields = ['servicios']

    def services_filter(self, queryset, name, values):
        #import pdb; pdb.set_trace()
        queryset = queryset.filter(reduce(operator.and_, (Q(servicios__contains=x) for x in values)))
        return queryset