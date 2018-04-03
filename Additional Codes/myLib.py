#!/bin/python

import getpass as gp

def show():
        print "show"
        ch = int(raw_input("1.Marathi \n2.English \nCHOICE : "))
        if (ch == 1):
                fd = open("marathi_book_list.txt")
        else:
                fd = open("english_book_list.txt")

        try:
                fd.seek(-100,2)
                count = int(fd.read(4))
        except IOError:
                print "NO DATA"
                exit()


        fd.seek(0,0)
        for i in range(count):
                strToRead = fd.read(100)
                print "\n *************************************** "
                print "ID : ",strToRead[0:4]
                print "Name Of Book : ",strToRead[4:44]
                print "Name of Author : ",strToRead[44:84]
                print "Date Book added : ",strToRead[84:92]
                print "comment : ",strToRead[92:]
        fd.close()

        print "********************************"


def give():
        print "give"

# file contents of book list
# ID (4) , name (40) , auther (40) , date_added (DDMMYYYY) , issued (2) , comment (8)
def addBook():
        print "add book"
        ch = int(input("1.Marathi \n2.English \nCHOICE : "))
        if(ch == 1):
                fd = open("marathi_book_list.txt","r+")
        else:
                fd = open("english_book_list.txt","r+")

        strToAdd = ""

        try:
                fd.seek(-100,2)
                count = int(fd.read(4))
        except IOError:
                count = 0

        print "count is : ",count
        fd.seek(0,2)


        ID = str(count + 1).rjust(4,"0")
        name = str(raw_input("Enter Name of Book : ")).ljust(40," ")
        auther = str(raw_input("Enter Authers name : ")).ljust(40," ")
        date = ''
        while (len(date) != 8):
                date = str(raw_input("DATE in format DDMMYYY : "))
        comment = ''
        while (len(comment)!= 8):
                comment = str(raw_input("Comments (8 char only) : ")).ljust(8," ")

        strToAdd = str(ID) + str(name) + str(auther) + str(date) + str(comment)

        fd.write(strToAdd)
        fd.close()


def rmvBook():
        print "remove book"

def chngAdminStng():
        print "Change admin settings"


def admin():
        print "admin"
        choice = 0
        while (choice != 4):
                choice = int(raw_input("1.add book \n2.remove book \n3.change admin settings \n4.exit \nCHOICE : "))
                if(choice == 1):
                        addBook()
                elif(choice == 2):
                        rmvBook()
                elif(choice == 3):
                        chngAdminStng()
                elif(choice == 4):
                        break
                else:
                        print "Wrong choice"



def main():
        print "\t\t\t\t..WELCOME TO LIBRARY.."
        choice = 0
        while (choice != 4):
                print "menu"
                choice = int(raw_input("1.show \n2.give \n3.admin \n4.exit \nchoice:"))
                if(choice == 1):
                        show()
                elif(choice == 2):
                        give()
                elif(choice == 3):
                        name = str(gp.getpass("Enter admin name : "))
                        sword = str(gp.getpass("Enter admin password : "))
                        admin_name = "root"
                        admin_sword = "toor"
                        if (name != admin_name or sword != admin_sword):
                                print "something is wrong"
                                exit()
                        admin()
                elif(choice == 4):
                        print "EXITING."
                        exit()
                else:
                        print "Wrong choice"


if __name__ == '__main__':
        main()
