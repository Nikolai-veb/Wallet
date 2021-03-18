from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListWalletView.as_view()),
    path('wallets/<int:pk>/', views.DetailWalletView.as_view()),
    path('add_wallet/', views.CreateWalletView.as_view()),
    path('delete_wallet/<int:pk>/', views.DeleteWalletView.as_view()),
    path('update_wallet/<int:pk>/', views.UpdateWalletView.as_view()),

    path('transactions/', views.ListTransactionView.as_view()),
    path('add_transaction/', views.CreateTransactionsView.as_view()),
    path('debit_transaction/', views.DebitTransactionsView.as_view()),
    path('delete_transaction/<int:pk>', views.DeleteTransactionsView.as_view()),

]