from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # ===============================variable=======================================#
        self.member_var = StringVar()
        self.prnno_var = StringVar()
        self.id_var = StringVar()
        self.title_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postid_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()

        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.days_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()

        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="red", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # ================================DATAFRAMELEFT====================================#
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="#077602", bd=15,
                                   relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Member Type", padx=2, pady=6, bg="powder blue")
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_var, state="readonly",
                                 font=("arial", 12, "bold"), width=27)
        comMember["value"] = ("Admin staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PRN No:", padx=2, bg="powder blue")
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_N0 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.prnno_var, width=29)
        txtPRN_N0.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID NO:", padx=2, pady=4, bg="powder blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.id_var, width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="FirstName", padx=2, pady=6, bg="powder blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="LastName", padx=2, pady=6, bg="powder blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lastname_var, width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address1", padx=2, pady=6, bg="powder blue")
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address1_var, width=29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address2", padx=2, pady=6, bg="powder blue")
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.address2_var, width=29)
        txtAddress2.grid(row=6, column=1)

        lblPostcode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Postcode", padx=2, bg="powder blue")
        lblPostcode.grid(row=7, column=0, sticky=W)
        txtPostcode = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.postid_var, width=29)
        txtPostcode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile", padx=2, pady=6, bg="powder blue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Id:", padx=2, bg="powder blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=6,
                             bg="powder blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.booktitle_var, width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Author Name:", padx=2, pady=6, bg="powder blue")
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.author_var, width=29)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=6,
                                bg="powder blue")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.dateborrowed_var, width=29)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=6, bg="powder blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.datedue_var, width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="DAYS On Book:", padx=2, pady=6,
                              bg="powder blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.days_var, width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return fine:", padx=2, pady=6,
                                  bg="powder blue")
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.latereturnfine_var,
                                  width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=6,
                                bg="powder blue")
        lblDateOverDate.grid(row=7, column=2, sticky=W)
        txtDateOverDate = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.dateoverdue_var, width=29)
        txtDateOverDate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=6,
                               bg="powder blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.finalprice_var, width=29)
        txtActualPrice.grid(row=8, column=3)

        # =====================Data Frame Right===========================================#

        DataFrameRight = LabelFrame(frame, bd=12, padx=20, fg="#077602", relief=RIDGE, bg="powder blue",
                                    font=("arial", 12, "bold"), text="Books Details")
        DataFrameRight.place(x=870, y=5, width=580, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBooks = ['The guide', 'Malgudi days', 'The private life of indian prince', 'Untouchable by mulak raj anand',
                     'History of medieval india', 'Learn Python The Hard Way', 'Python Programming', 'Secrete Rahshy',
                     'The gift of cow', 'The white tiger', 'Sea of poppies', 'Python CookBook',
                     'Into to Machine Learning', 'Fluent Python', 'Programming python', 'The Algorithm',
                     'Machine tecno', 'My Python', 'Joss Ellif guru', 'Deep Python', 'Mumbai Python', 'Machine python',
                     'Advance Python', 'Inton Python', 'RedChilli Python', 'Python for beginners', 'let us c']

        self.listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        self.listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=self.listBox.yview)
        for item in listBooks:
            self.listBox.insert(END, item)
        self.listBox.bind("<ButtonRelease-1>", self.SelectBook)

        ################################## BUTTONS FRAME ###################################
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="#032b5c")
        framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(framebutton, command=self.showData, text="Show Data", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(framebutton, command=self.update, text="Update", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData = Button(framebutton, command=self.reset, text="Reset", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(framebutton, command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=23,
                            bg="blue", fg="white")
        btnAddData.grid(row=0, column=5)

        ################################## INFORMATION FRAME ###################################
        frameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="#032b5c")
        frameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(frameDetails, bd=6, relief=RIDGE, bg="#032b5c")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column=(
        "member", "prn_no", "id", "firstname", "lastname", "address1", "address2", "postid", "mobile", "bookid",
        "booktitle", "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),
                                          xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("member", text="Member Type")
        self.library_table.heading("prn_no", text="PRN No.")
        self.library_table.heading("id", text="Book ID")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table.column("member", width=100)
        self.library_table.column("prn_no", width=100)
        self.library_table.column("id", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)

        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def SelectBook(self, ev):
        index_ = self.listBox.curselection()
        x = self.listBox.get(index_)
        if (x == "The guide"):
            self.bookid_var.set("BKID1234")
            self.booktitle_var.set("Detail guideline ")
            self.author_var.set("Paul berry")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 788")
        elif (x == 'Malgudi days'):
            self.bookid_var.set("BKID1235")
            self.booktitle_var.set("Those Days ")
            self.author_var.set("Ryan")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 1280")
        elif (x == 'The private life of indian prince'):
            self.bookid_var.set("BKID1236")
            self.booktitle_var.set("Private life ")
            self.author_var.set("jacob")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 449")
        elif (x == 'Untouchable by mulak raj anand'):
            self.bookid_var.set("BKID1237")
            self.booktitle_var.set("AMOUNG WE PEOPLE ")
            self.author_var.set("Raj Anand")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 788")

        elif (x == 'History of medieval india'):
            self.bookid_var.set("BKID1238")
            self.booktitle_var.set("About the past ")
            self.author_var.set("Matthew")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 399")

        elif (x == 'Learn Python The Hard Way'):
            self.bookid_var.set("BKID1239")
            self.booktitle_var.set("Detail guideline ")
            self.author_var.set("Paul berry")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 788")
        elif (x == 'Python Programming'):
            self.bookid_var.set("BKID12310")
            self.booktitle_var.set("LET us do programming")
            self.author_var.set("Paul berry")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 1300")
        elif (x == 'Secrete Rahshy'):
            self.bookid_var.set("BKID12311")
            self.booktitle_var.set("SECRETE Rahshy")
            self.author_var.set("Paulhomen")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 1100")
        elif (x == 'The gift of cow'):
            self.bookid_var.set("BKID1212")
            self.booktitle_var.set("GODAN")
            self.author_var.set("Munshi Premchand")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 1299")
        elif (x == 'The white tiger'):
            self.bookid_var.set("BKID1213")
            self.booktitle_var.set("Detail guideline ")
            self.author_var.set("Thomes")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 740")

        elif (x == 'Python CookBook'):
            self.bookid_var.set("BKID1215")
            self.booktitle_var.set("Deep learning ")
            self.author_var.set("david")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 700")
        elif (x == 'Into to Machine Learning'):
            self.bookid_var.set("BKID1216")
            self.booktitle_var.set("Guideline ")
            self.author_var.set("james")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 788")
        elif (x == 'Fluent Python'):
            self.bookid_var.set("BKID1217")
            self.booktitle_var.set("Details ")
            self.author_var.set("ROBERT")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 799")
        elif (x == 'Programming python'):
            self.bookid_var.set("BKID1218")
            self.booktitle_var.set("Detail guideline ")
            self.author_var.set("jennifer")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 1288")
        elif (x == 'The Algorithm'):
            self.bookid_var.set("BKID121")
            self.booktitle_var.set("Detail guideline ")
            self.author_var.set("joseph")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 998")
        elif (x == 'Machine tecno'):
            self.bookid_var.set("BKID122")
            self.booktitle_var.set("Machine ")
            self.author_var.set("ROY")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 998")
        elif (x == 'My Python'):
            self.bookid_var.set("BKID123")
            self.booktitle_var.set("PYTHON")
            self.author_var.set("JAUN")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 1399")
        elif (x == 'Joss Ellif guru'):
            self.bookid_var.set("BKID124")
            self.booktitle_var.set("ABOUT GOD")
            self.author_var.set("RALPH")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 999")
        elif (x == 'Deep Python'):
            self.bookid_var.set("BKID125")
            self.booktitle_var.set("INTRODUCTION ")
            self.author_var.set("RUSSEL")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 668")
        elif (x == 'Mumbai Python'):
            self.bookid_var.set("BKID126")
            self.booktitle_var.set("MUMBAI PYTHON")
            self.author_var.set("MASON")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 778")
        elif (x == 'Machine python'):
            self.bookid_var.set("BKID127")
            self.booktitle_var.set("Detail guideline ")
            self.author_var.set("LOUIS")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 998")
        elif (x == 'Advance Python'):
            self.bookid_var.set("BKID128")
            self.booktitle_var.set("Detail guideline ")
            self.author_var.set("PHILIP")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 3998")
        elif (x == 'Inton Python'):
            self.bookid_var.set("BKID129")
            self.booktitle_var.set("Detail guideline ")
            self.author_var.set("ELIJAH")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 1998")
        elif (x == 'RedChilli Python'):
            self.bookid_var.set("BKID130")
            self.booktitle_var.set("DAY ONE")
            self.author_var.set("joseph")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 2998")
        elif (x == 'Python for beginners'):
            self.bookid_var.set("BKID131")
            self.booktitle_var.set("JUST BEGIN")
            self.author_var.set("joseph")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 3998")
        elif (x == 'let us c'):
            self.bookid_var.set("BKID132")
            self.booktitle_var.set("C PROGRAMMING ")
            self.author_var.set("EUGENE")
            d1 = datetime.datetime.today()
            d2 = datetime.timedelta(days=15)
            d3 = d1 + d2
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.days_var.set('15')
            self.latereturnfine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 4998")

    def add_data(self):
        if (self.prnno_var.get() == ""):
            messagebox.showerror('Error', "Please fill the fields")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Suraj@123",port='3307',database="surajkumar")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (self.member_var.get(),
                               self.prnno_var.get(),
                               self.id_var.get(),
                               self.firstname_var.get(),
                               self.lastname_var.get(),
                               self.address1_var.get(),
                               self.address2_var.get(),
                               self.postid_var.get(),
                               self.mobile_var.get(),
                               self.bookid_var.get(),
                               self.booktitle_var.get(),
                               self.author_var.get(),
                               self.dateborrowed_var.get(),
                               self.datedue_var.get(),
                               self.days_var.get(),
                               self.latereturnfine_var.get(),
                               self.dateoverdue_var.get(),
                               self.finalprice_var.get()
                               ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("success", "Member Has Been Inserted  successfully")

    def update(self):
        if (self.prnno_var.get() == ""):
            messagebox.showerror('Error', "Please fill the fields")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Suraj@123",port='3307', database="surajkumar")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update library set member=%s,id=%s,firstname=%s,lastname=%s,address1=%s,address2=%s,postid=%s,mobile=%s,bookid=%s,booktitle=%s,author=%s,dateborrowed=%s,datedue=%s,days=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where prnno=%s",
                (
                    self.member_var.get(),
                    self.id_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postid_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.author_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.days_var.get(),
                    self.latereturnfine_var.get(),
                    self.dateoverdue_var.get(),
                    self.finalprice_var.get(),
                    self.prnno_var.get(),
                ))
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("success", "member has been updated ")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Suraj@123",port='3307', database="surajkumar")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, ev):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prnno_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postid_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.days_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END, "Member Type:\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t" + self.prnno_var.get() + "\n")
        self.txtBox.insert(END, " Book ID:\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "First Name:\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Last Name:\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1:\t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2:\t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post ID:\t\t" + self.postid_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No:\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END, "Date of Borrowed\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "DateDue:\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Days\t\t" + self.days_var.get() + "\n")
        self.txtBox.insert(END, "LateReturnFine\t\t" + self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverDue:\t\t" + self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "Final Price:\t\t" + self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prnno_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postid_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.days_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library management system", "Do you want to exit")
        if iExit:
            self.root.destroy()
        else:
            return

    def delete(self):
        if (self.prnno_var.get()=="" or self.id_var.get()==""):
            messagebox.showerror("Error","First Select the Member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Suraj@123",port='3307', database="surajkumar")
            my_cursor = conn.cursor()
            query="delete from Library where PRN_No=%s"
            value=(self.prnno_var.get())
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Member has been deleted")





if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()