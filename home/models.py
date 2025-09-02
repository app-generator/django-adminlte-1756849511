# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Devices(models.Model):

    #__Devices_FIELDS__
    ip = models.TextField(max_length=255, null=True, blank=True)
    hostname = models.TextField(max_length=255, null=True, blank=True)
    community = models.TextField(max_length=255, null=True, blank=True)
    device_type = models.ForeignKey(device_type, on_delete=models.CASCADE)
    model_id = models.ForeignKey(models, on_delete=models.CASCADE)
    cidade_id = models.ForeignKey(cidades, on_delete=models.CASCADE)
    last_status_pgp = models.TextField(max_length=255, null=True, blank=True)
    last_pgp = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Devices_FIELDS__END

    class Meta:
        verbose_name        = _("Devices")
        verbose_name_plural = _("Devices")


class Comandos(models.Model):

    #__Comandos_FIELDS__
    pgp = models.CharField(max_length=255, null=True, blank=True)
    diretorio = models.TextField(max_length=255, null=True, blank=True)
    device = models.ForeignKey(devices, on_delete=models.CASCADE)

    #__Comandos_FIELDS__END

    class Meta:
        verbose_name        = _("Comandos")
        verbose_name_plural = _("Comandos")


class Cidades(models.Model):

    #__Cidades_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    sigla_cidade = models.TextField(max_length=255, null=True, blank=True)
    codigo = models.CharField(max_length=255, null=True, blank=True)
    ddd = models.CharField(max_length=255, null=True, blank=True)
    hfc = models.CharField(max_length=255, null=True, blank=True)
    gpon = models.CharField(max_length=255, null=True, blank=True)
    dc_ldap = models.TextField(max_length=255, null=True, blank=True)

    #__Cidades_FIELDS__END

    class Meta:
        verbose_name        = _("Cidades")
        verbose_name_plural = _("Cidades")


class Vendors(models.Model):

    #__Vendors_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)

    #__Vendors_FIELDS__END

    class Meta:
        verbose_name        = _("Vendors")
        verbose_name_plural = _("Vendors")


class Device_Type(models.Model):

    #__Device_Type_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)

    #__Device_Type_FIELDS__END

    class Meta:
        verbose_name        = _("Device_Type")
        verbose_name_plural = _("Device_Type")


class Models(models.Model):

    #__Models_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    device_type_id = models.ForeignKey(device_type, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(vendors, on_delete=models.CASCADE)

    #__Models_FIELDS__END

    class Meta:
        verbose_name        = _("Models")
        verbose_name_plural = _("Models")



#__MODELS__END
