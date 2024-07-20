# student-attendance-system
*Project: Student Attendance Management System*

*Introduction:*
This project is a Student Attendance Management System developed using Python and the Tkinter library for the GUI, along with SQLite for database management. The system is designed to allow both students and teachers to interact with the application, each having their own set of functionalities.

*Features:*

1. *Student Panel:*
   - *Registration:* Students can register themselves by providing their name, email, password, branch, and roll number. The information is stored in the SQLite database.
   - *Login:* Students can log in using their email and password. Upon successful login, they can view their profile details and attendance records.
   - *Profile and Attendance:* After logging in, students can see their profile information including name, email, password, branch, and roll number. Additionally, they can view their attendance records.

2. *Teacher Panel:*
   - *Login:* Teachers can log in using their email and password. Upon successful login, they are greeted with a welcome message and access to various functionalities.
   - *View Students:* Teachers can view a list of all students in their branch, including details like name, roll number, and branch.
   - *Update Student Profile:* Teachers can update the profile information of students, such as name and password.
   - *Mark Attendance:* Teachers can mark attendance for students. They can select which students are present and store this information in the database.

*Technical Details:*
- *GUI:* The GUI is created using Tkinter, which provides an easy-to-use interface for both students and teachers.
- *Database:* SQLite is used to store all the information, including student details, teacher details, and attendance records.
- *Data Integrity:* The application ensures data integrity by validating login credentials and handling updates appropriately.
- *Usability:* The system is designed to be user-friendly, with clear labels and buttons for navigation and actions.

*Implementation:*
- The application is divided into two main classes: studentPanel and TeacherPanel.
- *StudentPanel:*
  - Handles student registration and login.
  - Displays student profile and attendance records.
- *TeacherPanel:*
  - Handles teacher login.
  - Allows teachers to view and update student profiles.
  - Provides functionality for marking attendance.

*Database Schema:*
- student_det table stores student details (name, email, password, branch, roll number).
- teacher_det table stores teacher details (name, email, password, branch).
- student_attendance table stores attendance records (date, roll number, status, student name).

*Conclusion:*
This Student Attendance Management System provides a comprehensive solution for managing student attendance, making it easier for both students and teachers to keep track of attendance records. The use of Python, Tkinter, and SQLite ensures that the application is efficient, user-friendly, and reliable.

