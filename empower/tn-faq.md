# TN FAQ

*Source: TN-FAQ.pdf*

---

## Technical Note

Empower Troubleshooting Guide
© 2013 Encore Analytics, LLC
November 18, 2021

### Contents

- 1 Introduction 2
- 2 Empower Errors 3
  - 2.1 Browser Specific Issues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
  - 2.2 Contract Displaying "Empty Dataset" . . . . . . . . . . . . . . . . . . . . . . 3
  - 2.3 Unable to See "Check Queue" . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
  - 2.4 502 Error During Recalc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
  - 2.5 Login Screen Error . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 3 Helpful Empower Scripts 6
  - 3.1 Element Hierarchy Needs Updating . . . . . . . . . . . . . . . . . . . . . . . 6
  - 3.2 Enabling DQIs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
  - 3.3 Transfer User/Change CAM . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 4 Empower Utilities 8
  - 4.1 bulk_data.pl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

---

## Chapter 1: Introduction

This document contains troubleshooting steps for some common problems experienced by users of the Empower software. There are also included sections on helpful user scripts and empower command line utilities.

If the troubleshooting steps provided do not help solve the issue you are experiencing, please contact technical support by opening a ticket on the portal or sending an email to:
support@encore-analytics.com

---

## Chapter 2: Empower Errors

This section contains common Empower errors and troubleshooting steps.

### 2.1 Browser Specific Issues

Some errors in Empower can be caused by cached Javascript in the browser. These issues can include failure to download generated files, failure to display selected charts or reports, or an invalid parameter message when trying to complete an action.

To determine if you are experiencing one of these errors, try performing the same operation in Empower in a different browser. If you do not experience the same issue in the new browser, you are likely experiencing an issue related to cached Javascript.

You can resolve these issues by clearing the browser cache and refreshing the page. After refreshing, try completing the operation again.

### 2.2 Contract Displaying "Empty Dataset"

**Problem:** After selecting a contract in the "Open Dataset" dialog box or from the "File > Open Dataset" menu option, you may see an "Empty Dataset" message instead of the expected data.

Figure 2.1: Empty Dataset Message

To troubleshoot, try performing a single-period recalculation for the contract. After the recalc completes, try opening the dataset again.

### 2.3 Unable to See "Check Queue"

**Problem:** You are unable to see the "Admin > Check Queue" option.

Figure 2.2: Check QUEUE Option

You can resolve this by adding the "QUEUE" option to your "empower.conf" file. See chapter 6 of the watchdir technical note for more information.

### 2.4 502 Error During Recalc

**Problem:** User receives a 502 error when attempting to complete a recalc.

The 502 error is typically a sign of a time-out. To troubleshoot, try increasing your browser timeout setting. If you are still experiencing the error, try connecting directly using a browser on the Empower server by navigating to "localhost:5000". After connecting, try to complete a recalc. If you do not receive an error, the issue you are experiencing is a network-related timeout issue.

If you are using SSO with IIS, you may want to adjust your "Time-out" and "Response Buffer Threshold" settings. These settings can be found under "Application Request Routing > Server Proxy Settings".

If these settings do not resolve the issue, you may need to consult with your IT department on what other settings may affect your time-out.

### 2.5 Login Screen Error

**Problem:** If using SSO, when trying to login to Empower, the user may see the message "Unable to securely login, likely a key is missing or invalid. Please contact your Empower Admin for assistance."

This is typically related to an issue with "ntsh.conf". To troubleshoot, please verify that you have an "ntsh.conf" file in your Empower directory. If you do not have one, create one and add a line like `SSO_DIR=<the sso_dir path that you set in your default document>`. If you do already have an "ntsh.conf" please verify the entries are correct and that it is not named something like "ntsh.conf.txt".

---

## Chapter 3: Helpful Empower Scripts

Outlined below are some helpful user scripts for the Empower software. If you are missing any of the listed scripts please reach out to Encore Analytics support and they will be provided to you.

### 3.1 Element Hierarchy Needs Updating

Users will typically see this message in the streaming status for a recalculation when they are recalculating a new project for the first time. If you complete two recalcs in a row and see the message both times, that is a sign that there may be an issue with your element hierarchy.

Figure 3.1: Elem Hierarchy Needs Updating Message

There is an empower script called "Check Element Hierarchy" that will automatically check the element hierarchy of a selected contract, returning a .xlsx file. The sheets will be explained below.

The download will should populate sheets 1 and 6 of the document. Any element listed on sheets 2-4 indicates a structure problem with the data.

### 3.2 Enabling DQIs

Empower has scripts to enable specific DQIs, labeled "Enable _____ DQIs". The types of DQI tests are "Default", "DOD", or "DOE". These scripts can be run from the "Admin > Scripts > Run/Edit" menu. If you do not see the scripts in that menu please reach out to support and they can provide them to you.

### 3.3 Transfer User/Change CAM

The Empower "Transfer User" script can be used to transfer narrative approval roles from one user to another. This is commonly used when a user retires or leaves a site.

The "Change CAM" is used in similar cases to change one CAM name to another within a selected contract.

---

## Chapter 4: Empower Utilities

Empower contains command line utilities for performing specific functions.

### 4.1 bulk_data.pl

The Empower "bulk_data" utility can be used to download/upload the contents of an entire database, including contracts and user items.

#### To Export

1. Navigate to the empower folder in an administrator command prompt on the Empower server.
2. Download the contents of the desired database with the command `perl bulk_data.pl e [DSN]`, replacing `[DSN]` with the name of the database you want to download.
3. This will generate a file called `[DSN]_dump.zip`.

#### To Import

1. Navigate to the empower folder in an administrator command prompt on the Empower server (typically `c:\encore-analytics\empower`)
2. Import the contents of the folder with `perl bulk_data.pl n [Filename] [DSN]` where:
   - `[Filename]` is the name of the file to be loaded
   - `[DSN]` is the data source name for the db to import to
3. This will generate a file named `[DSN]_load.zip`
4. Make a new directory for loading files ("load" is an easy one) and move the load file to the load directory
5. cd to the load directory and unzip the file
6. **WINDOWS:** There will be a load file named `[DSN]_load.bat`. To load all the data into the database, just run the batch file. **LINUX/macOS:** There will be a load file named `[DSN]_load.sh`. To load all the data into the database, you need to execute the command `sh [DSN]_load.sh`.
