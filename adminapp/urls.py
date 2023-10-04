from django.urls import path
from.import views

urlpatterns = [
    path('adminindex/',views.adminindex,name='adminindex'),
    path('',views.adminhome,name='adminhome'),
    path('category/',views.category,name='category'),
    path('viewcategory/',views.viewcategory,name='viewcategory'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('catupdate/<int:id>/',views.catupdate,name='catupdate'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('product/',views.product,name='product'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('pedit/<int:id>/',views.pedit,name='pedit'),
    path('pupdate/<int:id>/',views.pupdate,name='pupdate'),
    path('pdelete/<int:id>/',views.pdelete,name='pdelete'),
    path('viewcustomer/',views.viewcustomer,name='viewcustomer'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('vieworders/',views.vieworders,name='vieworders'),
    path('sendconfirmation/<int:orderid>/',views.sendconfirmation,name='sendconfirmation'),
    path('productcat/',views.productcat,name='productcat'),
    path('history/',views.history,name='history'),
    path('reject/<int:orderid>/',views.reject,name='reject')







]


