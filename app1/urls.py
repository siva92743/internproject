from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.home, name='home'),

    #############################ADMIN##############################
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('trainer_register', views.trainer_register, name='trainer_register'),
    path('trainer_view', views.trainer_view, name='trainer_view'),
    path('trainer_update/<int:id>', views.trainer_update, name='trainer_update'),
    path('trainer_delete/<int:id>', views.trainer_delete, name='trainer_delete'),
    path('equipments_add', views.equipments_add, name='equipments_add'),
    path('equipments_view', views.equipments_view, name='equipments_view'),
    path('equipments_update/<int:id>', views.equipments_update, name='equipments_update'),
    path('equipments_delete/<int:id>', views.equipments_delete, name='equipments_delete'),
    path('add_bill', views.add_bill, name='add_bill'),
    path('view_bill', views.view_bill, name='view_bill'),
    path('customer_view', views.customer_view, name='customer_view'),
    path('login', views.login, name='login'),
    path('login_view', views.login_view, name='login_view'),
    path('add_attendance', views.add_attendance, name='add_attendance'),


    ######################################TRAINER#########################################
    path('trainer_panel', views.trainer_panel, name='trainer_panel'),
    path('trainer_customer_view', views.trainer_customer_view, name='trainer_customer_view'),
    path('trainer_view_trainer', views.trainer_view_trainer, name='trainer_view_trainer'),
    path('equipments_view_trainer', views.equipments_view_trainer, name='equipments_view_trainer'),




    #######################################CUSTOMER###############################################
    path('customer_register', views.customer_register, name='customer_register'),
    path('customer_panel', views.customer_panel, name='customer_panel'),
    path('trainer_view_customer', views.trainer_view_customer, name='trainer_view_customer'),
    path('equipments_view_customer', views.equipments_view_customer, name='equipments_view_customer'),
    path('user_customer_view', views.user_customer_view, name='user_customer_view'),
    path('view_bill_customer', views.view_bill_customer, name='view_bill_customer'),

    path('mark/<int:id>', views.mark, name='mark'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('day_attendance/<date>', views.day_attendance, name='day_attendance'),
    path('view_attendance_user', views.view_attendance_user, name='view_attendance_user'),
    path('log_out_view', views.log_out_view, name='log_out_view'),
    path('batch', views.batch, name='batch'),
    path('view_batch', views.view_batch, name='view_batch'),
    path('delete_batch/<int:id>', views.delete_batch, name='delete_batch'),






    path('ajax/load_batch', views.load_batch, name='load_batch'),

    path('profile', views.profile, name='profile'),
    path('payment', views.payment, name='payment'),

]