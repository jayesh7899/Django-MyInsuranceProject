from django.shortcuts import render
from customer.models import SignUp,Categary,Policy,PolicyRecord,Question1
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import date

def myhome(request):
	return render(request,'index.html')

def custviewcat(request):
	c1=Categary.objects.all()
	data={
				'data':c1
		}
	return render(request,'custviewcat.html',data)

def adminviewpolicyupdate(request):
	if request.method=='GET':
		id=request.GET['id']
		status=request.GET['status']
		p1=PolicyRecord.objects.get(id=id)
		p1.status=status
		p1.save()
		
		return HttpResponseRedirect('/adminviewpolicy')
def adminviewpolicy(request):

	p1=PolicyRecord.objects.all()
	data={
			'data':p1
	}


	return render(request,'adminviewpolicy.html',data)

def adminapporvedpolicy(request):

	p1=PolicyRecord.objects.all()
	data={
			'data':p1
	}
	return render(request,'adminapporvedpolicy.html',data)

def adminquestion(request):

	p1=Question1.objects.all()
	data={
			'data':p1
	}
	return render(request,'adminquestion.html',data)

def adminreplay(request):

	us=request.session['name']
	p1=Question1.objects.filter(customer=us)
	data={
			'data':p1
	}
	return render(request,'questionreplay.html',data)

def adminquestionupdate(request):
	if request.method=='GET':

		id=request.GET['id']
		que=request.GET['que']
		print(id,que)
		data={
				'id':id,
				'que':que
		}
		return render(request,'adminquestionupdate.html',data)
	if request.method=='POST':
		id=request.POST['id']
		que=request.POST['que']
		rep=request.POST['rep']
		q1=Question1.objects.get(id=id)
		q1.admin_comment=rep
		q1.save()
		return HttpResponseRedirect('/adminleftpanel')

	

def adminrejectedpolicy(request):

	p1=PolicyRecord.objects.all()
	data={
			'data':p1
	}
	return render(request,'adminrejectedpolicy.html',data)

def adminpendingpolicy(request):

	p1=PolicyRecord.objects.all()
	data={
			'data':p1
	}
	return render(request,'adminpendingpolicy.html',data)

def custpendingpolicy(request):

	us=request.session['name']
	p1=PolicyRecord.objects.filter(customer=us)
	data={
			'data':p1
	}
	return render(request,'custpendingpolicy.html',data)

def historypolicy(request):
	return render(request,'historypolicy.html')

def custviewpolicy(request):
	p1=PolicyRecord.objects.all()
	data={
			'data':p1
	}
	return render(request,'custviewpolicy.html',data)
def viewpolicy(request):
	p1=Policy.objects.all()
	data={
			'data':p1
	}
	return render(request,'viewpolicy.html',data)

def delpolicy(request):
	p1=Policy.objects.all()
	data={
				'data':p1
		}
		
	try:
		
		if request.method=='GET':
			print("hi")
			id=request.GET['id']
			print(id)
			p2=Policy.objects.get(id=id)
			p2.delete()
			return HttpResponseRedirect('/policydash')

		

	except Exception as e1:
		print("Del policy=",e1)
	return render(request,'delpolicy.html',data)

def updatepolicy(request):
	try:
		id=request.GET['id1']
		p1=Policy.objects.get(id=id)
		data={
		  'd1':p1
		}

		if request.method=='POST':
			id=request.POST['id']
			cat=request.POST['cat']
			pname=request.POST['pname']
			sumassu=request.POST['sumassu']
			premium=request.POST['premium']
			tenure=request.POST['tenure']
			print(id,cat,pname,sumassu,premium,tenure)
			p1=Policy(id=id,cat=cat,name=pname,sumassu=sumassu,premium=premium,tenure=tenure)
			p1.save()
			print("2")
			return HttpResponseRedirect('/policydash')

		return render(request,'updatepolicy.html',data)
	except Exception as e1:
		print("update=",e1)

def addpolicy(request):
	try:
		if request.method=='POST':
			cat=request.POST['cat']
			name=request.POST['pname']
			sumassu=request.POST['sumassu']
			premium=request.POST['premium']
			tenure=request.POST['tenure']
			p1=Policy(cat=cat,name=name,sumassu=sumassu,premium=premium,tenure=tenure)
			p1.save()
			return HttpResponseRedirect('/policydash')

	except Exception as e1:
		print("add policy=",e1)

	c1=Categary.objects.only('cat')
	print(c1)
	data={
	  'cat':c1
	}
	return render(request,'addpolicy.html',data)

def policydash(request):
	return render(request,'policydash.html')

def viewupdatepolicy(request):
	p1=Policy.objects.all()
	data={
			'data':p1
	}
	return render(request,'viewpolicyupdate.html',data)

def delcat(request):
	try:
		c1=Categary.objects.all()
		data={
				'data':c1
		}
		
		if request.method=='GET':
			id=request.GET['id']
			c2=Categary(id=id)
			c2.delete()

		


		return render(request,'delcat.html',data)

	except Exception as e1:
		print("del cat=",e1)
	return render(request,'delcat.html',data)

def mycatupdate(request):
	if request.method=='GET':
		id=request.GET.get('id')
		cat=request.GET.get('cat')
		dt=request.GET.get('dt')
		print(id,cat,dt)
		data={
		'id':id,
		'cat':cat,
		'dt':dt
		}

		return render(request,'UpdateCat.html',data)

def catupdate(request):
	if request.method=='POST':

		id=request.POST.get('id')
		cat=request.POST.get('cat')
		dt=request.POST.get('dt')
		print(id,cat,dt)
		c1=Categary(id=id,cat=cat,dt=dt)
		c1.save()
	
	c1=Categary.objects.all()
	data={
				'data':c1
	}
	return render(request,'catupdate.html',data)

def viewcat(request):
	try:
		c1=Categary.objects.all()
		data={
				'data':c1
		}
		return render(request,'viewcat.html',data)

	except Exception as e1:
		print("view cat=",e1)
	


def addcat(request):
	data={
			'cat':'',
			'dt':''
	}
	try:
		if request.method=='POST':
			cat=request.POST.get('cat')
			dt=request.POST.get('dt')
			print(cat,dt)
			c1=Categary(cat=cat,dt=dt)
			c1.save()
			return HttpResponseRedirect('/mycategary')
		

	except Exception as e1:
		print("Categary=",e1)
	return render(request,'Addcat.html',data)

def mycategary(request):
	return render(request,'categary.html')

def custupdate(request):
	try:
		id=request.GET['id']
		s1=SignUp.objects.get(id=id)
		data={
					'data':s1
		}
		return render(request,'custupdate.html',data)
	except Exception as e1:
		print("Update",e1)

	return render(request,'custupdate.html')
def custdelete(request):
	try:
		id=request.GET['id']
		print("id=",id)
		s1=SignUp.objects.get(id=id)
		s1.delete()
		return HttpResponseRedirect('/viewcust')

	except Exception as e1:
		print("delete=",e1)
	return render(request,'view-cust.html')

def logout(request):
	del request.session['name']
	
	request.session['name']=None
	p=request.session['name']
	print("p",p)
	return render(request,'index.html')

def mysignup(request):

	try:
		if request.method=='POST':
			fname=request.POST.get('fname')
			lname=request.POST.get('lname')
			contact=request.POST.get('contact')
			address=request.POST.get('address')
			email=request.POST.get('email')
			user=request.POST.get('user')
			password=request.POST.get('password')
			pic=request.FILES['pic'];

			s1=SignUp(fname=fname,lname=lname,contact=contact,address=address,email=email,user=user,password=password,pic=pic)
			s1.save()
			return HttpResponseRedirect('/custlogin')

	except Exception as e1:
		print("SingUp Error=",e1)
	return render(request,'singup.html')

def custlogin(request):
	try:
		if request.method=='POST':
			user=request.POST.get("user")
			pass1=request.POST.get("pass")
			if SignUp.objects.filter(user=user,password=pass1):
				s1=SignUp.objects.get(user=user)
				pic=s1.pic
				request.session['name']=str(user)
				request.session['pic']=str(pic)
				return HttpResponseRedirect('/leftpanel')
			else:
				return HttpResponseRedirect('/custlogin')

	except Exception as e1:
		print("Cust Error=",e1)
	return render(request,'custlogin.html')

def adminlogin(request):
	try:
		if request.method=='POST':
			user=request.POST.get("user")
			pass1=request.POST.get("pass")
			#print(user,pass1)
			#u1=User.objects.get()

			#print(u1.username,u1.password)
			#print(u1.username==user and u1.password==pass1)
			if user=='Admin' and pass1=='admin':
				request.session['name']=str(user)
				return HttpResponseRedirect('/adminleftpanel')
			else:
				return HttpResponseRedirect('/adminlogin')

	except Exception as e1:
		print("Cust Error=",e1)
	return render(request,'adminlogin.html')

def contact(request):
	return render(request,'contact.html')

def askquestion(request):
	try:
		if request.method=='POST':
			que=request.POST['que']
			user=request.session['name']
			today =date.today()
			print(que,user,today)
			q1=Question1(customer=user,description=que,creation_date=today)
			q1.save()
			return HttpResponseRedirect('/leftpanel')

	except Exception as e1:
		print("Ask=",e1)

	return render(request,'askquestion.html')

def leftpanel(request):
	us=request.session['name']
	if us==None:
		return HttpResponseRedirect('/')

	return render(request,'leftpanel.html')
def applypolicysave(request):
	name1=request.session['name']
	pname=request.GET['pname']
	today = date.today()
	p1=PolicyRecord(customer=name1,policy=pname,creation_date=today)
	p1.save()
	return HttpResponseRedirect('/leftpanel')

def applypolicy(request):
	try:

		p1=Policy.objects.all()
		data={
				'data':p1
		}

	except Exception as e1:
		print("Apply policy=",e1)
	return render(request,'applypolicy.html',data)

def adminleftpanel(request):
	data={}
	try:
		us=request.session['name']
		if us==None:
			return HttpResponseRedirect('/')

		s1=SignUp.objects.count()
		p1=Policy.objects.count()
		c1=Categary.objects.count()
		q1=Question1.objects.count()
		pen=PolicyRecord.objects.filter(status='Pending').count()
		ap1=PolicyRecord.objects.filter(status='Apporved').count()
		rej=PolicyRecord.objects.filter(status='Rejected').count()
		data={
				'user':s1,
				'policy':p1,
				'cat':c1,
				'que':q1,
				'pen':pen,
				'ap1':ap1,
				'rej':rej
		}

	except Exception as e1:
		print("Admin panel=",e1)
	return render(request,'adminleftpanel.html',data)

def viewcust(request):
	data={}
	try:
		s1=SignUp.objects.all()
		data={
				'data':s1
		}

	except Exception as e1:
		print("Admin panel=",e1)
	
	return render(request,'view-cust.html',data)

def mycustupdate(request):
	try:
		if request.method=='POST':
			id=request.POST.get('id')
			fname=request.POST.get('fname')
			lname=request.POST.get('lname')
			contact=request.POST.get('contact')
			address=request.POST.get('address')
			email=request.POST.get('email')
			pic=request.FILES['pic'];

			s1=SignUp(id=id,fname=fname,lname=lname,contact=contact,address=address,email=email,pic=pic)
			s1.save()
			return HttpResponseRedirect('/adminleftpanel')

	except Exception as e1:
		print("SingUp Error=",e1)
	return HttpResponseRedirect('/custupdate')