from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from blogapp.models import Users,Blog
# Create your views here.
def index(request):
	name='guest'
	return render(request,'index.html',{"name":name})
def login(request):
	return render(request,'login.html')
def sign(request):
	return render(request,'sign.html')
def mailing(request):
	ob=Blog.objects.all()
	res=''
	for x in ob:
		res=x.blogid
	return render(request,'mailing.html',{"res":res})
def main(request):
	return render(request,'admin.html')
def tryc(request):
	msg='Hey This is'
	return HttpResponse(msg)
@csrf_exempt
def check(request):
	a=request.POST.get('mail')
	b=request.POST.get('pass')
	msg=''
	ob=Users.objects.filter(email=a, password=b)
	if not ob:
		msg="<script> alert('Wrong Details');window.location.href='/login/';</script>"
	else:
		name=''
		ob1=Users.objects.filter(email=a)
		for y in ob1:
			name=y.email
		return render(request,'user.html',{"name":name})
	return HttpResponse(msg)
@csrf_exempt
def sendmail(request):
	a=request.POST.get('mail')
	b=request.POST.get('subject')
	c=request.POST.get('msg')
	recipient_list=[a,]
	email_from=settings.EMAIL_HOST_USER
	send_mail(b,c,email_from,recipient_list)
	res='mail send'
	return HttpResponse(res)
@csrf_exempt
def saveuser(request):
	name=request.POST.get('name')
	mail=request.POST.get('mail')
	amail=request.POST.get('amail')
	cat=request.POST.get('cat')
	aadhar=request.POST.get('aadhar')
	college=request.POST.get('college')
	address=request.POST.get('address')
	password=request.POST.get('pass')
	ob=Users(rollno=name,email=mail,aemail=amail,bcat=cat,aadhar=aadhar,college=college,address=address,password=password)
	ob.save()
	msg="<script> alert('Details Submitted Go for login');window.location.href='/login/';</script>"
	return HttpResponse(msg)
def forget(request):
	return render(request,'forget.html')
@csrf_exempt
def getpass(request):
	a=request.POST.get('mail')
	ob=Users.objects.filter(email=a)
	b='your password is: '
	w=''
	for x in ob:
		w=x.password
	recipient_list=[a,]
	email_from=settings.EMAIL_HOST_USER
	send_mail(b,w,email_from,recipient_list)
	res="<script> alert('password Send SuccessFully');window.location.href='/login/';</script>"
	return HttpResponse(res)
def postblog(request,uid):
	ud=uid
	return render(request,'postblog.html',{"uid":ud})
@csrf_exempt
def saveblog(request):
	bid=request.POST.get('blogid')
	uid=request.POST.get('userid')
	sub=request.POST.get('subject')
	btext=request.POST.get('blogtext')
	rat=0
	ob=Blog(blogid=bid,userid=uid,subject=sub,blogtext=btext,rating=rat)
	ob.save()
	# msg="<script> alert('Blog is Posted');window.location.href='/showmyblog/';</script>"
	ob=Blog.objects.all()
	return render(request,'blog.html',{"blog":ob,"d":uid})
	# return HttpResponse(msg)
def showblog(request):
	ob=Blog.objects.all()
	res="BLogs are : "
	res=res+"<table border='1' width='100%'>"
	res=res+"<tr>"
	res=res+"<td> Blog id</td>"
	res=res+"<td>User ID</td>"
	res=res+"<td>Subject</td>"
	res=res+"<td>Blog </td>"
	res=res+"<td>Rating</td>"
	res=res+"<td>Rate</td>"
	res=res+"</tr>"
	for x in ob:
		res=res+"<tr>"
		res=res+"<td><a href='/showbloguser/"+x.blogid+"'>"+x.blogid+"</a></td>"
		res=res+"<td>"+x.userid+"</td>"
		res=res+"<td>"+x.subject+"</td>"
		res=res+"<td>"+x.blogtext+"</td>"
		res=res+"<td>"+str(x.rating)+"</td>"
		res=res+"<td><input type='number' name='rate' max='10' min='0'></td>"
		res=res+"</tr>"
	res=res+"</table>"
	return HttpResponse(res)
def showbloguser(request,bid,uid):
	ob=Blog.objects.filter(blogid=bid)
	return render(request,'singleblog.html',{"blog":ob,"d":uid})
def showmyblog(request,uid):
	ob=Blog.objects.filter(userid=uid)
	return render(request,'blog.html',{"blog":ob,"d":uid})
def deleteblog(request,uid):
	ob=Blog.objects.filter(userid=uid)
	return render(request,'deleteblog.html',{"blog":ob,"d":uid})
def DeleteB(request,bid):
	ob=Blog.objects.filter(blogid=bid)
	ob.delete()
	res="<script> alert('Blog is Deleted');</script>"
	return HttpResponse(res)
def blog(request,uid):
	ob=Blog.objects.all()
	return render(request,'blog.html',{"blog":ob,"d":uid})
def showuser(request):
	ob=Users.objects.all()
	res="BLogs are : "
	res=res+"<table border='1' width='100%'>"
	for x in ob:
		res=res+"<tr>"
		res=res+"<td>"+x.email+"</td>"
		res=res+"<td>"+x.password+"</td>"
		res=res+"</tr>"
	res=res+"</table>"
	return HttpResponse(res)
def confg(request,uid):
	if uid=='guest':
		return render(request,'index.html')
	else:
		return render(request,'user.html',{"name":uid})