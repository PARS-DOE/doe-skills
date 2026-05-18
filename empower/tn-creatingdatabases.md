# Creating Databases for Empower

*Source: TN-CreatingDatabases.pdf*

---

© 2013 Encore Analytics, LLC
May 15, 2025

## Contents

1. [Introduction](#1-introduction)
2. [Database Options](#2-database-options)
3. [Creating Empower Databases](#3-creating-empower-databases)
   - 3.1 [Using a Remote Database](#31-using-a-remote-database)
   - 3.2 [Bulk Import Tools](#32-bulk-import-tools)
   - 3.3 [PostgreSQL](#33-postgresql)
   - 3.4 [SQL Server](#34-sql-server)
   - 3.5 [Oracle](#35-oracle)
   - 3.6 [Create a database manually](#36-create-a-database-manually)
   - 3.7 [Create a new data source name](#37-create-a-new-data-source-name)
   - 3.8 [Populate the new database with your data](#38-populate-the-new-database-with-your-data)
4. [Database Utilities](#4-database-utilities)
   - 4.1 [Add Database (add_db)](#41-add-database-add_db)
   - 4.2 [Delete Database (del_db)](#42-delete-database-del_db)
   - 4.3 [Add Data Source Name (add_dsn)](#43-add-data-source-name-add_dsn)
   - 4.4 [Delete Data Source Name (del_dsn)](#44-delete-data-source-name-del_dsn)
   - 4.5 [Add Data Source Non-Interactively (np_add_dsn)](#45-add-data-source-non-interactively-np_add_dsn)
   - 4.6 [Bulk Data (bulk_data)](#46-bulk-data-bulk_data)
5. [Updating the Empower Database Manually](#5-updating-the-empower-database-manually)

---

## 1. Introduction

This document explains how to create databases for use with Empower, how to migrate existing data from wInsight or other sources, to the new Empower database, and how to use several utilities to manage Empower databases and data sources. This document applies to all Empower installation scenarios: Empower hosted on a Docker container, Empower installed directly on a Windows, Unix/Linux or Mac computer, and Empower installed on an Amazon Web Services instance.

## 2. Database Options

Empower works with these database products:

1. **PostgreSQL.** The Windows setup program for Empower automatically installs a Postgres server, creates an Empower database, and populates the database with sample contracts. This Postgres instance will be installed on the application (i.e., Empower) server. Postgres is an enterprise-quality, open-source database system, and we recommend it if you don't already have a preferred database system. (Note: the official name is "PostgreSQL," but many people, including ourselves, usually call the product simply "Postgres.") Postgres is available for Windows, Unix/Linux, and Mac OS X.

2. **Microsoft SQL Server.** Empower supports SQL Server Authentication (logging on with a database user name and password), and Windows Authentication (using the user's Windows credentials to log in to the database).

3. **Oracle.** This well-known commercial product is available for Unix/Linux and Windows.

Note that since Empower doesn't have to be on the same server as the database, Empower doesn't have to run under the same OS as the database. Thus, Empower running on, say Linux, can access a SQL Server database, which may be running on Windows.

We recommend that you install the Postgres server and the sample database even if you intend to use one of the other products for your production data, as you can use the Postgres database and the sample contracts that are supplied with Empower for testing and training.

If you are using the Docker version of Empower, or have installed Empower on a Windows machine using the setup script, you will already have the Postgres database and sample contracts pre-loaded. If you prefer another database product, you can uninstall Postgres. However, we recommend that you keep the Postgres server and the sample database even if you intend to use one of the other products for your production data, as you can use the Postgres database and the sample contracts for testing and training.

## 3. Creating Empower Databases

Empower comes with scripts to create its database on the supported database servers. These scripts are found in a folder called sql in the Empower directory. On Docker machines, the Empower directory will be /root/empower/; on Windows machines, with the default installation, it will be c:\encore-analytics\empower. The scripts you need and their locations are shown in the table below.

| Database | Location |
|----------|----------|
| PostgreSQL | sql/Postgres |
| SQL Server | sql/MSSQL |
| Oracle | sql/Oracle |

You should always create your Empower database using the scripts that accompany your Empower installation. This ensures that your database version is compatible with your Empower application version. If you use the scripts appropriate to your Empower version, there is no need to run any of the database update scripts. Otherwise, if you use an earlier version of the scripts, you will need to run the approprate database update scripts after creating the database. If you use a later version of the scripts to build your database you should have no problems.

Note: the "database update scripts" have the naming convention db#n-#m.sql where #n is the database version the script is updating from, and #m is the version it is updating to. The database version can be found in the "dbver" table in your Empower database.

For default installations, the steps described in this document should work without change. In each case, change to the directory containing the database creation files before launching the indicated scripts. A database administrator should review the scripts and make any necessary local modifications, consulting with your local tech support as required.

Note that Empower can use more than one database. A database on a particular database server is a data source, and is referred to by a data source name (DSN). You could set up muliple data sources, each identified by a meaningful DSN, perhaps to distinguish production work from training data. When users log onto Empower, they will choose which data source they wish to use by selecting from a dropdown list of DSNs.

### 3.1 Using a Remote Database

If you are using a remote SQL Server or Oracle database with Empower, you must install the appropriate client files on the Empower server in order to connect to the database. You can obtain the SQL Server client files at https://www.microsoft.com/en-us/download/details.aspx?id=53339 and the Oracle client files from https://www.oracle.com/database/technologies/instant-client.html

### 3.2 Bulk Import Tools

A further note: Empower can import files in its own optimized format, as well as files in various XML formats. Importing files in the optimized format (also called "bulk import") offers significant performance improvements. To support importing such files, the command line client for the target database must be present on the application server (i.e., the machine on which Empower is installed). In many cases, the application server and the database server will be different machines, and so an extra step will be required in order to support importation of optimized files. In these sections that follow, we will identify the required command line client for each database. If you cannot, for some reason, install the command line client on your application server, you will need to set the configuration variable NO_BULK (in Empower's configuration file empower.conf) to the name of your database product (pg, mssql, or oracle. If you are using more than one database product, and you want to set NO_BULK for more than one of them, provide a list of databases separated by semicolons, e.g., NO_BULK=mssql;oracle.

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

SQL Server databases, of course, can only be created on machines running Windows. If the target machine is not the Empower application server, copy the all the scripts from the Empower server's sql/MSSQL folder to the target machine. Open a command window, navigate to the folder where you copied the scripts, and run build_empower.bat [sa-un], where [sa-un] is the database super user's username, as follows:

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

### 3.6 Create a database manually

If you are unable to use the build_empower scripts described in the previous sections, you also have the option of manually creating your database by running our SQL scripts. Essentially, instead of using our build_empower scripts (which would call our SQL scripts in the correct order) you would run the SQL scripts yourself. As a reminder, you would find the necessary SQL scripts for creating your database in the empower/sql/<yourdbtype> folder on your Empower server.

To manually create the database, you would run these SQL scripts in order. Make sure to run the scripts as a user with sufficient privileges.

- empdb.sql
- empsch.sql
- maint.sql
- recalc_cc.sql
- recalc_cd.sql
- recalc_inc.sql
- populate.sql

### 3.7 Create a new data source name

A data source name (abbreviated DSN) is how a user refers to a particular database on a particular database server. When one starts Empower, a list of DSNs will be shown in a listbox on the login page. (Of course, if you only have one data source configured, there will only be one DSN in the list.)

If you created your database by using the Windows setup script, or you used the utility add_postgres_db, the new data source name has already been created and you can skip this step. Otherwise, you will need to tell Empower how to reach your new database.

You will need to create an entry in the datasrc.ini file in the Empower directory telling Empower where to find the database and how to connect to it. To do this, open a command window, and cd to the Empower directory. Then run the add_dsn utility. How you do this will be slightly different depending on whether you are on the Linux virtual machine or on a Windows machine. On Unix/Linux, just type add_dsn. On Windows or the Mac, you will need to type perl add_dsn.pl.

The utility will then prompt for the values it needs, listed below:

1. **Data source:** You may enter anything you like for the data source name (DSN). This is what you will select from the dropdown box when you log into Empower.

2. **Database type:** Enter P, O, or S, for Postgres, Oracle, or SQL Server respectively.

3. **IP address of your [db] instance:** Enter the IP address of the machine on which your database server is running. If the database server is the same machine as the Empower server, you can accept the default of "localhost".

4. **Port on which db is listening:** The script will suggest the default port on which your chosen database type normally listens. If your database instance is set up to listen on a different port, you will need to enter that value; if you don't know what this means, you'll need to ask your database administrator.

5. **Name of the Empower database:** Default is "empower".

6. **Name of the Empower user:** Default is "empower".

7. **Password of the Empower user:** Default is "empowerpwd".

8. **sid (MSSQL and Oracle):** a system identifier for SQL Server or Oracle

9. **svc (Oracle):** the service name used when connecting to your Oracle database. Note that you can set up the data source to connect to your Oracle database using the service name without using the "sid." To do this, ensure that you have a valid "svc" entry, then remove the "sid" entry from your "datasrc.ini" file after creating your data source.

10. **dvr (MSSQL):** the driver name for SQL Server. See the "Database Utilities" chapter for more information.

Empower users do not need to know the name of the database or the database user name and password; this information is important, however, for Empower administrators and database administrators.

### 3.8 Populate the new database with your data

At this point, we assume you have installed Empower. When you have an Empower database, you will want to populate it with your own data.

Your data might be in a wInsight database, or it might be in some EDI format, such as a wInsight or Empower export file (*.xml), an Empower archive (otherwise known as optimized) file (*_ea.zip), an ANSI X12 839 file (*.trn), a wInsight archive (*.wsa), a UN/CEFACT Format 1–4, 6 or 7 file (*.xml), or an Empower-compatible Excel file, such as an export from Primavera P6, Microsoft Project or MPM, or a Department of Energy Flat File (*.xls, *.xlsx).

If the data you want is in a wInsight database, back up your data from wInsight, and save the wInsight archive to any convenient directory. If the data is already in an EDI file, just continue on with the next paragraph.

Start Empower by browsing to http://[host]:[port], where [host] is the IP address or host name of the machine on which Empower is installed and [port] is the port on which the Empower server is listening (5000 by default).

You should see Empower's default screen layout, with a "Dataset" window at the top, and two windows, named "Chart" and "Reports", side-by-side below.

First, from the Empower menu, select Admin | Import EDI File. Press the Choose File button. Your system's file browser will appear. Find your data file and press Open. The name of the file will now appear in the Import EDI File dialog. Press Upload. The dialog will change to show you a list of files. If you originally selected a single non-zip file, the list will have just that file. If, on the other hand, you originally selected a zip file, the list will show all the individual files that are compressed within the zip file. You may select one or more of the files in the list. Press Import. You will see a textbox named Status which will show the progress of the import, ending, one hopes, with "Import Succeeded. Done." Close the dialog. (For a fuller treatment of the EDI Import command, including the various import options not mentioned here, see the User's Manual.)

Next, you need to recalculate. In recalculation, Empower adds value to the incoming data by perfoming many calculations to generate additional fields and uncover data quality issues. To recalculate, select the Admin | Recalculate menu command. A dialog will appear, showing you a list of contracts and their associated periods in the database. If you select a contract and press the Recalculate button below the Contracts listbox, Empower will recalculate that contract for all periods. You can recalculate just a single period for a given contract by selecting the contract and a period, then pressing Recalculate under the Periods listbox. A dialog will appear showing the progress of the recalculation. Again, there are many options for the recalculation process which are described in the User's Manual.

Now that you have prepared some data, you can start analyzing it by choosing File | Open Dataset from Empower's menu. A dialog will appear allowing you to choose the contract, period, structure, and units. Press OK to make your selection, then close the dialog. You should see your data appear, in different perspectives, in the three windows of Empower.

## 4. Database Utilities

Empower comes with several utilities to help you manage your Empower databases and data sources.

These utilities are Perl scripts. On Unix or Linux, you run them by just entering the base name of the utility (e.g., add_dsn). Under Windows or Mac OS X, you will need to enter the name of the Perl interpreter and add the file extension (e.g., perl add_dsn.pl.

The utilities each ask a series of questions, with default answers enclosed in square brackets. Press ENTER to accept the default, or supply an alternative before pressing ENTER. Usually the defaults allow you to proceed, but sometimes (as when deleting a database) the default is "N" or no. In such cases, enter an upper-case "Y" to proceed.

The utilities to add and delete databases work only with Postgres. The utilities to add and delete DSNs work with any database type.

### 4.1 Add Database (add_db)

This utility creates an empty Empower PostgreSQL database and a corresponding entry in the datasrc.ini file.

At the command prompt, type

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

### 4.2 Delete Database (del_db)

This utility will delete a PostgreSQL database and delete its entry in the datasrc.ini configuration file.

At the command prompt, type

```
del_db (Unix/Linux)
```

or

```
perl del_db.pl [sw-un [su-pw]] (Windows or Mac)
```

to remove a PostgreSQL database.

The utility will ask if you really want to delete a database. After you assure it that you do, it will present you with a numbered list of all the databases in the server. Enter the number corresponding to the database you want to delete. The utility will delete the data source entry in the configuration file and then delete the database itself. You will also have the option to delete the user associated with the database as well.

Note: The list of databases may contain non-Empower "housekeeping" databases (for example, performance_schema) that are used internally by the database engine, and should be left alone. You can safely delete empower or any database you created with the add_postgres_db utilities.

### 4.3 Add Data Source Name (add_dsn)

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

Next, it asks you for several more parameters, suggesting reasonable defaults.

The resulting entry will be written to the end of the datasrc.ini file. If you would like to change the order, for instance if you want the new entry to be the default choice when Empower starts, see the del_dsn utility below.

### 4.4 Delete Data Source Name (del_dsn)

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

### 4.5 Add Data Source Non-Interactively (np_add_dsn)

This utility allows you to add data sources non-interactively by providing all of the data source information as command line parameters. Running perl np_add_dsn.pl with no arguments provides a list of valid parameters.

```
Usage: np_add_dsn DSN dbtype host port dbname dbuser pwd [sid svc]

DSN: data source name, e.g. 'Empower'
dbtype: database type, one of postgres | mssql | oracle
host: database IP address or host name
port: database port, usually 5432 | 1433 | 1521
dbname: database name, e.g. 'empower'
dbuser: database user, e.g. 'empower'
pwd: database password, e.g. 'empowerpwd'
sid: (Oracle) system ID, default 'ORCL'
svc: (Oracle) service ID, default 'ORCL'
```

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

### 4.6 Bulk Data (bulk_data)

Empower has a tool for downloading an entire database, called bulk_data.pl. Note that when used for importing data this method will overwrite existing data in the import database with the data in the import file. The export method can be used to create a backup file without impacting the data in the database being exported from.

#### 4.6.1 Exporting Data

The bulk_data tool can be used to generate an Empower optimized export of the entire contents of a given data source. This export is more comprehensive than an export generated via the Empower UI since it will contain items such as custom views, charts, dashboards, etc. In general, this more comprehensive file should only be imported via the corresponding bulk_data import method, NOT via the Empower UI.

To export data:

1. Navigate to the "empower" folder in an administrator command prompt on the Empower server where you want to export

2. Export the contents of the desired database with the command `perl bulk_data.pl e [DSN]`, replacing [DSN] with the name of the data source that you want to export data for. Example: To export data from a data source called "Empower" you would execute `perl bulk_data.pl e Empower`

3. This will generate a bulk backup file called [DSN]_dump.zip in the "empower" folder

#### 4.6.2 Importing Data

To import data:

1. Navigate to the "empower" folder in an administrator command prompt on the Empower server where you want to import. Make sure the bulk export file generated from the bulk_data export process is placed in this directory.

2. Run `perl bulk_data.pl n [Filename] [DSN]` where: [Filename] is the name of the file generated in step 3 of the export instructions and [DSN] is the data source name where you want to import the data

3. This will generate a file named [DSN]_load.zip

4. Make a new directory under the empower directory for loading files (for example, you could use "load") and move the [DSN]_load.zip file to the new directory. This will make cleanup easier later.

5. cd to the directory that you created in the previous step and unzip the bulk load file

6. If you are using Windows, you should see a file named something like [dbtype]_load.bat, where [dbtype] is the database type of the database that you're loading data into (e.g. Postgres, Oracle, MSSQL). To load all the data into the database, you need to execute the command [dbtype]_load.bat. If you are not using Windows, you can use the ".sh" file instead of the ".bat" file. Recall that this method will overwrite any existing data in the database.

## 5. Updating the Empower Database Manually

Typically, your Empower database(s) will automatically be updated during the Empower update process, whether that is done via an update script or a patch file. However, if you do choose not to update a database during that process, or have a database that needs updating for some other reason, you can update your database manually.

To update your database manually, you will need to run the appropriate SQL scripts in order for your empower database. In general, the scripts should be run as the "empower" database user. These scripts can be found in the empower/sql directory. Which scripts need to be run will depend on the current version of your database and the database version that you are updating to. You can find your current database version in the dbver table in your database. The version that you are updating to is indicated by the last part of your new Empower version. For example, if you updated to version "4.4.2.95" of Empower, you should update your database version to "95".

Once you know which database version you are updating from and to, run the database update scripts starting at the version you are updating from and continuing sequentially until the version you are updating to. The "database update scripts" have the naming convention db#n-#m.sql where #n is the database version the script is updating from, and #m is the version it is updating to.

For example, say your database is at version 90 and we want to update it to version 95. We would run these scripts in order:

- db90-91.sql
- db91-92.sql
- db92-93.sql
- db93-94.sql
- db94-95.sql

After importing the database update scripts, you should always import these scripts in order:

- maint.sql
- recalc_cc.sql
- recalc_cd.sql
- recalc_inc.sql
- recalc_user.sql (if present)
