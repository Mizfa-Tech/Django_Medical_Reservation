from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models import DateBasic
from django_jalali.db import models as jmodels

class Session(DateBasic):
    class Meta:
        verbose_name = _('وقت')
        verbose_name_plural = _('وقت ها')
        
    class Status(models.TextChoices):
        SET = 'SET' , _('ثبت شده')
        DONE = 'DONE', _('جلسه انجام شد')
        ABSENT = 'ABSENT', _('نیامد')
        
    patient = models.ForeignKey('mediuser.CustomUser', on_delete=models.CASCADE, verbose_name=_('بیمار'), related_name="ses_patient")
    datetime = jmodels.jDateTimeField(verbose_name=_('زمان و تاریخ وقت'), null=True, blank=True)
    status = models.CharField(_("وضعیت"), max_length=50, default='ثبت شده', choices=Status.choices)
    fee = models.IntegerField(_("هزینه ویزیت به تومان"), default=85000)
    
class Prescription(DateBasic):
    class Meta:
        verbose_name = _('نسخه')
        verbose_name_plural = _('نسخه ها')
        
    patient = models.ForeignKey('mediuser.CustomUser', on_delete=models.CASCADE, verbose_name=_('بیمار'), related_name="pre_patient")
    session = models.ForeignKey('Session', on_delete=models.CASCADE, verbose_name=_('وقت'), related_name="pre_session")
    description = models.TextField(verbose_name=_('توصبحات نسخه'))
        
