# Chapter 18: Security in Empower

*From the Empower User Manual*

---

## Chapter 18

Security in Empower

Security in Empower involves control over who accesses the database, who can log into the Empower application, and what different users are allowed to do within the application.

Empower fully supports the wInsight user security model including: 1) contract access, 2) security pre-filters, 3) groups, 4) publication level, and 5) single sign-on (for some platforms).

This chapter discusses Empower security, along with issues that can arise when logging into Empower and how to resolve them.

## 18.1 Database Security

Empower's databases are secured by the use of a database username and password. This is transparent to Empower users, and only of interest to those installing Empower and maintaining the installation. Therefore, it is not discussed further in this manual. (See the Empower Installation guide for details.)

The key thing to remember here is, if you are responsible for installing and maintaining Empower, and you have the database credentials, that you not confuse the database username and password with the username and password you use to log in to Empower.

## 18.2 Application-Level Security

Application-level security controls who can login to the Empower application and what privileges those users have while running the application.

When Empower is first installed, application-level security is off by default. This means that anybody can log in; Empower disregards whatever username and password the user may have entered at the login screen. Furthermore, every user is the Admin user. Naturally, most sites will want to turn application-level security on immediately, though sites with just one user may find it convenient to stick with the default.

In every Empower installation, there is a user, named "Admin", who has privileges not granted to ordinary users. These privileges include the ability to create and delete other users, assign contract-level permissions to users (see Section 16.15.1), delete shared items (Section 16.15.3), and rescale the entire database (Section 16.15.4).

Note that a non-admin user can be granted the ability (by the Admin user) to log in as the Admin; see Section 16.15.1 for details.

Once application-level security is turned on, users must enter their usernames and passwords to login to Empower (unless using Windows Integrated Authentication, described below).

To turn on application-level security, follow these steps:

1. Log out of Empower using the File > Log Out.
2. Enter 'Admin' in the 'User Name' box, leave 'Password' blank, and press OK.
3. Select File > Set Password, and enter a password. This will be the Admin password.

To turn off application-level security, the Admin user clears his or her password (sets it to a zero-length string).

## 18.3 Single Sign-On

Empower supports single sign-on (SSO). In an SSO implementation, the user enters his or her credentials once to the operating system (via a username/password combination, smartcard, or some other method), and then other applications trust that authentication and log the user on without asking for another set of credentials. That is, other applications trust the identity of the user because the SSO component vouches for the user.

Single sign-on is implemented in different ways at different sites. Please contact our technical support for assistance in interfacing your authentication infrastructure with Empower.

## 18.4 Contract-Level Security and Groups

Contract-level security is a way of controlling the access of users on a contract-by-contract basis. Each user can be granted read access, write access, or denied all access to individual contracts in the database. Furthermore, groups of users can be created, and access rights assigned to the group. When a user is added to such a group, the user automatically inherits the access rights for the group. See Section 16.15.1 for more details.

## 18.5 Security Prefilters

Security Prefilters is a mechanism that offers finer-grained security than contract-level security. A security prefilter is a logical expression that limits what elements of a contract (i.e., rows in the Sort Window) a given user is allowed to see. This prefilter is set by the Admin user and prevents rows that don't satisfy the prefilter expression from even being downloaded from the Empower server to the user's computer. See Section 6.5 for more information on this topic.

## 18.6 Publication Level

Publication level is a mechanism for limiting user access; it works in two ways.

First, publication level (publevel for short) is a way of preventing certain users from opening a given period of a contract. This can be useful when a new period's worth of data has been loaded for a contract, but it needs to be checked and corrected by more privileged users before it is made visible to all users.

Each period of a contract can be assigned a publication level, which is a small integer. (This will be done using the Download Data/Upload Data functions on the Admin menu; see Section 16.9.) Users can likewise be assigned a publication level in the User Maintenance dialog. (See Section 16.15.1.) The default publevels for both periods and users is zero.

Users will only be allowed to see a period if their publication levels are greater than or equal to the publication level of the period in question.

Second, the publication level can be used to lock inputs for VAR Narratives, User Narratives, User EAC, and EAC Narratives (i.e., everything on the Inputs menu except Scope of Work) once those documents have been approved. If the publication level for a period is set to -1, no user (Admin or otherwise) can save any edits to those documents.

You are free to use the publication level to fit the workflow at your site. You can choose any integers for publication levels, except that a publevel of -1 for a period always prevents saving edits to an input (VAR Narrative, etc.) for that period.

Here is a sketch of how publication levels might be used in a typical workflow.

First, users are assigned publevels. CAMs are assigned a publevel of 0. Some users, who are responsible for the initial importation of a new period's data, are assigned a publevel of 2. We'll say these users are in the importers category. Other users, who are responsible for reviewing the newly imported data and approving it for general viewing, are assigned a publevel of 1. We'll say these users are in the reviewers category.

1. A new period's worth of data is imported. While the data is being imported and checked for basic correctness, the publevel for that period is set to 2. Only importer users see this period's data in Empower.
2. When the data is ready for review, the period's publevel is set to 1. Now the reviewer users can see this period's data.
3. When these users have approved the data for general viewing, the period's publevel will be set to 0, and now all the CAMs, with their publevels of 0, will be able to view the data for the new period.
4. As CAMs use Empower to analyze the parts of the contract for which they are responsible, they will be editing and saving VAR Narratives, User Narratives, User EAC, and EAC Narratives. When these items have been approved and the authorities have decided these items should be frozen for the period, the period's publevel will be set to -1. Now these items cannot be changed.
5. A new period's worth of data comes in and the cycle repeats.

## 18.7 User Codes

Each user (and group) can be assigned a User Code. This is a string of one to four characters. You are free to use this code as a way to group users into classes. (This is not the same as the user Groups you can create in the User Maintenance dialog to grant permissions to contracts to groups of users.)

Empower uses the User Code together with settings in the Empower configuration file to control which elements of the user interface are shown to different classes of users. For instance, let's say that at your installation, the management has decided that it doesn't want the CAMs to use the AI Narrative report. You could assign the User Code "C" to each CAM. Then your administrator would configure Empower so that if a user's User Code begins with "C", the AI Narrative report option will be removed from the Reports menu when that user runs Empower.

The User Codes are case-sensitive (so "Cam" and "cam" would be different), and you can use letters and digits in the code.

Note that User Codes can have multiple characters; if they do configuration options for each character can apply for that user. This can be useful if, for instance, you want to use different letter codes for menu configurations and default filter configurations. For example, you could assign a User Code of "CA" for a user where "C" is used for menu configuration items and "A" is used for the default filter for that user. (See the technical note, "The Empower Configuration File," available on our support website http://encoreanalyticsllc.freshdesk.com/support/solutions for more details on configuration options.)

"User Code" can also be used to disable an Empower user so that they are no longer able to log in and use Empower, but their VAR history etc. will be maintained under that username. A deactivated user will not be counted under your Empower license count, allowing you to use that license for another user. You can disable a user by setting their User Code to "NA."

(Configuring Empower to customize the user interface is beyond the scope of this User's Manual and is described in a Technical Note available from Encore Analytics technical support.)

## 18.8 Login Issues and How to Resolve Them

Section 2.2 presented the basics of logging in. This section provides more detail on this subject.

### 18.8.1 Invalid Credentials

If the user enters invalid credentials (i.e., a username that doesn't exist in the database, or an incorrect password for an existing user), the following screen will appear:

Figure 18.1: Invalid username or password

The solution, of course is to enter the correct credentials. If you have forgotten your password, you need to notify the Admin user, who will reset your password, which will allow you to log on and change your password to something you will remember.

### 18.8.2 Empower License Files Missing

A legal Empower installation will include a pair of license files. If these files are missing, the user will see the message in Figure 18.2 when he or she tries to start Empower (whether or not application-level security is turned on).

Figure 18.2: Login Failure Due to Missing License File(s)

If you do have valid license files somewhere (e.g., they have been emailed to you but you haven't uploaded them yet), press Upload and upload the good license files as described in Section 18.8.7. Otherwise, obtain a set of valid license files from Encore Analytics.

### 18.8.3 Empower Account Deactivated

If a user is disabled, they will see the message in Figure 18.3 when they try to log into Empower. For information on how to disable users, see section 18.7.

Figure 18.3: User Has Been Disabled

The disabled user will not be able to login to Empower unless an Empower Admin re-enables them by changing their "User Code" from "NA."

### 18.8.4 Empower License Files Modified

If the license files are present but have been modified, the message below will be displayed:

Figure 18.4: Login Failure Due to Modified License File(s)

Either locate your unmodified license files (if you have them; of course it is a good practice to make a backup copy of them) or get a set of valid license files from Encore Analytics, then press Upload and install the license files as described in Section 18.8.7.

### 18.8.5 Empower License Has Expired

If your Empower license has expired (this only applies to customers who have leased, not purchased, the software), you will see a message like the one in Figure 18.5 when you attempt to log in:

Figure 18.5: Login Failure Due to Expired License

The solution, naturally, is to renew your Empower license. Once you have the new license files, press the Upload button and upload the good license files as described in Section 18.8.7.

### 18.8.6 License Limit is Exceeded

You need to buy a client license for each Empower user. Users are assigned a number (in increasing order) as they are added to Empower's database. If, for instance, you have purchased three client licenses, you can add three users to the database (in addition to the admin user, who always exists and does not count against your total). If you add a fourth user to the database, when that user attempts to log in, he or she will see the screen shown below and will not be able to log in.

Figure 18.6: Login Failure Due to License Limit Exceeded

At this point, you have two choices.

If you decide that some of your existing users don't need to use Empower you can delete them from Empower's list of users, making room (under the "salary cap" as it were) for the latest user. In the happy event that your business is thriving and you really do need more people using Empower to keep your projects running smoothly, you can buy more client licenses, and upload the new license files via the procedure described in Section 16.15.6.

### 18.8.7 Uploading License Files after a Login Failure

If you could not login because your license files were missing or damaged, or your license had expired, Empower will show you an Upload button and you can upload valid files according to this procedure.

Click Upload; you will then see this dialog. Click Choose File and browse to find your valid license files.

Figure 18.7: Uploading License Files after a Login Failure, Step 1

Once you have picked your license files, you will see this screen:

Figure 18.8: Uploading License Files after a Login Failure, Step 2

Click Upload and you will see the screen below. Now you can click Continue, and you will be returned to Empower's usual logon screen.

Figure 18.9: Uploading License Files after a Login Failure, Step 3
