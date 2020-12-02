from eve import Eve
from flask import Flask, render_template, request, redirect
import subprocess

name_id = {}
planned = []
inprogress = []

def create_id(resource,items):
    item = items[0]
    first = item.get('firstname')
    last = item.get('lastname')
    id = str(item.get('_id'))
    if resource == 'Planned':
        name_id[first+last] = id
    if resource == 'Inprogress':
        name_id[first+last+'1'] = id
    pass

def create_guest(collections,first,last):
    subprocess.check_output('http http://127.0.0.1:5000/'+collections+' firstname='+first+' lastname='+last)
    print('Создан гость в '+collections+' Имя='+first+' Фамилия='+last)

def delete_guest(collections,id):
    subprocess.check_output('http delete http://127.0.0.1:5000/'+collections+'/'+id)
    print('Удален гость в '+collections+' ID='+id)

def update_guest(collections,id,first,last):
    subprocess.check_output('http put http://127.0.0.1:5000/'+collections+'/'+id+' firstname='+first+' lastname='+last)
    print('Изменен гость в '+collections+' Имя='+first+' Фамилия='+last)

app = Eve(__name__)

@app.route('/book', methods=['POST', 'GET'])
def index():
    print(name_id)
    return render_template("index.html", planned=planned, inprogress=inprogress)

@app.route('/add', methods=['POST'])
def add():
    a = request.form["collection"]
    b = request.form["firstname"]
    c = request.form["lastname"]
    create_guest(a,b,c)
    if a == 'Planned':
        planned.append(b+' '+c)
    if a == 'Inprogress':
        inprogress.append(b+' '+c)
    return redirect("/book", code=302)

@app.route('/update', methods=['POST'])
def update():
    a = request.form["collection1"]
    b = request.form["firstname1"]
    c = request.form["lastname1"]
    d = request.form["collection2"]
    e = request.form["firstname2"]
    f = request.form["lastname2"]
    if a == d:
        if d == 'Planned':
            planned.remove(b+' '+c)
            planned.append(e+' '+f)
            g = name_id.get(b+c)
            update_guest(d,g,e,f)
            name_id.pop(b+c)
            name_id[e+f] = g
        if d == 'Inprogress':
            inprogress.remove(b+' '+c)
            inprogress.append(e+' '+f)
            g = name_id.get(b+c+'1')
            update_guest(d,g,e,f)
            name_id.pop(b+c+'1')
            name_id[e+f+'1'] = g
    if a != d:
        if d == 'Planned':
            planned.append(e+' '+f)
            g = name_id.get(b+c+'1')
            update_guest(d,g,e,f)
            name_id[e+f] = g
        if d == 'Inprogress':
            inprogress.append(e+' '+f)
            g = name_id.get(b+c)
            update_guest(d,g,e,f)
            name_id[e+f+'1'] = g
    return redirect("/book", code=302)

@app.route('/del', methods=['POST'])
def delete():
    a = request.form["collection3"]
    b = request.form["firstname3"]
    c = request.form["lastname3"]
    if a == 'Planned':
        planned.remove(b+' '+c)
        d = name_id.get(b+c)
        delete_guest(a,d)
        name_id.pop(b+c)
    if a == 'Inprogress':
        inprogress.remove(b+' '+c)
        d = name_id.get(b+c+'1')
        delete_guest(a,d)
        name_id.pop(b+c+'1')
    return redirect("/book", code=302)

@app.route('/delete_all', methods=['POST'])
def delete_all():
    subprocess.check_output('http delete http://127.0.0.1:5000/Planned')
    subprocess.check_output('http delete http://127.0.0.1:5000/Inprogress')
    return redirect("/book", code=302)

if __name__ == '__main__':
    app.on_inserted += create_id
    app.run()
