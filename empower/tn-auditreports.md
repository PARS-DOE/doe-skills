# TN AuditReports

*Source: TN-AuditReports.pdf*

---

## Technical Note: Empower's Audit Report

© 2013 Encore Analytics, LLC
March 18, 2024

## Contents

- [1 Introduction](#chapter-1-introduction)
- [2 Customizing the Agency Name](#chapter-2-customizing-the-agency-name)
- [3 The Audit Report Spreadsheet](#chapter-3-the-audit-report-spreadsheet)
  - [3.1 Audit Report Download Tabs](#31-audit-report-download-tabs)
  - [3.2 Report References](#32-report-references)
  - [3.3 Hidden Tests](#33-hidden-tests)
- [4 Setting Manual Values](#chapter-4-setting-manual-values)
- [5 Creating New Tests and Reports](#chapter-5-creating-new-tests-and-reports)
  - [5.1 Creating a New Test](#51-creating-a-new-test)
  - [5.2 Creating Per-Period Tests](#52-creating-per-period-tests)
  - [5.3 Creating New Reports](#53-creating-new-reports)
  - [5.4 Audit Tests in Sort Window Views](#54-audit-tests-in-sort-window-views)

---

## Chapter 1: Introduction

This document explains how to customize Empower's Audit Report. It shows how to:

- Customize the name of the auditing agency in Empower's menus and the report
- Set manual values for the test metrics
- Understand how Empower calculates the test metrics, and how to change these calculations
- Create entirely new tests
- Create different revisions of tests that will be applied to different periods
- Create an entirely new audit report and apply audit reports on a contract-by-contract basis

Encore Analytics is committed to providing and maintaining standard test sheets compatible with major government procuring agencies; however, Empower provides complete flexibility both to customize the standard test sheets and to develop unique test sheets as required. This tech note explains how to accomplish those tasks.

This technote assumes you are familiar with the use of Empower's Download Data and Upload Data commands. Customizing the calculations for the test metrics requires that you be comfortable with writing and modifying SQL statements.

All the examples in the following chapters use the standard MOH-2 contract that ships with Empower.

---

## Chapter 2: Customizing the Agency Name

By default, Empower uses "Audit Metrics" as the name for the Attributes and Test report, and this is the name that appears in the Reports menu. You may wish to change this name to reflect the auditing agency you work with, e.g., DCMA or DoE. You can do this by modifying Empower's configuration file, empower.conf, which resides in Empower's home directory.

To change the name of the auditing agency, set the value of the variable AUDIT_AGENCY to the desired value. In the listing below of a empower.conf file, we have changed the auditing agency to DCMA.

```
# Empower configuration file
# Audit_Agency=Dcma
```

---

## Chapter 3: The Audit Report Spreadsheet

Understanding the Audit Report spreadsheet is the key to understanding how to work with Empower's Audit Reports. You can have different audit reports associated with different contracts, so the first thing you need to do is find out which audit report your contracts are using. To do this, download the Contracts table, open it, and switch to the Settings tab. We have done this in Figure 3.1, hiding some columns for clarity. The AuditID column shows the report ID associated with each contract in the database. The figure shows that all our contracts are using the default audit report (report id = 1). Later in this tech note will show you how to create different audit reports and assign them to contracts of your choosing.

Notice that the "Contracts" download has several tabs, including one titled "Audit." This tab contains settings that should be filled out before calculating your Audit DQIs. These settings include your workpackage symbol, hard constraint symbols, soft constraint symbols, and control account symbol, to name a few.

Now it's time to download the Audit Report spreadsheet and get familiar with its contents. Using Download Data, download the item Audit Reports (this is a shared item).

The resulting spreadsheet is shown in Figure 3.4. Empower is shipped with three Audit Reports, named "Default", "DOE", and "(Default)-AatCA" as you can see from the Audit Reports tab. You can see that there are several other tabs, including (Default)-Tests, (Default)-SQL, and (Default)-Notes. If you add another audit report, you will get another row on the Audit Reports tab, and three more tabs. The names of the new tabs will begin with the name of the new audit report; one tab name will end with "-Tests", one with "-SQL", and the other with "-Notes".

You may notice that the "(Default)-AatCA" Audit Report looks very similar to the "Default" Audit Report; the difference between these reports is that the "AatCA" report uses tests designed to run with ACWP at the control account level instead of the work package level.

The "RefID" field on the Audit Reports tab indicates which set of columns should be displayed in the UI (e.g. in the "Audit EVMS" section of "Edit Sort View") for the current contract. RefID1 uses columns with DECM names, while RefID2 uses columns with DOE names.

### 3.1 Audit Report Download Tabs

#### 3.1.1 Tests Tab

Figure 3.5 shows the tests for the Default audit report. Each test has a Test ID; this is a unique identifier assigned by Empower. Each test also has a RptID, Revision, Attribute, and Metric. These four fields taken together must be unique. The Revision column is used to indicate the effective date of a test (we will return to this later). The Attribute and Metrics columns hold the items of the same name from the DCMA test guide. The Test and Goal fields are how Empower decides whether the test has passed or failed. Empower calculates some number X (how will be described in a moment), then compares X to the Goal value with the operator in the Test column. The Hidden column can be used to remove tests from the Audit report output. The DQIs column indicates which (if any) of Empower's Data Quality Indicators (either default or user-defined) are used in this test. We will return to this topic at the end of this chapter.

The rest of the fields indicate fragments of SQL that are used to calculate the X value mentioned above. X is (usually) calculated as a numerator divided by a denominator, then converted to a percent (since the Goal values are — usually — specified as percentages).

If the Numerator field is blank for a test, that test is a manual test. The test will appear in the report with an asterisk in the M column, and the values will need to be entered manually, not calculated with SQL statements. Setting manual values is covered in the next chapter of this technical note.

In some cases, the SQL fragment is fairly simple and is entered directly in the relevant column of the Tests tab. For instance, in test 03A101a (row 14 of the spreadsheet), the numerator is just the count of records meeting the specified condition, so the Numerator column is "count(*)". In other cases, the SQL fragment is more complicated (and likely used in a number of tests); in these cases, the relevant column in the Tests tab contains not the SQL fragment itself, but one or more references to rows of the SQL tab. For instance, in row 14 the From column shows references to three SQL fragments (ev, wc, and wh1) that are used to build up the SQL statement. Notice that in row 40, there is a semicolon (;) in the list of references to SQL code fragments. If there is a semicolon, the SQL fragments referenced before the semicolon are used in building the SQL statement for the numerator, while the references used after the semicolon are used in building up the denominator's SQL statement; otherwise, the referenced fragments are used for both numerator and denominator.

#### 3.1.2 SQL Tab

Now to the SQL tab. Figure 3.6 shows the SQL tab for the Default audit report.

Each record in this tab has a RptID and ID field; these together must be unique, and the RptID value must match the report ID value for this audit report.

Here we see that the ev value that appears frequently on the Tests tab refers to a fragment of SQL that refers to the Contract table and continues with a string of join clauses. You can usually figure out the focus of the SQL fragment from the code: ev involves earned values, t tasks, tl task links, tp task predecessors, etc.

The SQL statements to calculate the numerator and denominator are assembled from the values on the Test and SQL tabs. There are two cases:

1. In the most common case, the SQL for the numerator is formed as "Select [Numerator] from [concatenation of the SQL fragments referenced in the From column (before the semicolon if present)] + [Where (numerator)] + [Where(both)]", with conjunctions added as necessary.

   The SQL for the denominator is formed as "select [Denominator] from [concatenation of the SQL fragments referenced in the From column (after the semicolon if present)]+[Where(denominator)]+[Where(both)]", again with conjunctions added as necessary.

   (In the above, the [Where (numerator)], [Where (denominator)], and [Where (both)] are only used if present, of course.)

2. In the second case, an entire SQL statement is supplied. It is simply used as is. Typically this is necessary when the DQI test sums multiple elements. Test 06A208a is an example of this case; note that the Numerator field on the Tests tab has sql-ea01. This refers to row 14 on the SQL tab. Notice there are several complete SQL statements on this tab, each of which has an ID that begins with sql-ea; we follow the convention that SQL statements we supply on this tab begin with sql-ea ('ea' for Encore Analytics); if you add your own SQL statements to this tab, we suggest you name yours according to the pattern sql-X, where X is some string identifying your organization.

Note the bracketed {un}, {st}, and {cd} terms that occur in several of the fragments, notably the wh1, and wh2 fragments in lines 39 and 40. These specify the Unit, Structure and Period IDs, respectively, of the current dataset. If you write your own custom SQL statements or clauses, you will almost certainly need to use these.

You should not modify the standard SQL fragments on the SQL tab; if you add new fragments, put them below the existing rows.

Here is an example of how Empower reads the pieces of SQL from the audit report Tests and SQL tabs to build up the query it uses to calculate the numerator for the test metric 03A101a:

```sql
select count(*)
from Contract c
inner join Element e on e.ContrID = c.ContrID
inner join EarnedValue ev on ev.ElemID = e.ElemID
inner join ContrUnit cu on cu.ContrID = c.ContrID
and cu.UnitID = ev.UnitID
inner join dpns d on d.kce = ev.ElemID
and d.kcd = ev.PeriodID
and d.kun = ev.UnitID
inner join WorkAuthCalc wc on wc.ElemID = ev.ElemID
and wc.PeriodID = ev.PeriodID
where e.StruID in (1, 3)
and ev.PeriodID = 9
and ev.UnitID = 1
and EvasCmp = 0
and T52 > 0
```

In this listing, the Numerator SQL fragment (count(*)) is at line 2. We see on the (Defaults)-Tests tab that the From column on the SQL tab provides lines 4–11 (ev); lines 12 and 13 (wc), and lines 14–16 (wh1). Note that the "where" keyword is part of the wh1 SQL fragment.

Line 17 of the where clause comes from the Where (Both) field on the Tests tab, and line 18 comes from the Where (Numerator) field on the same tab.

#### 3.1.3 Notes Tab

Figure 3.7 shows the Notes tab for the DOE audit report.

Each record in this tab has a RptID and NoteID field; these together must be unique, and the RptID value must match the report ID value for this audit report.

The Notes tab is used for additional details about test calculations. These notes may be referenced in Audit Test descriptions, and are denoted by a number in parentheses. For example, you might see a test description like:

```
Number of activities with actual start date different than
prior report (1)
```

The '(1)' indicates that NoteID 1 applies to this test.

Now you have the information you need to make modifications to the existing tests, or write your own tests. We encourage you to contact Encore Analytics technical support if you have any questions.

### 3.2 Report References

While we're looking at the Audit Report spreadsheet, we'll tell you how to add a reference line to your reports. In Figure 3.8, you see that there is a RptRef field in each Audit Report record.

We can put in a value in this field, put "c" in the action column, and upload the Audit Report spreadsheet. When we have done that, the reference will appear in the report output.

The reference will also appear in the Audit Trends report.

### 3.3 Hidden Tests

Now to return to the Hidden column. The Hidden column can contain a 'T' or 'F', or be blank. If it contains a 'T', the test is hidden. If it contains an 'F', the test is not hidden. If it is blank, and the test is based on an Empower DQI (so that the DQI column isn't empty), the TestGroup value of the DQI controls the test's visibility, as with other reports (See 'Removing DQIs from Reports' in the Empower User's Manual).

---

## Chapter 4: Setting Manual Values

Some of the tests shown in audit reports are calculated from data which is not normally available to Empower and thus must be provided manually. This chapter describes how to set such manual values.

We begin by looking at the beginning of an Audit report, shown in Figure 4.1: The asterisks in the M, Value, Total, and Percent columns indicate that this test (01A101a) is a manual test, and the values necessary to calculate the test metric must be input manually. Once this has been done, you will see numbers in the Value, Total, and Percent columns of the report, but the asterisk will remain in the M column to remind you that this test is based on manually entered values.

To enter values manually, we download the Manual Audit Test Notes and Values spreadsheet, specifying the contract and period.

In the resulting spreadsheet, we add the numerator (Num) and denominator (Denom) values that will be used to calculate the test value, and put an "a" in the Action column. (We use "a" — for add — because we are adding a row for each row we edit. If there were values in the Num and/or Denom columns, perhaps because updated values have become available for this period, we would enter the new values and put "c" in the Action column, as we would now be changing an existing record.) In the "AuditNotes" tab of the spreadsheet, the Note field can be used to add details or explanations about the manual test we are adding, while the Link field can be used to add a link to data external to Empower.

In Figure 4.3, we have added values for two tests, 01A101a and 03A103b.

Next we upload the AuditVals spreadsheet and recalculate. Opening the Audit Metrics report, we see the results of our labors.

Note the asterisk denoting manual tests. Clicking the "Note" column header or a "..." entry in the column will expand the note. Clicking "Note" again or clicking the note text itself will collapse the Note column.

Notice the link icon in the "Test" column. This icon will only appear for tests that have an entry in the "Link" column for the current period. Clicking the link icon will open the "Link" URL for that test in an external window. Depending on your browser, you may need to allow popups in order to use clickable links in the Audit Metrics report. Clickable links are not available in the Audit Metrics Report if it is opened as an external report or for cross-contract summary elements.

Notes and links can also be added to automatic tests. To add a note or link to an automatic test, download the Automated Audit Test Notes spreadsheet, specifying the contract and period.

In the "AuditNotes" tab of the resulting spreadsheet, we can add a note to an automatic test by putting text in the "Note" column and adding a "c" to the Action column.

After uploading the spreadsheet and recalculating, we see our note and link icon when we open the Audit Metrics report.

---

## Chapter 5: Creating New Tests and Reports

### 5.1 Creating a New Test

In this chapter we illustrate how to create a completely new test. Suppose we want a test metric that will be tripped if the actual finish of a task is before the baseline finish. There isn't such a test in the default audit report, so we create one. This metric is similar to others in the 06A2 series, as it deals with tasks, so we pick a metric that isn't being used in this series and call our new test 06A214a. We look at the tests tab and find that the existing test 06A208a counts summary tasks with logic applied. That's what we want to do (with a different bit of logic), so we copy that row as the starting point for our test and paste it at the end of the Tests tab.

We put "a" in the action column, since we are going to add a row to the database. We set the TestID to 8192 (IDs below 8192 are reserved, and we can tell by scanning the Tests tab that there have been no tests added, so 8192 is available for us). We set the Attribute and Metric fields respectively to "06A2" and "14a", and put the appropriate text in the Description column. We want the test to trip if there are any tasks with the actual finish earlier than the baseline finish, so we set the Test and Goal to be "=" and "0", respectively. In the numerator, we want to count the number of non-conforming tasks, so the Numerator column becomes "count(*)", and the condition we are applying goes in the Where (numerator) column: "t.ActualFinish < t.BaselineFinish". For the denominator, we want to count the total number of tasks, conforming or not, so the Denominator column gets "count(*)", and we want both the numerator and denominator to be counting only non-summary tasks, so we put "t.Summary='F'" in the Where (both) column.

Once we have written our test, we save the Audit Report spreadsheet, upload it with the Upload Data File command, recalculate our contract, and open the Audit Report. For MOH-2, JAN04, our new test looks like this in the report: The report shows that one of the 111 non-summary tasks finished before the baseline finish date.

If we want to be able to view this new test in the sort window that will require some additional steps, see section 5.4 for more details.

### 5.2 Creating Per-Period Tests

As reporting systems get more sophisticated, manual tests may be replaced by automated ones. In this scenario, the audit report for the earlier, pre-automated periods should be run using the manual tests, while the later periods should use the automated tests. This scenario is handled by creating per-period tests. Different versions of a test can be created that apply to different periods.

For the purposes of explaining the process of creating a per-period test, we will actually implement a change to an existing automated test, rather than creating an automated revision for an originally manual test. Consider test 03A101g, for which the goal value is 5%. Imagine that the auditing agency decides that this is too stringent a goal and decides to relax the standard to 20%. (We didn't say this would be a realistic example.) This change will go into effect with the first period in 2017, but for earlier periods, the old value of 5% will still be used. We need to create a new version of test 03A101g that applies from January 2017 on, while retaining the old version for prior periods.

We begin by downloading the Audit Reports spreadsheet. We copy the row containing test 03A101g and paste it in right below the original row. Then we edit it by: (a) changing the goal value to 20%; (b) changing the Revision to the new effective date of 2017-01-01; and (c) blanking out the TestID field. We have to blank out the TestID because we are going to be adding a new row to the database; Empower will take care of generating the new TestID. And because we are adding a new row, we put an "a" in the Action column of the new row. The Audit Report spreadsheet now looks like Figure 5.3:

Next we upload the Audit Report spreadsheet and recalculate the contract. For the example, we recalculate the whole contract (instead of just JAN17) because we want to show that test 03A101g still is calculated the old way for DEC 16, while the new goal value is used for JAN17.

Here in Figure 5.4 is the relevant portion of the Audit Report for the DEC 16 period. Notice that the goal is 5%, and the background of the actual value (18.8%) is colored to indicate that the test failed.

And Figure 5.5 shows the 03A101g test from the JAN 17 report. The goal is now 20%, and the background color shows that the test passed in this period (though in fact the test value was the same as in the previous period).

### 5.3 Creating New Reports

What if you have two different auditing agencies, with some of your contracts subject to one agency's data tests, and other contracts subject to the other agency's metrics? Empower lets you create multiple audit reports, assigning them to your various contracts as necessary.

In the following example, we walk you through the steps of creating a new audit report.

We begin by downloading the Audit Report spreadsheet. We want a new audit report, which means adding a row to the Audit Report tab. We name the report "NewAudit" and put "Mike's Auditing" as the reference. We leave RptID blank because we are going to add a new row to the database, which means Empower will generate the ID, and since we are adding a new row, in the action column we put—wait for it—an "a". The Audit Report tab now looks like Figure 5.6:

Next we upload the spreadsheet, and download it again. The downloaded spreadsheet is shown in Figure 5.7.

There are two things to note: First, Empower has added a new Audit Report record and assigned it a Report ID of 16. Audit IDs 1 and 2 are used by our standard Default report and DOE report respectively and IDs 3-16 are reserved. Second, Empower has added three more tabs, named NewAudit-Tests, NewAudit-SQL, and NewAudit-Notes. (The names of the tabs, up to the hyphen, need to match the name of the in the RptDesc column of the Audit Report tab.)

You will need to download the Contract spreadsheet and set the AuditID value on the Settings tab for MOH-2 to this new Report ID of 16. Otherwise, the Audit Report for MOH-2 will continue to be based on the default set of tests, instead of the ones you are about to create. You can set Contract.AuditID now, or wait until you have finished creating the new audit report. We recommend doing it now, as you might forget to do so after doing all the steps below, and then you will wonder why your new report doesn't seem to have taken. We speak from experience.

Now, let's look at the Tests tab for the newly created NewAudit audit report, as displayed in Figure 5.8:

There isn't much here, which is not surprising as Empower doesn't know what tests the Mike's Auditing agency might see fit to prescribe. In real life, you would take the requirements from your agency and turn them into the appropriate fields on this and the matching SQL tab.

Let's say that we want our new audit report to hide test 03A101a, and we want the goal for test 03A101f to be 10 rather than 5, which we feel is much too draconian. Of course adding the 03A101a test only to hide it is not a likely to be useful in the real world, but we will do so for the sake of illustration. We copy just the two tests that we want from the (Default)-Test tab to the NewAudit-Test tab and change RptID to 2 for both rows. We hide the 03A101a by setting Hidden = "T", and we change the Goal for 03A101f to 10. We're adding rows to the database, so we put an "a" in the action column for both rows of the spreadsheet. We also copy any necessary SQL entries from the (Default)-SQL tab to the NewAudit-SQL tab and put an 'a' in the action column for all the rows we copied. When it's ready to be uploaded, the Tests tab looks like Figure 5.9:

We upload the spreadsheet and recalculate MOH-2 (remember, this new audit report only applies to MOH-2). When we open the Audit Report, it looks like Figure 5.10. Note that test 03A101a is not in the report, and the Goal for 03A101f has been increased to 10 (not that it did us much good in this case!).

### 5.4 Audit Tests in Sort Window Views

In order to view your custom tests in the sort window, there are some additional steps that must be taken after creating the test in the Audit Reports download.

#### 5.4.1 Set Metric Type

First, use the Metric Type field in the test tab of the Audit Reports download to indicate whether your test is related to cost or schedule; this will determine whether the metric can be viewed in cost sort window views or in task mode (Gantt) views.

In general, metrics that are tied to a certain element in the structure would be marked with Metric Type = 0 for "cost" mode, while metrics that are tied to a specific task would be marked with Metric Type = 1 for "schedule" mode.

You can set Metric Type for your test either by changing an existing test with c or when creating your test.

#### 5.4.2 Create Columns Entry

Second, you must create Columns entries for any audit tests that you wish to make available to use in sort window views.

To add Columns entries, do a "Data Download" of Columns, then select the "Metrics" tab. Items added to the "Metrics" tab will be treated as custom Audit Metrics. Empower will fill in the necessary information on this tab as long as you supply a valid Audit Test ID and Col Name.

Figure 5.12 shows a minimal entry for the Metrics tab in the Columns download.

This would create a Columns entry with the ColName "CM1" and information populated based on the Audit Metric with TestID 8192; use your Audit Metrics data download for reference when determining the correct TestID.

Notice that you can leave most of the fields blank; these will be populated by Empower on upload based on the Audit TestID that you provide. You can change items like "Alias", "TestSum", and "ColDesc" after creating the Columns entry via the usual method of data download/upload with a 'c' in the "action" column.

Unlike other custom Columns, the UserDef for custom Audit Metrics will be 'P'.

After uploading our new Column, if we do another data download of Columns, we'll see an entry like this on the Metrics tab:

Figure 5.13 shows a Columns Metric Tab Entry.

A number of fields have been populated with default values based on the TestID that we provided and the Metric Type of that TestID. In this example, TestID 8192 was a cost test with Attribute name "03A1" and Metric name "01a". For reference, rows with TestGroup 6 are cost tests, while rows with TestGroup 7 are schedule tests. Notice that the SQLL column is not populated yet. This is because we have not yet done a recalculation after uploading our new Column.

The final step after uploading our new Column is to run a recalculation on some data that uses the new test with "Calculate Audit Metrics" checked. This will populate the SQLL so that we can use our new Column in the sort window.

#### 5.4.3 Using Valid Test IDs

Suppose we tried to add a new entry to the Columns Metrics tab with a TestID that does not exist in our Audit Reports download. When we try to upload our new Columns entry, we'll see a message indicating which row failed and why, and the bad entry will not be created. The fix for this is to make sure that your TestID is valid. We recommend using your Audit Reports download for reference when creating your Columns entry.

#### 5.4.4 Sort Window Audit Test Limits

It is important to note that you will be limited to 200 "cost" audit metrics and 100 "schedule" audit metrics that can be displayed in the sort window. This limit includes both custom metrics and any default audit metric Columns entries. If you try to add Column entries that would exceed this limit you will see a message indicating which row failed and which limit (Cost or IMS) was exceeded.

Note that you may have more audit metric tests in your Audit Reports download than these limits allow, however not all of them will be available for display in sort window views.
