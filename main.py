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
                            <label for='Username'>Username</label>
                        </td>
                        <td>
                            <input name='Username' type='text' value required>
                        </td>
                    <tr>
                    <tr>
                        <td>
                            <label for='Password'>Password</label>
                        </td>
                        <td>
                            <input name='password' type='password' value required>
                        </td>
                    <tr>
                    <tr>
                        <td>
                            <label for='Verify'>Verify Password</label>
                        </td>
                        <td>
                            <input name='verify' type='password' value required>
                        </td>
                    <tr>
                    <tr>
                        <td>
                            <label for='Email'>Email</label>
                        </td>
                        <td>
                            <input name='email' type='email' value required>
                        </td>
                    </tr>
            </table>
            <input type='submit'>
        </form>
        '''

        content = page_header + body + page_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
