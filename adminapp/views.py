from django.shortcuts import render,redirect
from adminapp.models import *
from userapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def adminindex(request):
    return render(request,'admin_index.html')

def adminhome(request):
    cat = Category.objects.all().count()
    cat1 = Product.objects.all().count()
    cat2 = Customer.objects.all().count()
    cat3 = Checkout.objects.all().count()
    cat4 = Contacts.objects.all().count()
    return render(request,'admin_home.html',{'cat':cat,'cat1':cat1,'cat2':cat2,'cat3':cat3,'cat4':cat4})


def category(request):
     if request.method=="POST":
        name1 = request.POST.get('name')
        image1 = request.FILES['image']
        description1 = request.POST.get('description')
        data = Category(cname=name1,cimage=image1,cdescription=description1)
        data.save()
     return render(request,'add_category.html')

def viewcategory(request):
    cdata = Category.objects.all()
    return render(request,'view_category.html',{'cdata':cdata})

def edit(request,id):
    edata=Category.objects.filter(id=id)
    return render(request,'edit.html',{'edata':edata})

def catupdate(request,id):
    if request.method=="POST":
        name2 = request.POST.get('name')
        description2 = request.POST.get('description')
        try:
            img_c = request.FILES.get('image')
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).cimage
        Category.objects.filter(id=id).update(cname=name2,cdescription=description2,cimage=file)
        return redirect('viewcategory')


def delete(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('viewcategory')

def productcat(request):
    data = Category.objects.all()
    return render(request,'add_product.html',{'data':data})

def product(request):
     if request.method=="POST":
        namep = request.POST.get('name')
        imagep = request.FILES['image']
        pricep = request.POST.get('price')
        category = request.POST.get('category')
        stock = request.POST.get('stock')
        quantityp = request.POST.get('quantity')
        pdata = Product(pname=namep,pimage=imagep,price=pricep,category=category,stock=stock,quantity=quantityp)
        pdata.save()
     return redirect('productcat')



def viewproduct(request):
    vpdata = Product.objects.all()
    return render(request,'view_product.html',{'vpdata':vpdata})

def pedit(request,id):
    edata=Product.objects.filter(id=id)
    return render(request,'product_edit.html',{'edata':edata})

def pupdate(request,id):
    if request.method=="POST":
        name3 = request.POST.get('name')
        price1 = request.POST.get('price')
        stock = request.POST.get('stock')
        quantity1 = request.POST.get('quantity')
        category = request.POST.get('category')
        try:
            img_c = request.FILES.get('image')
            if img_c:  # Check if the 'image' key exists in request.FILES
                fs = FileSystemStorage()
                file = fs.save(img_c.name, img_c)
            else:
                file = Product.objects.get(id=id).pimage
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).pimage
        Product.objects.filter(id=id).update(pname=name3, price=price1, category=category, stock=stock, quantity=quantity1, pimage=file)
    return redirect('viewproduct')


def pdelete(request,id):
    Product.objects.filter(id=id).delete()
    return redirect('viewproduct')

def viewcustomer(request):
    cdata = Customer.objects.all()
    return render(request,'view_customers.html',{'cdata':cdata})

def viewfeedback(request):
    fdata = Contacts.objects.all()
    return render(request,'view_feedback.html',{'fdata':fdata})

def vieworders(request):
    viewdata = Order.objects.filter(status=0)
    return render(request,'view_order.html',{'viewdata':viewdata})

def reject(request,orderid):
    Order.objects.filter(id=orderid).update(status=2)
    return redirect('vieworders')


def sendconfirmation(request,orderid):
    customerdetails = Order.objects.get(id=orderid)
    customeremail = customerdetails.userid.email
    print (customeremail)
    Order.objects.filter(id=orderid).update(status=1)
    data1 = Order.objects.get(id=orderid)
    quantity1 = data1.quantity
    producdetails1 = data1.productid.id
    print(producdetails1)
    productdetails = Product.objects.get(id=producdetails1)
    
    
    productdetails.stock -= quantity1
    productdetails.save()
    template = render_to_string('email_template.html')
    email = EmailMessage(
            'Greetings',
            template,
            settings.EMAIL_HOST_USER,
            [customeremail],
        )
    email.fail_silently = False
    email.send()
    return redirect('vieworders')


def history(request):
    cdata = Order.objects.all()
    return render(request,'view_history.html',{'cdata':cdata})



    




    