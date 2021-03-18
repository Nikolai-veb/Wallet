from django.contrib import admin

from .models import Wallet, Transactions


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "balance", "created")
    list_filter = ("name", "user", "created")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Transactions)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "wallet", "status", "created")
    list_filter = ("wallet",)
    list_editable = ("status",)
    search_fields = ("wallet",)
