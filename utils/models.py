from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels

class Settings(models.Model):
    fee_price_toman = models.IntegerField(_("هزینه ویزیت به تومان"), default=85000)

class DateBasic(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(_('تاریخ ساخت'), auto_now_add=True)
    updated_at = models.DateTimeField(_('تاریخ بروزرسانی'), auto_now=True)

    created_at_jalali = jmodels.jDateTimeField(_('تاریخ ساخت'), auto_now_add=True)
    updated_at_jalali = jmodels.jDateTimeField(_('تاریخ بروزرسانی'), auto_now=True)
