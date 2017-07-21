# -*- encoding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .compiler import compile


def DjangoDSLValidator(value):
    if not value:
        raise ValidationError(_("DSL query must not be an empty string"))

    if not value.strip():
        raise ValidationError(_("DSL query must not be an empty string"))

    try:
        compile(value)
    except Exception as e:
        raise ValidationError(
            _("DSL compilation failed (%(exception)s)"),
            params={"exception": e})
