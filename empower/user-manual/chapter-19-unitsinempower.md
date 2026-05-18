# Chapter 19: Units in Empower

*From the Empower User Manual*

---

## Chapter 19: Units in Empower

Empower 3.0 introduces several significant enhancements in handling units:

1. Primary values (BCWS, BCWP, ACWP, BAC, LRE, and related fields) are now stored as exact numbers with 14 digits, including two digits to the right of the decimal point. Previously, Empower stored numeric values in floating-point format ("floats"). Storing numbers as floats allows representation of very large and very small numbers, at the cost of losing some precision in the least significant digit. Now Empower provides precision down to the penny.

2. Storage and display of numeric values are now decoupled. Previously, if dollars were stored in the database as thousands of dollars, they would be displayed in thousands. If you wanted to see dollars in ones, you had to change the values in the database. Now you can store your values one way (say dollars in ones), and display them in thousands or millions or whatever makes the most sense in a given situation without having to change the values in the database. The display scaling and decimal place choices for a contract will be reflected in the formatting of primary values in the Sort Window, reports, VARs, and IMPRs.

   We recommend you store all units in ones (with up to two decimal places), and use DisplayScale (explained below) to adjust how values are scaled for display (ones, thousands, millions, etc.).

3. Scaling and decimal places can be different for each contract. Not only have storage and display been decoupled from each other, they are decoupled between contracts. Previously, if dollars were stored as thousands in a database, all contracts in that database would have their dollar amounts stored and displayed the same way; that is, all contracts in the database would display their dollar amounts in thousands. Now the display scaling can be set differently for each contract. For one contract, it might make sense to display dollars in thousands, while for a different contract it might be more convenient to display dollars in millions. Similarly, the number of digits shown to the right of the decimal point (decimal places) can be set differently for each contract.

4. In dialogs where a list of units is displayed for a given contract, only the units actually used by that contract are shown. Previously, all units available in the database were shown, whether or not the selected contract used them.

Now let's explain in detail how Empower handles units.

Empower stores a list of all the units in the database in a table called Units. You can see the contents of the Units table by using the Download Data File command (see Section 16.9 on how to use this command). We choose "Shared (selected)" for the DataType and "Units" for the Item. The resulting spreadsheet is shown below.

**Figure 19.1: Units (Shared)**

Note that all units are stored as ones (Scale is 0 for each unit; remember that 10^0 = 1). This applies to every contract in the database.

(At the end of this section, we will explain how to adjust your data to be in ones if you've started with a different scaling.)

Empower stores the list of units actually used in a given contract, and the scaling and the decimal places for each unit, in a table called ContrUnits. Let's look at the records in the ContrUnits table for the MOH-2 contract. Again, use the Download Data File command, selecting "ContractUnits" for the DataType and "MOH-2" for the Contract. The resulting spreadsheet is shown below.

**Figure 19.2: ContrUnits for MOH-2**

Some things to note: First, MOH-2 does not use all the units available in the database (for instance, it doesn't use the COM $ unit type). Second, all of the element of cost (EOC) units (things measured in dollars, like Dollars, G&A, LAB, etc.) have their DisplayScale set to 3. Therefore Dollars, and things measured in dollars, will be displayed as dollars in thousands. Third, all the EOC units will be shown with 2 decimal places. Hours and EQP, on the other hand, will be displayed in ones with no decimal places.

Notice the RptScale and RptDecimal columns. These fields indicate the scale and decimal places that should be used when exporting IMPRs. These values will not be used for scaling and decimal places in the Empower UI.

The SumOf column can be used to configure a unit with EarnedValue data that should be the sum of other units for this contract. If used, SumOf should be a comma separated list of valid UnitIDs. For example, if we had a unit called Non-Labor, we might set SumOf to "5,6,7,8" indicating that Non-Labor will be calculated as the sum of UnitIDs 5, 6, 7, and 8 (MAT, ODC, OH, GA). Note that you will need to recalculate your data after setting a SumOf value.

The IsCore column is used to indicate units that should be included in detailed recalculations. By default, only Dollars, Hours, and EQP are included in detailed recalculations; notice that IsCore = T (true) for those units, while it is set to F (false) for all other units. These values can be changed to include more units in detailed recalculations, however it should be noted that this can greatly impact recalculation times.

Now consider the record (there is just one) in the ContrUnits table for the BOOM-ERANG contract, shown below:

**Figure 19.3: ContrUnits for BOOMERANG**

Notice that BOOMERANG uses only one type of unit, namely Dollars. Dollars will be shown in millions (DisplayScale = 6; 10^6 = 1,000,000), and one decimal place will be shown.

We said that Empower will now only show the units actually used for a contract in various dialogs. To see this in action, we bring up the Open Dataset dialog and select MOH-2. As the figure below shows, in the units listbox we see lots of units, the same ones that we saw in the ContrUnits table for MOH-2.

**Figure 19.4: Open Dataset Dialog, MOH-2 Selected**

But when we select BOOMERANG in the same dialog, notice that only Dollars are showing in the list of units, exactly as we would expect after having peeked at the ContrUnits table.

**Figure 19.5: Open Dataset Dialog, BOOMERANG Selected**

The ContrUnits spreadsheet download also includes two extra tabs; these can be used as a reference when configuring some export or import formats. The "IPM-DAR JSON" tab lists the IDs that should be used when mapping Contract Units to IPM DAR JSON export units.

**Figure 19.6: ContrUnits IPM DAR JSON Tab**

The "DOE CPP JSON" tab lists the IDs that should be used when mapping Contract Units to DOE CPP JSON import units.

**Figure 19.7: ContrUnits DOE CPP JSON Tab**

We've already shown the DisplayScale and DisplayDecimal values in the ContrUnits table for both MOH-2 and BOOMERANG. In the Sort Window, the primary values for MOH-2 will have two decimal places and for BOOMERANG, one decimal place. The display scale will be shown in a number of ways. Charts and reports will indicate the scale in their headings. For example, the figure below shows a Cumulative Variance chart for BOOMERANG; note that in the chart title, dollars are indicated to be in millions.

**Figure 19.8: CV Chart, Showing Dollars in Millions**

The scale will also be shown in the Title Bar at the top of the Sort Window and in the Status Bar. The following two figures show the Title Bar for MOH-2 and BOOMERANG, respectively.

**Figure 19.9: MOH-2 Title Bar (Dollars in Thousands)**

**Figure 19.10: BOOMERANG Title Bar (Dollars in Millions)**

The alert reader might be wondering what will happen if we do a cross-contract query. Now that each contract has its own display scale and number of decimal places to display, what happens when we look at more than one contract at the same time? The answer is that Empower uses the largest DisplayScale value, and the highest number of decimal places, to display all the primary values.

So, for instance, if we open MOH-2 by itself, for Dollars with DisplayScale = 3 (dollars in thousands) and DisplayDecimal = 2, BAC for element 1000 will be shown as 20,796.20 (that is, 20.8 million dollars).

If we open BOOMERANG by itself, for Dollars with DisplayScale = 6 (dollars in millions) and DisplayDecimal = 1, BAC for element 100 will be shown as 292.4 (that is, 292.4 million dollars).

But when we use Open Dataset to view all contracts, MOH-2 element 1000's BAC will be displayed as 20.80 instead of 20,796.20 as before. In other words, it will be shown as dollars in millions with two decimal places; and of course, it will still be the same amount of money, namely 20.8 million dollars. And BOOMERANG element 100 will be displayed as 292.42 (still dollars in millions as before, but now with an extra decimal place).

We have shown you how to adjust DisplayScale and DisplayDecimal for all the units in a single contract, using the Download Data File/Upload Data File functionality. There is a simple way to set the DisplayScale and DisplayDecimal values for all Dollars and dollar-like units in all contracts in your database without having to download, edit, and upload the ContrUnits table for each contract in your database. The Set Dollar Display script (Admin > User Scripts > Run/Edit) will prompt you for values for DisplayScale and DisplayDecimal, then apply those choices to all the Dollar and dollar-like units (i.e., units that end with a dollar sign, like "LAB$", "MAT$", etc.) in the current database.

Finally, what if you decide to take our advice and store all your numbers in ones, but they are currently in some other multiple? You will use the Admin > Rescale Values command for this (see Section 16.15.4).

Let's assume that Dollars are stored in the database as thousands. The figure below shows how we would rescale all Dollar values to be in ones.

**Figure 19.11: Rescaling to Dollars in Ones for All Contracts**

1. Notice that the dialog mentions two possible use cases for the Rescale Values dialog. We are doing the first case. Since this change will affect every contract in the database, you need to be the Admin user to do it.

2. Note that we have checked "Adjust Scale". This means we are going to adjust the Scale field in the Units table. Recall that the Units table is shared by all contracts; this change will affect all contracts. (Hence the restriction of this function to administrators.) Therefore, all contracts in the Contract list box are automatically selected and grayed out: we cannot try to select just one contract. Furthermore, the Scale button under the Period list box is disabled; we are going to be changing all periods of all contracts, so Empower keeps us from trying to select just one or a few periods.

3. Note in the Scale - Unit list box, the entry "3 - Dollars". This means that the Dollars numbers in the database are currently stored in thousands of dollars (since 10^3 = 1000). So if a value was really $1,000, it will be 1 in the database.

4. We have entered 3 in the box labeled "Multiply values for the selected items by 10 to the". We are asking Empower to multiply all the Dollar values in the database by 1000 (again, 10^3 = 1000). Since they were in thousands before, they will be in ones afterward, which is what we wanted.

We press Scale, and all the Dollar values in the database will be multiplied by 1000, and the Scale field in the Units table will be set to 0.

It is important to realize that the values you see in Empower will not change. You are not inflating your project's budget or magically reducing your costs. If, for instance, MOH-2's element 2100 BCWS for JAN 04 was $294,600 before you did all this, it will still be $294,600 afterwards. Let us repeat: when you do a rescale with "Adjust Scale" checked, you don't change any real-world values. (The second use case mentioned on the dialog does change values; it is used when you have incorrect data and you need to fix it.)

Finally, let's verify that Dollars are indeed being stored in ones. We'll bring up the Rescale Values dialog one more time:

**Figure 19.12: After Rescaling to Dollars in Ones for All Contracts**

Notice that Dollars are now prefixed by a zero: 10^0 = 1 (as you are probably tired of being told by now), so Dollars are stored as ones. If the database has 1234.56, that means 1,234 dollars and 56 cents.
