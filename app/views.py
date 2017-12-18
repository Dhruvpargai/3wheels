# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponseRedirect , HttpResponse
from .models import Users

# Create your views here.
def newuserfunc(request):
    if request.method == 'POST':
        #fetching data
        name =request.POST.get("name", "")
        email_id =request.POST.get("email_id", "")
        dob =request.POST.get("dob", "")
        aadhar=request.POST.get("aadhar","")
        area=request.POST.get("area","")
        wallet=request.POST.get("wallet","")

        flag=0

        if(name=="" or email_id=="" or dob =="" or aadhar=="" or area=="" or wallet==""):
           flag=1
           return HttpResponse("All field should be filled !!! Try Register Again ");

        #addind data to database
        if(flag==0):
            try:
                u=Users()
                u.name=name
                u.email_id=email_id
                u.dob=dob
                u.aadhar=aadhar
                u.area=area
                u.wallet=wallet
                u.save()
       

            except IntegrityError as e:
                return HttpResponse('Aadhar and Email_ID must be unique');
    return render(request,'newuser.html');
