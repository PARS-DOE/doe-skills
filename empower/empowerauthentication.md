# Empower Authentication

*Source: EmpowerAuthentication.pdf*

---

## User Authentication in Empower

© 2013 Encore Analytics, LLC
February 1, 2024

## Contents

1. [Introduction](#introduction)
2. [Empower Application-Level Security](#empower-application-level-security)
   - [Empower Application-Level Security Off](#21-empower-application-level-security-off)
   - [Empower Application-Level Security On](#22-empower-application-level-security-on)
3. [Preparing Users for Single Sign-On](#preparing-users-for-single-sign-on)
4. [How Empower Handles SSO](#how-empower-handles-sso)
5. [User Attributes](#user-attributes)
   - [Valid attributes](#51-valid-attributes)
   - [Parameter Examples](#52-parameter-examples)
6. [Example: Single Sign-On with IIS](#example-single-sign-on-with-iis)
   - [Install Microsoft modules](#61-install-microsoft-modules)
   - [Enable proxy for ARR](#62-enable-proxy-for-arr)
   - [Enable handler mappings](#63-enable-handler-mappings)
   - [Create a physical directory containing default.aspx](#64-create-a-physical-directory-containing-defaultaspx)
   - [Create a rewrite rule](#65-create-a-rewrite-rule)
   - [Configure the IIS virtual directory](#66-configure-the-iis-virtual-directory)
   - [Access Empower](#67-access-empower)
   - [Addressing Caching Issues in IIS](#68-addressing-caching-issues-in-iis)
7. [Example: SimpleSAML with IIS](#example-simplesaml-with-iis)
   - [Install PHP and ARR](#71-install-php-and-arr)
   - [Create the Empower Reverse Proxy](#72-create-the-empower-reverse-proxy)
   - [Bind a certificate](#73-bind-a-certificate)
   - [Install SimpleSAML](#74-install-simplesaml)
   - [Configure SimpleSAML](#75-configure-simplesaml)
   - [Configure Empower SAML Setup](#76-configure-empower-saml-setup)
   - [Testing SAML with Empower](#77-testing-saml-with-empower)
   - [Changing IdPs](#78-changing-idps)
   - [Differences Between simpleSAML 1.19 and 2.0](#79-differences-between-simplesaml-119-and-20)
8. [Example: Active Directory with Empower User Management](#example-active-directory-with-empower-user-management)
   - [Install IIS with PHP and ARR](#81-install-iis-with-php-and-arr)
   - [Create the Empower Reverse Proxy](#82-create-the-empower-reverse-proxy)
   - [Create the Physical Directory](#83-create-the-physical-directory)
   - [Configure the IIS Virtual Directory](#84-configure-the-iis-virtual-directory)
   - [Creating custom attributes](#85-creating-custom-attributes)
   - [Adding attributes to a class](#86-adding-attributes-to-a-class)
   - [Set User Values](#87-set-user-values)
   - [Edit index.php](#88-edit-indexphp)
9. [Example: SSL in IIS Without SSO](#example-ssl-in-iis-without-sso)
10. [Setting Default Contracts for Users](#setting-default-contracts-for-users)
11. [Single Sign-On with HTTP Headers](#single-sign-on-with-http-headers)
    - [Set Up Single Sign-On Using HTTP Headers](#111-set-up-single-sign-on-using-http-headers)

---

## Chapter 1

### Introduction

This Technical Note describes authentication in Empower, Empower's support for Single Sign-On (SSO), and the requirements for interfacing your authentication scheme with Empower's single sign-on support.

Empower supports SSO in two ways. In the first method, the name of the authenticated user is passed to Empower via the HTTP header REMOTE_USER. This method is more general and works on all operating systems. The second method uses a small web site that gets the name of the authenticated user and redirects to Empower, passing the name as a query parameter. The advantage of this system is that it can work with IIS, which does not have the rewrite capability to populate the REMOTE_USER header.

Please note that the SSO setups described in this document are provided as examples of how SSO can be integrated with Empower; you may need to adjust the setup for your site.

The flow of events during login is as follows:

1. The name of a user who has been authenticated by the operating system is presented to Empower. This can be either through an HTTP header or a query parameter, as detailed in this document.

2. If a user name has been presented to Empower (it is possible that the HTTP header doesn't contain a username), Empower checks to see if the username is in Empower's database. If it is, and OS Authentication has been enabled for that user, Empower logs in the user without requiring the user to enter credentials on Empower's login page.

3. If no username is presented, the name doesn't match a name in the database, or "OS Authentication" is turned off for the user, the user is routed to Empower's login page and the usual rules apply for logging in with a username and password.

If a user logs out of Empower, they go to the usual login screen. They might do this to: 1) select a new data source; or 2) to log in as another user. In either case, a user name and password might be required, so the user will see the login page with username and password input boxes. When changing data sources, the user will be able to log in without supplying a user name or password (assuming they have the appropriate permissions in the newly selected data source).

Regardless of the authentication setup, Empower still has a privileged "Admin" user. "Admin" always has to supply a password, whether authenticated by the operating system or not. (The presence or absence of a password for "Admin" is the basis of Empower's application-security implementation.)

---

## Chapter 2

### Empower Application-Level Security

Application-level security controls who can login to the Empower application and what privileges the user has while running the application.

#### 2.1 Empower Application-Level Security Off

If application-level security is turned off, then anyone can log into Empower; the application will ignore the username and password entered. The user will be logged in as the "Admin" user. Most sites will want keep application-level security on, although stand-alone installations with one user may find it convenient to turn it off. To turn off application-level security, the "Admin" user simply clears their password (setting it to a zero-length string) using the menu option "File > Set Password" in Empower.

#### 2.2 Empower Application-Level Security On

To turn on application-level security, login to Empower as "Admin" (assuming that application-level security is off, the user will not need a password), select "File > Set Password", and enter a password. This password will be used for the "Admin" user. Other users can set their password using the same menu option, but only "Admin" can turn off application-level security.

---

## Chapter 3

### Preparing Users for Single Sign-On

Add each user who will run Empower to Empower's database using the User Maintenance dialog.

1. For users who will be logging in via SSO, the user names in Empower's database must match the names that will be supplied with the HTTP header or through the query parameter. For example, if usernames on your system include a domain prefix, you would enter something like BIG_COMPANY\Fred for the username, not just Fred. (You can also have users who will not be logging in via SSO; they will need to login with a username and password.)

2. Operating system authentication must be enabled for each of these SSO users (by checking "OS Authentication" on the dialog).

3. Empower's application security must also be enabled.

For more information, see the section on the "User Maintenance dialog" and the chapter on "Security in Empower" in the Empower User's Manual.

---

## Chapter 4

### How Empower Handles SSO

To use SSO, Empower requires that you send a query string with these parameters:

- **rlogn**: the name of your virtual directory for SSO
- **sd**: the "datasource name" you want to use with SSO
- **sa**: the user information for SSO

For example, a url with the required query parameters might look like:

```
https://localhost/empower/login.html?rlogn=empower-osn&sd=Empower&sa=0l5meqxg.z3c
```

The 'sa' parameter can contain either a filename or a base64-encoded string, see below for details.

The user information should be formatted as a JSON string and contain at least the UserName of the user. For example:

```json
{"UserName": "Tideman", "UserUpdate": 3 }
```

Note that "UserUpdate" tells Empower what to do with this user, and can have the following values:

- -1 => delete user
- 0 => do not add or update
- 1 => add but do not update
- 2 => update but do not add
- 3 => add and update

The default value for UserUpdate is 3.

The JSON string with user information should either be:

1. written to a temporary file, with the name of that file passed in the 'sa' parameter
2. or passed as a base64-encoded string in the 'sa' parameter. If you choose to use the base64-encoding format, you should not set SSO_DIR in your default document or your ntsh.conf file.

In the following chapters we provide some examples that show a few ways to meet these requirements, but you should do whatever is best in your environment.

---

## Chapter 5

### User Attributes

Additional attributes for users can be passed and set via SSO. In general, these attributes correspond to items that can be set in the "User Maintenance" dialog in the Empower UI.

These attributes should be specified in the JSON string containing user information that is passed to Empower, see Chapter 4 for more details on passing this information to Empower. Note that the UserName parameter is required.

#### 5.1 Valid attributes

The following are the recognized user attributes that can be passed to Empower.

- **UserUpdate**: This attribute tells Empower what to do with this user, and can have the following values:
  - -1 => delete user
  - 0 => do not add or update
  - 1 => add but do not update
  - 2 => update but do not add
  - 3 => add and update

  The default value for UserUpdate is 3. If the User does not already exist in Empower, they can be added by setting UserUpdate to 1 or 3.

- **UserName**: The UserName for this user.

- **UserGroup**: The user group(s) that this user is in. Note that the group must exist in Empower before the user can be added to the group. Unlike users, user groups cannot be created through active directory. Multiple groups can be passed in a comma separated list.

- **NarrRoleName**: The name of the narrative role of the user. (e.g. "Submitter")

- **AiRoleName**: The name of the action item role of the user. (e.g. "Reviewer")

- **AdminUser**: Enable or disable "Log in as Admin" for a user. Values for this attribute should be either 'T' or 'F' (True or False).

- **PubLevel**: The PubLevel of the user. The value for this attribute should be an integer.

- **Email**: The email address of the user.

- **DisplayName**: The display name for the user.

- **UserCode**: The user code for the user. For more information, see the technical document titled "The Empower Configuration File"

- **Prefilter**: A security prefilter for the user. This should be the code for the filter itself, not the name of a filter in Empower.

#### 5.2 Parameter Examples

User attributes can be set via SSO by passing the user attributes via JSON. For example, we could edit our sample default.aspx file as follows:

```vb
Dim sa = Replace(System.Web.HttpContext.Current.User.Identity.Name, "\", "\\")
sa = "{""UserName"": """ + sa + """, ""UserUpdate"": 3, ""NarrRoleName"": ""Submitter"", ""AiRoleName"": ""Reviewer"", ""UserGroup"": ""Instructors, Students"" }"
```

This would update the user's narrative role to "Submitter", action item role to "Reviewer", and put the user in the "Instructors" and "Students" groups. Note that the groups must exist in Empower prior to assigning a user to them via SSO.

We could assign a prefilter for our user by doing the following:

```vb
Dim sa = Replace(System.Web.HttpContext.Current.User.Identity.Name, "\", "\\")
sa = "{""UserName"": """ + sa + """, ""UserUpdate"": 3, ""Prefilter"": ""altelem.ElemLevel = 1"" }"
```

This would set a prefilter for the user restricting the data they can see to "level 1" elements only.

Of course, hard coding these parameters in default.aspx would result in setting those values for any users that go through this default document. In a real setup, the parameter values for the current user would likely be pulled into the default document from another source. The names and location of these values may vary, so we leave the method of pulling them into your default document to you. An example of pulling some user parameters from Active Directory into the default document index.php is provided in Chapter 8.

---

## Chapter 6

### Example: Single Sign-On with IIS

This example passes the authenticated user name to Empower using a query parameter, fulfilling the requirements outlined in Chapter 4. This setup works with IIS and does not require setting an HTTP header for the username.

Here are the steps for setting up SSO with IIS:

#### 6.1 Install Microsoft modules

If you have not already done so, you will need to add these Microsoft modules to your IIS installation:

- URL Rewrite (download from www.iis.net/downloads/microsoft/url-rewrite)
- Application Request Routing (www.iis.net/downloads/microsoft/application-request-routing)

#### 6.2 Enable proxy for ARR

- Open IIS Manager.
- Click on the top-level node in the "Connections" pane on the left side.
- In the IIS section, open Application Request Routing Cache.
- Under "Actions" (on the right side), click on "Server Proxy Settings..."
- Check the box labeled "Enable proxy"

Figure 6.1: Checking "Enable proxy"

- Under "Buffer Setting" set "Response buffer threshold" to 0

Figure 6.2: Buffer Settings

- Click "Apply", then "Back to AAR Cache".

#### 6.3 Enable handler mappings

These are usually already set up correctly, but we have seen instances when they needed to be enabled. They can be added via Turn Windows features on or off > Internet Information Services > World Wide Web Services > Application Development Features. Here is an example of items that you might check:

Figure 6.3: Turn Windows Features on or off

Depending on your setup, you may see different options. For example, you may have a different version of ".NET" available.

Select "Default Web Site", then click on Handler Mappings. The figure below shows the *.aspx handlers enabled on one of our machines.

Figure 6.4: Handler Mappings for *.aspx files

#### 6.4 Create a physical directory containing default.aspx

Create a directory that you will point your virtual directory to, for example C:\encore-analytics\empower-osn. Open a command window on your application server and navigate to your Empower directory (typically c:\encore-analytics\empower). Copy default.aspx into the directory you created using the following command:

```
copy .\setup\sso\login-osn\<filename> ..\empower-osn
```

Replace "<filename>" with the name of the default document you want to use, and the command will copy it to the empower-osn directory.

Options for the default document are:

- **default.aspx**

  Edit this file as necessary to fit your setup. In particular, the following items should be set:
  - sd should be set to your datasource name
  - rlogn should be set to the name of your virtual directory. If using our default setup, this should be "empower-osn"

- **index.php**

  To use index.php as your default document with this setup, install PHP in IIS. (See 7.1 for installation details) Edit the following items as necessary to fit your setup:
  - $sd should be set to your datasource name
  - $rlogn should be set to the name of your virtual directory. If using our default setup, this should be "empower-osn"
  - $obj["UserGroup"] can be set to the name of an Empower User Group so that users added through SSO will automatically be assigned to the group. Note that the group must exist in Empower before users can be assigned to it.

##### 6.4.1 sso_dir

With either default document, sso_dir should be a path to a directory on the Empower server where we will create a temporary file containing the sso user's login information. The name of the temporary file is passed to Empower, the login is checked and rejected or validated, then the file is deleted. Note that the directory must exist, the service running Empower must have read permissions to the directory, and the service running PHP must have write permissions to the directory.

The default directory path is C:\encore-analytics\temp. This entry must match the entry for SSO_DIR in ntsh.conf. If you do not have an ntsh.conf file in your empower directory, create one and add a line like SSO_DIR=C:/encore-analytics/temp so that the SSO_DIR entry matches the sso_dir that you set in your default document. For more details on the ntsh.conf file, see the technical document "Encryption in Empower."

Note that the virtual directory name "empower-osn" is a suggested value, the directory can be named whatever you like, so long as the entry for rlogn matches it.

#### 6.5 Create a rewrite rule

Start IIS Manager. Click on Default Web Site. In the IIS section, double click on URL Rewrite. Create a new inbound rule named "Empower Reverse Proxy."

Set the rule properties as follows:

- Requested URL: "Matches the Pattern"
- Using: "Regular Expressions"
- Pattern: `empower/(.*)`
- IgnoreCase: Checked
- Action type to "Rewrite"
- Action Properties: `http://127.0.0.1:5000/{R:1}`
- Append query string: Checked
- Stop processing of subsequent rules: Checked

When you have finished setting the rule's properties, click "Apply" under Actions.

Note: If you are running Empower on a non-default port, you will need to use that port in the "Action Properties" property of the "Empower Reverse Proxy."

#### 6.6 Configure the IIS virtual directory

##### 6.6.1 Create the virtual directory

Click on Default Web Site in IIS. Right click on Default Web Site and select "Add Virtual Directory."

Set the properties as follows:

- Alias: `empower-osn` (This is a suggested value; the alias can be anything you choose as long as it matches the header value for rlogn in step 6.4 above.)
- Physical path: The directory you created in 6.4, for example C:\encore-analytics\empower-osn.

##### 6.6.2 Enable Windows Authentication

Still under Default Web Site, select the site you just created, empower-osn. In the IIS section, double-click the Authentication icon. Enable Windows Authentication and disable all other forms of authentication.

##### 6.6.3 Set Default Document

With the site empower-osn selected, double click on Default Document. Make sure that default.aspx is in the list, and delete all the other files listed, or reorder the list so that default.aspx is the first file listed. If default.aspx is not listed, it can be added manually by using "Add" under "Actions."

#### 6.7 Access Empower

Click on the top level in the Connections pane, and restart IIS (under Actions). You should now be able to start Empower by typing this in to your browser's address bar:

```
http://[host]/empower-osn/
```

where [host] is the name or IP address of the Empower server. The trailing slash is required.

#### 6.8 Addressing Caching Issues in IIS

For large volumes of users using SSO through IIS simultaneously, there is a known IIS caching issue where a user may receive a cached session instead of getting a new one. This may result in a user being logged into an application under another user's credentials.

If you encounter this behavior, you can prevent it by doing the following:

1. Open IIS and select your empower-osn virtual directory.
2. Under the IIS section select "Output Caching"
3. Under "Actions" select "Add"
4. Create an output caching rule so that caching is turned off for .aspx files (or whatever the extension of your default document is). For example:

Figure 6.5: Output caching rule

---

## Chapter 7

### Example: SimpleSAML with IIS

Like the previous example, this sample setup passes the authenticated user name to Empower using a query parameter, fulfilling the requirements outlined in Chapter 4. However, this time we will use a SAML IdP instead of Windows Authentication. If you are planning to use a SAML IdP, we strongly recommend that you work with someone at your site who is well-versed in SAML setup and configuration.

In general, this document will assume that you are installing simpleSAML php 2.0, although we will note some key differences between versions 1.19 and 2.0.

#### 7.1 Install PHP and ARR

Open 'Turn Windows Features on or off'. Make sure the box for IIS (Internet Information Services) is checked.

Install the following:

- .NET 3.5 or newer
- PHP 7.4 or newer. Older versions of SimpleSAMLphp may allow older PHP versions, but newer versions will require at least PHP 7.4. We have tested the SAML SSO setup for SimpleSAMLphp 2.0 with PHP 8.0 and 8.2. At the time of this documentation PHP 8.3 has some incompatibilties with the SimpleSAMLphp 2.0 code.
- ARR 3.0 (Application Request Routing)

If necessary, add any missing handler mappings in IIS and enable openssl for PHP. Instructions for installing these items and configuring them are available online, and are beyond the scope of this document.

Adjust the ARR settings as described in 6.2.

#### 7.2 Create the Empower Reverse Proxy

In IIS, create the rewrite rule "Empower Reverse Proxy" as described in section 6.5 of this document.

#### 7.3 Bind a certificate

To use SSL, you'll need to bind a certificate to your site. Most likely, you'll have your own certificate that you will need to use for your site; contact your server people for more information.

If you do not have your own certificate, one option could be to create a self-signed certificate.

- (Optional) If you plan to use a self-signed certificate, there are some options for creating your own:

1. (More Recommended) Run the PowerShell script below (between the dashes) in an Administrator window:

```powershell
$cert = New-SelfSignedCertificate -DnsName localhost, localhost, $env:computername -CertStoreLocation "cert:\LocalMachine\My"
$rootStore = New-Object System.Security.Cryptography.X509Certificates.X509Store -ArgumentList Root, LocalMachine
$rootStore.Open("MaxAllowed")
$rootStore.Add($cert)
$rootStore.Close()
```

Note that lines have been wrapped for readability.

2. (Not recommended) In IIS Manager, go to Server Certificates, Create Self-Signed Certificate. (Chrome 56 and later will not accept the certificate as valid. If this is an issue, use option 1 or do not use a self-signed certificate.)

- Back in IIS, navigate to 'Default Web Site' and select 'Bindings'. Add https and bind to port 443 (host name can be left blank), and choose the certificate you created for "SSL certificate" or the certificate of your choice. Set the Host Name if necessary for your certificate.

With the Empower service running, you should now be able to navigate to https://localhost/empower/. Internet Explorer, Chrome, and Edge will trust the self-signed certificate while Firefox will require you to add an exception.

Note that this URL allows you to verify that your certificate has been set up properly, but will not log you into Empower automatically.

#### 7.4 Install SimpleSAML

1. Download and install SimpleSAMLphp for your OS (See https://simplesamlphp.org/docs/stable/simplesamlphp-install#download-and-install-simplesamlphp)

2. Windows Installations:

   (a) For the purposes of this document, if you are using Windows we will assume that you unzipped and installed SimpleSAMLphp in the encore-analytics directory so that you have a encore-analytics/simplesamlphp directory. You may need to rename the directory so that it is called simplesamlphp.

   (b) Locate your simplesaml-windows.zip file (available from Encore Analytics technical support). This file will contain some sample configuration files.

   (c) Extract simplesaml-windows.zip to a conveniently location.

   (d) In IIS, create a virtual directory with the alias 'simplesaml', pointed to the simplesamlphp\public directory. For older versions of simpleSAML use simplesamlphp\www instead. (The simplesamlphp\www folder will not exist in newer versions, so determining which path to use should be simple)

   (e) Verify that index.php is listed under "Default Document" for your virtual directory in IIS. If index.php is not listed, add it manually by selecting "Add" under "Actions."

3. Docker Installations:

   (a) extract the simplesaml-docker.zip from Encore Analytics support so that the contents are placed in your \shared\sso\ directory. (Note: your "shared" directory may have a different name, but it should be the location with your other Empower configuration files) Once complete, you should have a \shared\sso\certs, \shared\sso\config\, \shared\sso\dist\, and \shared\sso\empower-simplesaml directory.

   (b) place any relevant certificates in the certs directory.

   (c) edit the certificate and certificate_key in \shared\sso\config\empower.conf as appropriate for your certificates

   (d) edit the alias for simplesaml in \shared\sso\config\empower.conf; use /sso/simplesamlphp/www/ for simpleSAML 1.19, use /sso/simplesamlphp/public/ for simpleSAML 2.0.

#### 7.5 Configure SimpleSAML

Navigate to C:\encore-analytics\simplesamlphp and verify the following settings, making changes if necessary using the text editor of your choice. Older versions of this setup will require you to make these changes. Other versions may already have these edits made for you. Replace simplesamlphp\config\authsources.php with the versions included in the simplesaml zip file that you received from Encore Analytics support. Place the saml20-idp-remote.php file in the simplesamlphp\metadata directory.

- In config\config.php, adjust the following fields to fit your setup. Descriptions for each field are included in the config.php file.
  - auth.adminpassword
  - secretsalt
  - technicalcontact_name
  - technicalcontact_email
  - timezone
  - loggingdir
  - tempdir
  - certdir

The last three items in the list should be valid paths on your server that are accessible to the simpleSAMLphp installation. If the paths that you set do not exist, you will need to create them.

- In config\authsources.php, the following lines (between the dashes) are used to add a test authentication source for SAML, allowing you to test your configuration with some sample users. If these lines are not present in your version of authsources.php, you can add them after the 'admin' array.

```php
// An authentication source that validates locally against this array
'default_sp' => array(
  'exampleauth:UserPass',
  'Student:stu' => array(
    'DSN' => 'Empower',
    'UserName' => 'EVM-101.Student-014',
    'DisplayName' => 'Student-014',
    'UserGroup' => 'Students',
    'UserCode' => 'C',
    'Email' => 'student014@example.com',
  ),
  'Instructor:ins' => array(
    'DSN' => 'Empower',
    'UserName' => 'EVM-101.Instructor-001',
    'DisplayName' => 'Instructor-001',
    'UserGroup' => 'Instructors',
    'UserCode' => 'C',
    'Email' => 'instructor001@example.com',
  ),
)),
```

- In config\config.php verify that exampleauth and admin are both "true" in the module.enable section.

To test the simpleSAML setup, navigate to https://localhost/simplesaml/admin/ in a browser. Click 'Test", then 'default-sp'. (For older simpleSAML versions, click 'Authentication', then 'Test configured authentication sources') Enter either Student/stu or Instructor/ins. The attributes you defined for the user in authsources.php should be displayed. For pre simpleSAML 2.0 versions, use https://localhost/simplesaml/ instead.

Note: 'DSN', 'UserName', and 'UserGroup' are required attributes, and the Data Source Name (DSN) and UserGroup must already exist in Empower. The user can be created or updated from the remaining attributes.

#### 7.6 Configure Empower SAML Setup

1. Create the directory C:\encore-analytics\empower-simplesaml.

Note: Using "empower-" to indicate a login directory is purely a convention, the SAML setup can be adjusted to change this.

2. Copy index.php from the simplesaml zip file or C:\encore-analytics\empower\setup\sso\login-saml into the directory created in (1)

3. Verify the path in the 'require_once' call (line 2 in index.php) This path should exist on your server.

4. Verify $rlogn in index.php. Note that "rlogn" must resolve to a valid virtual directory, which in turn must point to the physical directory where index.php is located.

5. $sso_dir should be a path to a directory on the Empower server where we will create a temporary file containing the sso user's login information. The name of the temporary file is passed to Empower, the login is checked and rejected or validated, then the file is deleted. Note that the directory must exist, the service running Empower must have read permissions to the directory, and the service running PHP must have write permissions to the directory.

The default directory path is C:\encore-analytics\temp.

6. Set $idp to the IdP name that you set in authsources.php. To use our test users, "Student" and "Instructor", you would set this to "default-sp".

7. If it does not already exist, create the file ntsh.conf in the empower directory. Add a line to the file with the value for SSO_DIR that you set in index.php. For example:

```
SSO_DIR=C:/encore-analytics/temp
```

8. In IIS, create a virtual directory named 'empower-simplesaml' pointing to the directory in (1). This virtual directory should match the entry for "rlogn" in index.php as mentioned in (4).

9. Verify that index.php is listed under "Default Document" for your virtual directory in IIS. If index.php is not listed, add it manually by selecting "Add" under "Actions."

#### 7.7 Testing SAML with Empower

You can follow these steps to test your SAML setup with Empower and ensure that different users and groups can login to Empower using SSO.

1. Log into Empower as 'Admin' and create two groups, one called 'Students', and the other called 'Instructors'. Assign at least one contract to each, with at least read permission.

2. Navigate to https://localhost/empower-simplesaml/. You will be directed to the SimpleSAML login page.

3. Log in as 'Student/stu'. You should be signed into Empower.

4. In the same browser session, navigate to https://localhost/simplesaml/admin/ and click 'Test', 'default-sp', and your attributes should display without having to log in again. Click 'Logout' (at the bottom of the page).

5. Go back to 'Authentication'. Now log in as 'Instructor/ins'. You should see the information for 'Instructor'.

6. In the same browser session, navigate to https://localhost/empower-simplesaml/ and you should be logged in as 'Instructor' without being prompted again.

#### 7.8 Changing IdPs

Should you wish to use a different IdP with Empower, follow these steps to adjust your SAML setup.

1. Obtain the metadata from your IdP

2. Open https://localhost/simplesaml/admin/ and navigate to "Federation", then select the "XML to SimpleSAMLphp metadata converter". You will need to log in as administrator using the password you set in config.php.

3. Upload or paste the metadata from (1) and click "Parse"

4. Copy the converted metadata and paste it into saml20-idp-remote.php, which is located by default in simplesamlphp\metadata. Take note of the url in the first line of the pasted content.

5. Edit authsources.php to include the new IdP. For 'idp', enter the url from (4). A minimal example looks like:

```php
'saml' => array(
  'saml:SP',
  'idp' => 'https://example.com/saml/metadata',
),
```

6. Edit empower-simplesaml\index.php so that $idp matches the entry in authsources.php. For our example, we would set $idp = 'default-sp'.

Note: If your version of index.php does not define $idp, then verify that line 2 in index.php matches your entry for your IdP in authsources.php. For example:

```php
$as = new \SimpleSAML\Auth\Simple('saml');
```

7. Verify that rlogn in index.php resolves to a valid virtual directory

#### 7.9 Differences Between simpleSAML 1.19 and 2.0

There are a few differences between versions 1.19 and 2.0 of simpleSAMLphp that should be noted:

- simpleSAMLphp 2.0 requires PHP 7.4 or newer
- in your default document (index.php), the declaration of $as will look like `new \SimpleSAML\Auth\Simple($idp)` for version 2.0
- with version 2.0, your virtual directory for simplesaml should be pointed to simplesamlphp\public while version 1.19 uses simplesamlphp\www
- for testing SAML configuration and IDPs, use the URL https://localhost/simplesaml/ for version 1.19 and https://localhost/simplesaml/admin/ for version 2.0
- in version 1.19, the exampleauth file is used to enable some test IDPs. In 2.0 this configuration is done in config.php. To enable exampleauth in 1.19: in \modules\exampleauth there should be a file called enable. If the file is not present, create a file named enable with a line of text that says:

```
'This file enables the exampleauth module. Remove it to disable.'
```

---

## Chapter 8

### Example: Active Directory with Empower User Management

This sample setup passes the authenticated user name and other user information to Empower using a query parameter, fulfilling the requirements outlined in Chapter 4. The steps outlined in this chapter might be used by a site using Active Directory for user management instead of managing users in Empower. For example, the setup described in this chapter allows the creation of new Empower users through Active Directory. With this setup, there is no need to add the user in Empower before they can use SSO, the user is simply created when they access Empower for the first time.

Those using Active Directory for authentication who do not need to manage Empower users in Active Directory could simply follow the instructions in section 6 to set up SSO; there are no special steps needed to indicate to Empower that Active Directory is being used.

#### 8.1 Install IIS with PHP and ARR

Install IIS, .NET 3.5, PHP, and ARR as described in section 7.1.

#### 8.2 Create the Empower Reverse Proxy

In IIS, create the rewrite rule "Empower Reverse Proxy" as described in section 6.5.

#### 8.3 Create the Physical Directory

Copy index.php from \setup\sso\login-ad in the empower directory (C:\encore-analytics\empower in the default installation) to the location where you will point your virtual directory in the next step, for example C:\encore-analytics\empower-ad.

#### 8.4 Configure the IIS Virtual Directory

##### 8.4.1 Create the virtual directory

Select Default Web Site in IIS. Right click on Default Web Site and select "Add Virtual Directory." Set the properties as follows:

- Alias: `empower-ad` (This is a suggested value; the alias can be anything you choose as long as it matches the value for rlogn in index.php from step 8.3 above.)
- Physical path: The physical path where you put index.php in step 8.3.

##### 8.4.2 Set authentication form

Still under Default Web Site, select the site you just created, empower-ad. In the IIS section, double-click the Authentication icon. Disable all forms of authentication you do not want and enable "Windows Authentication."

##### 8.4.3 Set Default Document

With the site empower-ad selected, double click on Default Document. Make sure that index.php is in the list and delete all the other files listed, or reorder the list so that index.php is the first file listed. If index.php is not listed, it can be added manually by using "Add" under "Actions."

#### 8.5 Creating custom attributes

For Empower to recognize a UserName or add a new user through Active Directory, custom attributes in Active Directory must be mapped to the corresponding attributes in Empower.

Active Directory custom attributes can be created by doing the following:

1. Open "Active Directory Schema" by doing the following:
   - Run "mmc.exe"
   - If Active Directory Schema is not listed on the left-hand side, select "File > Add/Remove Snap-ins" and add "Active Directory Schema"
   - Expand "Active Directory Schema" until you see "Attributes"

2. Right-click "Attributes"

3. Select "Create Attribute"

4. Fill out the information for the custom attribute:
   - Common Name: use the attribute name
   - LDAP Display Name: keep consistent with the 'Common Name'
   - Unique X500 Object ID: enter a valid OID
   - Description: enter a description of the attribute (optional)
   - Syntax: choose 'Unicode String'

5. click "OK"

#### 8.6 Adding attributes to a class

Once you have created your custom attributes, they can be added to an Active Directory class. For example, if you would like the custom attributes to be available for use with all Users, you would add the custom attributes to the User class.

1. Open the Active Directory Schema administrative tool

2. Select "Classes" in the left pane

3. Select the class you wish to update, then select "Properties"

4. Select the "Attributes" tab, then click "Add"

5. Select the desired attribute, then click "OK"

6. Repeat for all desired attributes

For a list of valid attributes, see Chapter 5. Note that the custom attribute in Active Directory may have a different name than the Empower attribute it is passed to, but must be mapped to the correct corresponding attribute in index.php in order to be recognized by Empower.

#### 8.7 Set User Values

The values of each attribute created in section 8.5 must be set for each Empower user. Attributes can be set through "Active Directory Users and Computers". To set attributes, do the following:

1. Select "Users"

2. Right click the user you want to set values for, then select "Properties"

3. Select the "Attribute Editor" tab

4. Select the custom attribute you want to set, then click Edit

5. Set the Value field as appropriate for the user

Note: If a user is created automatically without specifying a value for "UserGroup", the user will be created in Empower, but will not have any permissions set. The permissions for the user can be set later by Admin. If "UserGroup" is set for the user when they are created, the user will automatically inherit the permissions of the group.

#### 8.8 Edit index.php

Edit index.php as necessary so that the settings for $ldapserver, $ldapuser, $ldappass, and $ldaptree match your setup, and your custom Active Directory attributes are mapped to their corresponding Empower attributes correctly. The following line from index.php lists the Active Directory attribute names. (Recall that these names can be whatever you like.)

```php
$only = array("eadsn", "eausername", "eausergroup", "eausercode", "eadisplayname");
```

The next line shows the mapping of the attributes to the names Empower expects.

```php
$kmap = array('eausername' => 'UserName', 'eausergroup' => 'UserGroup', 'eausercode' => 'UserCode', 'eadisplayname' => 'DisplayName');
```

Also, set $rlogn to match the name of your virtual directory and $sso_dir to match your SSO_DIR as set in ntsh.conf.

---

## Chapter 9

### Example: SSL in IIS Without SSO

If you want to install an SSL cert in IIS to use with Empower, but do not want to set up Single Sign On, you could complete these steps:

1. Complete sections 6.1, 6.2, and 6.5 in IIS.
2. Bind a certificate to your "Default Web Site" in IIS, see section 7.3 for details.

---

## Chapter 10

### Setting Default Contracts for Users

Passing the ds parameter in your query string allows you to set a default contract for users so that when they login to Empower the default contract is automatically opened in the sort window. This parameter can be set manually in your default document, which will apply the default contract to all of your SSO users, or passed as a parameter for each user.

The ds parameter should be a JSON string with this format:

```json
{"cstr":"MOH-2","dstr":"2017-01-01", "sstr":"WBS","ustr":"Dollars","dashstr":"MyDash"}
```

Where the entries are set as follows:

- **cstr** - the name of the contract that should be opened by default when logging into Empower
- **dstr** - the end date of the period that should be opened by default (optional). Defaults to the most recent period of the contract.
- **sstr** - the name of the structure that should be opened by default (optional). Defaults to WBS.
- **ustr** - the name of the unit that should be opened by default (optional). Defaults to Dollars.
- **dashstr** - the name of the dashboard that should be opened by default (optional). The user's personal dashboard, if it exists, will be used first. If the user does not have a dashboard with the specified name then the global dashboards will be searched. If no match is found then no dashboard will be opened.

Note that only the "cstr" entry is required, the others may be omitted if desired.

---

## Chapter 11

### Single Sign-On with HTTP Headers

When using HTTP headers for SSO, Empower looks to see if the name of an authenticated user has been passed to it through the REMOTE_USER header.

1. During the login phase, Empower checks for the presence of a REMOTE_USER header. If the header is present and it has a user name, Empower moves to step 2.

2. If a username has been presented to Empower, Empower checks the database for a match between the user specified in the header and a user name in the database. If Empower finds a match and OS Authentication is set for that user, Empower assumes that the user has been authenticated and grants access to that user, bypassing Empower's login page, and respecting Empower's rules for granting access to contracts. At this point, logon is complete.

3. If no username is presented, the name doesn't match a name in the database, or "OS Authentication" is turned off for the user, the user is routed to Empower's login page and the usual rules apply for logging in with a username and password.

#### 11.1 Set Up Single Sign-On Using HTTP Headers

Different sites implement single sign-on in different ways. Some sites control access to their applications through a single web page that requires users to present their credentials, while others use the operating system's authentication mechanisms (e.g., Active Directory). To interface your single sign-on scheme with Empower, you will need to ensure that a REMOTE_USER header with the authenticated user's name is sent to Empower. This is the part that is site-dependent.

One way to do this would be to reverse-proxy Empower. You would configure your reverse proxy to obtain an authenticated user name and set the REMOTE_USER header appropriately. Sample configuration files for Apache and Nginx may be found in empower/setup. At present, IIS does not have the capability to populate the REMOTE_USER header. If you require an all-Microsoft solution, see chapter 6, "Single Sign-On with IIS".
