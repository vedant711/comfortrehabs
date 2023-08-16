from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from rehabs.models import Products, Joints, People, Contact
from deep_translator import GoogleTranslator
import os

def handle_uploaded_file(f,id):  
    with open(f'rehabs/static/uploads/products/{id}.jpg', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def handle_uploaded_people_file(f,id):  
    with open(f'rehabs/static/uploads/people/{id}.jpg', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def login1(request):
    if request.method == 'POST':
        username, password = request.POST['username'],request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            # return redirect(nxt)
            return redirect('/super-root-user/contact')
        else:messages.info(request,'Incorrect Username or Password')
    return render(request,'login.html')

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def contact(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    return render(request,'contact_root.html',context)


@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def product(request):
    products = Products.objects.all()
    joints = Joints.objects.all()
    context = {'products':products,'joints':joints}
    return render(request,'products_root.html',context)

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def product_add(request):
    if request.method == 'POST':
        img = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        joint = request.POST['joint']
        new_product = Products()
        new_product.title = title
        new_product.description= description
        translator = GoogleTranslator(source='auto',target='zh-CN')
        new_product.chinese_description = translator.translate(description)
        translator = GoogleTranslator(source='auto',target='ar')
        new_product.arabic_description = translator.translate(description)
        translator = GoogleTranslator(source='auto',target='sw')
        new_product.swahili_description = translator.translate(description)
        new_product.joint = Joints.objects.get(id=int(joint))
        new_product.save()
        handle_uploaded_file(img,new_product.id)
        new_product.img_path = f'uploads/products/{new_product.id}.jpg'
        new_product.save()
    return redirect('/super-root-user/products')

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def product_edits(request,id):
    if request.method == 'POST':
        img = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        joint = request.POST['joint']
        new_product = Products.objects.get(id=id)
        new_product.title = title
        new_product.description= description
        translator = GoogleTranslator(source='auto',target='zh-CN')
        new_product.chinese_description = translator.translate(description)
        translator = GoogleTranslator(source='auto',target='ar')
        new_product.arabic_description = translator.translate(description)
        translator = GoogleTranslator(source='auto',target='sw')
        new_product.swahili_description = translator.translate(description)
        new_product.joint = Joints.objects.get(id=int(joint))
        handle_uploaded_file(img,id)
        new_product.img_path = f'uploads/products/{id}.jpg'
        new_product.save()
        
        # new_product.save()
        return redirect('/super-root-user/products')
    product = Products.objects.get(id=id)
    joints = Joints.objects.all()
    context = {'product':product,'joints':joints}

    return render(request,'edit_product.html',context)

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def people_edit(request,id):
    if request.method == 'POST':
        img = request.FILES['image']
        name = request.POST['name']
        description = request.POST['description']
        designation = request.POST['designation']
        linkedin = request.POST['linkedin']
        new_product = People.objects.get(id=id)
        new_product.name = name
        new_product.description= description
        new_product.designation = designation
        new_product.linkedin = linkedin
        handle_uploaded_people_file(img,id)
        new_product.img_path = f'uploads/people/{id}.jpg'
        new_product.save()
        return redirect('/super-root-user/people')
    people = People.objects.get(id=id)
    context = {'people':people}
    return render(request,'edit_people.html',context)

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def people_add(request):
    if request.method == 'POST':
        img = request.FILES['image']
        name = request.POST['name']
        description = request.POST['description']
        designation = request.POST['designation']
        linkedin = request.POST['linkedin']
        new_product = People()
        new_product.name = name
        new_product.description= description
        new_product.designation = designation
        new_product.linkedin = linkedin

        new_product.save()
        handle_uploaded_people_file(img,new_product.id)
        new_product.img_path = f'uploads/people/{new_product.id}.jpg'
        new_product.save()
    return redirect('/super-root-user/people')

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def joints_add(request):
    if request.method == 'POST':
        joint = request.POST['joint']
        new_joint = Joints()
        new_joint.joint = joint
        new_joint.save()
    return redirect('/super-root-user/joints')


@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def joints(request):
    joints = Joints.objects.all()
    print(joints)
    context = {'joints':joints}
    return render(request,'joints_root.html',context)

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def people(request):
    people = People.objects.all()
    context = {'people':people}
    return render(request,'people_root.html',context)

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def edit_joints(request,id):
    if request.method == 'POST':
        joint = request.POST['joint']
        new_joint = Joints.objects.get(id=id)
        new_joint.joint = joint
        new_joint.save()
        return redirect('/super-root-user/joints')
    joint = Joints.objects.get(id=id)
    context = {'joint':joint}

    return render(request,'edit_joint.html',context)

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def remove_product(request,id):
    Products.objects.get(id=id).delete()
    os.remove(f'rehabs/static/uploads/products/{id}.jpg')
    return redirect('/super-root-user/products')

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def remove_people(request,id):
    People.objects.get(id=id).delete()
    os.remove(f'rehabs/static/uploads/people/{id}.jpg')
    return redirect('/super-root-user/people')

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def remove_contact(request,id):
    Contact.objects.get(id=id).delete()
    return redirect('/super-root-user/contact')

@csrf_exempt
@staff_member_required(login_url='/super-root-user')
def remove_joint(request,id):
    Joints.objects.get(id=id).delete()
    return redirect('/super-root-user/joints')

def logout_root(request):
    logout(request)
    return redirect('/super-root-user/')



