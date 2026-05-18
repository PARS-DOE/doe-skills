# Chapter 11: Data Quality Indicators

*From the Empower User Manual*

---

## Chapter 11

Data Quality Indicators

In this chapter, we gather together information about working with Data Quality Indicators (DQIs). Except for the first section of this chapter, we assume you know how to use the Admin > Download Data File and Admin > Upload Data File commands, so you might want to skip forward to familiarize yourself with those, then return to this chapter.

---

## 11.1 Getting Elements Flagged by a DQI

Here we describe how to download a spreadsheet showing all the WBS (or OBS, etc.) elements flagged by a particular DQI. Consider Figure 11.1 below. Say we would like a spreadsheet listing just the elements that contributed to the 21 NoLogic DQI errors shown at level 2 for WBS element 3000.

Figure 11.1: Getting Elements Flagged by DQI

We perform a control-right click with the mouse cursor on the NoLogic cell for element 3000, and Empower asks if we want to download NoLogic details for element 3000:

Figure 11.2: Getting Elements Flagged by DQI

We click "Yes"; the downloaded spreadsheet looks like Figure 11.3:

Figure 11.3: Getting Elements Flagged by DQI

This shows that elements 3200, 3400, and 3600 were responsible for the 21 NoLogic DQI errors.

---

## 11.2 DQI TestSums

When Empower calculates DQI violations for non-lowest level elements (i.e., parent elements), it has to know whether you want to calculate just the DQI errors associated directly with that element, or whether you also want to include the number of DQI errors associated with the element's children in the parent's total; a strategy known as "summing up the tree."

You tell Empower which approach you want it to take by setting the appropriate value in the Columns table. You can set the strategy differently for each DQI.

Consider a portion of the second tab of the Column table spreadsheet download:

Figure 11.4: Column Table Download, Showing DQIs

In this figure we have hidden several rows and columns for clarity. Row 21 contains the first DQI. Its column name is T1, but it has the more helpful alias S>B, which is what you will see when you have the IMS DQI view applied in the Sort Window. Now we focus on the column TestSums. If this value is set to T ("True"), the number of violations of this DQI will be summed up the tree. If it is set to F ("False"), the children's violation total will not be charged to the parent's account.

---

## 11.3 Controlling DQI Cell Background Color with DQI FormatFlag

You can control the background color used for the DQI cells when the number of DQI errors is > 0. (When there are no DQI errors, the background color is a soothing green.)

Now let's look at the Columns download again; this time we focus on the DataType and FmtFlag columns.

When the number of DQI errors is greater than zero (e.g., T1 > 0), Empower sets the background color of the relevant cell in the Sort Window as follows: if FmtFlag is 65, the background will be yellow; if the flag is 66, the background will be red; if the flag is 64, the background will not be colored. To sum without colors, set FmtFlag to 64.

---

## 11.4 Removing DQIs from Reports

This section describes how to remove certain DQIs from Empower's reports. This procedure can be used to remove DQIs from the Data Quality Indicators and Six Period DQI Trends Reports. It can also be used to remove certain test metrics from the Audit Attributes and Tests Reports. (See the technical note, "Empower's Audit Report," available on our support website, http://encoreanalyticsllc.freshdesk.com/support/solutions for more details.)

Consider Figure 11.5, which shows the beginning of the DQI report for WBS 3400. Suppose that the DQI "BAC not equal to WAD BAC" is not particularly relevant in our context, and we don't want this showing up in our DQI reports.

Figure 11.5: DQI Report for WBS 3400 (Before)

The first step is to get the number Empower uses to refer to this DQI, the DQI ID. Use the command Help > Empower DQI Test Guide to download the file Empower_DQI_Test_Guide.xlsx. Open this in Excel and look for the Description of the DQI you wish to remove from the report.

Figure 11.6 shows that we want to remove the DQI with ID=53.

Figure 11.6: Empower Test Guide

Next we download the Columns table and open it in Excel. Go to the second tab where the DQIs are listed; the DQIs have column names that are made up of "T" followed by the DQI ID. Figure 11.7 shows that our DQI is in row 61. The TestGroup column is used, as its name suggests, to group the DQIs in the DQI report. (You can learn more about the TestGroup column in the technical note "Adding Custom Fields in Empower," available on our support website, http://encoreanalyticsllc.freshdesk.com/support/solutions). The TestGroups that are shown in the report begin with 1. If, however, you set TestGroup to 0, the DQI will not be displayed in the report. So, as the figure shows, we set TestGroup to 0, and put a "c" in the action column to tell Empower that we are changing a row.

The figure shows the Columns spreadsheet ready to upload.

(As you have probably figured out, to reinstate a DQI in the reports, put a non-zero value in the TestGroup column of the Columns table, upload, and recalculate.)

Figure 11.7: Columns Table Download

We upload the Columns spreadsheet and recalculate. We then re-open the DQI report, and, as Figure 11.8 shows, the DQI we wanted to remove is no longer present.

Figure 11.8: DQI Report for WBS 3400 (After)
