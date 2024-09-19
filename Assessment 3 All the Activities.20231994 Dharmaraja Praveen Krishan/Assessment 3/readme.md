                                                Membership Registration System

Author: Dharmaraja Praveen Krishan

This Python application is a console-based program which is designed to manage student memberships for a club. It allows users to register students, withdraw them, and display membership statistics. The system follows key software design principles to ensure maintainability, readability, and flexibility.

In this README, we will focus on the Single Responsibility Principle (SRP) and how it applies to the design of this application.

Single Responsibility Principle (SRP)
The Single Responsibility Principle (SRP) is one of the five SOLID principles of object-oriented design. According to SRP, every class should have only one reason to change, meaning that each class should only have one responsibility.

By the limiting class are responsible for one , makes becomes the coding be more easire and extended.so if you have more responsibilties which changes in one area makes invadertly effect the functionality of another area.so this leads to tidyup the fexibiltyt and the reusabilty of the code.


How SRP is Applied in this Code
In the context of the Membership Registration System, the SRP has been implemented through clear separation of responsibilities within the MembershipRegistrationSystem class. so this goes as follows:

Class Responsibilities:
The MembershipRegistrationSystem class has a clear responsibility: managing memberships. It performs tasks like registering, withdrawing, and displaying membership statistics, all directly related to managing the membership lifecycle.

By keeping the MembershipRegistrationSystem focused solely on membership management, we adhere to the SRP by preventing it from taking on unrelated responsibilities (e.g., handling database connections, input validation, or user authentication).

This allows for future expansion and updates to each part of the system without affecting the others.

Method Responsibilities:
Each method within the MembershipRegistrationSystem class is designed to handle one main specific task:

register_member(): This method handles the registration of new members in the task. It asks for user input (Student ID, Last Name, and Programme) and assigns a unique membership ID to the new member.

withdraw_member(): This method handles the withdrawal of an existing member by their Membership ID and Last Name and make sure they are removed. If found, the member is removed from the list of registered members and added to the withdrawn list.

display_members(): This method displays membership statistics, such as the number of registered members, how many are enrolled in each program, and how many have withdrawn.make sure that all the details are provided exactly and give the perfect output in the scenerio.

Why SRP Matters Here:
Maintainability: If, in the future, we need to change how members are registered (e.g., by introducing a new input field), we only need to modify the register_member() method. This ensures that the withdrawal and statistics-related functionality remains untouched.this provides more easy for adding and removing a member.

Separation of Concerns: Each method handles one aspect of the membership system. For example, withdraw_member() only deals with removing members and doesn’t concern itself with how to display members or handle new registrations.

Further Enhancements to SRP:
While SRP is well applied here, further enhancements could include separating different aspects of membership management into individual classes. For example:

Member Class: We could introduce a Member class responsible for holding individual member data (Student ID, Last Name, Programme, Membership ID). This would encapsulate all member-related properties and behaviors in a dedicated class.

Statistics Class: We could introduce a Statistics class that calculates and displays membership statistics, further reducing the responsibility of the MembershipRegistrationSystem class.

So this part shows how the program is been runned throughout the system.

How to Use the Program
Running the System:

Upon starting the program, the user is presented with a menu.
The user can choose to:
Register a new member.
Withdraw a member.
Display membership statistics.
Exit the system.
Registering a Member:

The system prompts the user for the student's ID, last name, and program (Diploma/Bachelor).
Upon successful registration, a unique membership ID is assigned to the student, and the user is notified.
Withdrawing a Member:

To withdraw a member, the system asks for the membership ID and last name.
If the details are correct, the member is removed from the list of registered members and added to the withdrawn members list.
Displaying Membership Statistics:

The system displays the total number of registered members, how many are in the Diploma and Bachelor programs, and how many members have withdrawn.

so at last the output.

Conclusion
The Membership Registration System demonstrates how the Single Responsibility Principle can be applied to a real-world problem. By ensuring that each class and method has a single, well-defined responsibility, the code becomes easier to maintain and extend.

Future changes (e.g., adding new features or modifying existing ones) can be made more safely, as each class and method handles only one aspect of the program, reducing the likelihood of introducing bugs in unrelated areas.

