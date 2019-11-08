import pymysql



class compareVersion():

    def readme(self,name,env):
        document = "test"
        if env == "test":
            document = "test.txt"
        elif env == "docu":
            document = "docu.txt"
        elif env == "prd":
            document = "prd.txt"
        filePath = "/Users/apple/Documents/mysite/document/"+document
        for lines in open(filePath):
            if name in lines:
                version = lines[-13:-1]
                print(name+" >>> "+version)
                return version

    #
    # def db_select(self):
    #     db = pymysql.connect("localhost", "root", "Passw0rd", "newbanker_py")
    #     cursor = db.cursor()
    #     sql = "select name from compare_number where status='1';"
    #     try:
    #         cursor.execute(sql)
    #         datas = cursor.fetchall()
    #         for data in datas:
    #             name = data[0]
    #             return str(name)
    #
    #     except Exception as e:
    #         print("select failed.Error info:%s"%e)
    #     finally:
    #         db.close()

    def db_update(self,version,name,env):
        db = pymysql.connect("localhost","root","Passw0rd","newbanker_py")
        cursor = db.cursor()
        column = "testNumber"
        if env == "test":
            column = "testNumber"
        elif env == "docu":
            column = "docuNumber"
        elif env == "prd":
            column = "prdNumber"
        sql = "update compare_number set "+column+"='"+version+"' where name='"+name+"' and status='1'; "
        try:
            cursor.execute(sql)
            db.commit()
            # print("undate success")
        except Exception as e:
            print("update failed.Error info:%s"%e)
            db.rollback()
        finally:
            db.close()

    def result(self):
        env = "prd"
        tup = ('im-service', 'im-web', 'is')
        for name in tup:
            version = self.readme(name,env)
            self.db_update(version,name,env)




if __name__ == '__main__':
    aa = compareVersion()
    aa.result()

