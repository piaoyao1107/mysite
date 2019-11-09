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


def del_class(request):
    nid = request.GET.get('nid')
    conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from class where  id=%s", nid)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/classes/')

def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class where id=%s",nid)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request,'edit_class.html',{'result':result})
    else:
        #nid = request.POST.get('id')
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("update class set title=%s where id=%s", [title,nid])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/classes/')

