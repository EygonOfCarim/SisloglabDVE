from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from unidades.models import Unidade


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unidade = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_created_by', default=datetime.now())
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_updated_by', default=datetime.now())

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return str(self.user)
