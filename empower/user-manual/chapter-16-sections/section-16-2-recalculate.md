## 16.2 Recalculate

The Empower database is loaded on a regular basis with data from an enterprise's scheduling and earned value systems. Empower then adds value to the incoming data by performing many calculations to generate additional fields and uncover data quality issues. This is the key behind much of Empower's analytical power.

The process of performing these calculations is called recalculation, and it is accessed through the Recalculate command. This command brings up the Recalculate dialog (Figure 16.23) which allows the user to choose the contract and periods to recalculate, as well as to select a number of options controlling the recalculate process.

**Figure 16.23: Recalculate Dialog**

There are a number of ways you can control which contracts and periods get recalculated. Note first that there are two Recalculate buttons on this dialog.

First, you can recalculate one or more contracts for all periods in each contract by selecting one or more contracts in the Contracts listbox, then pressing the Recalculate button under that listbox.

Second, you can recalculate one or more periods for a single contract. Begin by selecting that one contract in its list box. Notice that the periods shown in the Periods listbox will change to show just the periods in the selected contract. Select one or more periods in the Periods listbox, then press the Recalculate button under that listbox.

The first thing to notice is that the user can recalculate a contract for all periods, by selecting the contract and pressing the Recalculate button under the Contracts select box, or recalculate a contract for just one period, by selecting a contract and a period, and pressing the Recalculate button under the Periods select box.

In the figure below, when we press the Recalculate button under the Contracts list box, Empower will recalculate each of the selected contracts (BOOMERANG, LAR EMD, and MOH-2) for every period in each contract.

**Figure 16.24: Recalculating Several Contracts, All Periods**

In the next figure, we selected the MOH-2 contract, then selected three periods (NOV 03, DEC 03, and JAN 04). If we pressed the Recalculate button under the Contract list box, Empower would recalculate MOH-2 for all periods. But if we pressed the button under the Periods listbox, Empower would recalculate MOH-2 for just the three selected periods.

**Figure 16.25: Recalculating One Contract, Several Periods**

Finally, if you select multiple contracts and recalculate by periods (i.e., you press the Recalculate under the Periods listbox), Empower will recalculate the most recent period for each of the selected contracts.

Notice the button labeled "Show Advanced." Clicking this button will show a number of advanced recalculation options.

**Figure 16.26: Show Advanced Options**

To hide the advanced options again, simply click "Hide Advanced."

The button labeled "Toggle DQI/Audit" allows you to quickly toggle the "Set DQI flags" and "Calculate Audit metrics" options. This can be helpful if, for example, you recalculated your data without these options checked after importing to ensure that your data was correct, but later need to calculate your DQIs. Since they tend to be longer operations, unchecking the DQI / Audit options can save some time if you need to run a recalculation but have already calculated your DQIs.

**Figure 16.27: Toggle DQI/Audit metrics Off**

**Figure 16.28: Toggle DQI/Audit metrics On**

During the recalculation, you will see streaming status indicating the progress of the recalculation.

**Figure 16.29: Recalc Status**

Notice the "Refresh" button in the bottom right of the dialog box. Clicking the "Refresh" button will toggle polling for the recalc status. When toggled on, the refresh will periodically poll the Empower server for updates to the recalc status and update the streaming status accordingly.

**Figure 16.30: Recalc Status Polling**

Refreshing the recalc status can be helpful for instances where the recalc status would time-out due to server settings. For example, if you are using IIS with Empower, some IIS time-out settings limit the amount of time a connection can be open, which can result in the streaming status timing out. Refreshing allows you to continue seeing the recalc status as it updates, even if the browser connection timed out.

The "Refresh" button is also available in some other dialog boxes, including "Import EDI File", "Export Sort Window", "Export DQI Matrix", etc.

To toggle polling off, click the button again (now labeled "Polling...").

Note that if queueing is enabled, you will not see streaming status in the "Recalculate" window. In that case, you can check the status of your recalculation by using the menu option "Check Queue." See 16.3 for more information.

Some operations, such as colors/trends, VAR, and OTB calculations, are only done for Dollars, Hours, and EQP. They are not calculated for other units.

Next we consider the recalculate options.

### 16.2.1 Process EV data

If this option is checked, Empower will perform usual Earned Value calculations such as summing raw data, adding missing PMB elements, setting OTB values, calculating forecasts, setting colors and trends, performing custom user recalculation operations if present, and more. This box should likely be checked for most recalculations, but can be unchecked to reduce recalculation time if, for example, you had already recalculated your data but now want to just recalculate your DQIs.

### 16.2.2 Sum forecasts to summary levels

During recalculation, Empower calculates forecasted values for elements in the contract, based on past performance, the amount of work performed to date, and the budgeted value at completion (BAC). There are two ways to do this. One way is to perform this calculation for each of the lowest level elements in the contract, then sum these values to get the forecasted values for the parent elements, and so on to the top of the element hierarchy. In this case, the forecast for the top level element will be (by definition) exactly equal to the sum of all the forecasts for the lowest level elements. The other way to sum the forecasts is to calculate the forecasts for all elements at a given level, then do the same calculation for all the elements at the next highest level, and so on until the top level is reached. According to this method, the top level forecast value will not necessarily equal the sum of the child levels. Some earned value experts prefer the first method, others the second. So Empower offers a choice. If this box is checked, Empower will calculate forecasts according to the first method. Otherwise, Empower will calculate the forecasts at each level.

### 16.2.3 Process future period data

Future period data (BCWS and ETC) refers to the work that a contractor plans to do for a contract element in a given (future) period. (This should be distinguished from the forecasts that Empower calculates, as mentioned above, based on actual performance history.) If this option is checked, Empower will sum these values up the hierarchy of elements (as it does for forecasts, as described above) and calculate the EQP for future periods. Leaving this option unchecked can speed up a recalculation somewhat.

### 16.2.4 Process schedule

If this option is checked, Empower will calculate a variety of schedule-related items that will show in the Gantt chart window. If you don't have schedule data, uncheck this option.

Note that you must check this option if you want to calculate "Schedule Execution Metrics" (SEM) such as BEI and CEI. Furthermore, if you want to break down the SEM fields by task, you must check both "Process schedule" and "Set DQI flags" when recalculating.

### 16.2.5 Set DQI flags

Recall that the Data Quality Indicator column in the Sort Window shows the results of a large number of quality checks by displaying a code for each category of data quality checks breached by a contract element. (See Section 4.3 for more on these values.) Empower performs more than 40 data quality checks on each element of a contract during recalculation; users may wish to turn off this option to save time if they are recalculating frequently. If this option is turned off, the values in the DQI column in the Sort Window will not be updated to reflect changes in the data made after the option was turned off. Likewise, the Six Period DQI Trend report (see Section 9.6) might be outdated in some parts.

Users will typically do several recalculations after a new periodic import of data from the schedule and earned value systems, as they flush out and correct errors and inconsistencies in such data. Whether they should leave the DQI flags option unchecked or not depends on where the problems in their data are, or (since the problems are likely to be everywhere) what problems they're working on correcting at the moment. If they're working on the cost data, they can uncheck the DQI flags option until the cost data is squared away, then turn it on to give them some feedback on the quality of their estimates-to-complete. If they're scrubbing the schedule data, it might be very helpful to have it checked, since it will help them find the errors they're trying to correct.

DQIs are only calculated for WBS Dollars.

### 16.2.6 Calculate Audit Metrics

When this option is checked, Empower will update Audit Metric items during recalculation.

### 16.2.7 Set Cost Date Fields

For older versions of Empower, when this option is checked Empower calculates the cost/schedule integration dates described in Section 4.2.

For older versions of Empower this option must be checked for Empower to perform Integration DQI checks. In newer versions these calculations will be performed if "Set DQI flags" is checked.

### 16.2.8 Calculate ES metrics

When this option is checked, Empower calculates Earned Schedule metrics. Note that your Period End Dates must exist in the calendar for this contract in order for this calculation to complete successfully. Earned Schedule metrics are only calculated for the WBS structure and these units: Dollars, Hours, EQP.

### 16.2.9 Calculate Current Values

When this option is checked, Empower calculates current values based on the cumulative values in the imported file. If you are starting working with a contract in the middle of its life, the values for the current period will actually reflect all the work done in all periods to date, instead of just the current (first) period. You may prefer instead to manually enter current values for the first period, uncheck "Calculate Current Values", and do the recalculation. For all successive periods, you would recalculate with this option checked.

### 16.2.10 Set Reporting Elements

When this option is checked, Empower will set the "RptElem" and "RptElemE" values for the selected contract's structures. See section 16.9.1 for more details on the "RptElem" and "RptElemE" fields.

### 16.2.11 Calculate EQP

EQP stands for Equivalent Persons. If this option is checked, Empower will take the number of hours (planned, earned, actual) against a contract element and divide it by the number of hours specified in the calendar for the relevant period. For instance, if 240 hours were charged against an element in a 160-hour month, the result would be 1.5 equivalent persons.

### 16.2.12 Calculate F3

When checked, Empower calculates the Format 3 values from the underlying time-phased data. This calculation uses whichever structure you have set as your F3 StructID in the Contracts table.

### 16.2.13 Calculate F4

When checked, Empower calculates the Format 4 values from the underlying time-phased data.

### 16.2.14 Decalculate

If this is checked, all the other options are ignored and the effects of all recalculate operations (described in detail below) are undone. That is, all the sums of forecasts are set to zero, the EQP values are set to zero, and so on.

### 16.2.15 Unlinked Tasks

During recalculation Empower will automatically correct bad or missing task links. Tasks with bad or missing links will be linked to an element called "[Unlinked Tasks]." Links that meet these criteria will be linked to the "[Unlinked Tasks]" element:

- The task does not have a LinkVal
- The LinkVal for the task in TaskLink does not match any of the LinkVals in the Element table
- The task is linked to a summary level element, not a lowest level element
