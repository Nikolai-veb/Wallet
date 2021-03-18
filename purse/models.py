from django.contrib.auth.models import User
from django.db import models

from PIL import Image
from django.urls import reverse
from django.utils.text import slugify


class Wallet(models.Model):
    name = models.CharField("Wallet", max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    balance = models.DecimalField("Balance", max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField("Created", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now=True)
    slug = models.SlugField('URL', max_length=200, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse("wallet_detail", kwargs={"wl_slug": self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Wallet, self).save(*args, **kwargs)


class Transactions(models.Model):
    wallet = models.ForeignKey(Wallet, verbose_name="Wallet", on_delete=models.CASCADE, related_name="transactions")
    comment = models.CharField("Comment", max_length=500)
    summa = models.DecimalField("Summa", max_digits=10, decimal_places=2)
    status = models.BooleanField("Status", default=True)
    updated = models.DateTimeField("Updated", auto_now=True)
    created = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ['-created']


