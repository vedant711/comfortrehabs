from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from .models import Joints, Contact, Products, People

def index(request):
    try:
        people = People.objects.all()
        context = {'people':people}
        return render(request,'index.html',context)
    except:
        print('Ran into some error')

def pdf(request):
    try:
        return redirect('/static/uploads/catalog/catalog.pdf')
    except:
        print('Ran into some error')


def about(request):
    try:
        return render(request,'about.html')
    except:
        print('Ran into some error')


def contact(request):
    try:
        return render(request,'contact.html')
    except:
        print('Ran into some error')


def products(request):
    try:
        products = Products.objects.all()
        context = {'products':products}
        return render(request,'products.html',context)
    except:
        print('Ran into some error')


def products_joint(request,joint):
    try:
        products = Products.objects.filter(joint__joint__icontains = joint).all()
        context = {'products':products}
        print(products)
        return render(request,'products.html',context)
    except:
        print('Ran into some error')


def contact_data(request):
    # try:
        if request.method == 'POST':
            # messages.add_message(messages.info)
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            description = request.POST['description']
            lead = Contact()
            lead.name = name
            lead.phone = phone
            lead.email = email
            lead.message = description
            lead.save()
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            print('sending mail')

            msg = MIMEMultipart()
            msg.set_unixfrom('author')
            msg['From'] = 'yatin@comfortrehabs.com'
            msg['To'] = 'yatin@comfortrehabs.com'
            msg['Subject'] = f'New Query from {email}'
            message = f'You have a new query from {name}. The details for the same are as follows:\nPhone: {phone}\nEmail: {email}\nMessage: {description}'
            msg.attach(MIMEText(message))

            mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
            mailserver.ehlo()
            mailserver.login('yatin@comfortrehabs.com', 'yatingohil@1234')

            mailserver.sendmail('yatin@comfortrehabs.com','yatin@comfortrehabs.com',msg.as_string())

            mailserver.quit()

            messages.info(request,'Query Registered Successfully')
            return redirect('/contact')
    # except:
    #     print('Ran into some error')





# Create your views here.