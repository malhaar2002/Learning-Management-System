import mysql.connector
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from functools import partial
import os
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "malhaar",
database = "school_portal")
mycursor = mydb.cursor()

class Teacher():

    def __init__(self, name, regno, dob, contactno, subject, pin, email):
        self.name = name
        self.regno = int(regno)
        self.dob = dob
        self.contactno = int(contactno)
        self.subject = subject
        self.pin = int(pin)
        self.emailID = email

class Student():

    def __init__(self, name, regno, dob, contactno, grade, section, pin, email):
        self.name = name
        self.regno = int(regno)
        self.dob = dob
        self.contactno = int(contactno)
        self.grade = int(grade)
        self.section = section
        self.pin = int(pin)
        self.emailID = email

def start():

    welcomeLabel = Label(root, text = "Welcome", fg = "white", bg = "black", font=("Segoe Print", 29)).grid(column = 1, row = 0, padx = 280, pady = (275, 180))

    createUserButton = Button(root, text = "Sign Up", padx = 10, pady = 10, command = create_user, borderwidth = 1, bg = "black", fg = "red", font = ('calibri', 15)).grid(column = 0, row = 1, padx = (20, 20))

    loginButton = Button(root, text = "Login", padx = 10, pady = 10, command = login, borderwidth = 1, bg = "black", fg = "red", font = ('calibri', 15)).grid(row = 1, column = 2, padx = (20, 20))


def create_user():

    root.wm_state('iconic')
    window1 = Toplevel()
    window1.title("Create User")
    window1.geometry("1000x600")
    window1.configure(bg = "#f5f5dc")
    window1.resizable(False, False)

    createUserLabel = Label(window1, text = "Create User", font=("Comic Sans MS", 24)).grid(row = 0, column = 1, padx = 30, pady = 40)

    RadioValue = StringVar()
    teacherRadio = Button(window1, text = "Teacher", font = ('Segoe Print', 12), command = create_teacher).grid(row = 1, column = 0, padx = (20, 20))
    studentRadio = Button(window1, text = "Student", font = ('Segoe Print', 12), command = create_student).grid(row = 1, column = 2, padx = (20, 20))

def create_teacher():

    window_teacher = Toplevel()
    window_teacher.title("Create User")
    window_teacher.geometry("1000x600")
    window_teacher.configure(bg = "#f5f5dc")
    window_teacher.resizable(False, False)

    createUserLabel = Label(window_teacher, text = "Create User", font=("Comic Sans MS", 24)).grid(row = 0, column = 1, padx = 30, pady = 40)

    nameLabel = Label(window_teacher, text = "Name").grid(row = 2, column = 0, pady = 10)
    nameVar = StringVar()
    nameInput = Entry(window_teacher, textvariable = nameVar).grid(row = 2, column = 1, padx = (20, 20), pady = 10)

    regNoLabel = Label(window_teacher, text = "Registration number").grid(row = 3, column = 0, pady = 10)
    regNoVar = IntVar()
    regNoInput = Entry(window_teacher, textvariable = regNoVar).grid(row = 3, column = 1, padx = (20, 20), pady = 10)

    dobLabel = Label(window_teacher, text = "Date of birth (YYYY-MM-DD)").grid(row = 4, column = 0, pady = 10)
    dobVar = StringVar()
    dobInput = Entry(window_teacher, textvariable = dobVar).grid(row = 4, column = 1, padx = (20, 20), pady = 10)

    contactLabel = Label(window_teacher, text = "Contact number").grid(row = 5, column = 0, pady = 10)
    contactVar = IntVar()
    contactInput = Entry(window_teacher, textvariable = contactVar).grid(row = 5, column = 1, padx = (20, 20), pady = 10)

    subjectLabel = Label(window_teacher, text = "Subject").grid(row = 6, column = 0)
    subjectVar = StringVar()
    physicsRadio = Radiobutton(window_teacher, text = "Physics", value = "Physics", font = ('Segoe Print', 12), indicator = 0, background = "light blue", variable = subjectVar).grid(row = 7, column = 0, padx = (20, 20), pady = 50)
    mathsRadio = Radiobutton(window_teacher, text = "Maths", value = "Maths", font = ('Segoe Print', 12), indicator = 0, background = "light blue", variable = subjectVar).grid(row = 7, column = 1, padx = (20, 20), pady = 50)
    chemistryRadio = Radiobutton(window_teacher, text = "Chemistry", value = "Chemistry", font = ('Segoe Print', 12), indicator = 0, background = "light blue", variable = subjectVar).grid(row = 7, column = 2, padx = (30, 100), pady = 50)
    csRadio = Radiobutton(window_teacher, text = "Computer Science", value = "CS", font = ('Segoe Print', 12), indicator = 0, background = "light blue", variable = subjectVar).grid(row = 7, column = 3, padx = (20, 20), pady = 50)

    emailLabel = Label(window_teacher, text = "Enter email address").grid(row = 8, column = 0, pady = 10)
    emailVar = StringVar()
    emailInput = Entry(window_teacher, textvariable = emailVar).grid(row = 8, column = 1, pady = 10)

    pinLabel = Label(window_teacher, text = "Enter 4-digit pin").grid(row = 9, column = 0, padx = (20, 20), pady = 10)
    pinVar = IntVar()
    pinEntry = Entry(window_teacher, textvariable = pinVar).grid(row = 9, column = 1, padx = (20, 20), pady = 10)

    def submit_createUser():

        try:
            teacherChar = Teacher(nameVar.get().title(), regNoVar.get(), dobVar.get(), contactVar.get(), subjectVar.get(), pinVar.get(), emailVar.get())
            sql = "INSERT INTO teachers (Name, Pin, Subject, RegistrationNo, DOB, ContactNo, EmailID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (teacherChar.name, teacherChar.pin, teacherChar.subject, teacherChar.regno, teacherChar.dob, teacherChar.contactno, teacherChar.emailID)
            mycursor.execute(sql, val)
            mydb.commit()
            accountCreatedLabel = Label(window_teacher, text = "Account created successfully!").grid(row = 11, column = 0)

        except Exception as e:
            accoundNotCreatedLabel = Label(window_teacher, text = "Oops! We could not create the account. Please check all the details and try again.").grid(row = 11, column = 0)
            print(e)

    submitButton = Button(window_teacher, text = "Submit", command = submit_createUser).grid(row = 10, column = 0, pady = 30)

def create_student():

    window_student = Toplevel()
    window_student.title("Create User")
    window_student.geometry("1000x600")
    window_student.configure(bg = "#f5f5dc")
    window_student.resizable(False, False)

    createUserLabel = Label(window_student, text = "Create User", font=("Comic Sans MS", 24)).grid(row = 0, column = 1, padx = 30, pady = 40)

    nameLabel = Label(window_student, text = "Name").grid(row = 2, column = 0, pady = 10)
    nameVar = StringVar()
    nameInput = Entry(window_student, textvariable = nameVar).grid(row = 2, column = 1, padx = (20, 20), pady = 10)

    regNoLabel = Label(window_student, text = "Registration number").grid(row = 3, column = 0, pady = 10)
    regNoVar = IntVar()
    regNoInput = Entry(window_student, textvariable = regNoVar).grid(row = 3, column = 1, padx = (20, 20), pady = 10)

    dobLabel = Label(window_student, text = "Date of birth (YYYY-MM-DD)").grid(row = 4, column = 0, pady = 10)
    dobVar = StringVar()
    dobInput = Entry(window_student, textvariable = dobVar).grid(row = 4, column = 1, padx = (20, 20), pady = 10)

    contactLabel = Label(window_student, text = "Contact number").grid(row = 5, column = 0, pady = 10)
    contactVar = IntVar()
    contactInput = Entry(window_student, textvariable = contactVar).grid(row = 5, column = 1, padx = (20, 20), pady = 10)

    gradeLabel = Label(window_student, text = "Grade").grid(row = 6, column = 0, pady = 10)
    gradeVar = IntVar()
    gradeInput = Entry(window_student, textvariable = gradeVar).grid(row = 6, column = 1, pady = 10)

    sectionLabel = Label(window_student, text = "Section").grid(row = 7, column = 0, pady = 10)
    sectionVar = StringVar()
    sectionInput = Entry(window_student, textvariable = sectionVar).grid(row = 7, column = 1, pady = 10)

    emailLabel = Label(window_student, text = "Enter email address").grid(row = 8, column = 0, pady = 10)
    emailVar = StringVar()
    emailInput = Entry(window_student, textvariable = emailVar).grid(row = 8, column = 1, pady = 10)

    pinLabel = Label(window_student, text = "Enter 4-digit pin").grid(row = 9, column = 0, padx = (20, 20), pady = 10)
    pinVar = IntVar()
    pinEntry = Entry(window_student, textvariable = pinVar).grid(row = 9, column = 1, padx = (20, 20), pady = 10)

    def submit_createUser():

        try:
            studentChar = Student(nameVar.get().title(), regNoVar.get(), dobVar.get(), contactVar.get(), gradeVar.get(), sectionVar.get(), pinVar.get(), emailVar.get())
            sql = "INSERT INTO students (Name, Pin, RegistrationNo, DOB, ContactNo, Grade, Section, EmailID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (studentChar.name, studentChar.pin, studentChar.regno, studentChar.dob, studentChar.contactno, studentChar.grade, studentChar.section, studentChar.emailID)
            mycursor.execute(sql, val)
            mydb.commit()
            accountCreatedLabel = Label(window_student, text = "Account created successfully!").grid(row = 11, column = 0)

        except Exception as e:
            accoundNotCreatedLabel = Label(window_student, text = "Oops! We could not create the account. Please check all the details and try again.").grid(row = 11, column = 0)
            print(e)

    submitButton = Button(window_student, text = "Submit", command = submit_createUser).grid(row = 10, column = 0, pady = 30)


def login():

    root.wm_state('iconic')
    window2 = Toplevel()
    window2.title("Login")
    window2.geometry("1000x600")
    window2.configure(bg = "#f5f5dc")
    window2.resizable(False, False)

    createUserLabel = Label(window2, text = "Login", font=("Comic Sans MS", 24)).grid(row = 0, column = 1, padx = 30, pady = 20)

    RadioValue = StringVar()
    teacherRadio = Radiobutton(window2, text = "Teacher", value = "Teacher", font = ('Segoe Print', 12), indicator = 0, background = "light blue", variable = RadioValue).grid(row = 1, column = 0, padx = (20, 20), pady = 50)
    studentRadio = Radiobutton(window2, text = "Student", value = "Student", font = ('Segoe Print', 12), indicator = 0, background = "light blue", variable = RadioValue).grid(row = 1, column = 2, padx = (20, 20), pady = 50)

    regNoLabel = Label(window2, text = "Enter your registration number", font = ('Segoe Print', 12)).grid(row = 2, column = 0)
    global regNoVar
    regNoVar = IntVar()
    nameInput = Entry(window2, textvariable = regNoVar).grid(row = 2, column = 1, padx = (20, 20), pady = 60)

    pinLabel = Label(window2, text = "Enter 4-digit pin", font = ('Segoe Print', 12)).grid(row = 3, column = 0, padx = (20, 20), pady = 60)
    pinVar = IntVar()
    pinEntry = Entry(window2, textvariable = pinVar).grid(row = 3, column = 1, padx = (20, 20), pady = 60)

    def submit_login():

        try:
            mycursor.execute(f"select Pin from {RadioValue.get()}s where RegistrationNo = '{regNoVar.get()}'")
            actual_pin = mycursor.fetchall()

            if pinVar.get() == actual_pin[0][0]:
                if RadioValue.get() == "Teacher":
                    teacher()
                    window2.destroy()
                elif RadioValue.get() == "Student":
                    student()
                    window2.destroy()
            else:
                wrongPinLabel = Label(window2, text = "Wrong pin entered").grid(row = 5, column = 0)

        except Exception as e:
            errorLabel = Label(window2, text = "Oops! We could not login. Please check all the details and try again.").grid(row = 5, column = 0)
            print(e)

    loginButton = Button(window2, text = "Login", command = submit_login).grid(row = 4, column = 0)


def teacher():

    window3 = Toplevel()
    window3.title("Home Page")
    window3.geometry("1100x800")
    background_label = Label(window3, image = homescreen)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    window3.resizable(False, False)

    sql = f"SELECT Name FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
    mycursor.execute(sql)
    teacher_name = mycursor.fetchall()
    welcomeLabel = Label(window3, text = f"Welcome, {teacher_name[0][0]}!", font=("Helvetica", 24, "bold"), fg = "blue").grid(row = 0, column = 0, padx = 30, pady = (40, 0))

    def live_class():

        liveclassframe = Frame(window3)
        liveclassframe.grid(row = 1, column = 0)

        linkLabel = Label(liveclassframe, text = "Enter live class link:").grid(row = 0, column = 0)
        linkValue = StringVar()
        linkInput = Entry(liveclassframe, textvariable = linkValue).grid(row = 0, column = 1, padx = 5)

        def submit_link():

            sql = "DELETE FROM LiveClassLink"
            mycursor.execute(sql)
            mydb.commit()

            sql = f"INSERT INTO LiveClassLink VALUES ('{linkValue.get()}')"
            mycursor.execute(sql)
            mydb.commit()
            linkUploadSuccessfulLabel = Label(liveclassframe, text = "Link uploaded successfully").grid(row = 1, column = 0)

        def quit():

            liveclassframe.grid_forget()
            liveclassframe.destroy()

        linkSubmitButton = Button(liveclassframe, text = "Submit", command = submit_link).grid(row = 2, column = 0, pady = 30)
        quitButton = Button(liveclassframe, text = "Quit", font = ('calibri', 10, 'bold', 'underline'), foreground = 'red', command = quit).grid(row = 2, column = 1, pady = 30, padx = 10)


    def check_attendance():

        window_attendance = Toplevel()
        window_attendance.title("Attendance")
        window_attendance.geometry("1000x600")
        window_attendance.configure(bg = "#f5f5dc")
        window_attendance.resizable(False, False)

        sql = "SELECT * FROM attendance ORDER BY Student ASC"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for i in range(len(result)):

            studLabel = Label(window_attendance, text = result[i][0]).grid(row = 0, column = i)

            fig = matplotlib.figure.Figure(figsize=(2,2))
            ax = fig.add_subplot(111)

            school_start = datetime(2020, 3, 1)
            now = datetime.now()
            time_difference = now - school_start
            days_passed = time_difference.days
            present = result[i][1]
            absent = days_passed - result[i][1]

            ax.pie([present, absent])
            ax.legend([f"Present: {present}", f"Absent: {absent}"])

            circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
            ax.add_artist(circle)

            canvas = FigureCanvasTkAgg(fig, master=window_attendance)
            canvas.get_tk_widget().grid(row = 1, column = i)
            canvas.draw()

    def assignment():

        assignmentframe = Frame(window3)
        assignmentframe.grid(row = 2, column = 0)

        chapterLabel = Label(assignmentframe, text = "Chapter name").grid(row = 0, column = 0, pady = 20)
        chapterValue = StringVar()
        chapterInput = Entry(assignmentframe, textvariable = chapterValue).grid(row = 0, column = 1, pady = 20, padx = 5)

        topicLabel = Label(assignmentframe, text = "Topic").grid(row = 1, column = 0, pady = 20)
        topicValue = StringVar()
        topicInput = Entry(assignmentframe, textvariable = topicValue).grid(row = 1, column = 1, pady = 20, padx = 5)

        lastDateLabel = Label(assignmentframe, text = "Last date of submission (YYYY-MM-DD)").grid(row = 2, column = 0, pady = 20)
        lastDateValue = StringVar()
        lastDateInput = Entry(assignmentframe, textvariable = lastDateValue).grid(row = 2, column = 1, padx = 5, pady = 20)

        def choose_file():

            filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = (("pdf files", "*.pdf"), ("text files", "*.txt")))

            sql = f"SELECT Subject FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            sql = f"INSERT INTO assignments (Subject, Chapter, Topic, Link, LastDate) VALUES ('{result[0][0]}', '{chapterValue.get()}', '{topicValue.get()}', '{filename}', '{lastDateValue.get()}')"
            mycursor.execute(sql)
            mydb.commit()

            assignmentUploadSuccessful = Label(assignmentframe, text = "Notes uploaded successfully.").grid(row = 4, column = 0)

        def quit():

            assignmentframe.grid_forget()
            assignmentframe.destroy()

        chooseFileButton = Button(assignmentframe, text = "Choose file", command = choose_file).grid(row = 3, column = 0, pady = 20)
        quitButton = Button(assignmentframe, text = "Quit", font = ('calibri', 10, 'bold', 'underline'), foreground = 'red', command = quit).grid(row = 3, column = 1, pady = 20, padx = 10)


    def class_notes():

        notesframe = Frame(window3)
        notesframe.grid(row = 2, column = 1)

        chapterLabel = Label(notesframe, text = "Chapter name").grid(row = 0, column = 0, pady = 20)
        chapterValue = StringVar()
        chapterInput = Entry(notesframe, textvariable = chapterValue).grid(row = 0, column = 1, pady = 20, padx = 5)

        classNoLabel = Label(notesframe, text = "Class number").grid(row = 1, column = 0, pady = 20)
        classNoValue = IntVar()
        classNoInput = Entry(notesframe, textvariable = classNoValue).grid(row = 1, column = 1, pady = 20, padx = 5)

        def choose_file():

            filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = (("pdf files", "*.pdf"), ("text files", "*.txt")))

            sql = f"SELECT Subject FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            sql = f"INSERT INTO {result[0][0]} (Chapter, ClassNumber, Notes) VALUES ('{chapterValue.get()}', {classNoValue.get()}, '{filename}')"
            mycursor.execute(sql)
            mydb.commit()

            classNotesUploadSuccessful = Label(notesframe, text = "Notes uploaded successfully.").grid(row = 3, column = 0)

        def quit():

            notesframe.grid_forget()
            notesframe.destroy()

        chooseFileButton = Button(notesframe, text = "Choose file", command = choose_file).grid(row = 2, column = 0, pady = 20)
        quitButton = Button(notesframe, text = "Quit", font = ('calibri', 10, 'bold', 'underline'), foreground = 'red', command = quit).grid(row = 2, column = 1, pady = 20, padx = 10)

    def class_recording():

        recordframe = Frame(window3)
        recordframe.grid(row = 2, column = 2)

        chapterLabel = Label(recordframe, text = "Chapter name").grid(row = 0, column = 0, pady = 20)
        chapterValue = StringVar()
        chapterInput = Entry(recordframe, textvariable = chapterValue).grid(row = 0, column = 1, pady = 20, padx = 5)

        classNoLabel = Label(recordframe, text = "Class number").grid(row = 1, column = 0, pady = 20)
        classNoValue = IntVar()
        classNoInput = Entry(recordframe, textvariable = classNoValue).grid(row = 1, column = 1, pady = 20, padx = 5)

        def choose_file():

            filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = [("Mp4 files", "*.mp4")])

            sql = f"SELECT Subject FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            sql = f"INSERT INTO {result[0][0]} (Chapter, ClassNumber, Recording) VALUES ('{chapterValue.get()}', {classNoValue.get()}, '{filename}')"
            mycursor.execute(sql)
            mydb.commit()

            classRecordingUploadSuccessful = Label(recordframe, text = "Recording uploaded successfully.").grid(row = 3, column = 0)

        def quit():

            recordframe.grid_forget()
            recordframe.destroy()

        chooseFileButton = Button(recordframe, text = "Choose file", command = choose_file).grid(row = 2, column = 0, pady = 20)
        quitButton = Button(recordframe, text = "Quit", font = ('calibri', 10, 'bold', 'underline'), foreground = 'red', command = quit).grid(row = 2, column = 1, pady = 20, padx = 10)


    LiveClassLinkButton = Button(window3, image = liveClassPhoto, command = live_class).grid(row = 1, column = 0, padx = 30, pady = 40)
    checkAttendanceButton = Button(window3, image = attendancePhoto, command = check_attendance).grid(row = 1, column = 1, padx = 30, pady = 40)
    newAssignmentButton = Button(window3, image = assignmentPhoto, command = assignment).grid(row = 2, column = 0, padx = 30, pady = 40)
    classNotesButton = Button(window3, image = classNotesPhoto, command = class_notes).grid(row = 2, column = 1, padx = 30, pady = 40)
    classRecordingButton = Button(window3, image = classRecordingPhoto, command = class_recording).grid(row = 2, column = 2, padx = 30, pady = 40)


def student():

    window4 = Toplevel()
    window4.title("Home Page")
    window4.geometry("1100x800")
    background_label = Label(window4, image = homescreen)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    window4.resizable(False, False)

    sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
    mycursor.execute(sql)
    student_name = mycursor.fetchall()
    welcomeLabel = Label(window4, text = f"Welcome, {student_name[0][0]}!", font=("Helvetica", 24, "bold"), fg = "blue").grid(row = 0, column = 0, padx = 30, pady = 40)

    def live_class():

        sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
        mycursor.execute(sql)
        studName = mycursor.fetchall()

        sql = f"UPDATE attendance SET NoOfDaysPresent = NoOfDaysPresent + 1 where Student = '{studName[0][0]}'"
        mycursor.execute(sql)
        mydb.commit()
        print("Attendance marked successfully.")

        print("Joining live class...")
        from selenium import webdriver
        chromedriver = r"C:\Users\Malhaar\Downloads\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver)

        sql = "SELECT Link FROM LiveClassLink"
        mycursor.execute(sql)
        result = mycursor.fetchall()[0][0]
        driver.get(result)
        driver.maximize_window()
        while True:
            pass

    def check_attendance():

        window_attendance = Toplevel()
        window_attendance.title("Attendance")
        window_attendance.geometry("600x600")
        window_attendance.configure(bg = "#f5f5dc")
        window_attendance.resizable(False, False)

        sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
        mycursor.execute(sql)
        student_name = mycursor.fetchall()

        sql = f"SELECT * FROM attendance WHERE Student = '{student_name[0][0]}'"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        studLabel = Label(window_attendance, text = result[0][0]).grid(row = 0, column = 0)

        fig = matplotlib.figure.Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)

        school_start = datetime(2020, 3, 1)
        now = datetime.now()
        time_difference = now - school_start
        days_passed = time_difference.days
        present = result[0][1]
        absent = days_passed - result[0][1]

        ax.pie([present, absent])
        ax.legend([f"Present: {present}", f"Absent: {absent}"])

        circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
        ax.add_artist(circle)

        canvas = FigureCanvasTkAgg(fig, master=window_attendance)
        canvas.get_tk_widget().grid(row = 1, column = 0)
        canvas.draw()

    def assignment():

        assignmentWindow = Toplevel()
        assignmentWindow.title("Assignments")
        assignmentWindow.geometry("1200x700")
        background_label = Label(assignmentWindow, image = matrixBackground)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        assignmentWindow.resizable(False, False)
        window4.wm_state('iconic')

        def open_this(address):
            os.startfile(address)

        def cs_assignments():

            sql = "SELECT * FROM assignments WHERE Subject = 'CS' order by Chapter"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(result)

            csframe = Frame(window_notes)
            csframe.grid(row = 1, column = 1)


        physicsAssignmentButton = Button(assignmentWindow, image = physicsphoto, font = ('Segoe Print', 12)).grid(row = 0, column = 0, padx = (20, 20), pady = 50)
        mathsAssignmentButton = Button(assignmentWindow, image = mathsphoto, font = ('Segoe Print', 12)).grid(row = 0, column = 1, padx = (20, 20), pady = 50)
        chemistryAssignmentButton = Button(assignmentWindow, image = chemphoto, font = ('Segoe Print', 12)).grid(row = 1, column = 0, padx = (20, 20), pady = 40)
        csAssignmentButton = Button(assignmentWindow, image = csphoto, font = ('Segoe Print', 12), command = cs_assignments).grid(row = 1, column = 1, padx = (20, 20), pady = 40)


    def class_notes():

        window_notes = Toplevel()
        window_notes.title("Class Notes")
        window_notes.geometry("1200x700")
        background_label = Label(window_notes, image = matrixBackground)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        window_notes.resizable(False, False)
        window4.wm_state('iconic')


        def open_this(address):
            os.startfile(address)

        def physics_notes():

            sql = "SELECT * FROM physics where Notes is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            physicsframe = Frame(window_notes)
            physicsframe.grid(row = 0, column = 0)

            for i in range(len(result)):
                link = f"{result[i][0]} Class {result[i][1]}"
                global address
                address = result[i][2]
                noteLinkButton = Button(physicsframe, text = link, command = partial(open_this, address)).grid(row = 0, column = i)

        def maths_notes():

            sql = "SELECT * FROM maths where Notes is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            mathsframe = Frame(window_notes)
            mathsframe.grid(row = 0, column = 1)

            for i in range(len(result)):
                link = f"{result[i][0]} Class {result[i][1]}"
                global address
                address = result[i][2]
                noteLinkButton = Button(mathsframe, text = link, command = partial(open_this, address)).grid(row = 0, column = i)

        def chemistry_notes():

            chemframe = Frame(window_notes)
            chemframe.grid(row = 1, column = 0)

            sql = "SELECT * FROM chemistry where Notes is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            for i in range(len(result)):
                link = f"{result[i][0]} Class {result[i][1]}"
                global address
                address = result[i][2]
                noteLinkButton = Button(chemframe, text = link, command = partial(open_this, address)).grid(row = 0, column = i)

        def cs_notes():

            csframe = Frame(window_notes)
            csframe.grid(row = 1, column = 1)

            sql = "SELECT * FROM cs where Notes is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            for i in range(len(result)):
                link = f"{result[i][0]} Class {result[i][1]}"
                global address
                address = result[i][2]
                noteLinkButton = Button(csframe, text = link, command = partial(open_this, address)).grid(row = 0, column = i)

        physicsnotesButton = Button(window_notes, image = physicsphoto, font = ('Segoe Print', 12), command = physics_notes).grid(row = 0, column = 0, padx = (20, 20), pady = 50)
        mathsnotesButton = Button(window_notes, image = mathsphoto, font = ('Segoe Print', 12), command = maths_notes).grid(row = 0, column = 1, padx = (20, 20), pady = 50)
        chemistrynotesButton = Button(window_notes, image = chemphoto, font = ('Segoe Print', 12), command = chemistry_notes).grid(row = 1, column = 0, padx = (20, 20), pady = 40)
        csnotesButton = Button(window_notes, image = csphoto, font = ('Segoe Print', 12), command = cs_notes).grid(row = 1, column = 1, padx = (20, 20), pady = 40)

    def class_recording():

        window_recording = Toplevel()
        window_recording.title("Class Recording")
        window_recording.geometry("1200x700")
        background_label = Label(window_recording, image = matrixBackground)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        window_recording.resizable(False, False)
        window4.wm_state('iconic')


        def open_this(address):
            os.startfile(address)

        def physics_recording():
            sql = "SELECT Chapter, ClassNumber, Recording FROM physics where Recording is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for i in range(len(result)):
                link = f"{result[i][0]} Class {result[i][1]}"
                global address
                address = result[i][2]
                noteLinkButton = Button(window_recording, text = link, command = partial(open_this, address)).grid(row = 6, column = i)

        def maths_recording():
            sql = "SELECT Chapter, ClassNumber, Recording FROM maths where Recording is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for i in range(len(result)):
                link = f"{result[i][0]} Class {result[i][1]}"
                global address
                address = result[i][2]
                noteLinkButton = Button(window_recording, text = link, command = partial(open_this, address)).grid(row = 6, column = i)

        def chemistry_recording():
            sql = "SELECT Chapter, ClassNumber, Recording FROM chemistry where Recording is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for i in range(len(result)):
                link = f"{result[i][0]} Class {result[i][1]}"
                global address
                address = result[i][2]
                noteLinkButton = Button(window_recording, text = link, command = partial(open_this, address)).grid(row = 6, column = i)

        def cs_recording():
            sql = "SELECT Chapter, ClassNumber, Recording FROM cs where Recording is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for i in range(len(result)):
                link = f"{result[i][0]} Class {result[i][1]}"
                global address
                address = result[i][2]
                noteLinkButton = Button(window_recording, text = link, command = partial(open_this, address)).grid(row = 6, column = i)

        physicsrecButton = Button(window_recording, image = physicsphoto, font = ('Segoe Print', 12), command = physics_recording).grid(row = 0, column = 0, padx = (20, 20), pady = 50)
        mathsrecButton = Button(window_recording, image = mathsphoto, font = ('Segoe Print', 12), command = maths_recording).grid(row = 0, column = 1, padx = (20, 20), pady = 50)
        chemistryrecButton = Button(window_recording, image = chemphoto, font = ('Segoe Print', 12), command = chemistry_recording).grid(row = 1, column = 0, padx = (20, 20), pady = 40)
        csrecButton = Button(window_recording, image = csphoto, font = ('Segoe Print', 12), command = cs_recording).grid(row = 1, column = 1, padx = (20, 20), pady = 40)


    LiveClassLinkButton = Button(window4, image = liveClassPhoto, command = live_class).grid(row = 1, column = 0, padx = 30, pady = 40)
    checkAttendanceButton = Button(window4, image = attendancePhoto, command = check_attendance).grid(row = 1, column = 1, padx = 30, pady = 40)
    newAssignmentButton = Button(window4, image = assignmentPhoto, command = assignment).grid(row = 2, column = 0, padx = 30, pady = 40)
    classNotesButton = Button(window4, image = classNotesPhoto, command = class_notes).grid(row = 2, column = 1, padx = 30, pady = 40)
    classRecordingButton = Button(window4, image = classRecordingPhoto, command = class_recording).grid(row = 2, column = 2, padx = 30, pady = 40)


root = Tk()
root.title("Learning Management System")
root.geometry("1000x600")
welcomePhoto = PhotoImage(file = r"Images\welcome.png")
background_label = Label(root, image = welcomePhoto)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.attributes("-fullscreen", False)
root.resizable(False, False)

#-------------------------------------IMAGES----------------------------------------------------------------
#You need to initialise them here instead of inside the functions, otherwise they take too much time to load

homescreen = PhotoImage(file = r"Images\home.png")
liveClassPhoto = PhotoImage(file = r"Images\liveclass.png")
classNotesPhoto = PhotoImage(file = r"Images\classnotes.png")
classRecordingPhoto = PhotoImage(file = r"Images\recording.png")
assignmentPhoto = PhotoImage(file = r"Images\assignment.png")
attendancePhoto = PhotoImage(file = r"Images\attendance.png")

physicsphoto = PhotoImage(file = r"Images\physics.png")
chemphoto = PhotoImage(file = r"Images\chemistry.png")
mathsphoto = PhotoImage(file = r"Images\maths.png")
csphoto = PhotoImage(file = r"Images\cs.png")
matrixBackground = PhotoImage(file = r"Images\matrix_background.png")

start()

root.mainloop()
