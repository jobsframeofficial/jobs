from django.shortcuts import render
from django.http import HttpResponse
from jobs1.models import Job,Catagories,Courses_and_certification,Visitors,Categary_label
from math import ceil
from .forms import NameForm
from jobs1.queries import NumberOfRecordsBy
from django.http import HttpResponseRedirect
from datetime import date
import uuid


# Create your views here.
def details_page(request):
    
    # if Visitors.objects.filter(date = date.today()).count() ==0:
    #     Visitors.objects.create(date = date.today()).save()
    # count = Visitors.objects.get(date = date.today())
    
    # count.detail_page = count.detail_page+1
    # count.save()
    return render(request,'jobs1/details_page.html')
def index(request):
    # if Visitors.objects.filter(date = date.today()).count() ==0:
    #     Visitors.objects.create(date = date.today()).save()
    # count = Visitors.objects.get(date = date.today())
    # count.detail_page = count.detail_page+1
    # count.save()
    no_of_pages=8
    
    
    data = Job.objects.order_by('id').reverse()[:no_of_pages]

    page_list=[]
    counts = int(Job.objects.count()/no_of_pages)
    for i in range(1,counts+1):
        page_list.append(i)

    data2 = Courses_and_certification.objects.all()
    data3=Job.objects.filter(catagories__in = Catagories.objects.values('id').filter(catagory='competative_coding'))

    #params = {'jobs':data,'certs':data2,'comp_coding':data3,'page_list':page_list,'category_name':'all_jobs','no_of_records':data.count()}
    return render(request, 'jobs1/index.html',NumberOfRecordsBy.jobs_by_category('all_jobs',1))

def index1(request,category_name,page_number):
    # if Visitors.objects.filter(date = date.today()).count() ==0:
    #     Visitors.objects.create(date = date.today()).save()
    # count = Visitors.objects.get(date = date.today())
    # count.index_page = count.index_page+1
    # count.save()
    return render(request, 'jobs1/index.html',NumberOfRecordsBy.jobs_by_category(category_name,page_number))



def about_us(request):
    # if Visitors.objects.filter(date = date.today()).count() ==0:
    #     Visitors.objects.create(date = date.today()).save()
    # count = Visitors.objects.get(date = date.today())
    # count.detail_page = count.detail_page+1
    # count.save()
    
    print(uuid.getnode())
    return render(request,'jobs1/about_us.html')

def contact_us(request):
    # if Visitors.objects.filter(date = date.today()).count() ==0:
    #     Visitors.objects.create(date = date.today()).save()
    # count = Visitors.objects.get(date = date.today())
    # count.detail_page = count.detail_page+1
    # count.save()
    return render(request,'jobs1/contact_us.html')



def detailed1(request,job_id,post_type):
    # if Visitors.objects.filter(date = date.today()).count() ==0:
    #     Visitors.objects.create(date = date.today()).save()
    # count = Visitors.objects.get(date = date.today())
    # count.detail_page = count.detail_page+1
    # count.save()
    params={}
    no_of_rows=8
    categories = Categary_label.objects.all()[:15]
    jobs = Job.objects.order_by('id').reverse()[:no_of_rows]
    if post_type=="jobs":
        data = Job.objects.filter(id=job_id)
        related_jobs = Job.objects.filter(profile_name__icontains = data[0].profile_name)[:20]
        params = {'company_name':data[0].company_name,
            'looking_for':data[0].looking_for,
            'profile_name' :data[0].profile_name,
            'description' :data[0].description,
            'location' :data[0].location,
            'exp_from' :data[0].exp_from,
            'exp_to' :data[0].exp_to,
            'post_date' :data[0].post_date,
            'last_date' :data[0].last_date,
            'apply_link' :data[0].apply_link,
            'website' :data[0].website,
            'organised_by' :"",
            'certification_name' :"",
            'jobs':jobs,
            'related_jobs':related_jobs,
            'categories':categories
            }
    else:
        data = Courses_and_certification.objects.filter(id=job_id)
        related_jobs = Job.objects.filter(profile_name__icontains = data[0].certification_name)
        params = {'company_name':"",
                'looking_for':"",
        'profile_name' :"",
        'description' :data[0].description,
        'location' :"",
        'exp_from' :"Not",
        'exp_to' :"Needed",
        'post_date' :data[0].post_date,
        'last_date' :data[0].last_date,
        'apply_link' :data[0].apply_link,
        'website' :data[0].website,
        'organised_by' :data[0].organised_by,
        'certification_name' :data[0].certification_name,
        'jobs':jobs,
        'related_jobs':related_jobs,
        'categories':categories}
    return render(request, 'jobs1/details_page.html',params)



def get_name(request,category_name,page_number):
    # if this is a POST request we need to process the form data
    company_name=""
    location=""
    experience=""
    if request.method == 'POST':
        print("post")
        
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            company_name1 = form.cleaned_data['company_name']
            profile = form.cleaned_data['profile']
            location = form.cleaned_data['location']
            experience = form.cleaned_data['experience']
            params = NumberOfRecordsBy.search_records(company_name1,profile,location,experience,category_name,page_number)
            print("company name:"+company_name1)
            print("profile name:"+profile)
            print("experience:"+form.cleaned_data['experience'])
            print("location:"+form.cleaned_data['location'])
            #print(form)
                        
            #params={'company_name':company_name1,'experience':experience,'location':form.cleaned_data['location'],'jobs':data,'certs':data2,'comp_coding':data3,'page_list':page_list,'category_name':category_name}
            # redirect to a new URL:
            return render(request, 'jobs1/index.html',params)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print("else")
    print("complete")
    #params={'company_name':form.cleaned_data['company_name'],'form':form}
    return render(request, 'jobs1/index.html')
