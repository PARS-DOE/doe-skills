# TN EmailNotifications

*Source: TN-EmailNotifications.pdf*

---

## Technical Note: Email Notifications with Empower

© 2013 Encore Analytics, LLC
November 29, 2022

---

## 1 Introduction

This document describes how to automate the sending of Empower's email notifications for VAR and User Narratives, and action items. We assume you are familiar with Empower's implementation of workflows for VAR and User narratives and action items, and with sending email notifications using the Empower user interface.

Just for completeness, we begin by reminding you of the steps necessary to configure Empower to send email notifications, whether manually or automatically. In the rest of this document, we will assume we are setting up email notifications for VAR Narratives; the process is the same for action items.

### 1.1 Edit the Empower configuration file

You will need to add the EMAIL_CONFIG key with the appropriate value to the Empower configuration file (empower.conf). If you are unfamiliar with this config file, see our Tech Note "The Empower Configuration File" (TN-ConfFile.pdf). Adding the EMAIL_SUBJECT and its value is optional.

```
Email_Config={
  "sender": <email address from which the automated emails will come>,
  "server": <address of your email server, e.g., "smtp.mycompany.net",
  "port": <port used by your email server; e.g. "587">,
  "auth_user": <email address of authorized email user>,
  "auth_pwd": <password of auth_user encrypted with our encryption routine>,
  "tls":"yes"|"no"|"auto" <as the case may be>,
  "limit" : <(optional) limits the number of emails sent per connection; default = 100.
  sendemails automatically drops and reestablishes the connection as needed>
}
```

**Notes:**

1. EMAIL_CONFIG and its value must be written all on one line (it is shown wrapped in this document for readability).
2. The value for EMAIL_CONFIG must be a legal JSON string.
3. To encrypt auth_pwd, use the following url after logging into Empower: `http://localhost:5000/empower.pl?func=getpwd`
   This will bring up a page in the browser that will prompt you for your password and display the encrypted result. The encryption algorithm and key can be specified in ntsh.conf, see the technical note "Encryption in Empower" for details.

```
EMAIL_SUBJECT=<a string, possibly including the placeholders (|Role|), (|Type|), and/or (|Name|)>
```

This key is optional; if it is absent, the default is "Empower (|Role|) action required".

**Notes:**

1. (|Name|) is a placeholder that will be replaced by the user name of the Empower user receiving the email.
2. (|Role|) is a placeholder that will be replaced by the role of the user receiving the email, e.g., 'Submitter', 'Reviewer', 'Approver'.
3. (|Type|) is a placeholder that will be replaced by the type of email being sent; Narrative or Action Item.

### 1.2 Add email addresses for all users whose role is 'Submitter', 'Reviewer', or 'Approver'

You can do this with the User Maintenance dialog, or using Download Data for the User table, editing the resulting spreadsheet to add the email addresses, and uploading the modified spreadsheet with Upload Data.

---

## 2 Automated email sending

To set up automated sending of email notifications, follow these three steps:

1. Create an arguments file
2. Configure sendemails
3. Setup scheduled job to run sendemails on a regular basis

### 2.1 Create an arguments file

The sendemails utility needs to know what contracts and period you want to send email notifications for, what database to use, and so on. You get that information from the Empower user interface and save it in an arguments file (sometimes called 'argfile' for short).

In the Empower user interface, run the command Admin > Send Email Notifications. Follow the instructions on the dialog. Check the box labeled 'Generate argument string only', and press 'Submit'. A good way to generate a reusable argument file is to start with a cross-contract query ("All Contracts" in the Open Dataset dialog) and chose CUR-0 for the period (or CUR-1 depending on your reporting cycle). If you wish, you can limit by contract via an interactive filter on ContractName.

You will see something like this in the Status window:

```
Copy and save the string below to use these options for
automated email processing.
------
{ "ao" : 0, "key" : "1SrfTQPJ", "id" : 1, "note" : "", "dsn" :
"local-Pg", "st" : 1, "un" : 1, "rows" : { "st" : 1, "dd" :
0, "un" : 1, "sdir" : 0, "ipf" : null, "upf" : null, "cc" :
0, "cd" : 1, "count" : 853, "scol" : 146, "pf" : "", "ce" :
"63.59" }, "eo" : 0, "uid" : 1}
------
```

Copy the text between the dashes and save to a file in a directory of your choosing. For the sake of this example, we'll name the file MonthlyNarrativeEmails, and we will save it in the directory `/Users/mike/empower_narratives`.

### 2.2 Create a sendemails.conf configuration file

In order for sendemails.pl to run, the sendemails.conf file must exist. Attempting to run sendemails.pl without first creating sendemails.conf will result in an error. The sendemails.conf file will go in the same directory as sendemails.pl (that is, the Empower directory).

Here is a sample file:

```
dir=/Users/mike/empower_narratives
log=/Users/mike/empower_narratives/sendemails.log
```

This config file says that the arguments file will be found in the `/Users/mike/empower_narratives` directory, and that a log file will be written to the file `/Users/mike/empower_narratives/sendemails.log`.

If the sendemails.conf file is left empty, the following default values will be used:

```
dir=. (i.e., the directory in which sendemails.pl is)
log=sendemails.log
```

#### 2.2.1 Running sendemails.pl

Here is how to run sendemails.pl. You will need to be in a command window in the Empower directory.

```
Usage: perl sendemails.pl [-c | -d] <argfile>
  -c check arguments
  -d dry run
  <argfile> name of the file containing information needed
            to generate the emails
```

#### 2.2.2 Check the config file and arguments file for correctness

The -c option tells sendemails to check the config file for correctness. Here is a sample run and output:

```
mike dev-empower $ perl sendemails.pl -c MonthlyNarrativeEmails
args => /Users/mike/empower_narratives/MonthlyNarrativeEmails
dryrun => 0
log => /Users/mike/empower_narratives/sendemails.log
OK
```

sendemails.pl -c checks to make sure that argfile MonthlyNarrativeEmails exists in the directory specified in the config file, and tells you where it will write the log file.

#### 2.2.3 Doing a dry run

Next, you should do a dry run to make sure the generated emails are what you expect. Running sendemails.pl with the -d option creates a dry run: the content of the generated emails will be displayed on the screen, but the emails will not actually be sent.

Here is part of a sample run:

```
mike dev-empower $ perl sendemails.pl -d MonthlyNarrativeEmails
Jones (XXX@mycompany.com)
--------------------------------------------------
To: XXX@mycompany.com
From: YYY@mycompany.com
Subject: Submitter Jones, you have work to do.
Dear Jones,
For Period ending JAN 04, the following elements have VARs
that require attention.
Regards,
Admin
Contract: MOH-2

# Wbs: 1000

Description: MOH-2
VAR Flags: c
Submitter: Jones
Approver: Jones
VAR State:
Last Updated By:
Last Updated On:
Reject Reason (if any):
--------------------------------------------------
(Not) Sending..OK
Novak (XXX@mycompany.com)
--------------------------------------------------
To: XXX@mycompany.com
From: YYY@mycompany.com
Subject: Submitter Novak, you have work to do.
Dear Novak,
For Period ending JAN 04, the following elements have VARs
that require attention.
Regards,
Admin
Contract: MOH-2

# Wbs: 5100

Description: ENG DATA
VAR Flags: scSC
Submitter: Novak
Approver: Jones
VAR State:
Last Updated By:
Last Updated On:
Reject Reason (if any):
[snip]
Generated 20 of 20 emails.
```

### 2.3 Configure sendemails to run automatically

Once you have verified that sendemails.conf is correct and performed a dry run to verify that the generated emails are what you want, you will set up sendemails.pl to run on a regular schedule. How often sendemails is run is, of course, up to you.

The command to be scheduled is:

```
perl sendemails.pl argfile
```

where argfile is the name of the file in which you stored the arguments from the Send Narrative Emails dialog.

How you schedule the sendemails job differs, depending on your operating system. We assume you are familiar with cron for Unix-like systems or Task Scheduler for Windows.
