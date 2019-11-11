from django.shortcuts import render,redirect,HttpResponse
import pymysql
from utils import sqlhelper


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
        if len(title) > 0:
            conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute("insert into class(title) values(%s)",title)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/classes/')
        else:
            return render(request,'add_class.html',{'msg':"班级名称不能为空"})


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


def students(request):
    """
    学生列表
    :param request:
    :return:
    """

    conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select student.id,student.name,class.title from student left join class on student.class_id = class.id;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request,'students.html',{'result':result})


def add_student(request):
    if request.method == "GET":
        conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,title from class")
        class_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request, "add_student.html", {'class_list': class_list})
    else:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into student(name,class_id) values(%s,%s)", [name, class_id])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/students/')

def miniProgram(request):
    conn = pymysql.connect("localhost", "root", "Passw0rd", "mysite")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(
        "select id,name,appId,appSecret,ghId,account,password,tenant from MiniProgram;")
    miniProgram_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request,"miniProgram.html",{'miniProgram_list':miniProgram_list})


def edit_student(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        class_list = sqlhelper.get_List("select id,title from class",[])
        current_student_info = sqlhelper.get_one("select id,name,class_id from student where id=%s",[nid,])
        return render(request,'edit_student.html',{'class_list':class_list,'current_student_info':current_student_info})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        sqlhelper.modify("update student set name=%s,class_id=%s where id=%s",[name,class_id,nid])
        return redirect('/students/')


def modal_add_class(request):
    title = request.POST.get('title')
    print(" >>> "+title)
    if len(title) > 0:
        sqlhelper.modify("insert into class(title) values(%s)", [title, ])
        return HttpResponse('ok')
        #return redirect('/classes/')
    else:
        return HttpResponse('不ok')




    #
    # sqlhelper.modify("insert into class(title) values(%s)",[title,])
    # return redirect('/classes/')

