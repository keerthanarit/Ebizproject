from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", password="", database="dbstore")
c = db.cursor()

# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    msg = ""
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        s = "select count(*) from tbllogin where username='" + username + "'"
        c.execute(s)
        i = c.fetchone()
        if i[0] > 0:
            s = "select * from tbllogin where username='" + username + "'"
            c.execute(s)
            i = c.fetchone()
            if i[1] == password:
                request.session["username"] = username
                if i[2] == "admin":
                    return HttpResponseRedirect("/adminhome")
                elif i[2] == "user":
                    return HttpResponseRedirect("/userhome")
                elif i[2] == "staff":
                    return HttpResponseRedirect("/staffhome")
                else:
                    msg = "You are not authenticated to login"
            else:
                msg = "Wrong password"
        else:
            msg = "User does not exist"
    return render(request, "login.html", {"msg": msg})
def register(request):
    msg = " "
    if request.POST:
        name = request.POST.get('name')
        place = request.POST.get('place')
        address = request.POST.get('address')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        s = "select count(*) from tbllogin where username='" + username + "'"
        c.execute(s)
        col = c.fetchone()
        print(col)
        if col[0]:
            msg = "Already Registered"
        else:
            print(name)
            print(email)
            s = "insert into tblregister(name,place,address,mob,email,username,password,cpassword) values('" + name + "','" + place + "','" + address + "','" + mob + "','" + email + "','" + username + "','" + password + "','" + cpassword + "')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Error"
            else:
                msg = "Registration Succesfull"
                s = "insert into tbllogin(username,password,role) values('" + username + "','" + password + "','user')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Error"
            else:
                msg = "Registration Succesfull"
            #return HttpResponseRedirect("/login")
    return render(request, "register.html", {"msg": msg})
def adminhome(request):
    return render(request,"adminhome.html")
def userhome(request):
    return render(request,"userhome.html")
def adminviewuserlist(request):
    s = "select * from tblregister"
    c.execute(s)
    x = c.fetchall()
    return render(request,"adminviewuserlist.html",{"x": x})
def admindeleteuser(request):
    username = request.GET.get("username")
    print(username)
    s = "delete tblregister,tbllogin from tblregister join tbllogin on tblregister.username= tbllogin.username  where username='" + str(username) + "'"

    try:
        print("no")
        c.execute(s)
        db.commit()
    except:
        msg = "Error"
    else:
        print("yes")
        msg = "Deleted"
    return HttpResponseRedirect("/adminviewuserlist")
def adminaddservicecategory(request):
    msg = " "
    s = "select * from tblservicecategory"
    c.execute(s)
    x = c.fetchall()
    if request.POST:
        category = request.POST.get('category')
        s = "insert into tblservicecategory(category) values('" + category + "')"

        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Error"
        else:
            msg = "Registration Succesfull"
            s = "select * from tblservicecategory"
            c.execute(s)
            x = c.fetchall()
    return render(request, "adminaddservicecategory.html", {"msg": msg,"x":x})
#def admindeletecategory(request):
#    cid = request.GET.get("cid")
#   s = "delete from tblservicecategory where cid='" + cid + "'"
#    try:
#        print("no")
#        c.execute(s)
#        db.commit()
#    except:
#        msg = "Error"
#    else:
#        print("yes")
#        msg = "Deleted"
#        s = "select * from tblservicecategory"
#        c.execute(s)
#        x = c.fetchall()
#        #return HttpResponseRedirect("/adminaddservicecategory")
#    return render(request, "adminaddservicecategory.html", {"msg": msg, "x": x})
def adminaddplans(request):
    msg = " "
    s = "select * from tblplans"
    c.execute(s)
    x = c.fetchall()
    if request.POST:
        validity = request.POST.get('validity')
        price = request.POST.get('price')

        s = "insert into tblplans(validity,price) values('" + validity + "','" + price + "')"

        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Error"
        else:
            msg = "Registration Succesfull"
            s = "select * from tblplans"
            c.execute(s)
            x = c.fetchall()
    return render(request, "adminaddplans.html", {"msg": msg, "x": x})
def userviewprofile(request):
    msg = " "
    username = request.session.get("username")
    s = "select * from tblregister where username='" + username + "'"
    c.execute(s)
    x = c.fetchall()

    return render(request, "userviewprofile.html", {"x": x})
def useraddservices(request):

    return render(request,"useraddservices.html")
def useraddadvertisement(request):
    return render(request,"useraddadvertisement.html")
def useraddjobs(request):
    return render(request,"useraddjobs.html")