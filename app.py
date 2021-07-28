from flask import *
from DBManager import *
app = Flask(__name__)
app.secret_key="art@12ka4"

db=DBManager()

@app.route('/')
def index():
    return render_template("index.html",loginmsg="")

@app.route("/login",methods=["POST"])
def login():
    uid=request.form["userid"]
    pwd=request.form["pwd"]
    res=db.login(uid,pwd)
    if res==None:
        return  render_template("index.html",loginmsg="Invalid UserID/Pwd")
    elif res=="admin":
        session["userid"]=uid
        return render_template("adminindex.html")
    else:
        return "artist"

@app.route("/adminaddpainting",methods=["GET","POST"])
def adminaddpainting():
    if request.method=="GET":
        lst=db.getCatagories()
        ddlclst=Format.getDDL(lst,"cid",1,0)
        return render_template("adminaddpainting.html",catagories=ddlclst)
    if request.method=="POST":
        ast=request.form["artist"]
        cid=request.form["cid"]
        siz=request.form["size"]
        prc=request.form["price"]
        uid=session["userid"]
        pid=db.addpainting(ast,cid,siz,prc,uid)
        photoobj=request.files["photo"]
        photoobj.save("static/paintings/"+str(pid)+".jpg")
        msg=f"Painting added successfully..<br><img src='static/paintings/{pid}.jpg' height=200px>"
        return render_template("adminresult.html",title="Add Painting",msg=msg)

@app.route("/adminpaintings")
def adminpaintings():
    selected=list(request.args.values())
    if len(selected)==0:
        selected.append('0')
    plst=db.getSelectedPaintings(selected)
    lst=db.getCatagories()
    cblclst=Format.getCBLx(lst,selected,1,0,6)
    return render_template("adminpaintings.html",catagories=cblclst,paintings=plst)

@app.route("/adminshowpainting")
def adminshowpainting():
    pid=request.args["pid"]
    rec=db.getPaintingInfo(pid)
    inm=str(pid)+".jpg"
    return render_template("adminshowpainting.html",record=rec,inm=inm)

@app.route("/admindelpainting")
def admindelpainting():
    pid=request.args["pid"]
    db.delPainting(pid)
    return render_template("adminresult.html",title="Delete Painting",msg="painting deleted successfully..")

@app.route("/adminchangepwd",methods=["GET","POST"])
def adminchangepwd():
    if request.method=="GET":
        return render_template("adminchangepwd.html")
    if request.method=="POST":
        npwd=request.form["npwd"]
        opwd = request.form["opwd"]
        uid=session["userid"]
        res=db.changePwd(uid,opwd,npwd)
        if res==True:
            msg="Password Changed Successfully.."
        else:
            msg="Invalid Old Password.."
        return render_template("adminresult.html",title="Change Password",msg=msg)

@app.route("/adminedit",methods=["GET","POST"])
def adminedit():
    if request.method=="GET":
        pid=request.args["pid"]
        rec = db.getPaintingInfo(pid)
        inm = str(pid) + ".jpg"
        return render_template("adminedit.html",record=rec,inm=inm)
    if request.method=="POST":
        art=request.form["artist"]
        siz = request.form["size"]
        prc = request.form["price"]
        pid = request.form["pid"]
        db.updatepainting(pid,art,siz,prc)
        rec = db.getPaintingInfo(pid)
        inm = str(pid) + ".jpg"
        return render_template("adminshowpainting.html", record=rec, inm=inm)

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    if request.method=="POST":
        ed=request.form["emailid"]
        nm=request.form["name"]
        cn=request.form["contactno"]
        mt=request.form["mtype"]
        pw=request.form["pwd"]
        return ".."

if __name__ == '__main__':
    app.run()
