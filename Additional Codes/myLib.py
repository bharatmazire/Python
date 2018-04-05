#!/bin/python

import getpass as gp

def show():
        print "\tSHOWING BOOKS ..."
        ch = int(raw_input(" Enter Language \n 1.Marathi \n 2.English \n CHOICE : "))
        if (ch == 1):
                fd = open("marathi_book_list.txt")
        else:
                fd = open("english_book_list.txt")

        try:
                fd.seek(-100,2)
                count = int(fd.read(4))
        except IOError:
                print "\n NO BOOK IN LIST "
                count = 0

        fd.seek(0,0)
        for i in range(count):
                strToRead = fd.read(100)
                print "\n *************************************** "
                print "ID : ",strToRead[0:4]
                print "Name Of Book : ",strToRead[4:44]
                print "Name of Author : ",strToRead[44:64]
                print "Date Book added : ",strToRead[64:72]
                print "comment : ",strToRead[72:]
        fd.close()

        print " ********************************"


def give():
        show()
        print "\t Giving Book ..."
        ch = int(input(" Enter Language \n 1.Marathi  \n 2.English \n CHOICE : "))
        if(ch == 1):
                fd = open("marathi_book_list.txt","r+")
        else:
                fd = open("english_book_list.txt","r+")

        ID = int(raw_input(" Enter the Id of book you want :  "))

        try:
                fd.seek(-100,2)
                count = int(fd.read(4))
        except IOError:
                print "\n NO BOOK IN LIST "
                count = 0
        print "Total count of Books : ",count
        print "Book Id You want : ",ID
        if(ID <= count and count != 0):
                fd.seek(ID * 100 - 28)
                comment = fd.read(8)
                if(comment == "REMOVED!"):
                        print " BOOK REMOVED FROM BOOK LIST"
                elif(comment == "TAKEN BY"):
                        print " BOOK NOT AVAILABLE [ALREADY TAKEN ]"
                else:
                        fd.seek(-8,1)
                        fd.write("TAKEN BY")
                        taken_name = str(raw_input(" Enter Name : ")).rjust(20," ")
                        fd.write(str(taken_name))
        else:
                print "Invalid ID (Book Not Present !!)"
        fd.close()

# ID (4) , name (40) , auther (20) , date_added (DDMMYYYY) , comment (8) , taken_name(20)
def addBook():
        print " IN ADD BOOK"
        ch = int(input(" Choose Language \n 1.Marathi  \n 2.English \n CHOICE : "))
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

        print " Count Is : ",count
        fd.seek(0,2)

        ID = str(count + 1).rjust(4,"0")
        name = str(raw_input(" Enter Name of Book : ")).ljust(40," ")
        auther = str(raw_input(" Enter Authers name : ")).ljust(20," ")
        date = ''
        while (len(date) != 8):
                date = str(raw_input(" DATE in format DDMMYYY : "))
        comment = ''
        while (len(comment)!= 8):
                comment = str(raw_input(" Comments (8 char only) : ")).ljust(8," ")
        taken_name = " ".ljust(20," ")

        strToAdd = str(ID) + str(name) + str(auther) + str(date) + str(comment) + str(taken_name)

        fd.write(strToAdd)
        fd.close()


def rmvBook():
        show()
        print "REMOVING BOOK ...."
        ch = int(input(" Choose Language \n 1.Marathi \n 2.English \n CHOICE : "))
        if(ch == 1):
                fd = open("marathi_book_list.txt","r+")
        else:
                fd = open("english_book_list.txt","r+")

        ID = int(raw_input(" Enter Id of book you want to remove : "))
        try:
                fd.seek(-100,2)
                count = int(fd.read(4))
        except IOError:
                print " NO BOOK IN LIST"
                count = 0

        if(count <= ID and count != 0):
                fd.seek(ID * 100 - 28)
                fd.write("REMOVED!")
        else:
                print "Book Not Available"
        fd.close()


def admin():
        print " \nWELCOME ADMIN "
        print "\n\t**** FREEDOM COMES WITH GREAT RESPONSIBILITIES  ****"
        choice = 0
        while (choice != 4):
                choice = int(raw_input(" 1.Add Book To Book List \n 2.Remove Book From Book List \n 3.EXIT \n CHOICE : "))
                if(choice == 1):
                        addBook()
                elif(choice == 2):
                        rmvBook()
                elif(choice == 3):
                        break
                else:
                        print " Wrong Choice"


def main():
        print "\t\t\t\t..WELCOME TO LIBRARY.."
        print "\t :: NOTE :: \n\t READ AND THEN GIVE ANY CHOICE "
        choice = 0
        while (choice != 4):
                print "\n\n\t\t\t\t      M E N U"
                choice = int(raw_input(" 1.Show Book List \n 2.Give Book \n 3.Admin Task \n 4.EXIT \n CHOICE : "))
                if(choice == 1):
                        show()
                elif(choice == 2):
                        give()
                elif(choice == 3):
                        name = str(gp.getpass(" Enter admin name : "))
                        sword = str(gp.getpass(" Enter admin password : "))
                        if (name != "root" or sword != "toor"):
                                print " ADMIN name or password is WRONG \nEXITING..."
                                exit()
                        admin()
                elif(choice == 4):
                        print " EXITING..."
                        break
                else:
                        print " Wrong choice"


if __name__ == '__main__':
        main()
