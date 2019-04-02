from flask import Flask, render_template, request, redirect
import requests

app = Flask("My App")

def send_simple_message(input_email):
     return requests.post(
        "http://api.mailgun.net/v3/sandbox1e05bbe5e7af4fb8b891f02c3467573a.mailgun.org/messages",
        auth=("api", "a15b60cd3f1f5d64e7a907b50a1751ce-acb0b40c-a28b0668"),
        data={"from": "Jugaad <mailgun@sandbox1e05bbe5e7af4fb8b891f02c3467573a.mailgun.org>",
        "to":[input_email],
        "subject": "Confirmation of Message", 
        "text": "Thankyou! We have recieved your message and will be in touch soon..."})

@app.route("/")
def hello():
    return render_template("contact.html")

@app.route("/sendmessage", methods=["POST"])
def sign_up():
    form_data = request.form  
    print(form_data)

    send_simple_message(input_email=form_data ["email"])
    print (form_data["email"])
    return redirect("/thankyou")

@app.route("/thankyou")
def thank_you():
        return render_template("message.html")


app.run(debug=True)
