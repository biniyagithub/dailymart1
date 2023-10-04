from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from adminapp.models import *
from userapp.models import *
from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.conf import settings
from django.contrib import messages

# Create your views here.
def userindex(request):
    if 'u_id' in request.session:
        cart = Cart.objects.filter(status=0).count()
    data1 = Product.objects.all()
    data2 = Category.objects.all()
    uid = request.session.get('u_id')
    vdata = Order.objects.filter(userid=uid)
    user_status = Order.objects.filter(userid=uid).count()
    user_st=None
    if user_status >= 5:
        user_st = "Platinum User"
    elif user_status == 3 :
        user_st = "Golden User"
    else:
        user_st = "Silver User"
    return render(request,'userindex.html',{'data1':data1,'data2':data2,'vdata':vdata,'user_st':user_st})

def userhome(request):
    if 'u_id' in request.session:
       cart = Cart.objects.filter(status = 0).count()
       data1 = Product.objects.all()
       data2 = Category.objects.all()
       return render(request,'user_home.html',{'data1':data1,'data2':data2,'cart':cart})
    else:
        data1 = Product.objects.all()
        data2 = Category.objects.all()
        return render(request,'user_home.html',{'data1':data1,'data2':data2,})


def productview(request,category):
    if 'u_id' in request.session:
        cart = Cart.objects.filter(status=0).count()
        
        if(category == "all"):
            data1 = Product.objects.all()
            data2 = Category.objects.all()
        else:
            data1 = Product.objects.filter(category=category)
            data2 = Category.objects.all()
        return render(request,'product_view.html',{'data1':data1,'data2':data2,'cart':cart})
    else:
    
    
        if(category == "all"):
            data1 = Product.objects.all()
            data2 = Category.objects.all()
        else:
            data1 = Product.objects.filter(category=category)
            data2 = Category.objects.all()
        return render(request,'product_view.html',{'data1':data1,'data2':data2})
       


def singleview(request,sid):
    if 'u_id' in request.session:
        cart = Cart.objects.filter(status=0).count()
        sdata = Product.objects.filter(id=sid)
        data2 = Category.objects.all()
        return render(request,'single_pview.html',{'sdata':sdata,'cart':cart,'data2':data2})
    else:
        sdata = Product.objects.filter(id=sid)

        return render(request,'single_pview.html',{'sdata':sdata})

def registration(request):
    if request.method=="POST":
        rname1 = request.POST.get('fname')
        rname2 = request.POST.get('lname')
        rcountry = request.POST.get('country')
        raddress = request.POST.get('address')
        rtown = request.POST.get('town')
        rstate = request.POST.get('state')
        rpincode = request.POST.get('pincode')
        rphone = request.POST.get('phone')
        remail = request.POST.get('email')
        rpassword = request.POST.get('password')
        cnf = request.POST.get('pass1')
        user_id = request.session.get('u_id')
        rdata = Customer(uname1=rname1,uname2=rname2,country=rcountry,address=raddress,town=rtown,state=rstate,pincode=rpincode,phone=rphone,email=remail,password=rpassword)
        rdata.save()
       
    return render(request,'customer_registration.html') 

def cart(request):
    if 'u_id' in request.session:
        data1 = Product.objects.all()
        data2 = Category.objects.all()
        cart = Cart.objects.filter(status=0).count()
        user_id=request.session.get('u_id')
        data=Cart.objects.filter(userid=user_id,status=0)
        s = Cart.objects.filter(userid=user_id,status=0).aggregate(Sum('total'))
        return render(request,'cart.html',{'data1':data1,'data2':data2,'data':data,'s':s,'cart':cart})
    else:
        return render(request,"user_login.html",{'msg':"u r not login yet"})

def cartdata(request,id):
    if 'u_id' in request.session:
        if request.method == "POST":
            user_id=request.session.get('u_id')
            quantity=request.POST.get('quantity')
            total=request.POST.get('total')
            data=Cart(userid=Customer.objects.get(id=user_id),productid=Product.objects.get(id=id),quantity=quantity,total=total)
            data.save()
            return redirect('cart')
        return render(request,'user_home.html')
    else:
        return render(request,"user_login.html",{'msg':"u r not login yet"})
    
def carticon(request,id):
     if 'u_id' in request.session:
        cart = Cart.objects.filter(status=0).count()
        if request.method == "POST":
            user_id=request.session.get('u_id')
            quantity=1
            total=request.POST.get('price')
            data=Cart(userid=Customer.objects.get(id=user_id),productid=Product.objects.get(id=id),quantity=quantity,total=total)
            data.save()
            return redirect('cart')
        return render(request,'user_home.html',{'cart':cart})
     else:
        return render(request,"user_login.html",{'msg':"u r not login yet"})

    

def checkout(request):
    user_id=request.session.get('u_id')
    if 'u_id' in request.session:
        data1 = Product.objects.all()
        data2 = Category.objects.all()
        cart = Cart.objects.filter(userid=user_id,status=0).count()
        print(cart)
        data=Cart.objects.filter(userid=user_id,status=0)
        s = Cart.objects.filter(userid=user_id,status=0).aggregate(Sum('total'))
        print (s)
        return render(request,'checkout.html',{'data1':data1,'data2':data2,'data':data,'s':s,'cart':cart})
    return redirect('userhome')

stripe.api_key=settings.STRIPE_SECRET_KEY
def checkoutdata(request):
     if request.method=="POST":
         user_id=request.session.get('u_id')
         cname1 = request.POST.get('fname')
         cname2 = request.POST.get('lname')
         ccountry = request.POST.get('country')
         caddress = request.POST.get('address')
         ctown = request.POST.get('town')
         cstate = request.POST.get('state')
         cpincode = request.POST.get('pincode')
         cphone = request.POST.get('phone')
         cemail = request.POST.get('email')
         request.session['checkout_name1']=cname1
         request.session['checkout_name2']=cname2
         request.session['checkout_country']=ccountry
         request.session['checkout_address']=caddress
         request.session['checkout_town']=ctown
         request.session['checkout_state']=cstate
         request.session['checkout_pin']=cpincode 
         request.session['checkout_phone']=cphone
         request.session['checkout_email']=cemail
         

         cdata = Cart.objects.filter(userid=user_id,status=0)
         product_id = None
         cart_id = None
         cart_total_amount = None
         cart_quantity = None 
         for i in cdata:
           
            product_id = i.productid.id
            cart_id = i.id
            cart_total_amount = i.total
            cart_quantity = i.quantity
           
         request.session['cart_productid'] = product_id
         request.session['cart_total'] = cart_total_amount
         request.session['quantity_cart'] = cart_quantity
         
         payment_variable = Cart.objects.filter(userid=user_id,status=0)
         total_amount = 0
         user_name = request.session.get('name1_u')
         for i in payment_variable:
            total_amount += i.total
            
         session = stripe.checkout.Session.create(
         payment_method_types = ['card'],
         line_items=[{
                'price_data':{
                    'currency': 'inr',
                    'product_data':{
                        'name': user_name,
                    },
                    'unit_amount':int(total_amount)*100,
                   
                },
                'quantity':1,
         }],
         mode='payment',
         success_url = "http://127.0.0.1:8000/paysuccess?session_id={CHECKOUT_SESSION_ID}",
         cancel_url = "http://127.0.0.1:8000/pay_cancel",
         client_reference_id = cart_id
         )
         Cart.objects.filter(userid=user_id).update(status=1)
         return redirect(session.url, code=303)
     return render(request,'checkout.html')

def paysuccess(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    cart_id1 = session.client_reference_id
    user_id=request.session.get('u_id')
    cname1=request.session.get('checkout_name1')
    cname2=request.session.get('checkout_name2')
    ccountry=request.session.get('checkout_country')
    caddress=request.session.get('checkout_address')
    ctown=request.session.get('checkout_town')
    cstate=request.session.get('checkout_state')
    cpincode=request.session.get('checkout_pin')
    cphone=request.session.get('checkout_phone')
    cemail=request.session.get('checkout_email')
    product_id=request.session.get('cart_productid')
    cart_quantity=request.session.get('cart_total')
    cart_total_amount=request.session.get('quantity_cart')
    data=Checkout(userid=Customer.objects.get(id=user_id),cartid=Cart.objects.get(id=cart_id1),uname1=cname1,uname2=cname2,country=ccountry,address=caddress,town=ctown,state=cstate,pincode=cpincode,phone=cphone,email=cemail)
    data.save()
    Order.objects.create(userid=Customer.objects.get(id=user_id),productid=Product.objects.get(id = product_id), cartid = Cart.objects.get(id=cart_id1), quantity=cart_quantity, total=cart_total_amount)
    return render(request,'success_page.html')

def login(request):
    return render(request,'user_login.html')

def userlogin(request):
    data1 = Product.objects.all()
    data2 = Category.objects.all()
    if request.method == "POST":
        useremail=request.POST.get('email')
        userpassword=request.POST.get('password')
        if Customer.objects.filter(email=useremail,password=userpassword).exists():
           data = Customer.objects.filter(email=useremail,password=userpassword).values('uname1','uname2','country','address' , 'town'  ,'state' ,'phone', 'id').first()
           request.session['name1_u'] = data['uname1']
           request.session['name2_u'] = data['uname2'] 
           request.session['country_u'] = data['country']
           request.session['u_id'] = data['id']
           request.session['address_u'] = data['address']
           request.session['town_u'] = data['town']
           request.session['state_u'] = data['state']
           request.session['phone_u'] = data['phone']
           request.session['useremail_u'] = useremail
           request.session['password_u'] = userpassword
           return redirect('userhome') 
        else:
            return render(request,'user_login.html',{'msg':'invalid user credentials'})
    else:
        return render(request,'user_login.html',{'data1':data1,'data2':data2})

def userlogout(request):
    del request.session['name1_u']
    del request.session['name2_u']
    del request.session['country_u']
    del request.session['u_id']
    del request.session['address_u']
    del request.session['town_u']
    del request.session['state_u']
    del request.session['phone_u']
    del request.session['useremail_u']
    del request.session['password_u']
    return redirect('userlogin')

def feedback(request):
     data1 = Product.objects.all()
     data2 = Category.objects.all()
     if request.method=="POST":
         cusname = request.POST.get('name')
         cusemail = request.POST.get('email')
         msg = request.POST.get('message')
         data= Contacts (name=cusname,email=cusemail,message=msg,)
         data.save()
     return render(request,'contact.html',{'data1':data1,'data2':data2})

def comments(request):
    if 'u_id' in request.session:
         cart = Cart.objects.filter(status=0).count()
         data1 = Product.objects.all()
         data2 = Category.objects.all()
         return render(request,'about.html',{'data1':data1,'data2':data2,'cart':cart})
    else:
         data1 = Product.objects.all()
         data2 = Category.objects.all()
         return render(request,'about.html',{'data1':data1,'data2':data2,'cart':cart})


def cdelete(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('cart')

def proceedcheck(request):
    cart = Cart.objects.filter(status=0).count()
        
    user_id=request.session.get('u_id')
    pdata=Cart.objects.filter(userid=user_id,status=0)
    productdata = Product.objects.all()
    s = Cart.objects.filter(userid=user_id,status=0).aggregate(Sum('total'))
    print (s)
    return render(request,'checkout.html',{'pdata':pdata,'s':s,'cart':cart,'productdata':productdata})



def wishlist(request,id):
    wdata = Product.objects.filter(id=id).update(status=1)
    return redirect('viewwishlist')

def viewwishlist(request):
     if 'u_id' in request.session:
        cart = Cart.objects.filter(status=0).count()
        data1 = Product.objects.all()
        data2 = Category.objects.all()    
        wdata1 = Product.objects.filter(status=1)
        return render(request,'wishlist.html',{'data1':data1,'data2':data2,'wdata1':wdata1,'cart':cart})
     else:
        return redirect('userlogin')
     

def removewishlist(request,id):
    Product.objects.filter(id=id).update(status=2)
    return redirect('viewwishlist')

def vieworder(request):
    if 'u_id' in request.session:
        cart = Cart.objects.filter(status=0).count()
        data1 = Product.objects.all()
        data2 = Category.objects.all()     
        uid = request.session.get('u_id')
        vdata = Order.objects.filter(userid=uid)
    return render(request,'view_orderhistory.html',{'data1':data1,'data2':data2,'vdata':vdata,'cart':cart})


def historyproductview(request):
    if 'u_id' in request.session:
        hcart = Cart.objects.filter(status=0).count()
        hdata = Product.objects.all()
        data2 = Category.objects.all()
    return render(request,'order_productview.html',{'hcart':hcart,'hdata':hdata,'data2':data2})

@csrf_exempt
def cartupdate(request):
    if request.method=="POST":
        cartid=request.POST['pid']
        q=request.POST['qty']
        p=request.POST['price']
        t=float(q)*float(p)
        Cart.objects.filter(id=cartid).update(total=t,quantity=q)
        return HttpResponse()
    

def buy(request,id):
     if 'u_id' in request.session:
        buy_data = Product.objects.filter(id=id)
        sb =  Product.objects.get(id=id).price
        print(sb)
        return render(request,'buynow.html',{'sb':sb,'id':id,'buy_data':buy_data}) 
     else:
         return redirect('userlogin')
       
    
stripe.api_key=settings.STRIPE_SECRET_KEY
def buynow(request): 
      if request.method=="POST":
         user_id=request.session.get('u_id')
         productid = request.POST.get('productid')
         uname = request.POST.get('fname')
         baddress = request.POST.get('address')
         bpincode = request.POST.get('pincode')
         bphone = request.POST.get('phone')
         bmail = request.POST.get('email')
         bdate = request.POST.get('date')
         request.session['buy_name']=uname
         request.session['buy_address']=baddress
         request.session['buy_pincode']=bpincode
         request.session['buy_phone']=bphone
         request.session['buy_mail']=bmail
         request.session['buy_date']=bdate
      
         payment_variable = Product.objects.filter(id=productid)
         total_amount = 0
         user_name = request.session.get('name1_u')
         for i in payment_variable:
            total_amount += i.price
         request.session['buy_total']=total_amount
         session = stripe.checkout.Session.create(
         payment_method_types = ['card'],
         line_items=[{
                'price_data':{
                    'currency': 'inr',
                    'product_data':{
                         
                        'name': user_name,
                    },
                    
                    'unit_amount':int(total_amount)*100,
                   
                },
                'quantity':1,
         }],
         
         mode='payment',
         success_url = "http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}",
         cancel_url = "http://127.0.0.1:8000/pay_cancel",
         client_reference_id = productid
         )
         
         Cart.objects.filter(userid=user_id).update(status=1)
         return redirect(session.url, code=303)
      return render(request,'buynow.html') 

def success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    product_id = session.client_reference_id
    print(product_id)
    user_id=request.session.get('u_id')
    uname=request.session.get('buy_name')
    baddress =request.session.get('buy_address')
    bpincode =request.session.get('buy_pincode')
    bphone =request.session.get('buy_phone')
    bmail =request.session.get('buy_mail')
    bdate =request.session.get('buy_date')
    total_amount = request.session.get('buy_total')
    data=Buy(userid=Customer.objects.get(id=user_id),productid=Product.objects.get(id=product_id),user_name=uname,address=baddress,pin=bpincode,contact=bphone,user_email=bmail,date=bdate)
    data.save()
    Order.objects.create(userid=Customer.objects.get(id=user_id), productid=Product.objects.get(id=product_id),date=bdate,total=total_amount,quantity=1)
    data1 = Product.objects.all()
    data2 = Category.objects.all()
    return render(request,'success_page.html',{'data1':data1,'data2':data2})

def reset(request):
     return render(request,'reset.html')

def resetpass(request):
    if request.method=="POST":
        usermail = request.POST.get('mail')
        passw1 = request.POST.get('pass1')
        passw2 = request.POST.get('pass2')
        if Customer.objects.filter(email=usermail).exists():
            if passw1!=passw2:
                messages.error(request, 'Password Incorrect')
                return redirect('reset')
            else:
                rdata = Reset(email1=usermail,password1=passw1,password2=passw2)
                rdata.save()
                Customer.objects.filter(email=usermail).update(password=passw2)
        else:
            messages.warning(request, 'you have not registerd ,you must signup') 
    return redirect('userlogin')


         

        

    





    






















