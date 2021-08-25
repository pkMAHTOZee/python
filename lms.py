import random
import datetime
import json

def admin_login():
    file=open("admin.json",)
    admin=json.load(file)
    username=input('enter username:')
    password=input('password:')
    for admin_info in admin["admin"]:
        if username ==admin_info['username'] and password==admin_info['password']:
            print('logged in')
            return True
            break
    else:
        print('invalid username or password')
        return False

def add_admin():
    admin={}
    admin['name']=input('enter name:')
    admin['username']=input('user name :')
    admin['password']=input('create a new password :')
    with open("admin.json","r+") as file:
        addadmin=json.load(file)
        addadmin["admin"].append(admin)
        file.seek(0)
        json.dump(addadmin,file,indent=4)
    print('admin added')
    
def add_book():
    book={}
    book['book_id']=random.randint(1000000,10000000)
    book['book_name']=input('enter name of the book:')
    book['Author']=input('enter name of the author')
    book['pages']=input('enter no. of pages of the book:')
    book['no_of_copies']=int(input('enter no of copies:'))
    book['published_year']=input('enter published year:')
    book['ISBN']=input('enter ISBN :')
    
    with open("books.json","r+") as file:
        addbook=json.load(file)
        addbook["books"].append(book)
        file.seek(0)
        json.dump(addbook,file,indent=4)
    print('book added')
    
    
def delete_book():
    print('delete book')
    b_id=input('enter book id')
    file = open("books.json",'r+') 
    popbook=json.load(file)
    for book_info in popbook["books"]:
        if b_id in book_info['book_id']: 
            x=popbook["books"].index(book_info)
            popbook["books"].pop(x)
            print("book deleted")
            break
        else:
            print('no book with this id is available')
    file.seek(0)
    json.dump(popbook,file,indent=4)
    file.close()
    

    
def borrower_signup():
    borrower={}
    borrower['fullname']=input('enter your full name')
    borrower['dob']=input('enter your DOB')
    borrower['contact']=input('enter your mobile no.')
    borrower['email']=input('enter your email id')
    borrower['password']=input('create password')
    print(borrower)
    
    with open("registered.json","r+") as file:
        signup=json.load(file)
        signup["register"].append(borrower)
        file.seek(0)
        json.dump(signup,file,indent=4)
    print("Signed up")

def borrower_login(uid,upass):
    file=open("registered.json",)
    borrower_reg=json.load(file)
    
    for details in borrower_reg["register"]:
        
        if uid == details['email'] and upass == details['password']:
            print('logged in')
            file.close()
            return True
            break
        
    else:
        return False
    
        

def borrow_book():
    
    print('borrow book')
    b_id=input('enter book id : ')
    openbook=open("books.json",'r+')
    books=json.load(openbook)
    for book in books["books"]:
        if b_id == book['book_id'] and book['no_of_copies']>0:
            
            email=input('enter borrower mail:')
            with open("registered.json") as file:
                registered=json.load(file)
            for borrower_info in registered["register" ]:
                if email == borrower_info['email']:
                    
                    
                    borrower_info['book_id']=book['book_id']
                    borrower_info['book_borrowed']=book['book_name']
                    x = datetime.datetime.now()
                    borrower_info['borrowed_date']=x.strftime("%x")
                    f = open('borrowers.json','r+')
                    borrowers=json.load(f)
                    borrowers["borrowers"].append(borrower_info)
                    f.seek(0)
                    json.dump(borrowers,f,indent=4)
                    book['no_of_copies']-=1
                
                    openbook.seek(0)
                    json.dump(books,openbook,indent=4)
                    print('book borrowed')
                    
                    f.close()
                    openbook.close()
                    break
            else:
                print('no such email registered\nborrower need to register himself first')
        else:
            print('no book available with this ID')


def book_return():
    print('Enter details for book return')
    file=open("borrowers.json",'r+')
    borrowers=json.load(file)
    email=input('enter borrower email :')
    for borrower_info in borrowers["borrowers"]:
        if email == borrower_info['email']: 
            b_id=input('enter book ID:')
            if b_id == borrower_info['book_id']:
               
                x = datetime.datetime.now()
               
                borrower_info['returned_date']=x.strftime("%x") 
                file1=open("books.json",'r+')
                books=json.load(file1)
                for book in books["books"]:
                    if b_id==borrower_info['book_id']:
                        book['no_of_copies']+=1
                        
                        break
                file2=open("borrowers_his.json",'r+')
                borrowers_his=json.load(file2)
                borrowers_his["borrowers_his"].append(borrower_info)
                
                borrowers["borrowers"].pop(borrowers["borrowers"].index(borrower_info))
                
                file2.seek(0)
                json.dump(borrowers_his,file2,indent=4)
                file1.seek(0)
                json.dump(books,file1,indent=4)
                file.seek(0)
                json.dump(borrowers,file,indent=4)
                print("book returned")
                file.close()
                file1.close()
                break
            else:
                print('enter valid book id')
        else:
            print('no book borrowed with this email')
            
            

            
print('==================Welcome to this library Program===================')
while True:
    print("""\n 
                ==>> press 1 for user panel
                ==>> press 2 for admin panel
                ==>> press 5 for exit
         
         """)
    choice=int(input('==>> Please enter your choice : '))
    if choice==1:
        #login and signup function
        print('================== This is user panel ===================')
        print("""
                 ==>> press 1 to see available books
                 ==>> press 2 for login
                 ==>> press 3 for signup
                 ==>> press 5 for exit
                 """)
        ch1=int(input("please enter your choice : "))
        if ch1==1:
            print("""======== Available Books ========""")
            file=open("books.json",'r')
            books=json.load(file)
            for book in books["books"]:
                print(book)
        elif ch1==2:
            print("""======= user login ========""")
            print('borrowers login\n**enter your email as username**')
            uid=input('enter username:')
            upass=input('enter password:')
            if borrower_login(uid,upass):
                print("""
                          ==>> press 1 to see currently borrowed book 
                          ==>> press 2 to see borrowed history
                
                """)
                file1=open("borrowers.json",'r+')
                borrowers=json.load(file1)
                ch2=int(input("please enter your choice :"))
                if ch2==1:
                    for borrowed in borrowers["borrowers"]:
                        if uid==borrowed['email']:
                            print(borrowed)
                            
                        else:
                            print('you didnt borrowed any book currently')
                    file1.close()
                elif ch2==2:
                    file2=open('borrowers_his.json','r+')
                    borrowers_his=json.load(file2)
                    for borrowed in borrowers_his['borrowers_his']:
                        if uid==borrowed['email']:
                            print(borrowed)
                        else:
                            print('you didnt borrowed any book')
                    file2.close()
                else:
                    print('invalid choice')
            else:
                print('you have to sign up')
                borrower_signup()
                continue
        elif ch1==3:
            borrower_signup()
            continue
        
        elif ch1==5:
            print('thank you, visit again')
            break
        else:
            print('invalid choice')
    if choice==2:
            
        print("""==========Admin login=========""")
        check=admin_login()
        if check:

            while True:
                print('================== Admin panel ===================')
                print("""
                      ==>>press 1 to issue a book to borrower
                      ==>>press 2 to accept a book return from borrower
                      ==>>press 3 for add books
                      ==>>press 4 for delete book
                      ==>>press 5 for add admin
                      ==>>press 6 for Back
                      
                      """)
                ch3=int(input('enter your choice : '))
                if ch3==1:
                    borrow_book()
                elif ch3==2:
                    book_return()
                elif ch3==3:
                    add_book()
                elif ch3==4:
                    delete_book()
                elif ch3==5:
                    add_admin()
                elif ch3==6:
                    break
                else:
                    print('invalid choice')
        else:
            print('you are not authorised')
    elif choice==5:
        print('thank you, visit again')
        break
    else:
        print('invalid:choice')
    