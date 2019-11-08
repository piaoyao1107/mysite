from django.shortcuts import render,redirect
import pymysql


def classes(request):
    conn = pymysql.connect("localhost","root","Passw0rd","mysite")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id,title from class")
    result = cursor.fetchall()
    cursor.close()
    conn.close()


    return render(request,"classes.html",{'result':result})



def add_class(request):
    if request.method == "GET":
        return render(request, "add_class.html")
    else:
        print(request.POST)
        title = request.POST.get('title')
        conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into class(title) values(%s)",title)
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')