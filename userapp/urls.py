from django.urls import path
from.import views

urlpatterns = [
     path('userindex/',views.userindex,name='userindex'),
     path('userhome/',views.userhome,name='userhome'),
     path('productview/<str:category>/',views.productview,name='productview'),
     path('singleview/<int:sid>/',views.singleview,name='singleview'),
     path('registration/',views.registration,name='registration'),
     path('cartdata/<int:id>/',views.cartdata,name='cartdata'),
     path('checkout/',views.checkout,name='checkout'),
     path('userlogin',views.userlogin,name='userlogin'),
     path('userlogout',views.userlogout,name='userlogout'),  
     path('feedback/',views.feedback,name='feedback'),
     path('comments/',views.comments,name='comments'),
     path('cart/',views.cart,name='cart'),
     path('cdelete/<int:id>/',views.cdelete,name='cdelete'),
     path('checkoutdata/',views.checkoutdata,name='checkoutdata'),
     path('proceedcheck/',views.proceedcheck,name='proceedcheck'),
     path('success/',views.success,name='success'),
     path('login/',views.login,name='login'),
     path('carticon/<int:id>/',views.carticon,name='carticon'),
     path('wishlist/<int:id>/',views.wishlist,name='wishlist'),
     path('viewwishlist/',views.viewwishlist,name='viewwishlist'),
     path('removewishlist/<int:id>/',views.removewishlist,name='removewishlist'),
     path('vieworder/',views.vieworder,name='vieworder'),
     path('historyproductview/',views.historyproductview,name='historyproductview'),
     path('cartupdate/',views.cartupdate,name='cartupdate'),
     path('buy/<int:id>/',views.buy,name='buy'),
     path('buynow/',views.buynow,name='buynow'),
     path('reset/',views.reset,name='reset'),
     path('resetpass/',views.resetpass,name='resetpass'),
     path('paysuccess/',views.paysuccess,name='paysuccess')


    









]