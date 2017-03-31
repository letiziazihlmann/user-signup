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

page_header = """
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
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        body = '''
        <form method='post'>
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for='username'>Username</label>
                        </td>
                        <td>
                            <input name='username' type='text' value required>
                            <span class='error'></span>
                        </td>
                    <tr>
                    <tr>
                        <td>
                            <label for='password'>Password</label>
                        </td>
                        <td>
                            <input name='password' type='password' value="" value required>
                        </td>
                    <tr>
                    <tr>
                        <td>
                            <label for='verify'>Verify Password</label>
                        </td>
                        <td>
                            <input name='verify' type='password' value="" value required>
                            <span class='error'></span>
                        </td>
                    <tr>
                    <tr>
                        <td>
                            <label for='email'>Email</label>
                        </td>
                        <td>
                            <input name='email' type='email'>
                            <span class='error'></span>
                        </td>
                    </tr>
            </table>
            <input type='submit'>
        </form>
        '''

        error = self.request.get("error")
        if error:
            error_esc = cgi.escape(error, quote=True)
            error_element = '<p class="error">' + error_esc + '</p>'
        else:
            error_element = ''

        content = page_header + body + page_footer
        self.response.write(content)

        def post(self):
            #this will pull all of the values entered for the above inputs and assign them to a variable that i can use to test
            # if the input is valid
            entered_username = self.request.get('username')
            entered_password = self.request.get('password')
            entered_verify = self.request.get('verify')
            entered_email = self.request.get('email')

            #starting to validate the input, the re_username.match(entered_username) should be a boolean so true or false
            re_username = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
            def valid_username(entered_username):
                username_valid = re_username.match(entered_username)
                return username_valid

            #test to see if the username is valid if not, line 109 will redirect to line 89
            if username_valid == False:
                username_error = "Please enter a valid username"
                self.redirect("/?error=" + username_error)

            content = page_header + body + error_element + page_footer
            self.response.write(content)




#class WelcomeHandler(webapp2.RequestHandler):

    #def post(self):
        #username = self.request.get('username')
        #welcome_body = "<h1>Welcome " + username + "</h1>"
        #self.response.write(welcome_body)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
    #('/welcome', WelcomeHandler)
], debug=True)
