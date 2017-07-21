# -*- encoding: utf-8 -*-
from django.db.models.fields import TextField

from .compiler import compile
from .validators import DjangoDSLValidator


class DjangoDSLField(TextField):
    default_validators = [DjangoDSLValidator]

    def __init__(self, verbose_name=None, name=None, **kwargs):
        super(DjangoDSLField, self).__init__(
            verbose_name, name, **kwargs)
