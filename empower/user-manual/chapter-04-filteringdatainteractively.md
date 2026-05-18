# Chapter 4: Filtering Data Interactively

*From the Empower User Manual*

---

## Chapter 4

### Filtering Data Interactively

As mentioned earlier, there are two types of filters in Empower: interactive filters and prefilters. Chapter 6 will discuss prefiltering. This chapter addresses interactive filtering.

Interactive filtering is best for when you want to create a filter on the fly; you just fill in the filter criteria in the filter bar above the Sort Window. Prefilters offer more power, but take a little more effort to develop. As will be explained in a moment, interactive filtering allows you to specify multiple conditions, each joined with a logical AND. Using a prefilter allows you to create more complex conditions which can be combined with ANDs and/or ORs.

Interactive filtering is invoked via the Filter Bar. The Filter Bar can be toggled on or off in the View Menu. Figure 4.1 shows the Filter bar with some filter criteria entered.

**Figure 4.1: Sample Filters**

The user can enter more than one filter criterion; multiple filter criteria are always joined with a logical AND. For example if you entered the filters shown in Figure 4.1, it would return all accounts that (1) are at the lowest level (LL), AND (2) are between 5% and 90% Complete, AND (3) and have a CPI of less than .95.

Filter criteria can be entered in two different ways. Some of the filter boxes are dropdown lists, and the user must pick the criterion from the given list. In Figure 4.1, the LL filter field is a dropdown list (as signaled by the down arrow), and the user is restricted to choosing only elements that are at the lowest level ("x" in the filter box), or all elements.

The other method uses free-form text entry. The rules for entering filter criteria in these filter boxes vary, depending on the nature of the data in the given column.

In some columns, numeric input is expected. The user can enter a numeric comparison; the format is shown in the list below. (These operators also work with date and date/time data, discussed below.)

- Equal to: = N
- Not Equal to: <> N
- Greater than: > N
- Less than: < N
- Less or equal: <= N
- Greater or equal: >= N
- Range of values: N1.. N2

Note that in Figure 4.1, the %CMP filter is set to select all elements whose %CMP value is between 0.5 and 0.9, while the CPI filter is set to select all rows where the CPI is less than 0.95.

If no operator or range is specified, the numeric filter will default to "=".

Filtering on some of the other columns is bit more complicated; the following subsections describe these special cases.

## 4.1 Filtering on Text Columns

For text fields, the user simply enters some text, and the filter returns all elements where the first characters in the column match the filter criterion. For instance, if the user entered "SMITH" in the CAM filter box, the filter would return elements in which the CAM was named SMITH, or SMITHSON, or SMITHSONIAN, and so on (but not BLACKSMITH).

Text fields also allow the use of a logical OR to specify multiple conditions for a column. For example, the filter for CAM in figure 4.2 will return any rows where the CAM begins with 'J' or 'B.'

**Figure 4.2: Logical OR Filter**

Entering a space in a text field filter will return rows where that field is blank (i.e. a NULL value or ' '). Entering an underscore will return rows where the field is not blank.

Entering '!' operates as a negation. For example, entering '!J' for CAM will return rows where CAM does not begin with 'J.' This allows for more complex interactive filters. For example, entering '!(J|B)' in the CAM filter would return all CAMs whose name do not begin with 'J' or 'B.'

**Figure 4.3: Negation Filter**

Entering '%' changes the filter matching so that it will look for entries that contain the filter text, as opposed to entries that start with the filter text. For example, if the user entered '%n' in the CAM filter box, the filter would return elements in which the CAM had a name containing the letter 'n'. Note that this behavior is case sensitive, so entries with 'N' would not be included. However, you could adjust the filter to include both cases by using a logical OR filter in combination with the 'contains' filter.

**Figure 4.4: Contains Filter**

The 'contains' filter can also be combined with other filter options such as the logical OR filter. For instance, entering '%n|J' in the CAM filter would filter to those CAMs whose names either begin with 'J' or contain the letter 'n'.

**Figure 4.5: Contains With Logical OR Filter**

## 4.2 Filtering on Dates

If the column contains date or date/time values, you enter the date part in the order four-digit year, month, day, with or without a dash between the parts (e.g., yyyy-mm-dd or yyyymmdd). You can enter the time part as hh:mm:ss, or hhmmss, with either a blank or a period to separate the date from the time. You only need enter as much of the time part as logically necessary for your filter. So if you want to filter for times after 2 p.m., you only need to enter 14; you don't need to enter 140000 or 14:00:00.

You can filter date or date/time columns by specifying the exact timestamp you want to match, or you can use the comparison operators listed above.

As an example, the following would all be legal ways to filter for dates after October 25, 2016, at 7 a.m.:

- >2016-10-25 07:00:00,
- >2016-10-25 07,
- >20161025 07,
- >20161025.070000, and
- >20161025.07.

Entering a blank character will filter for columns with no date.

We now discuss a group of date columns that can be used for any purpose but are particularly intended for filtering. These date columns fall naturally into four groups of three. The middle of each group is a schedule date (from the element's linked tasks), which should lie on or between the dates on either side. To the schedule date's left is the corresponding beginning-of-period cost date (from the element's Earned Value or Future Etc records); to its right is the corresponding end-of-period cost date.

So, for example, FirstStart (the earliest start date of an element's linked tasks) is a schedule date that should lie between PrevFirstAorE (the beginning of the first period with ACWP or ETC), and FirstAorE (the end of the first period with ACWP or ETC).

If schedule data is not present, the schedule-related fields (the middle in each group of three) will naturally be blank.

Here are the groups, with the database field name followed by its alias in parentheses, if any:

- PrevFirstAcwp (PrevFirstAorE)
- FirstStart
- FirstAcwp (FirstAorE)
- PrevLastEtc (PrevLastAorE)
- LastFinish
- LastEtc (LastAorE)
- PrevFirstBcws
- FirstBaselineStart (FirstBLStart)
- FirstBcws
- PrevLastBcws
- LastBaselineFinish (LastBLFinish)
- LastBcws

To calculate these dates (so they appear in the Dates filter), you need to set the recalculation option "Set DQI flags" (see Section 16.2.7).

Entering a blank in a date field filters to nulls.

The Dates view uses these dates; of course, you can add any or all of these fields to your own dates (and prefilters) in the usual way.

**Figure 4.6: Sort Window with Dates View Applied**

## 4.3 Filtering on the Data Quality Indicator Column

The Data Quality Indicator (DQI) field is a powerful analysis tool, unique to the Empower application. It identifies accounts that have breached the data quality checks defined in documents such as the DCMA-EA PAM200.1, EVMS Program Analysis Pamphlet. The quality checks are grouped into four categories, listed below along with the letter codes Empower uses to identify them:

- 'E': earned value anomalies,
- 'S': schedule anomalies,
- 'F': forecast/EAC reasonableness anomalies, and
- 'I': cost/schedule integration anomalies.

The DQI column in the Sort Window will contain a combination of these code letters that indicate which categories of data quality checks have been violated by the account.

To filter on the DQI field, just enter one or more of the above four code letters, in any order. Any element whose DQI field contains any of the letters entered will be shown. For instance, entering "ES" would return elements with "E," "EFS," "FS," or just "S" in the DQI field. Note that the filter will return elements with other letters as well; as long as the DQI field for an element contains at least one of the filter characters, that element will be shown. This filter is case-sensitive; "E" is not the same as "e."

The default behavior when multiple letters are entered is to combine them with logical ANDs. To combine letters with logical ORs, use a vertical bar, '|'. For example, entering "E|S" will return rows containing either "E" or "S", or both "E" and "S".

As with text fields, entering a space will filter to blank entries, while entering an underscore will filter to entries that are not blank.

Entering '!' operates as a negation. For example, entering '!F' in the DQI filter will return rows where the DQI does not contain 'F.'

Note: filtering executes differently in the WBS Tree mode, as described in Section 4.6.

## 4.4 Filtering on the VAR Column

To filter for all elements that do not have a VAR entry, enter a space in the VAR filter box. To filter for all elements that do have a VAR entry, enter an underscore in the VAR filter box. To display elements that have a VAR breach enters, c, S, C or V. Note that this filter is case-sensitive; "s" is not the same as "S." As with the DQI column, the filter normally combines any letters entered with an implicit AND.

That is, if the user enters ''sc", the Empower will show rows that have an ''s" and a ''c". The user can get the effect of an OR by adding a vertical bar between sections. For example, ''s|c" means ''s" OR ''c", and will return rows that contained either "s" OR "c."

Entering '!' operates as a negation for the entry that follows it. For example, entering "!c" in the DQI filter will return rows where the DQI does not contain "c."

## 4.5 Filtering on Color and Trend Columns

The three columns SV, CV, and VAC are called "Color and Trend Columns" for obvious reasons. To enter filter criteria, the user enters letter codes for the colors and trend arrows.

The color codes are based on the first letter of the color's name, as follows:

- "R": Red,
- "Y": Yellow,
- "G": Green,
- "B": Blue.

The trend arrow codes are:

- "U": Up,
- "D": Down,
- "F": Flat.

The user can enter a color, or a direction, or a color and a direction. It is important to note that if both color and direction are specified, they must be given in that order. For example, "Y" gives all the elements with yellow, "RD" gives all the elements with red and down arrows, "F" gives all the elements with flat or sideways arrows. Entering "DY" returns no rows because this combination violates the rule that the color code must be entered before the arrow code.

## 4.6 Filtering in WBS Tree Mode

Recall that in WBS Tree mode, the elements of a contract will be shown in a hierarchical format, with sub-elements indented below their parents. This difference in the way elements are displayed affects the operation of the interactive filters. To illustrate this, consider Figure 4.7 below. WBS Tree mode is turned off in the Sort Window (command Options > Show/Hide WBS Tree). As expected, only the rows with Smith in the CAM field are displayed.

**Figure 4.7: Filter CAM="Smith" Applied in Non-WBS Tree Mode**

Next we leave the filter as it was, and change the display to WBS Tree mode. The result is shown below in Figure 4.8. Note how element 1000 is shown, even though element 1000's CAM is Jones, not Smith. This is because when filtering in WBS Tree mode, the parents of elements selected by the filter are also shown, all the way up to the root of the tree.

**Figure 4.8: Filter CAM="Smith" Applied in WBS Tree Mode**
