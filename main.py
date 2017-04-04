#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re



body = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">User Signup</a>
    </h1>
<form method='post'>
    <table>
        <tbody>
            <tr>
                <td>
                    <label for='username'>Username</label>
                </td>
                <td>
                    <input name='username' type='text' value required value="%(username)s">
                    <span class='error' name='username_error'>%(username_error)s</span>
                </td>
            <tr>
            <tr>
                <td>
                    <label for='password'>Password</label>
                </td>
                <td>
                    <input name='password' type='password' value="" value required>
                    <span class='error' name='password_error'>%(password_error)s</span>
                </td>
            <tr>
            <tr>
                <td>
                    <label for='verify'>Verify Password</label>
                </td>
                <td>
                    <input name='verify' type='password' value="" value required>
                    <span class='error' name='verify_error'>%(verify_error)s</span>
                </td>
            <tr>
            <tr>
                <td>
                    <label for='email'>Email (Optional)</label>
                </td>
                <td>
                    <input name='email' type='email' value='%(email)s'>
                    <span class='error' name='email_error'>%(email_error)s</span>
                </td>
            </tr>
    </table>
    <input type='submit'>
</form>
</body>
</html>
"""



# function to test if the username is valid - will be used on line 104
user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def username_valid(username):
    return username and user_re.match(username)

password_re = re.compile(r"^.{3,20}$")
def password_valid(password):
    return password and password_re.match(password)

email_re = re.compile(r"[/S]+@[/S]+.[/S]+$")
def email_valid(email):
    return not email or email_re.match(email)

class MainHandler(webapp2.RequestHandler):
    def write_form(self, username='', username_error = '', password_error ='', verify_error = '', email_error = '', email = '' ):
        self.response.write(body % {"username": username,
                                    "username_error": username_error,
                                    "password_error": password_error,
                                    "verify_error": verify_error,
                                    "email_error": email_error,
                                    "email": email})

    def get(self):
        self.write_form()


    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')



        error = False
        #test 1: username should be 3-20 letters, no spaces, can contain dashes and underscores
        #if username is not valid:
        username_error = ''
        if not username_valid(username):
            #enter an error - error + username_error
            username_error += "Please enter a valid username"
            error = True

        #test 2: must be 3-20 characters
        #if password is not valid:
        password_error = ''
        if not password_valid(password):
            #enter an error - error + password_error
            password_error += "Please enter a valid password"
            error = True

        #test 3: verfies that password and verify matches
        #if password != verify:
        verify_error = ''
        if password_valid(password) and password != verify:
            #enter an error - error + verify_error
            verify_error += "Please enter a matching password"
            error = True

        #test 4: email address is valid
        #if email is not valid:
        email_error = ''
        if not email_valid(email):
            #enter an error - error + email_error
            email_error += "Please enter a valid email address"
            error = True

        if error == True:
            self.write_form(username, username_error, password_error, verify_error, email_error, email)
        #if all is valid - redirect to Welcome page
        else:
            self.redirect('/welcome?username=' + username)


        #self.response.write(username + password + verify + email)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        body = "<h1>Welcome, " + username + "</h1>"

        self.response.write(body)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
