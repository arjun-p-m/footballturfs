from django.shortcuts import render,HttpResponseRedirect
from capp.models import *
import os
import hashlib
import datetime
# Create your views here.
def INDEX(request):
	tur=turf_tb.objects.filter(status="1")
	trf=turf_tb.objects.all()
	return render(request,"index.html",{"data":tur,"data1":trf})

# def SEARCH(request):
# 	if request.method=="POST":
# 		name=request.POST['search']
# 		tur=turf_tb.objects.filter(name=name)
# 		if tur:
# 			return render(request,"single.html",{"data":tur})
# 		else:
# 			return HttpResponseRedirect("/product/")
# 	else:
# 		return render(request,"index.html")

def OWNERACCOUNT(request):
	if request.session.has_key("myid"):
		ow1=request.session["myid"]
		owner=register_tb.objects.filter(id=ow1)
		return render(request,"owneraccount.html",{"data":owner})
	else:
		return HttpResponseRedirect("/")

def USERACCOUNT(request):
	if request.session.has_key("userid"):
		us1=request.session["userid"]
		user=user_tb.objects.filter(id=us1)
		return render(request,"useraccount.html",{"data":user})
	else:
		return HttpResponseRedirect("/")

def REGISTER(request):
	if request.method=="POST":
		fname=request.POST['rFname']
		lname=request.POST['rLname']
		email=request.POST['rEmail']
		password=request.POST['rPassword']
		phone=request.POST['rPhone']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		check=register_tb.objects.filter(email=email)
		if check:
			return render(request,"register.html",{"msg":"this email has already registered"})
		else:
			add=register_tb(fname=fname,lname=lname,email=email,password=password,phone=phone,epassword=hashpass,status="0")
			add.save()
			return render(request,"register.html",{"msg":"successfully registered"})
	else:
		return render(request,"register.html")

def USER(request):
	if request.method=="POST":
		fname=request.POST['rFname']
		lname=request.POST['rLname']
		email=request.POST['rEmail']
		password=request.POST['rPassword']
		phone=request.POST['rPhone']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		check=user_tb.objects.filter(email=email)
		if check:
			return render(request,"user.html",{"msg":"this email has already registered"})
		else:
			add=user_tb(fname=fname,lname=lname,email=email,password=password,phone=phone,epassword=hashpass)
			add.save()
			return render(request,"user.html",{"msg":"successfully registered"})
	else:
		return render(request,"user.html")

def OWNERTAB(request):
	owner=register_tb.objects.all()
	return render(request,"ownertab.html",{"data":owner})

def USERTAB(request):
	user=user_tb.objects.all()
	return render(request,"usertab.html",{"data":user})

def OWNEREDIT(request):
	if request.method=='GET':
		id1=request.GET['uid']
		owner=register_tb.objects.filter(id=id1)
		if owner:
			return render(request,"ownerupdate.html",{"data":owner})
		else:
			return HttpResponseRedirect("/ownerview/")
	else:
		return HttpResponseRedirect("/ownerview/")

def OWNERUPDATE(request):
	if request.method=="POST":
		up=request.GET['uid']
		fname=request.POST['rFname']
		lname=request.POST['rLname']
		email=request.POST['rEmail']
		password=request.POST['rPassword']
		phone=request.POST['rPhone']
		register_tb.objects.filter(id=up).update(fname=fname,lname=lname,email=email,password=password,phone=phone)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/ownerview/")

def OWNERDELETE(request):
	id2=request.GET['uid']
	register_tb.objects.filter(id=id2).delete()
	return HttpResponseRedirect("/ownerview/")

def USEREDIT(request):
	if request.method=='GET':
		id15=request.GET['usid']
		user=user_tb.objects.filter(id=id15)
		if user:
			return render(request,"userupdate.html",{"data":user})
		else:
			return HttpResponseRedirect("/userview/")
	else:
		return HttpResponseRedirect("/userview/")

def USERUPDATE(request):
	if request.method=="POST":
		us2=request.GET['usid']
		fname=request.POST['rFname']
		lname=request.POST['rLname']
		email=request.POST['rEmail']
		password=request.POST['rPassword']
		phone=request.POST['rPhone']
		user_tb.objects.filter(id=us2).update(fname=fname,lname=lname,email=email,password=password,phone=phone)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/userview/")

def USERDELETE(request):
	id16=request.GET['usid']
	user_tb.objects.filter(id=id16).delete()
	return HttpResponseRedirect("/userview/")


def OWNEREDITPASSWORD(request):
	if request.method=='GET':
		id12=request.GET['uid']
		owner=register_tb.objects.filter(id=id12)
		if owner:
			return render(request,"ownerchangepassword.html",{"data":owner})
		else:
			return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/login/")

def OWNERCHANGEPASSWORD(request):
	if request.method=="POST":
		id13=request.GET['uid']
		password=request.POST['rPassword']
		register_tb.objects.filter(id=id13).update(password=password)
		return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/login/")

def FORGOTPASSWORD(request):
	if request.method=="POST":
		fname=request.POST['rFname']
		owner=register_tb.objects.filter(fname=fname)
		user=user_tb.objects.filter(fname=fname)
		if owner:
			return render(request,"ownerchangepassword.html",{"data":owner})
		elif user:
			return render(request,"userchangepassword.html",{"data":user})
		else:
			return HttpResponseRedirect("/login/")
	else:
		return render(request,"forgotpassword.html")

def USEREDITPASSWORD(request):
	if request.method=='GET':
		id17=request.GET['usid']
		user=user_tb.objects.filter(id=id17)
		if user:
			return render(request,"userchangepassword.html",{"data":user})
		else:
			return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/login/")

def USERCHANGEPASSWORD(request):
	if request.method=="POST":
		id18=request.GET['usid']
		password=request.POST['rPassword']
		user_tb.objects.filter(id=id18).update(password=password)
		return HttpResponseRedirect("/login/")
	else:
		return HttpResponseRedirect("/login/")

def LOGIN(request):
	if request.method=="POST":
		uname=request.POST['rFname']
		password=request.POST['rPassword']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		owner=register_tb.objects.filter(fname=uname,password=password,status="1")
		user=user_tb.objects.filter(fname=uname,password=password)
		if owner:
			for x in owner:
				if request.session.has_key("userid"):
					del request.session["userid"]
				request.session["myid"]=x.id
				request.session["myname"]=x.fname
				tur=turf_tb.objects.all()
				return render(request,"index.html",{"data":tur})
		elif user:
			for x in user:
				if request.session.has_key("myid"):
					del request.session["myid"]
				request.session["userid"]=x.id
				request.session["username"]=x.fname
				tur=turf_tb.objects.all()
				return render(request,"index.html",{"data":tur})
		else:
			return render(request,"login.html",{"msg":"invalid creditionals or not approved"})
	else:
		return render(request,"login.html")	
def logout(request):
	if request.session.has_key("myid"):
		del request.session["myid"]
		del request.session["myname"]
		return HttpResponseRedirect("/")
	elif request.session.has_key("userid"):
		del request.session["userid"]
		del request.session["username"]
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")

def PROFILE(request):
	if request.session.has_key("myid"):
		pr=request.session["myid"]
		profile=register_tb.objects.filter(id=pr)
		return render(request,"profile.html",{"data":profile})
	elif request.session.has_key("userid"):
		us=request.session["userid"]
		prof=user_tb.objects.filter(id=us)
		return render(request,"profile.html",{"data":prof})
	else:
		return HttpResponseRedirect("/")

def PRODUCTS(request):
	prd=turf_tb.objects.filter(status="1")
	return render(request,"products.html",{"data":prd})

def SINGLE(request):
	if request.session.has_key("myid"):
		if request.method=='GET':
			id11=request.GET['tid']
			trf=turf_tb.objects.filter(id=id11)
			tur=turf_tb.objects.all()
			if trf:
				return render(request,"single.html",{"data1":trf,"data2":tur})
			else:
				return HttpResponseRedirect("/product/")
		else:
			return HttpResponseRedirect("/product/")
	elif request.session.has_key("userid"):
		if request.method=='GET':
			id14=request.GET['tid']
			trf=turf_tb.objects.filter(id=id14)
			tur=turf_tb.objects.all()
			if trf:
				return render(request,"single.html",{"data1":trf,"data2":tur})
			else:
				return HttpResponseRedirect("/product/")
		else:
			return HttpResponseRedirect("/product/")
	else:
		return HttpResponseRedirect("/login/")

def ADDTURF(request):
	if request.session.has_key("myid"):
		if request.method=="POST":
			name=request.POST['tName']
			image=request.FILES['tImage']
			ii=request.session["myid"]
			owner=register_tb.objects.get(id=ii)
			# owner=request.POST['tOwner']
			address=request.POST['tAddress']
			# ratings=request.POST['tRatings']
			price=request.POST['tPrice']
			timing=request.POST['tTiming']
			add=turf_tb(name=name,image=image,address=address,owner=owner,price=price,timing=timing,status="0")
			add.save()
			return render(request,"addturf.html")
		else:
			return render(request,"addturf.html")
	else:
		return HttpResponseRedirect("/login/")

def TURFTAB(request):
	if request.session.has_key("myid"):
		ii=request.session["myid"]
		owner=register_tb.objects.get(id=ii)
		turf=turf_tb.objects.filter(status="1",owner=owner)
		if turf:
			return render(request,"turftab.html",{"data":turf})
		else:
			return render(request,"turftab.html",{"msg":"not approved"})
	else:
		return HttpResponseRedirect("/login/")

def EDITTURF(request):
	if request.method=='GET':
		id7=request.GET['tid']
		turf=turf_tb.objects.filter(id=id7)
		if turf:
			return render(request,"updateturf.html",{"data":turf})
		else:
			return  HttpResponseRedirect("/turftab/")
	else:
		return  HttpResponseRedirect("/turftab/")

def UPDATETURF(request):
	if request.method=="POST":
		up=request.GET['tid']
		name=request.POST['tName']
		# owner=request.POST['tOwner']
		address=request.POST['tAddress']
		ratings=request.POST['tRatings']
		price=request.POST['tPrice']
		timing=request.POST['tTiming']
		imgup=request.POST['img']
		if imgup=='yes':
			image1=request.FILES['tImage']
			oldrec=turf_tb.objects.filter(id=up)
			updrec=turf_tb.objects.get(id=up)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('successfully deleted')
			updrec.image=image1
			updrec.save()
		turf_tb.objects.filter(id=up).update(name=name,address=address,price=price,timing=timing)
		return HttpResponseRedirect("/turftab/")
	else:
		return HttpResponseRedirect("/turftab/")

def DELETETURF(request):
	id8=request.GET['tid']
	oldrec=turf_tb.objects.filter(id=id8)
	updrec=turf_tb.objects.get(id=id8)
	for x in oldrec:
		imgurl=x.image.url
		pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
		if os.path.exists(pathtoimage):
			os.remove(pathtoimage)
			print('successfully deleted')
		updrec.delete()
		turf_tb.objects.filter(id=id8).delete()
		return HttpResponseRedirect("/turftab/")
	else:
		return HttpResponseRedirect("/turftab/")

def PRODUCT(request):
	return render(request,"product.html")

def INDEX1(request):
	return render(request,"backend/index.html")

def SIGNIN(request):
	if request.method=="POST":
		uname=request.POST['aName']
		password=request.POST['aPassword']
		check=signin_tb.objects.filter(uname=uname,password=password)
		if check:
			for x in check:
				request.session["admid"]=x.id
				request.session["admname"]=x.uname
				return render(request,"backend/index.html",{"msg":"login successfull"})
		else:
			return render(request,"backend/signin.html",{"msg":"invalid credetionals"})
	else:
		return render(request,"backend/signin.html")
def signout(request):
	if request.session.has_key("admid"):
		del request.session["admid"]
		return HttpResponseRedirect('/1/')
	else:
		return HttpResponseRedirect('/1/')

def ADMPROFILE(request):
 	if request.session.has_key("admid"):
 		us=request.session["admid"]
 		admin=signin_tb.objects.filter(id=us)
 		return render(request,"backend/profile.html",{"data":admin})
 	else:
 		return HttpResponseRedirect("/1/")

def ADOWNERTAB(request):
	if request.session.has_key("admid"):
		owner=register_tb.objects.all()
		return render(request,"backend/ownertab.html",{"data":owner})
	else:
		return HttpResponseRedirect("/signin/")

def APPROVED(request):
	id5=request.GET['uid']
	user=register_tb.objects.filter(id=id5).update(status="1")
	return HttpResponseRedirect("/adownertab/")

def REJECTED(request):
	id6=request.GET['uid']
	user=register_tb.objects.filter(id=id6).update(status="2")
	return HttpResponseRedirect("/adownertab/")

def ADCARTTAB(request):
	if request.session.has_key("admid"):
		ii=request.session["admid"]
		# cart=cart_tb.objects.filter(name=ii,status="pending")
		myprd=cart_tb.objects.all().filter(status="0")
		grandtotal=0
		for x in myprd:
			grandtotal=float(x.totalprice)+grandtotal
		return render(request,'backend/carttab.html',{'gt':grandtotal,"data":myprd})
	else:
		return HttpResponseRedirect("/signin/")

def ADTURFTAB(request):
	if request.session.has_key("admid"):
		turf=turf_tb.objects.all()
		return render(request,"backend/turftab.html",{"data":turf})
	else:
		return HttpResponseRedirect("/signin/")

def ADUSERTAB(request):
	if request.session.has_key("admid"):
		user=user_tb.objects.all()
		return render(request,"backend/usertab.html",{"data":user})
	else:
		return HttpResponseRedirect("/signin/")

def ADAPPROVED(request):
	id9=request.GET['tid']
	turf=turf_tb.objects.filter(id=id9).update(status="1")
	return HttpResponseRedirect("/adturftab/")

def ADREJECTED(request):
	id10=request.GET['tid']
	turf=turf_tb.objects.filter(id=id10).update(status="2")
	return HttpResponseRedirect("/adturftab/")

def ADMPROFILE(request):
	if request.session.has_key("admid"):
		us=request.session["admid"]
		admin=signin_tb.objects.filter(id=us)
		return render(request,"backend/profile.html",{"data":admin})
	else:
		return HttpResponseRedirect("/1/")

def ADDCART(request):
	if request.session.has_key("userid"):
		if request.method=="POST":
			tids=request.GET['id']
			prd=turf_tb.objects.filter(id=tids)
			for x in prd:
				unitprice=x.price
			bdate=request.POST['time']
			btiming=request.POST['timing']
			total=int(unitprice)*float(btiming)
			date= datetime.datetime.now()
			ii=request.session["userid"]
			uid=user_tb.objects.get(id=ii)
			turfid=turf_tb.objects.get(id=tids)
			ii=user_tb.objects.get(id=ii)
			check=cart_tb.objects.filter(name=ii,turfid=tids,status="notordered")
			if check:
				for x in check:
					cartid=x.id
					print(cartid,"++++++++++++++")
					cart_tb.objects.filter(id=cartid).update(price=unitprice,totalprice=total,date=date,time=bdate,btiming=btiming)
					myprd=cart_tb.objects.all().filter(name=ii,status="notordered")
					grandtotal=0
					for x in myprd:
						grandtotal=float(x.totalprice)+grandtotal
					return render(request,'cart.html',{'msgkey':'cart updated','gt':grandtotal,"data":myprd})
			else:
				data=turf_tb.objects.all().filter(id=tids)
				for x in data:
					turf_owner=x.owner
					# t_owner=register_tb.objects.get(id=turf_owner)
				tocart=cart_tb(name=ii,owner=turf_owner,turfid=turfid,price=unitprice,totalprice=total,date=date,time=bdate,status="notordered",btiming=btiming)
				tocart.save()
				myprd=cart_tb.objects.all().filter(name=ii,status="notordered")
				grandtotal=0
				for x in myprd:
					grandtotal=float(x.totalprice)+grandtotal
				return render(request,'cart.html',{'msgkey':'Added to cart','gt':grandtotal,"data":myprd})
		else:
			return render(request,"login.html")
	else:
		return HttpResponseRedirect("/login/")

def CART(request):
	if request.session.has_key("userid"):
		ii=request.session["userid"]
		cart=cart_tb.objects.filter(name=ii,status="notordered")
		myprd=cart_tb.objects.all().filter(name=ii,status="notordered")
		grandtotal=0
		if myprd:
			for x in myprd:
				grandtotal=float(x.totalprice)+grandtotal
				return render(request,'cart.html',{'gt':grandtotal,"data":myprd})
		else:
			myprd=cart_tb.objects.all().filter(name=ii,status="payed")
			grandtotal=0
			for x in myprd:
				grandtotal=float(x.totalprice)+grandtotal
			return render(request,'cart.html',{'gt':grandtotal,"data":myprd})
	else:
		return HttpResponseRedirect("/login/")

def REMOVE(request):
	cid=request.GET['id']
	cart_tb.objects.filter(id=cid).delete()
	return HttpResponseRedirect("/cart/")

def REMOVEALL(request):
	if request.session.has_key("userid"):
		ii=request.session["userid"]
		cart_tb.objects.filter(name=ii,status="0").delete()
		return HttpResponseRedirect("/cart/")
	else:
		return HttpResponseRedirect("/cart/")

def CHECKOUT(request):
	if request.session.has_key("userid"):
		ii=request.session["userid"]
		cart=cart_tb.objects.filter(name=ii,status="0")
		myprd=cart_tb.objects.all().filter(name=ii,status="1")
		grandtotal=0
		for x in myprd:
			grandtotal=float(x.totalprice)+grandtotal
		return render(request,'checkout.html',{'gt':grandtotal,"data":myprd})
	else:
		return HttpResponseRedirect("/login/")

def INDEX2(request):
	return render(request,"payment/index.html")

def BOOKINGORDER(request):
	if request.session.has_key("myid"):
		ii=request.session["myid"]
		myprd=cart_tb.objects.all().filter(owner=ii,status="payed")
		grandtotal=0
		if myprd:
			for x in myprd:
				cid=x.id
				turfid=x.turfid
				user=x.name
				grandtotal=float(x.totalprice)+grandtotal
				return render(request,"bookingorder.html",{"data":myprd})
		else:
			# myprd=cart_tb.objects.all().filter(owner=ii,status="notavailable")
			# grandtotal=0
			# for x in myprd:
			# 	grandtotal=float(x.totalprice)+grandtotal
			return render(request,'bookingorder.html',{'gt':grandtotal,"data":myprd})
	else:
		return HttpResponseRedirect("/login/")

def AVAILABLE(request):
	id19=request.GET['cid']
	order=cart_tb.objects.filter(id=id19).update(status="confirmed")
	return HttpResponseRedirect("/bookedorders/")

def NOTAVAILABLE(request):
	id20=request.GET['cid']
	order=cart_tb.objects.filter(id=id20).update(status="notavailable")
	return HttpResponseRedirect("/bookingorder/")

def PAYMENT(request):
	if request.session.has_key("userid"):
		if request.method=="POST":
			nameoncard=request.POST['pcName']
			uid=request.session["userid"]
			uname=user_tb.objects.get(id=uid)
			date=datetime.datetime.now()
			check=cart_tb.objects.all().filter(name=uid,status='notordered')
			for x in check:
				cartid=x.id
				cid=cart_tb.objects.get(id=cartid)
				grandtotal=request.POST['total']
				payment=payment_tb(nameoncard=nameoncard,username=uname,cartid=cid,date=date,grandtotal=grandtotal,status="payed")
				payment.save()
			mypr=cart_tb.objects.all().filter(name=uid,status="notordered")
			for x in mypr:
				cart_tb.objects.all().filter(name=uid,status="notordered").update(status="payed")
			return HttpResponseRedirect("/cart/")
		else:
			grandtotal=request.GET['gt']
			return render(request,"payment/index.html",{'gt':grandtotal})
	else:
		return HttpResponseRedirect("/login/")

def BOOKING(request):
	if request.session.has_key("userid"):
		ii=request.session["userid"]
		# cart=cart_tb.objects.filter(name=ii,status="pending")
		myprd=cart_tb.objects.all().filter(name=ii,status="confirmed")
		grandtotal=0
		if myprd:
			for x in myprd:
				grandtotal=float(x.totalprice)+grandtotal
			return render(request,'bookingtab.html',{'gt':grandtotal,"data":myprd})
		else:
			# myprd=cart_tb.objects.all().filter(name=ii,status="notavailable")
			# for x in myprd:
			# 	grandtotal=float(x.totalprice)+grandtotal
			return render(request,'bookingtab.html',{'gt':grandtotal,"data":myprd})
	else:
		return HttpResponseRedirect("/login/")

def BOOKEDORDERS(request):
	if request.session.has_key("myid"):
		ii=request.session["myid"]
		myprd=cart_tb.objects.all().filter(owner=ii,status="confirmed")
		if myprd:
			for x in myprd:
				owner=x.owner
				user=x.name
				return render(request,'bookedorder.html',{"data":myprd})
		else:
			return render(request,"bookedorder.html")
	else:
		return HttpResponseRedirect("/login/")

def FEEDBACK(request):
	if request.session.has_key("userid"):
		id21=request.GET['tid']
		print(id21,"************")
		tur=turf_tb.objects.get(id=id21)
		print(tur,"************")
		turf=turf_tb.objects.all().filter(id=id21)
		for x in turf:
			ownerid=x.owner
		if request.method=="POST":
			ii=request.session["userid"]
			uid=user_tb.objects.get(id=ii)
			feedback=request.POST["rFeedback"]
			feed=feedback_tb(uid=uid,turfid=tur,owner=ownerid,feedback=feedback)
			feed.save()
			return render(request,"feedback.html")
		else:
			return render(request,"feedback.html",{"tid":id21})
	else:
		return HttpResponseRedirect("/login/")

def FEEDBACKED(request):
	if request.session.has_key("myid"):
		ii=request.session["myid"]
		feedb=feedback_tb.objects.all().filter(owner=ii)
		return render(request,"feededtab.html",{"data":feedb})
	else:
		return HttpResponseRedirect("/login/")

# def CONTACT(request):
# 	if request.method=="POST":
# 		name=request.POST['cName']
# 		email=request.POST['cEmail']
# 		message=request.POST['cMessage']
# 		add=contact_tb(name=name,email=email,message=message)
# 		add.save()
# 		return render(request,"contact.html")
# 	else:
# 		return render(request,"contact.html")

# def ADCONTACTTAB(request):
# 	if request.session.has_key("admid"):
# 		contact=contact_tb.objects.all()
# 		return render(request,"backend/contacttab.html",{"data":contact})
# 	else:
# 		return HttpResponseRedirect("/signin/")