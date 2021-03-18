from decimal import Decimal

from rest_framework import serializers

from .models import Wallet, Transactions


class CreateTransactionSerializers(serializers.ModelSerializer):
    """Create Serializers Transactions"""

    class Meta:
        model = Transactions
        fields = ('wallet', 'comment', 'summa', 'status')

    def validate(self, attrs):
        wallet = Wallet.objects.get(name=attrs['wallet'])
        wallet.balance = wallet.balance + attrs['summa']
        wallet.save()
        return attrs


class DebitTransactionSerializers(serializers.ModelSerializer):
    """Debit Serializers Transactions"""

    class Meta:
        model = Transactions
        fields = ('wallet', 'comment', 'summa', 'status')

    def validate(self, attrs):
        wallet = Wallet.objects.get(name=attrs['wallet'])
        wallet.balance = wallet.balance - attrs['summa']
        wallet.save()
        return attrs


class DeleteTransactionSerializers(serializers.ModelSerializer):
    """Delete Serializers Transactions"""

    class Meta:
        model = Transactions
        fields = ('wallet', "id")


class TransactionSerializers(serializers.ModelSerializer):
    """Serializers model Transactions"""

    class Meta:
        model = Transactions
        fields = ('id', 'comment', 'summa', 'status', 'created')


class CreateWalletSerializers(serializers.ModelSerializer):
    """Create Serializer Wallet"""

    class Meta:
        model = Wallet
        fields = ('user', 'name')


class DeleteWalletSerializers(serializers.ModelSerializer):
    """Delete Serializer Wallet"""

    class Meta:
        model = Wallet
        fields = ('user', 'name')


class UpdateWalletSerializers(serializers.ModelSerializer):
    """Update Serializer Wallet"""

    class Meta:
        model = Wallet
        fields = ('user', 'name')


class WalletSerializers(serializers.ModelSerializer):
    """Serializer model Wallet"""
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Wallet
        fields = ('id', 'user', 'name', 'created')


class DetailWalletSerializers(serializers.ModelSerializer):
    """ Single Wallet Serializer"""
    transactions = TransactionSerializers(many=True)

    class Meta:
        model = Wallet
        fields = ('user', 'name', 'balance', 'created', 'transactions')
