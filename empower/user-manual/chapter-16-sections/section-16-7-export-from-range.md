# 16.7 Export From Range

This menu option allows the user to export an Empower-optimized file for the selected contract with values adjusted as if the contract begins in the period selected for 'From' and ends in the 'To' period.

The intent of this tool is to export the enclosing fiscal year for the selected period in the 'Periods' column so that it can be used for fiscal year reporting. For example, you might export the 2017 fiscal year, then import that file into a different database used specifically for fiscal year reporting.

The "Export Name" field at the top of the dialog allows you to specify a new name for the exported contract.

**Note:** The new contract will need to be recalculated after importing in order for the calculated metrics to be correct for the contract.

## Figure 16.43: Export From Range Dialog

This utility requires consistent Calendar and Period End Dates. In order for the tool to select appropriate 'From' and 'To' dates when a period is selected, the Calendar 'FyEnd' should also be correct. For this feature, the contract Calendar should have End Date entries for the complete fiscal year before the first Period of data for the contract and the complete fiscal year after the last FutureEtc End Date. The automatically selected 'From' and 'To' dates can be overridden, but some restrictions apply.

When selecting a 'From' date, note that the 'From' date must be on or before the earliest selected 'Period' date. Should you select a 'From' date after the earliest selected 'Period', you will receive this message:

## Figure 16.44: From Date Warning

Also note that the selected 'From' date must be earlier than the selected 'To' date. Otherwise, you will receive the following message on selecting 'Export.'

## Figure 16.45: From To Date Warning

This utility subtracts prior periods that are outside of the export range as well as future period data outside of the export range. The first exported period will have equal current and cumulative values.
