# TN IncrementalUpdate

*Source: TN-IncrementalUpdate.pdf*

---

## Technical Note: Incremental Update

© 2013 Encore Analytics, LLC
September 13, 2018

### Introduction

Incremental update serves as an alternative to importing large files when only small changes need to be made in your data. With incremental updates, you can make small changes to your data without reimporting entire tables. As a result, updates can be made to performance data during the monthly close-out cycle much more quickly.

There are three tables that can be updated using incremental update: the Element table, Earned Value table, and FutureEtc table. Two methods of implementing incremental update are available; it can be used as an extension of Watchdir, or as an independent web page.

**Note:** Incremental update can only be used with Empower version 3.7 or later.

### Recalculation of incremental updates

Along with updating data, incremental update also recalculates data as necessary. As an added feature with this recalculation procedure, incremental recalculations can be queued. This means that if a recalculation is already being done on your data, using incremental update will simply add a recalculation to the queue which will be executed after the original recalculation has completed.

If the incremental update cannot recalculate immediately, the line "Queuing incremental recalc.." will appear in the log. When the queued recalc is executed, the line "Executing queued incremental recalcs..." will appear in the log and the recalculation will continue as usual.

The following is an excerpt of watchdir.log showing a successful incremental update with a queued recalc:

```
2017-10-25:15:25:41: Importing jeep.inc to Empower
Cleaning.. OK
Reading jeep.inc.. OK.
Validating.. OK.
Updating Jeep 240z WBS 1.3.1.11 601277425 SSHA 2012-02-26 Dollars.. OK
Queuing incremental recalc.. OK
Update succeeded
Executing queued incremental recalcs...
Recalculating Jeep 240z WBS 1.3.1.11 601277425 SSHA 2012-02-26
Summing raw data... 0.01 sec
Setting PMB values... 0.00 sec
Calculating current period values and deltas... 0.01 sec
Setting VAR flags... 0.02 sec
Summing future period data... 0.02 sec
Done... 0.06 sec
```

If another recalculation has already been started before an incremental update recalculation has been queued, the queued recalculation(s) will be executed after the current recalculation. The Recalculation window in Empower will also show the execution status of the queued recalculations.

**Figure 1:** Queued recalculation status in Empower

---

## Setting up Incremental Update with Watchdir

Setup Watchdir as described in the technical note "Empower's Watchdir facility for automated imports and recalculations."

In watchdir.conf add "inc" to the list of extensions to monitor. The list should now look something like this:

```
# extensions to monitor
exts=trn;xml;wsa;xls;xlsx;zip;inc
```

Now start Watchdir as usual. At this point you can import .inc files by putting them in the directory specified under watch_dirs in watchdir.conf. (See the tech note "Empower's Watchdir facility for automated imports and recalculations." for more information on watchdir.conf and running Watchdir.)

### File Format for Incremental Update in Watchdir

To use incremental update with Watchdir, the data must be formatted as a tab delimited text file with an .inc extension. This format can have up to three sections, one each for the Element, Earned Value, and FutureETC tables. You may include any or all of these sections, and each section can contain multiple records. Each section begins with the table name on its own line, immediately followed by a line specifying the columns of the table to be updated. The subsequent line(s) contain the data for each column.

Table 1 shows an excerpt of a .inc file. This file indicates that we want to set Bcws and Etc to 0 for WBS 3200 in the contract MOH-2 wherever the FutureDate is February 28 or March 31 and the unit is Dollars.

**Table 1: Watchdir data format**

```
FutureEtc
ContrName StruName WbsNum EndDate UnitName UnitScale FutureDate Bcws Etc
MOH-2 WBS 3200 2017-01-31 Dollars 3 2017-02-28 0.0 0.0
MOH-2 WBS 3200 2017-01-31 Dollars 3 2017-03-31 0.0 0.0
```

### Key Fields

Each of the three sections has key fields that must be filled out to correctly identify the piece of data that you want to update. The key fields for each table are:

- **Element:** ContrName, StruName, WbsNum
- **Earned Value:** ContrName, StruName, WbsNum, EndDate, UnitName
- **FutureEtc:** ContrName, StruName, WbsNum, EndDate, UnitName

If these sections are not filled out, the import will be cancelled and the following message will display in watchdir.log:

```
2017-12-05:13:29:21: Importing required.inc to Empower
Cleaning.. OK
Reading required.inc.. OK.
Validating..Required key field missing, aborting: EndDate (section 2).
```

**Note:** When updating the Element table, entries for ParentID, ElemLevel, or NumChild will be ignored.

### Example

This example uses sample data from MOH-2 and the sample files zero.inc and restore.inc. In this example we use "watch directory" to refer to a directory listed under watch_dirs in watchdir.conf. The actual name of the directory may differ depending on your Watchdir setup.

Move zero.inc into the watch directory. Now open MOH-2 in Empower. You will see that WBS 3200 has been zeroed out and Tideman's name has been replaced with x's, as shown below.

**Figure 2:** Zeroed out data in Empower

Now copy restore.inc into the watch directory. After the file is processed, refresh Empower. Now Tideman is back as the CAM for 3200 and our data is no longer zeroed out.

**Figure 3:** Reset data in Empower

The following is an excerpt of the watchdir.log file showing the log of an incremental update:

```
2017-10-25:13:40:37: Importing restore.inc to Empower
Cleaning.. OK
Reading restore.inc.. OK.
Validating.. OK.
Updating MOH-2 WBS 3200.. OK
Updating MOH-2 WBS 3200 2017-01-31 Dollars.. OK
Updating MOH-2 WBS 3200 2017-01-31 Dollars 2017-02-28.. OK
Updating MOH-2 WBS 3200 2017-01-31 Dollars 2017-03-31.. OK
Recalculating MOH-2 WBS 3200 2017-01-31
Summing raw data... 0.01 sec
Setting PMB values... 0.00 sec
Calculating current period values and deltas... 0.00 sec
Setting VAR flags... 0.01 sec
Summing future period data... 0.00 sec
Done... 0.03 sec
Update succeeded
```

The first line tells us which file is being imported, in this case restore.inc. Further down we see the updates that were made, then the recalculation that was done on the data. Notice that the entire import took less than one second to complete.

---

## Setting up Incremental Update using an HTML webpage

Unlike the Watchdir method, this implementation does not keep a log of the files imported into Empower. Instead, the import status appears directly in the webpage.

**Figure 4:** Webpage import status

To use this this method, the data to be imported must be in JSON format. The JSON is made available to the webpage, which connects to Empower to import the data. try.html (available from Encore Analytics support) serves as an example of a possible implementation of this method, using buttons to execute different incremental updates. We expect that the user would customize their own html document to achieve the look and functionality desired. Depending on the browser used, you may need to allow your page to run scripts.

The core of try.html is the Javascript function "doPost". This function sends a standard HTML POST request using the data provided as a parameter for the function. Again, try.html serves simply as an example of one implementation of this method. The service does not care how it is called, so long as it receives a standard HTML POST request.

Note that a data source is specified in try.html, indicating which Empower data source should be updated. In the sample file, the data source is "Postgres".

```javascript
var dsn = 'Postgres';
var url = 'http://localhost:5000/inc_update.cgi';
```

Should you choose to put the file inc_update.cgi somewhere other than the default empower/cgi/ directory, then you must add its location to your ATR_DIR in emower.conf.

inc_update.cgi is set up to allow "cross-origin resource sharing". The sites allowed to call this service can be controlled through customizing the headers in the file.

```perl
print header(
-access_control_allow_headers => 'X-Requested-With',
-access_control_allow_origin => '*',
-type => 'text/html',
);
```

Notice that the default for "access_control_allow_origin" is '*', which indicates that any domain may call the service. To restrict this, change '*' to specify the URI that you want to allow to call the service.

### JSON Format

The JSON format for this method requires that the data be an array of JSON objects. There should be one object per table you wish to update. Each object should have these pairs:

- **"columns":** an array of column names
- **"table":** the name of the table to be updated, eg. "Element"
- **"values":** an array containing arrays of values to be updated. Each inner array is a row to be updated, and should be the same length as the "columns" list.

The tables require the same key fields mentioned previously in this document.

The object below shows that we want to update the Element table so that "ProjOff", "ElemType", and "Evm" are all x'd out, while "Submitter", "Approver", and "Reviewer" are all set to "Admin".

```json
{
  "columns" : [
    "ContrName",
    "StruName",
    "WbsNum",
    "ProjOff",
    "ElemType",
    "Evm",
    "Submitter",
    "Approver",
    "Reviewer"
  ],
  "table" : "Element",
  "values" : [
    [
      "Moh-2",
      "Wbs",
      "3200",
      "xxxxxxx",
      "xx",
      "xxx",
      "Admin",
      "Admin",
      "Admin"
    ]
  ]
}
```

See the sample files zero-json.inc and restore-json.inc for examples of data in the JSON format.
