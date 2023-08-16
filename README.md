# Library Management System

A user-menu pops up on starting the program, from where the user can access 2 modes: ‘ADMIN’ and ‘STUDENT’. We used Python’s MySQL Connector to establish a connection between the library application and the SQL database. The database contains tables that store the book, staff, and student details. It also securely stores the usernames and passwords of the staff.

## Student

After entering the Student mode, the user is directed to a page where they can either Issue a book, Return a book or View the book details.

**1. View Book List –** The user can view the genres, author, book codes, and the issued status of all the books currently available in the library.

**2. Issue Book –** The user can issue a book by entering their Admission Number and the Book Code (Book codes can be viewed through the View Button).

**3. Return Book –** The user can return their issued book by entering their Admission Number.

## Admin

When the Admin button is clicked, a login window pops up where the staff member needs to enter the correct username and password to enter the Admin mode. If they want to change the password, they can do so by entering their old password followed by their new password.

**1. View Book Records –** The Admin can see the Date of Issue of all the books and the Date of Return if it has been returned.

**2. Book Details –** The Admin has the option to Add, Delete, and View Book Details.

**3. Student Details –** The Admin has the option to Add, Delete, and View Student Details.

**4. Staff Details -** The Admin has the option to Add, Delete, and View Staff Details.

<em>See further details and images in:</em>

[Project file](https://github.com/kan-uki/Library-Management-System/blob/main/Library%20Management%20System%20Documentation.pdf)


