from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Wallet, Transactions
from . import serializers


class ListWalletView(ListAPIView):
    """List Wallets"""
    queryset = Wallet.objects.all()
    serializer_class = serializers.WalletSerializers


class DetailWalletView(RetrieveAPIView):
    """Single Wallet"""
    queryset = Wallet.objects.all()
    serializer_class = serializers.DetailWalletSerializers


class CreateWalletView(CreateAPIView):
    """Create new Transaction"""
    serializer_class = serializers.CreateWalletSerializers


class DeleteWalletView(DestroyAPIView):
    """Delete Wallet"""
    serializer_class = serializers.DeleteWalletSerializers
    queryset = Wallet.objects.all()


class UpdateWalletView(UpdateAPIView):
    """Update Wallet"""
    serializer_class = serializers.UpdateWalletSerializers


class ListTransactionView(ListAPIView):
    """List Transactions"""
    queryset = Transactions.objects.all()
    serializer_class = serializers.TransactionSerializers


class CreateTransactionsView(CreateAPIView):
    """Creates a new transaction and changes the wallet balance in a positive direction"""
    serializer_class = serializers.CreateTransactionSerializers


class DebitTransactionsView(CreateAPIView):
    """Creates a new transaction and changes the balance of the wallet in the negative direction"""
    serializer_class = serializers.DebitTransactionSerializers


class DeleteTransactionsView(DestroyAPIView):
    """Delete Transaction"""
    queryset = Transactions.objects.all()
    serializer_class = serializers.DeleteTransactionSerializers
