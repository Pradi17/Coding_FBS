# step1 import mysql conector
import mysql.connector
# Create  connection
try:
    conection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="compony"
    )
    # if conection.is_connected():
    #     print("DB Conected Succesfully... ")
    # Create cursor
    cursor=conection.cursor()
    qur="insert into employee( id, name, sal) values(%s,%s,%s)"
    # values=(1,"Rahul",12222)
    # values1=(18,"Virat",12222)
    # values1=(7,"MSD",12222)
    # values1=(10,"Sachin",12222)
    # values1=(45,"Rohit",12222)
    # cursor.execute(qur,values)
    # li=[(7,"MSD",12222),(10,"Sachin",12222),(45,"Rohit",12222)]
    # for i in li:
    #     cursor.execute(qur,i)
    # conection.commit()
    # print("Record insreted... ")
    
    # qur="select * from employee"
    # cursor.execute(qur)
    # records=cursor.fetchall()
    # # print(type(rerds))
    # print("Record in Datab se Table ")
    # for row in records:
    #     print(row)
    
    # qur="update employee set sal=%s where id=%s"
    # cursor.execute(qur,(4554334,45))
    # conection.commit()
    # print("Salaray updated sucessfully ... ")
    
    qur="delete from employee where id=%s"
    cursor.execute(qur,(7,))
    conection.commit()
except Exception as e:
    print("DB NOT CONEcted ")
    print(e)