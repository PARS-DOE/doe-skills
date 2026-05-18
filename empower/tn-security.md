# TN Security

*Source: TN-Security.pdf*

---

## Technical Note: Setting Up Security Features in Empower

© 2013 Encore Analytics, LLC
July 9, 2024

### Contents

1. Additional HTTP Security Headers
2. Enable Session Timeout
3. Specify User Password Complexity Requirements
4. Setting Check Level
5. Remove Sample CGI files
6. Changing the Encryption Settings in Empower
   - 6.1 getpwds
   - 6.2 setpwds
   - 6.3 Example

---

## Chapter 1: Additional HTTP Security Headers

Additional HTTP headers can be enabled with these steps:

1. Copy the file headers.conf from the empower\setup directory into the empower directory (C:\encore-analytics\empower by default) on your Empower application server.
2. Edit headers.conf as desired to add additional HTTP headers.
3. Restart the Empower service

---

## Chapter 2: Enable Session Timeout

The EXPIRE entry in the empower.conf file indicates the number of seconds a user can be idle before they are logged out automatically. If not present or set to 0, auto-logout is turned off. If set to a number, Empower will prompt users to either continue their session or log out after that number of seconds. If the user does not click either option within a certain amount of time, they will be logged off automatically. For example, "EXPIRE=1800" would prompt users to continue or log out after they have been idle for 30 minutes.

To enable session timeout, add an EXPIRE entry to your empower.conf file on a new line. For example, the entry could look like:

```
EXPIRE=1800
```

which would automatically logout idle users after 30 minutes.

After adding EXPIRE to empower.conf, restart the Empower service.

---

## Chapter 3: Specify User Password Complexity Requirements

The PWD_TMPL entry in empower.conf defines rules for user passwords including password length and complexity. The format for the entry is: `PWD_TMPL=<length>;<required types>`. For example, to set a minimum length of 8 characters, use `PWD_TMPL=8`. The entry `PWD_TMPL=8;aA` would require that passwords have a minimum length of 8 characters and have at least one lower-case and one upper case letter. `PWD_TMPL=8;Aa0+` would require a minimum length of 8 characters, at least one lower-case letter, at least one upper case letter, at least one number, and at least one symbol. If the PWD_TMPL entry is omitted, there are no restrictions on user passwords and empty passwords will be allowed.

To set password complexity requirements for your user passwords, add a PWD_TMPL entry to your empower.conf file. For example:

```
PWD_TMPL=8;Aa0+
```

Once the complexity requirement has been set, when a user uses "File > Set Password" and enters a new password they will receive the message "Password does not meet minimum complexity requirements" if their new password does not meet the requirements.

---

## Chapter 4: Setting Check Level

The CHECK_LEVEL setting in empower.conf enables additional security checks for users attempting to access Contract, Period, or Element level data. The value set determines the level at which the check will be run.

Valid values for CHECK_LEVEL are:

- `0` – no additional verification checks
- `1` – verify that the user has read access to the requested contract
- `2` – verify that the user's PubLevel allows access to the requested period
- `3` – verify that the user's security prefilter allows access to the requested element

For example, adding `CHECK_LEVEL=2` to your empower.conf file would prevent users from bypassing the application security to access periods of data that they do not have permissions for. Note that these users would not be able to view this data through normal Empower use regardless of the CHECK_LEVEL setting.

---

## Chapter 5: Remove Sample CGI files

We include a few sample CGI files that are used with some custom charts and reports. For enhanced security, these sample files can be removed. To remove the files:

1. Delete any .cgi files in the empower\cgi directory.
2. Delete the corresponding charts and reports in Empower:
   - In Empower, use "Charts > Custom Charts > Delete / Reorder" to delete the "WhoCharged" chart.
   - In Empower, use "Reports > Custom Reports > Delete / Reorder" to delete the "WhoCharged," "WADReconciliation," and "CustomExtra" reports.

Note that if you remove inc_update.cgi, you will not be able to use incremental updates via a HTML web page. (See the document "Incremental Updates in Empower" for more details.)

---

## Chapter 6: Changing the Encryption Settings in Empower

### 6.1 getpwds

The getpwds utility will read current passwords from all data sources listed in datasrc.ini, calculate new passwords based on the supplied key, and write all this information out in JSON format to the console or to a specified file. This information can then be used by the companion setpwds utility to update passwords, or to restore the previous passwords if something goes wrong.

The encryption key can be changed without installing any additional perl modules, but changing the algorithm will require the installation of the Crypt::CBC module. The module can be downloaded from https://metacpan.org/pod/Crypt::CBC.

Note: You should make sure that all databases listed in datasrc.ini are online before using this utility.

Several options are available for use with this utility:

- `-f` specifies a file to write the JSON data to.
- `-key` specifies an encryption/decryption key.
- `-cipher` specifies an algorithm to use for encryption. The algorithm must be installed on the Empower server. These algorithms are installed by default with the Crypt::CBC Perl module on Windows.
  - `Des`
  - `Aes`
  - `Blowfish`
  - `Idea`

Other command line arguments are available and different algorithms can be installed for use with the utility, see https://metacpan.org/pod/Crypt::CBC for details.

### 6.2 setpwds

The setpwds utility will set passwords from the supplied file (generated by its companion utility getpwds). Specify `-n` to set new passwords, and `-o` to restore old passwords. Running setpwds will automatically create the DSN_CRYPT entry in ntsh.conf.

Before running, please ensure all databases in datasrc.ini are online.

### 6.3 Example

Suppose that you wanted to change your encryption algorithm to "AES" and your key to "abcde". To do this, you could run this command in the empower directory:

```
perl getpwds.pl -key abcde -cipher Cipher::AES -f newkey.txt
```

This would generate a txt file containing the information needed to switch from using the current algorithm to the "AES" algorithm and the current key to "abcde". Additional options are available, see the Crypt::CBC documentation (available online) for more information. The file also contains the information necessary to revert your changes.

To apply the changes, you would run this command in the empower directory:

```
perl setpwds.pl newkey.txt -n
```

To revert your changes, you would run this command:

```
perl setpwds.pl newkey.txt -o
```

After running setpwds, an entry called DSN_CRYPT in your ntsh.conf file will be updated with the encryption changes. In our example, after setting the algorithm to "AES" and the key to "abcde" your ntsh.conf file will look something like:

```
SSO_DIR=C:/encore-analytics/temp
DSN_CRYPT={"cipher":"Cipher::AES","key":"abcde"}
```

The SSO_DIR entry in ntsh.conf is used in our Single Sign On setup, see the technical documents "Encryption in Empower" and "Authentication in Empower" for more details.
