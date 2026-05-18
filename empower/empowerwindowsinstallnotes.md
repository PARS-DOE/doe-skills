# Empower Windows Install Notes

*Source: EmpowerWindowsInstallNotes.pdf*

---

## Installing Encore Analytics Empower on Windows

© 2013 Encore Analytics, LLC
May 15, 2023

## Contents

- 1 Introduction 3
- 2 Automated Setup 4
- 3 Creating Empower Databases 6
  - 3.1 Using a Remote Database 7
  - 3.2 Bulk Import Tools 7
  - 3.3 PostgreSQL 8
  - 3.4 SQL Server 8
  - 3.5 Oracle 9
  - 3.6 Create a new data source name 10
- 4 Populate the new database with your data 12
- 5 Setting up a Reverse Proxy Rule 14
- 6 Update to the latest version of Empower 16
  - 6.1 Install SSH keys 16
  - 6.2 Running an Empower Update 17
  - 6.3 The sys_update and db_update scripts 18
- 7 Database Utilities 20
  - 7.1 Add Database (add_db) 20
  - 7.2 Delete Database (del_db) 21
  - 7.3 Add Data Source Name (add_dsn) 22
  - 7.4 Delete Data Source Name (del_dsn) 22
  - 7.5 Add Data Source Non-Interactively (np_add_dsn) 23
- 8 Testing and Troubleshooting 25
- 9 Uninstalling Empower 27
- 10 Getting Help 28

---

## Chapter 1: Introduction

This document describes the steps necessary to install Empower on Windows 7. System administrators familiar with Windows Server should easily be able to make any necessary modifications for their particular system.

**Background:** Empower is an HTML5 web application implemented primarily in Perl on the server side and JavaScript on the client. Supported hosts include Windows 7, 8, and 10, Windows Server 2008 and 2012, Mac OS X, and mainstream variations of Linux (e.g., Centos, Debian, etc.). Empower is also available on Linux appliances through Amazon Web Services. The client needs only an HTML5 capable browser, such as is found on Windows, Mac OS X, Linux, iPad, Android tablets, and even smartphones. The Perl code is written to the Perl Web Server Gateway Interface (PSGI), which uncouples the application itself from the server back end. This provides great flexibility in deployment. Empower can be deployed as an ordinary CGI application in IIS or a mod_perl application in Apache, for example, but it can also be deployed as a stand-alone, pre-compiled, multi-threaded application running on a separate Windows, Linux, or Mac OS X host. In this latter configuration, Empower can provide desktop-like responsiveness without requiring any modification to the existing web-server configuration other than a reverse proxy or rewrite rule to connect the app to the user. This document describes installation to the latter configuration.

**Stand-alone Install:** The instructions in this document can also be used to install Empower locally on a Windows machine as a stand-alone install. In this configuration, a single user would be using the Empower application installed on their machine. The user would still access Empower via a browser like they would with a server install, but instead of using the server name in their URL they will use "localhost."

If you will be taking advantage of Empower's one-touch update ability, you will need to install the SSH key files, as described in Chapter 6.1.

---

## Chapter 2: Automated Setup

This section describes how to install Empower to a Windows machine (which we will often call the server in what follows) using the no-net install package, which does not require access to the Internet during installation.

1. Unzip Empower Setup No Net.zip to a conveniently location on your server.

2. Open a command window as Administrator and cd to the location in which you unzipped Empower Setup No Net.zip.

3. Run the batch file InstallEmpower.bat. This will install Empower in the directory c:\encore-analytics\empower. To install Empower in an alternate location, specify the desired directory as a command line argument when running InstallEmpower.bat. For example:

   ```
   .\InstallEmpower.bat D:\encore-analytics
   ```

   To install Postgres, Git, Perl, or Java to a non-default location, please contact Encore Analytics technical support for an alternate InstallEmpower.bat file.

   If you are not connected to the Internet, you may get some error messages when the Perl package manager cpanm tries to get packages from the web. These messages can be ignored; all the necessary Perl packages are part of the install package. The installer will start the Empower service as the last thing it does.

   **Note:** If installing Empower on a Windows 10 machine, uncomment line 90 in the file InstallEmpower.bat using a text editor, so that it reads:

   ```
   nssm set Empower AppNoConsole 1
   ```

4. At this point, you should be able to run Empower against the Postgres database that comes with Empower. In your browser's address bar, on the machine on which Empower is installed, type:

   ```
   http://localhost:5000
   ```

   You will see Empower's login screen. If you are directed to a "not found" instead of the login screen, append the URL with "/index.html", like:

   ```
   http://localhost:5000/index.html
   ```

   Log in with "Admin/admin". Once you are logged in you will see Empower's trip panel layout. You may be prompted for license files; if so click Upload and follow the prompts. Once you are logged in, do File > Open Dataset. You will see a list of one or more sample contracts preloaded in the Postgres database that comes with Empower. You can use this Postgres database for your production data or use it, and the sample contracts, for training purposes.

   In the Open Dataset dialog, pick the MOH-2 contract and click OK. You should see the MOH-2 contract appear in Empower's trip panel layout.

5. Now that Empower has been installed, we suggest reviewing the "Empower Configuration File" and "Security Settings in Empower" technical documents (available on our support site here). These documents describe additional configuration options and security settings for Empower. The CHECK_LEVEL setting in "Security Settings in Empower" may be of particular interest for sites that wish to protect against hacking threats such as command injection and cross-site scripting. This setting prevents Empower users from bypassing the application security via the hacking techniques mentioned above to access data that they do not have permissions for. See the "Security Settings in Empower" document for more details, including enabling session time-out and setting the password complexity standard.

   The User's Manual can be accessed through Empower's Help menu. It can also be found in \encore-analytics\empower\www.

   As mentioned, you already have one data source, containing one or more sample contracts, running on the included Postgres database. If you wish to add more data sources on other database products, you can go to Chapter 3. Otherwise, you can jump to Chapter 4.

---

## Chapter 3: Creating Empower Databases

If you installed Empower using the setup script, you already have a Postgres database server with an Empower database that contains one or more sample contracts. If you would like to add databases on a different database product that Empower supports, or if you are doing the manual installation and you haven't created any databases yet, this chapter will explain how to created Empower databases on the database server products Empower supports (PostgreSQL, SQL Server, and Oracle). We assume that you have already installed your database product.

Empower comes with scripts to create its database on the supported database servers. These scripts are found in a folder called sql in the Empower directory. On Docker machines, the Empower directory will be /root/empower/; on Windows machines, with the default installation, it will be c:\encore-analytics\empower. The scripts you need and their locations are shown in the table below.

| Database Type | Location |
|---|---|
| PostgreSQL | sql/Postgres |
| SQL Server | sql/MSSQL |
| Oracle | sql/Oracle |

You should always create your Empower database using the scripts that accompany your Empower installation. This ensures that your database version is compatible with your Empower application version. If you use the scripts appropriate to your Empower version, there is no need to run any of the database update scripts. Otherwise, if you use an earlier version of the scripts, you will need to run the approprate database update scripts after creating the database. If you use a later version of the scripts to build your database you should have no problems.

**Note:** The "database update scripts" have the naming convention db#n-#m.sql where #n is the database version the script is updating from, and #m is the version it is updating to. The database version can be found in the "dbver" table in your Empower database.

For default installations, the steps described in this document should work without change. In each case, change to the directory containing the database creation files before launching the indicated scripts. A database administrator should review the scripts and make any necessary local modifications, consulting with your local tech support as required.

Note that Empower can use more than one database. A database on a particular database server is a data source, and is referred to by a data source name (DSN). You could set up muliple data sources, each identified by a meaningful DSN, perhaps to distinguish production work from training data. When users log onto Empower, they will choose which data source they wish to use by selecting from a dropdown list of DSNs.

### 3.1 Using a Remote Database

If you are using a remote SQL Server or Oracle database with Empower, you must install the appropriate client files on the Empower server in order to connect to the database. You can obtain the SQL Server client files at https://www.microsoft.com/en-us/download/details.aspx?id=53339 and the Oracle client files from https://www.oracle.com/database/technologies/instant-client.html

### 3.2 Bulk Import Tools

A further note: Empower can import files in its own optimized format, as well as files in various XML formats. Importing files in the optimized format (also called "bulk import") offers significant performance improvements. To support importing such files, the command line client for the target database must be present on the application server (i.e., the machine on which Empower is installed). In many cases, the application server and the database server will be different machines, and so an extra step will be required in order to support importation of optimized files. In the sections that follow, we will identify the required command line client for each database. If you cannot, for some reason, install the command line client on your application server, you will need to set the configuration variable NO_BULK (in Empower's configuration file empower.conf) to the name of your database product (pg, mssql, or oracle). If you are using more than one database product, and you want to set NO_BULK for more than one of them, provide a list of databases separated by semicolons, e.g., NO_BULK=mssql;oracle.

You will still be able to import optimized files, though you will not get the performance advantages associated with optimized files. See the Technical Note "The Empower Configuration File" (available from Encore Analytics tech support) for more information on Empower's configuration file.

### 3.3 PostgreSQL

If the machine on which the database is to be created has a Perl interpreter, you can use a utility script to create the Postgres database (and a corresponding DSN). Change to the Empower directory, then:

```
perl add_db.pl
```

You will be prompted to enter the IP address for the database server, as well as the database superuser's name (which is often postgres) and password.

If, on the other hand, you are creating the database on a machine without Perl, copy the all the *.sql scripts from the sql/postgres folder to the target machine. Then, on the target machine, open a command window, cd to the folder containing the scripts you just copied, start the Postgres command line client and run the build_empower.sql script to build the database, as follows:

```
psql -U [sa-un] -f build_empower.sql
[enter super user's password when prompted]
```

#### 3.3.1 Application and Database Server on Different Servers

The Postgres command line client is psql. If for some reason you cannot put the location of psql in your path variable, then edit empower.conf to include PG_HOME=<path to psql>. If you cannot install psql on your application server, and your app server and db server are different, edit your empower.conf file to include NO_BULK=postgres.

### 3.4 SQL Server

SQL Server databases, of course, can only be created on machines running Windows. If the target machine is not the Empower application server, copy the all the scripts from the Empower server's sql/MSSQL folder to the target machine. Open a command window, navigate to the folder where you copied the scripts, and run build_empower.bat[sa-un], where [sa-un] is the database super user's username, as follows:

```
build_empower [sa-un]
[enter super user's password when prompted]
```

#### 3.4.1 Application and Database Server on Different Servers

If you are using SQL Server as your database, and your application server and database server are different machines, you will need to install sqlcmd.exe on the app server (and its prerequisite, the SQL Server native client). Another necessary program, bcp.exe, will also be installed as part of installing the command line client. See https://www.microsoft.com/en-us/download/details.aspx?id=53591 to get these free utilities.

The Microsoft ODBC Driver for SQL Server is a prerequisite for installing sqlcmd. If it is not already installed on your system, you can download it from https://www.microsoft.com/en-us/download/details.aspx?id=53339.

The command line programs necessary to support bulk loading of optimized files with SQL Server are sqlcmd.exe and bcp.exe. If for some reason you cannot put the location of sqlcmd and bcp in your path variable, then edit empower.conf to include MSSQL_HOME=<path to sqlcmd and bcp>. If you cannot install sqlcmd and bcp on your application server, and your app server and db server are different, edit your empower.conf file to include NO_BULK=mssql.

#### 3.4.2 SQL Server with Windows Authentication

If you are using SQL Server with Windows Authentication, you will need to make sure that the Empower service is running as a user that SQL Server trusts, or that the "Local System Account" has permissions for SQL Server.

### 3.5 Oracle

Copy the contents of the Oracle folder to a convenient folder on the database server, open a command window, and navigate to that folder. You may have to adjust the last line of the script empdb.sql (the connection string) for your system. Then run the database creation script as follows:

```
sqlplus /nolog
SQL> CONN SYSTEM/[super user's password]
SQL> @build_empower
SQL> exit
```

#### 3.5.1 Application and Database Server on Different Servers

The Oracle command line client is sqlldr. If for some reason you cannot put the location of sqlldr in your path variable, then edit empower.conf to include ORA_HOME=<path to sqlldr>. If you cannot install sqlldr on your application server, and your app server and db server are different, edit your empower.conf file to include NO_BULK=oracle.

### 3.6 Create a new data source name

A data source name (abbreviated DSN) is how a user refers to a particular database on a particular database server. When one starts Empower, a list of DSNs will be shown in a listbox on the login page. (Of course, if you only have one data source configured, there will only be one DSN in the list.)

If you created your database by using the Windows setup script, or you used the utility add_postgres_db, the new data source name has already been created and you can skip this step. Otherwise, you will need to tell Empower how to reach your new database.

You will need to create an entry in the datasrc.ini file in the Empower directory telling Empower where to find the database and how to connect to it. To do this, open a command window, and cd to the Empower directory. Then run the add_dsn utility. How you do this will be slightly different depending on whether you are on the Linux virtual machine or on a Windows machine. On Unix/Linux, just type add_dsn. On Windows or the Mac, you will need to type perl add_dsn.pl.

The utility will then prompt for the values it needs, listed below:

1. Data source: You may enter anything you like for the data source name (DSN). This is what you will select from the dropdown box when you log into Empower.

2. Database type: Enter P, O, or S, for Postgres, Oracle, or SQL Server respectively.

3. IP address of your [db] instance: Enter the IP address of the machine on which your database server is running. If the database server is the same machine as the Empower server, you can accept the default of "localhost".

4. Port on which db is listening: The script will suggest the default port on which your chosen database type normally listens. If your database instance is set up to listen on a different port, you will need to enter that value; if you don't know what this means, you'll need to ask your database administrator.

5. Name of the Empower database: Default is "empower".

6. Name of the Empower user: Default is "empower".

7. Password of the Empower user: Default is "empowerpwd".

8. sid (MSSQL and Oracle): a system identifier for SQL Server or Oracle

9. svc (Oracle): the service name used when connecting to your Oracle database. Note that you can set up the data source to connect to your Oracle database using the service name without using the "sid." To do this, ensure that you have a valid "svc" entry, then remove the "sid" entry from your "datasrc.ini" file after creating your data source.

10. dvr (MSSQL): the driver name for SQL Server. See the "Database Utilities" chapter for more information.

Empower users do not need to know the name of the database or the database user name and password; this information is important, however, for Empower administrators and database administrators.

---

## Chapter 4: Populate the new database with your data

At this point, we assume you have installed Empower. When you have an Empower database, you will want to populate it with your own data.

Your data might be in a wInsight database, or it might be in some EDI format, such as a wInsight or Empower export file (*.xml), an Empower archive (otherwise known as optimized) file (*_ea.zip), an ANSI X12 839 file (*.trn), a wInsight archive (*.wsa), a UN/CEFACT Format 1–4, 6 or 7 file (*.xml), or an Empower-compatible Excel file, such as an export from Primavera P6, Microsoft Project or MPM, or a Department of Energy Flat File (*.xls, *.xlsx).

If the data you want is in a wInsight database, back up your data from wInsight, and save the wInsight archive to any convenient directory. If the data is already in an EDI file, just continue on with the next paragraph.

Start Empower by browsing to http://[host]:[port], where [host] is the IP address or host name of the machine on which Empower is installed and [port] is the port on which the Empower server is listening (5000 by default).

You should see Empower's default screen layout, with a "Dataset" window at the top, and two windows, named "Chart" and "Reports", side-by-side below.

First, from the Empower menu, select Admin | Import EDI File. Press the Choose File button. Your system's file browser will appear. Find your data file and press Open. The name of the file will now appear in the Import EDI File dialog. Press Upload. The dialog will change to show you a list of files. If you originally selected a single non-zip file, the list will have just that file. If, on the other hand, you originally selected a zip file, the list will show all the individual files that are compressed within the zip file. You may select one or more of the files in the list. Press Import. You will see a textbox named Status which will show the progress of the import, ending, one hopes, with "Import Succeeded. Done." Close the dialog. (For a fuller treatment of the EDI Import command, including the various import options not mentioned here, see the User's Manual.)

Next, you need to recalculate. In recalculation, Empower adds value to the incoming data by perfoming many calculations to generate additional fields and uncover data quality issues. To recalculate, select the Admin | Recalculate menu command. A dialog will appear, showing you a list of contracts and their associated periods in the database. If you select a contract and press the Recalculate button below the Contracts listbox, Empower will recalculate that contract for all periods. You can recalculate just a single period for a given contract by selecting the contract and a period, then pressing Recalculate under the Periods listbox. A dialog will appear showing the progress of the recalculation. Again, there are many options for the recalculation process which are described in the User's Manual.

Now that you have prepared some data, you can start analyzing it by choosing File | Open Dataset from Empower's menu. A dialog will appear allowing you to choose the contract, period, structure, and units. Press OK to make your selection, then close the dialog. You should see your data appear, in different perspectives, in the three windows of Empower.

---

## Chapter 5: Setting up a Reverse Proxy Rule

This chapter describes setting up a reverse proxy rule to run Empower with IIS. This chapter is optional; it just describes different way of starting Empower in the browser that may be more comfortable for some users.

As mentioned above, Empower does not require IIS to run on Windows. However, if you are using IIS and you think your users would be more comfortable invoking Empower with a syntax like http://[host]/empower/ than the standard syntax of http://[host]:[port], you can create a rule in IIS to achieve this. Here are the steps:

1. Start IIS Manager. (Click the Start button, enter "inetmgr" in the "Search Programs and Files" textbox, then click on the resulting link.)

2. Click on "Default Web Site" under "Sites".

3. In the "IIS" section, double-click on "URL Rewrite".

4. In the pane on the left, click "Add Rules". "Blank rule" will be selected by default. Click "OK" to accept this choice. You will see a screen entitled "Edit Inbound Rule". The Requested URL field should already be set to "Matches the Pattern" and the Using field should already be set to "Regular Expressions". "Ignore case" should already be checked.

5. Set the Name field to "Empower Reverse Proxy".

6. Set the Pattern field to "empower/(.*)".

   The Match URL section should now look like this:

   **Figure 5.1: Match URL Section**

7. In the Action section, the Action type should already be set to "Rewrite". Under Action Properties, set the Rewrite URL field to:

   ```
   http://127.0.0.1:5000/{R:1}
   ```

   (Of course, if you used a different port than the default value of 5000, you would enter your value instead of 5000 here.)

8. Check both the "Append query string" box and the "Stop processing of subsequent rules" box.

   The Action section should now look like this:

   **Figure 5.2: Action Section**

9. In the pane on the right, click Apply.

10. Restart IIS. (Click on Default Web Site in the left pane, and Restart in the right pane.)

Once you have performed these steps, your users can start Empower by typing http://[host]/empower/ in their browser (note the trailing slash).

---

## Chapter 6: Update to the latest version of Empower

In this chapter, we describe how to update your Empower installation. You might want to do this soon after finishing the installation, in case we have released a new version of Empower since you obtained the installation package (i.e., the EmpowerSetupNoNet.zip file). At any rate, you may want to keep this chapter handy for when a new release is available and you want to update your Empower.

This update process requires:

1. An Internet connection from the Empower application server,
2. The ability to access port 22 through your firewall, and
3. The SSH keys used to authenticate yourself to our source code repository.

(Some sites do not meet the first two criteria due to security policies. If this describes your site, please contact Encore Analytics tech support to request a patch file instead.)

### 6.1 Install SSH keys

Empower can be updated, to get new feature releases or bug fixes, by simply running an update script. To take advantage of this feature, your application server (the machine on which the Empower software is installed) needs to have Internet access, your firewall needs to allow access through port 22, and you need to have the SSH keys that will allow you to access our source code repository. This chapter describes how to install those SSH keys.

(At some sites, security policy forbids Internet access from application servers, or traffic through port 22. Such sites will not be able to use the update script, and so will not need to install the SSH keys. If your site is in this category, you can skip this chapter. Please contact Encore Analytics technical support for other update options.)

Access to Empower's source code is controlled by means of public-private key pairs, which need to be installed in a user's home directory on the server. That user will be, by definition, the Empower administrator for that server.

The keys used in this process may change, requiring you to replace them. If your keys stop working, contact Encore Analytics support for updated keys.

To install the SSH keys:

1. You should have received a file named something like empower_ssh.zip. Copy that file to the admin's home directory.

2. Extract the contents of the zip file to the admin's directory itself. This can be tricky — if you do the natural thing, the files will wind up in the wrong place, or the folder will not have permissions set correctly. Please follow this procedure exactly.

   (a) Right-click on the zip file and choose Extract All.

   (b) Change the destination folder to the user's directory, e.g.:

       ```
       C:\Users\Your_User_Name
       ```

   (c) Click Extract. You should wind up with a folder named .ssh in the user's home directory (not a folder named ssh with a subfolder named .ssh.) In the .ssh folder you should have a config vile and a key file: config and eadistrib.

**Note:** You will probably want to give the ability to run the update script to several system administrators. Simply repeat the procedure above to install the keys in each SA's home directory.

### 6.2 Running an Empower Update

To update, open a command window as the administrator, and cd to the empower directory (if you accepted the defaults during installation, that will be c:\encore-analytics\empower). Then run update.

The script will show you some status messages, depending on how many files need updating. Soon it will say: Empower system files are up to date. Then it will run through any remote data sources you've created with add_dsn and ask if you want to update the databases they point to. Typically, you'll want to do this, so enter Y (uppercase).

Finally, you will see the update script stopping and starting the Empower service (Net stop Empower; Net start Empower).

After update is finished with the list of data source names, it will return you to the command prompt, and you're finished updating.

### 6.3 The sys_update and db_update scripts

If necessary, you can run the empower system and database update scripts manually. For example, if you choose not to update a remote database while applying a patch file but now want to update it, you can run db_update.pl to update the database. These scripts are run automatically when you update Empower with the update command or a patch file, but running them multiple times is harmless.

Running the sys_update.pl and db_update.pl Perl scripts will update the Empower files and database to the latest versions, and, if needed, install software necessary to run programs written to the PSGI standard (e.g., Plack and Thrall). Open a command prompt, cd to the empower directory, and run the scripts in order as follows:

```
perl sys_update.pl
perl db_update.pl
```

If your Empower installation is completely up to date, you'll see messages like this:

```
Empower system files are up to date.
Updating local-Pg . . .
```

If your installation needs some updating, the messages might look like this:

```
executing update_sys_9_to_10 . . .
Plack is up to date. (1.0029)
Updating local-Pg . . .
executing sql/Postgres/maint.sql . . .
executing sql/Postgres/recalc_cc.sql . . .
executing sql/Postgres/recalc_cd.sql . . .
```

If a Perl module needs updating, you might see something like:

```
-> Working on CGI::Compile
Fetching http://www.cpan [etc etc etc] CGI-Compile [blah blah blah]
Configuring CGI-Compile-0.16 ... OK
Building and testing CGI-Compile-0.16 ... OK
Successfully installed CGI-Compile-0.16

# 1 distribution installed
```

**Note:** If you are updating via a patch file, any new Perl modules will be included as a standalone file in the patch zip and installed when the patch is run.

After running the system update command, the database update command should be run.

The database update command can also be run as `perl db_update.pl N`. Notice the command line parameter 'N'. This parameter indicates that you would NOT like to be prompted when updating remote databases, instead they will automatically be updated. This can be useful when updating multiple remote databases at once. By default db_update will prompt the user for a 'Y' (yes) or 'N' (no) when updating each remote database.

---

## Chapter 7: Database Utilities

Empower comes with several utilities to help you manage your Empower databases and data sources.

These utilities are Perl scripts. On Unix or Linux, you run them by just entering the base name of the utility (e.g., add_dsn). Under Windows or Mac OS X, you will need to enter the name of the Perl interpreter and add the file extension (e.g., perl add_dsn.pl).

On Windows, run a script named script with command line parameters params like this:

```
perl script.pl params
```

The utilities each ask a series of questions, with default answers enclosed in square brackets. Press ENTER to accept the default, or supply an alternative before pressing ENTER. Usually the defaults allow you to proceed, but sometimes (as when deleting a database) the default is "N" or no. In such cases, enter an upper-case "Y" to proceed.

The utilities to add and delete databases work only with Postgres. The utilities to add and delete DSNs work with any database type.

### 7.1 Add Database (add_db)

This utility creates an empty Empower PostgreSQL database and a corresponding entry in the datasrc.ini file.

At the command prompt, type:

```
add_db (Unix/Linux)
```

or

```
perl add_db.pl (Windows or Mac)
```

to create a PostgreSQL database.

The utility will ask you if really want to create a new database; enter "Y" (upper-case).

The utility will then ask for the database host (a name or IP address), the super user's name and password, a name for the database, a database user name, and a password for that user.

Next, the utility will ask you for a name for the data source. This is what you will select in the Data Source drop list when you login to Empower.

Once the utility has gathered all the information it needs, it will create an empty Empower database create a corresponding entry in the datasrc.ini file.

### 7.2 Delete Database (del_db)

This utility will delete a PostgreSQL database and delete its entry in the datasrc.ini configuration file.

At the command prompt, type:

```
del_db (Unix/Linux)
```

or

```
perl del_db.pl [sw-un [su-pw]] (Windows or Mac)
```

to remove a PostgreSQL database.

The utility will ask if you really want to delete a database. After you assure it that you do, it will present you with a numbered list of all the databases in the server. Enter the number corresponding to the database you want to delete. The utility will delete the data source entry in the configuration file and then delete the database itself. You will also have the option to delete the user associated with the database as well.

**Note:** The list of databases may contain non-Empower "housekeeping" databases (for example, performance_schema) that are used internally by the database engine, and should be left alone. You can safely delete empower or any database you created with the add_postgres_db utilities.

### 7.3 Add Data Source Name (add_dsn)

This utility creates a data source entry in the datasrc.ini configuration file. It does not create a database, nor does it check to see that the database exists. It is not limited to PostgreSQL databases; it will work with any database Empower supports.

At the command prompt, type:

```
add_dsn (Unix/Linux)
```

or

```
perl add_dsn.pl (Windows or Mac)
```

The utility will ask for a name for the data source. This is what you will select in the Data Source drop list when you login to Empower.

The utility will then ask you what type of database you are connecting to (PostgreSQL, Oracle, or SQL Server).

Next, it asks you for several more parameters, suggesting reasonable defaults. The resulting entry will be written to the end of the datasrc.ini file. If you would like to change the order, for instance if you want the new entry to be the default choice when Empower starts, see the del_dsn utility below.

### 7.4 Delete Data Source Name (del_dsn)

This utility does two things: first, it deletes entries from the datasrc.ini configuration file. Second, it gives the user the chance to reorder the entries that are kept. The reason for this is so that the user can change which entry appears at the top of the configuration file and therefore is the default choice when Empower starts. This command does not delete the actual databases referred to in the configuration file.

This utility is not limited to PostgreSQL databases; it will work with any database Empower supports.

At the command prompt, type:

```
del_dsn (Unix/Linux)
```

or

```
perl del_dsn.pl (Windows or Mac)
```

The utility will then present you with a screen listing the available data sources, for example:

```
Enter the numbers of the DSN's you wish to KEEP, in the order
in which they should appear.
1. local-Pg
2. remote-MSSQL
3. Empower
4. localhost-fred
Enter 1-4, separated by spaces, Q to quit. [Q]
```

Note carefully that you are telling the utility which entries you don't want to delete. Note also that the order in which you enter the numbers is the order in which the entries will appear in the configuration file. If you were to enter, for example, "4 3", the default data source would become "localhost-fred" instead of "local-Pg", and "local-Pg" and "remote-MSSQL" would no longer be available.

Once you have made your choices, the utility shows you the data sources that will be kept, and asks you if this is what you want. You can abort the whole process by entering "N', or write the changes by entering "Y".

### 7.5 Add Data Source Non-Interactively (np_add_dsn)

This utility allows you to add data sources non-interactively by providing all of the data source information as command line parameters. Running perl np_add_dsn.pl with no arguments provides a list of valid parameters.

```
Usage: np_add_dsn DSN dbtype host port dbname dbuser pwd [sid svc]
```

Parameters:

- **DSN**: data source name, e.g. 'Empower'
- **dbtype**: database type, one of postgres | mssql | oracle
- **host**: database IP address or host name
- **port**: database port, usually 5432 | 1433 | 1521
- **dbname**: database name, e.g. 'empower'
- **dbuser**: database user, e.g. 'empower'
- **pwd**: database password, e.g. 'empowerpwd'
- **sid**: (Oracle) system ID, default 'ORCL'
- **svc**: (Oracle) service ID, default 'ORCL'

These parameters correspond to the parameters that you would enter interactively when using add_dsn.pl. For example, you could run the following to add a Postgres data source called "Empower":

```
perl np_add_dsn.pl Empower postgres localhost 5432 empower empower empowerpwd
```

As with add_dsn, the dvr parameter can be added manually after creating your data source if necessary. This parameter is only used for SQL Server data sources where a non-default driver name should be specified. The default driver name is "SQL Server." The dvr entry should be added to datasrc.ini on its own line for the appropriate data source, making sure to leave a blank line between each data source entry. Note: make sure to leave a blank line at the end of the datasrc.ini file as well.

For example:

```
# [Mssql]

dbtype=mssql
host=localhost
port=1433
db=empower
user=empower
password=<encrypted password>
sid=localhost
nocache=1
dvr=ODBC Driver 13 for SQL Server
```

---

## Chapter 8: Testing and Troubleshooting

The following steps can be performed to verify successful installation.

1. In your browser's address line, enter "http://[host]:[port]" (e.g., http://192.168.56.101:5000). If application-level security is off, you'll go directly to Empower's main window; otherwise, you'll be shown the login screen.

2. If prompted, login as the Empower "Admin" user.

3. At the Empower screen, select Dataset from the far left of the toolbar. A populated dataset dialog box should appear.

4. Select a contract, period, structure and unit as usual, and press OK. You should see the Sort Window across the top, a chart at bottom left, and a report at bottom right. Close the dialog box by clicking the "x" at upper right. (This applies to all dialog boxes.)

   A problem with the above items is probably related to the database connection, or to application-level security. Run `perl checkconn.pl [dsn]` to verify that you have a working connection to the database. Check the User's Manual to learn how to manage application-level security.

5. Select the Export Sort Window command from the File menu. When prompted, choose Open. Depending on which browser you are using, an Excel file should appear, or the browser will ask you where to save the Excel file.

   A problem here likely means you didn't run `perl sys_update.pl` and `perl db_update.pl`.

6. Finally, in the upper right corner of the chart window (the lower left pane) click the menu button. This will look like three horizontal bars. From the resulting popup menu, select either Download PNG raster image or Download PDF document. When prompted, choose Open. Depending on which browser you are using, an image of the chart should appear, or the browser will ask you where to save the image file.

   A failure here most likely indicates one or more of the following:

   - If you are not using Batik:
     - the rsvg-convert.exe file is missing from your empower directory
     - the "Lucida Grande" font is not installed
   - a problem with the Batik installation
   - the line USE_BATIK=1 is missing from the empower.conf configuration file
   - a problem with the underlying Java installation
   - you didn't run perl post_update.pl

If any of these tests fail, please review the installations instructions above, and/or contact tech support for assistance. (See Section 10 for how to get help.)

---

## Chapter 9: Uninstalling Empower

To uninstall Empower from Windows follow these steps:

1. Stop the Empower service. This can be done via Windows Services.

2. Open an Administrator command prompt and 'cd' to your empower directory.

3. Next, to remove the service, run "./nssm.exe remove Empower" from the command prompt.

4. Now you can delete the Empower directory (typically C:\encore-analytics\empower), which will uninstall Empower.

5. Empower also installs Git, Postgres, and Strawberry Perl. If you wish to uninstall these as well, run the uninstaller (Control Panel > Add/remove programs) for each.

---

## Chapter 10: Getting Help

Empower's Help menu leads to a dialog telling the user how to contact technical support. That information is also presented here.

To obtain support, contact us between the hours of 8 a.m.–5 p.m. Pacific Time except for US Federal holidays.

- **Phone:** 866.890.4331x2
- **Web:** http://encoreanalyticsllc.freshdesk.com/

Empower's Help | User's Manual command also brings up the User's Manual (as a PDF) in another browser tab.
