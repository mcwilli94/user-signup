from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/invalid", methods=['POST'])
def invalid():
    # define variables
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['password-verification']
    verify_email = request.form['email']
    error_un = ""
    error_pwd = ""
    error_pwd_ver = ""
    error_email = ""


    # check username to make sure it is valid
    if (username == "") or (len(username) < 4) or (len(username) > 20) or ((" " in username) == True):
        error_un = "That's not a valid username".format(username)

    # check passwrd to make sure it is valid
    if (password == "") or (len(password) < 4) or (len(password) > 20) or ((" " in password) == True):
        error_pwd = "That's not a valid password".format(password)

    # check password verification to make sure it matches the password previously entered
    if (verify_password != password) or (verify_password == ""):
        error_pwd_ver = "Passwords don't match".format(verify_password)

    if (verify_email == ""):
        error_email = ""
    elif (("@" not in verify_email) == True) or (len(verify_email) < 4) or (len(verify_email) > 20) or (("." not in verify_email) == True) or ((" " in verify_email) == True):
        error_email = "Email is invalid".format(verify_email)

    if (error_un != "") or (error_pwd != "") or (error_pwd_ver != ""):
        return render_template("frontpage.html", error_un=error_un, error_pwd=error_pwd, error_pwd_ver=error_pwd_ver, 
        error_email=error_email)
        redirect("/?error=" + "invalid input")
    else:
        return render_template("welcome.html", username=username)



@app.route("/")
def index(error_un=""):
    error_encoded = request.args.get("error_un")
    error_encodedII = request.args.get("error_pwd")
    error_encodedIII = request.args.get("error_pwd_ver")

    return render_template("frontpage.html", error_un=error_encoded, error_pwd=error_encodedII, 
    error_pwd_ver=error_encodedIII)

app.run()