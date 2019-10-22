#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print("")

form = cgi.FieldStorage()
operands = form.getlist('operand')
print(f'Your total is: {sum(map(int, operands))}')