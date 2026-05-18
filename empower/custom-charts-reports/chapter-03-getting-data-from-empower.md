# Chapter 3: Getting Data From Empower

*From TN-CustomChartsReports*

---

## Overview

We will begin with the first task, specifying the data. You specify the data you want in your report by supplying a JSON string. This string will usually contain both literal data and special codes, called placeholders, that tell Empower how to get the data you want from its database.

Custom charts and "new-style" custom reports can also retrieve data from Empower's database with one or more user-defined SQL statements, in addition to or instead of using placeholders. Fields returned by SQL statements can optionally be formatted and scaled on the server (as with placeholders) or returned directly from the database for processing on the client. (See the BAC by CAM report.)

## 3.1 Hard-coded Data

Some of the data you will use in your report probably won't come from the database, but will be hard-coded by you in the report.

Say your report will include a table with rows for various kinds of data, and you want labels for each row. You might provide labels for the data like this:

```javascript
var args = {
  'label': ['BCWS Cur', 'BCWP Cur', 'ACWP Cur', 'SV Cur', 'CV Cur']
};
```

This creates an array of labels which you can loop through as you build up the HTML for your table.

You also get for free some data that came from the database. All your reports will know about a variable called `extra`. Where did this come from? The answer is that Empower knew you would probably need it and threw it in automatically. Empower populates the variable `extra` and adds it to the beginning of custom reports written to the new standard (i.e., reports written according to the instructions in this Tech Note). This variable is added on the fly; it isn't actually written to the report text stored in the database.

The `extra` variable contains helpful information like the current unit, scale factor, text associated with the display scale, etc.

Here is a typical value for the `extra` variable, as it is populated by Empower and added to your report HTML:

```javascript
var extra = {
  "scale": {
    "unit": "Dollars",
    "sf": -3,
    "text": "Thousands",
    "us": 0,
    "dd": 1,
    "ds": 3
  },
  "title": "MOH -2 JAN 17 WBS Dollars [1000 : MOH -2]"
};
```

Some of this is obvious: the unit we are working with is Dollars and we have a pre-formatted string we can use as the subtitle for our report, giving the contract name, period, structure, unit, WBS number, and the element description.

The meanings of some of the other parts of the `extra` variable are as follows:

- `us` is Unit.Scale
- `dd` is ContrUnit.DisplayDecimal, i.e., the number of decimal places we have specified to display for this contract
- `ds` is ContrUnit.DisplayScale: 3 means we have chosen for this contract to display dollars in thousands; 0 would mean we want dollars in ones, etc. Since we want dollars in thousands, Empower has set the `text` variable with the appropriate string as well.
- `sf` indicates the difference between the scaling of the unit in the database and the scaling we want to display. In this case, we need to multiply the values from the database (dollars in ones) by 10^−3 to get the thousands of dollars we want to display.

We'll use the `extra.scale.unit` in some of the examples below.

## 3.2 Getting Data from the Database with Placeholders

You can specify the data you want to be read from the database and inserted in your report with placeholders that have this format:

```
(| token-1 | token-2 | ... | token-N |)
```

A placeholder can have just one token, or several.

The tokens can specify:

- What database tables and columns you want the data to be drawn from
- Which period you want
- Which element
- Which unit
- How you want the data formatted
- A loop to retrieve many data elements with a single statement
- Whether you want LOE or non-LOE data

Note that not all database tables can be accessed via placeholder syntax. Allowed tables are:

- EarnedValue
- Element
- Contract
- Period
- Cpr
- DqiPivot
- Gantt
- NarrStatus
- NarrName
- AiStatus
- NarrHistory

One way to find fields that you can use with placeholder syntax is to take a look at your "Columns" data download. For the Gantt table, note that the necessary Task ID to pull data will only be defined if you have the Gantt chart open, or if you specify it. TaskID can be specified with the `^` symbol.

It should be noted that fields like "ContrName" will use the SQL as defined in the "Columns" data download. For "ContrName" specifically, this means that if your contract has a Contract Alias set, the Alias will be returned, not the ContrName. For items like the "Who Charged" sample chart and report which rely on matching data between Empower and external data, the name or alias must be consistent between Empower and the external data. So if you are using a contract alias, your external data should as well. If you are not using a contract alias, your external data should use the contract name.

In all the placeholder examples, we will be using the MOH-2 sample contract, open with WBS Dollars in JAN 17. If you have that contract (unmodified), you should be able to reproduce the examples here and get the same outputs.

You can insert these placeholders directly in the JavaScript statements that create your formatted output, or you can insert them in a JSON string. Here is a simple example showing two placeholders (each with just one token) in a JavaScript statement:

```javascript
em.push('The current element is (| WbsNum |): (| ElemDesc |) ');
```

(The `em.push` statement is a JavaScript function call that just adds its argument to the string of HTML that will become our report.)

The placeholder `(|WbsNum|)` tells Empower to get the WBS number of the element currently selected in the Sort Window. Empower does a lot of work for you; Empower knows what the currently selected element is, and it knows that the WbsNum column is part of the Element table, so you don't need to supply this information; likewise for the ElemDesc. In the same way, Empower knows to find BcwpCum in the EarnedValue table. To get the correct record from that table, you need the current element, period, unit, and structure; Empower knows all those values and automatically uses them to get the right record for you. Later, we'll see that we can override some of those choices.

The output for the example above is:

```
The current element is 1000: MOH -2
```

In the next example we get a value from the database and add it to the report, along with the name of the current unit. Note that we get the name of the currently selected unit from the `extra` variable.

```javascript
em.push('BCWP for current element is (| BcwpCum |) ');
em.push(extra.scale.unit);
```

The output from these two lines will be:

```
BCWP for the current element is 6,853.0 Dollars
```

Next we show how we can format the data returned from the database. The element `[n5]` says to format the result as a number with 5 decimal places; the element `[c3]` says to format the result as a number with 3 decimal places and commas separating the thousands, etc. The key idea here is that tokens beginning with `[` are formatting tokens. The result of these two lines:

```javascript
em.push('BCWP for current element is (| BcwpCum |[n5]|) ');
em.push(extra.scale.unit);
em.push('BCWP for current element is (| BcwpCum |[c3]|) ');
em.push(extra.scale.unit);
```

will be:

```
BCWP for the current element is 6853.00000 Dollars
BCWP for the current element is 6,853.000 Dollars
```

There is another formatting token that starts with `z`, which formats numbers close to zero as exactly zero. A number with, say, the `[z5]` token will be formatted as 0 if it is between −0.001 and +0.001; otherwise it will be formatted as if the token was `[n5]`.

We can also ask for data in different units than those of the currently open dataset. In the fragment below we add the token `%Hours%`. This, naturally, means we want BCWP to be returned in Hours, where 'Hours' must be the name of a unit existing in the database. So tokens that begin with the percent sign specify the units we want the results in.

```javascript
em.push('BCWP for current element is (| BcwpCum |% Hours %|) Hours ');
```

The result is:

```
BCWP for current element is 82,234 Hours
```

What if we are interested in data from a different period? We can do that too. In the lines below, we use the token `(-1)`; this means to pick the BCWP value from one period before (−1 means "one before") the current period.

```javascript
em.push('BCWP for current element in the previous period was (| BcwpCum |(-1)|) ');
em.push(extra.scale.unit);
```

The result will be:

```
BCWP for current element in the previous period was 5,341.6 Dollars
```

We can get a value for a given element id, using the `$` token:

```javascript
em.push('BCWP for element ce=4 is (| BcwpCum|$4$|) ');
em.push(extra.scale.unit);
```

which gives:

```
BCWP for element ce=4 is 241.0 Dollars
```

This isn't very useful by itself, as you shouldn't know or care what the element ids are, and they will probably change anyway. But specifying a value by element id will be very useful in the context of looping, as we will explain later.

You can also get the indirect elements by their short names between the dollar signs, so these placeholders:

```javascript
em.push('Getting elements by name rather than ElemID:<p>');
em.push('BCWS (OH): (| BcwsCum|$OH$|)<p>');
em.push('BCWS (CM): (| BcwsCum|$CM$|)<p>');
em.push('BCWS (GA): (| BcwsCum|$GA$|)<p>');
em.push('BCWS (UB): (| BcwsCum|$UB$|)<p>');
em.push('BCWS (PM): (| BcwsCum|$PM$|)<p>');
em.push('BCWS (MR): (| BcwsCum|$MR$|)<p>');
```

will produce this output:

```
Getting elements by name rather than ElemID:
BCWS (OH): 0.0
BCWS (CM): 0.0
BCWS (GA): 662.0
BCWS (UB): 0.0
BCWS (PM): 7,278.6
BCWS (MR): 0.0
```

Note that the shorthand for "Cost of Money" is CM, not COM; G&A is GA; and PMB is PM. Furthermore, you don't write the square brackets as you would see in the Sort Window.

We can get a value for a given period id, using the `#` token:

```javascript
em.push('BCWP for current element in the previous period was (| BcwpCum |#9#|) ');
em.push(extra.scale.unit);
```

which gives:

```
BCWP for current element in the previous period was 5,341.6 Dollars
```

Once again, this isn't very useful on its own, but is very handy in looping contexts.

We said that, given a column name, Empower knows in which table that column is found, so you don't need to specify the table. There are some exceptions. For example, the field EndDate occurs in both the FutureEtc and Period tables. So Empower allows you to disambiguate the table. You do this by putting the table name as a token before the column name. For example, this code:

```javascript
em.push('Disambiguating fields:<p>');
em.push('Current Period End Date: (| Period|EndDate |)<p>');
em.push('(| FutureEtc|EndDate |(0) |{1}|) BCWS: (| FutureEtc|Bcws |(0) |{1}|) ETC: (| FutureEtc|Etc |(0) |{1}|) <p>');
em.push('(| FutureEtc|EndDate |(0) |{2}|) BCWS: (| FutureEtc|Bcws |(0) |{2}|) ETC: (| FutureEtc|Etc |(0) |{2}|) <p>');
em.push('(| FutureEtc|EndDate |(0) |{3}|) BCWS: (| FutureEtc|Bcws |(0) |{3}|) ETC: (| FutureEtc|Etc |(0) |{3}|) <p>');
```

produces this output:

```
Disambiguating fields:
Current Period End Date: JAN 17
FEB 17 BCWS: 1,261,400.0 ETC: 1,312,200
MAR 17 BCWS: 1,384,400.0 ETC: 1,439,900
APR 17 BCWS: 1,387,600.0 ETC: 1,439,900
```

We slipped another token in on you in this example, namely the `{` (curly bracket) token. This token is used with FutureEtc values to specify which future period you want for a given period. The tokens `|(0)|{1}|` mean the first future period for the current period, while the tokens `|(-1)|{3}|` mean the third future period from the period before the current period.

(We should note that in a real report you would normally do this sort of thing by looping over the future periods you want, instead of hard-coding the 1, 2 and 3, and you would display your results in a nice table, but here we are just focusing on the placeholders.)

Another token, the colon (`:`), is used for action views. We'll reserve discussion of it until we treat the SyncActionWnd looping construct.

A colon can also be used in placeholder syntax to indicate the NarrID for a NarrHistory item. For example, you might use the placeholder syntax `(|NarrHistory|LastUser|:178:|)` to add the "LastUser" from NarrID 178 to a VAR narrative.

To specify whether to filter the field for LOE or discrete (non-LOE) values, add `~L` or `~D` to the placeholder syntax for your field. This is mostly useful for data from non-lowest-level elements. For example, if we wanted to add an extra table to the VAR Narrative Report that breaks out total values by LOE/Non-LOE, we could use:

```html
<td class="tmpl tb">Total</td>
<td class="tmpl rar">(| BcwsCur |)</td>
<td class="tmpl rar">(| BcwpCur |)</td>
<td class="tmpl rar">(| SvCur |)</td>
<td class="tmpl rar">(| SvpCur |)</td>
<td class="tmpl rar">(| SpiCur |)</td>
</tr>
<tr>
<td class="tmpl tb">Non-LOE</td>
<td class="tmpl rar">(| BcwsCur~D|)</td>
<td class="tmpl rar">(| BcwpCur~D|)</td>
<td class="tmpl rar">(| SvCur~D|)</td>
<td class="tmpl rar">(| SvpCur~D|)</td>
<td class="tmpl rar">(| SpiCur~D|)</td>
</tr>
<tr>
<td class="tmpl tb">LOE</td>
<td class="tmpl rar">(| BcwsCur~L|)</td>
<td class="tmpl rar">(| BcwpCur~L|)</td>
<td class="tmpl rar">(| SvCur~L|)</td>
<td class="tmpl rar">(| SvpCur~L|)</td>
<td class="tmpl rar">(| SpiCur~L|)</td>
</tr>
```

Note that this is an excerpt of the table. For a full example of this VAR template please contact tech support for the sample file.

In Empower, the table will look something like this:

**Figure 3.1: LOE/non-LOE table**

### Token Summary

Here is a table summarizing the tokens we've discussed so far:

| Character | Meaning |
|-----------|---------|
| `[` | Format result: `cx` for commified numbers with x decimal places; `nx` for un-commified numbers with x decimal places; `z` means replace the value with 0 if the value is between −0.001 and 0.001, otherwise treat like `nx` |
| `(` | Period ordval |
| `$` | Element id |
| `{` | Which FutureEtc record to return (1st, 2nd, etc.) |
| `#` | Period id |
| `%` | Unit name or id |
| `:` | Action item key, or narrative ID when used with NarrHistory |
| `^` | Task id |
| `~L/D` | LOE/non-LOE filter |

Another placeholder that you might find useful is `(|Meta|User|)`; this placeholder turns into the name of the current user in Empower.

### 3.2.1 Getting Data with Meta|Value

The `Meta|Value` construct allows you to get a single value with a SQL statement. The general form is:

```
(|Meta|Value|<counter>|<sql-statement>|)
```

The `<sql-statement>` must return only one value (a singleton, in SQL jargon).

The `<counter>` is used so you can have multiple `Meta|Value` constructs in a report. You would increment the counter, starting at 0, for successive `Meta|Value` tags in your report.

For example, the fragment:

```javascript
var args = {
  'num_periods': (| Meta|Value |0| select count (*) from Period where ContrID=cc_id |),
  'num_wbs_elements': (| Meta|Value |1| select count (*) from Element where ContrID=cc_id and StruID =1|)
};
```

would, for the currently loaded contract, set `args.num_periods` to the number of periods and `args.num_wbs_elements` to the number of elements in the WBS structure. Note how we set the counter to 0, then to 1 for the two occurrences of `Meta|Value`.

### 3.2.2 Getting Data with Loops

Empower provides powerful looping constructs that allow you to retrieve a large amount of structured data with a compact notation. All of these looping constructs begin with `(|Meta|BeginLoop|...` as the first two tokens.

#### 3.2.2.1 Looping: SyncSortWnd

This loop form loops through all the elements in the Sort Window. The general form is:

```
(|Meta|BeginLoop|ce|SyncSortWnd|)
loop body
(|Meta|EndLoop|ce|)
```

Below is an example that retrieves the WBS number and BCWP, in both Dollars and Hours, for each element in the Sort Window. In the example, `ce` is the loop variable, and it is used in the body of the loop in a `$` token to specify for which element Empower should be retrieving the BcwpCum value on each trip through the loop.

```javascript
(| Meta|BeginLoop|ce|SyncSortWnd |)
{
  'wbs': '(|WbsNum|$ce$ |)',
  'bcwp_dollars': '(| BcwpCum|$ce$ |% Dollars %|[n5]|)',
  'bcwp_hours': '(| BcwpCum|$ce$ |% Hours %|[n2]|)'
},
(| Meta|EndLoop|ce|)
```

The result begins like this:

```
1000, 6853.00000, 82234.00
2000, 869.40000, 10630.50
2100, 282.60000, 3211.40
```

#### 3.2.2.2 Looping: SyncActionWnd

This loop form was particularly designed to loop through all the action items in an action view, though it works with normal views as well. As explained in the User's Manual, the difference between a normal view and an action view is that in a normal view, the WBS (or OBS, etc.) number is unique, while in an action view, the combination of WBS number plus the item number plus the revision number is unique. The loop variable in the SyncActionWnd construct takes care of that detail for you.

The general form is:

```
(|Meta|BeginLoop|ai|SyncActionWnd|)
loop body
(|Meta|EndLoop|ai|)
```

Below is an example that gets the WBS number, revision number, and item title for all the action items in the current view. In the example output, you'll see, among other things, two different action items for 3200 ("Another Action Item" and "Review schedule 3200 to remove negative float"), and two revisions to the action item for 3300 (revisions 0 and 1).

This construct iterates through the loop variable `ai`. We use the token `:` to tell Empower to work its magic to expand the single variable `ai` to all the appropriate combinations of WBS element id, action number, and action revision.

```javascript
(| Meta|BeginLoop|ai|SyncActionWnd |)
{
  'wbs': '(| AiStatus|WbsNum |:ai:|)',
  'rev': '(|RevNum |:ai:|)',
  'title': '(| ItemTitle |:ai:|)'
},
(| Meta|EndLoop|ai|)
```

With a little formatting, the returned data looks like this:

```
1000, 0, Review Overhead rates with CFO
3200, 0, Review schedule 3200 to remove negative float
3200, 0, Another Action Item
3200, 1, Review schedule 3200 to remove negative float
3300, 1, Review budget and EAC to address new scope
3300, 0, Review budget and EAC to address new scope
3600, 2, Review Labor cost and future ETC
3600, 0, Review Labor cost and future ETC
3600, 1, Review Labor cost and future ETC
3700, 0, Determine why discrete account has no schedule tasks
```

#### 3.2.2.3 Looping: PerOrd

The PerOrd loop is used for looping over period OrdVals. The loop variable runs between the two values provided as `<left>` and `<right>` in the general form below:

```
(|Meta|BeginLoop|<loopvar>|PerOrd|<left>|<right>|)
loop body
(|Meta|EndLoop|<loopvar>|)
```

Example:

```javascript
(| Meta|BeginLoop|ord|PerOrd |5|0|)
[
  "(| EndDate |(-ord)|)",
  (| BcwsCum |(-ord)|[n5]|),
  (| BcwpCum |(-ord)|[n5]|),
  (| AcwpCum |(-ord)|[n5]|),
],
(| Meta|EndLoop|ord|)
```

This example loops through six periods, with the loop variable `ord` taking on the values 5, 4, 3, 2, 1, and 0, in that order. On each trip through the loop, it will retrieve values for the current period minus 5, on the next, the current period minus 4, and so on.

The following snippet of JavaScript code would step through the resulting data, printing one period's worth per line:

```javascript
var arr, i, j;
arr = args.ex_perord;
em.push(arr + '<p>');
for (i=0; i<arr.length; i++) {
  for (j=0; j<4; j++) {
    em.push(arr[i][j] + ', ');
  }
  em.push('<p>');
}
```

and the output would be:

```
AUG 16, 1415, 1376, 1485,
SEP 16, 2231, 2216, 2191,
OCT 16, 2517, 2742, 3027,
NOV 16, 4194, 3784, 4247,
DEC 16, 5633.2, 5341.6, 5642.8,
JAN 17, 7278.6, 6853, 7349.8,
```

If you reversed the loop limits as follows: `(|Meta|BeginLoop|ord|PerOrd|0|5|)`, the `ord` loop counter would run from 5 down to 0, and the output would be in reverse order, starting with the JAN 17 values and ending with AUG 16.

#### 3.2.2.4 Looping: IDSelect

In this type of loop, you supply a SQL statement that will return a list of the ids to be used as values for the loop variable.

The general form is:

```
(|Meta|BeginLoop|<loopvar>|IDSelect|<sql-statement>|)
loop body
(|Meta|EndLoop|<loopvar>|)
```

Example:

```javascript
(| Meta|BeginLoop|ce|IDSelect|select ElemID from Element where ProjOff='Price '|)
'(| WbsNum|$ce$ |)',
(| Meta|EndLoop|ce|)
```

In this example, the SQL statement returns a list of element IDs from elements where 'Price' is the project officer, and these element IDs are used to get the WBS numbers of the corresponding elements.

Here is a more involved example that also demonstrates the use of the `{` token.

```javascript
(| Meta|BeginLoop|ord|PerOrd |1|6|)
[
  '(| FutureEtc|EndDate |(0) |{ord }|)',
  '(| FutureEtc|Bcws |(0) |{ord }|)',
  '(| FutureEtc|Etc |(0) |{ord }|)',
],
(| Meta|EndLoop|ord|)
```

In this placeholder, the `(0)` tokens mean we want the FutureEtc records corresponding to the current period, while the `{ord}` token, combined with the loop from 1 to 6, means we want the first FutureEtc record from the current period, the second FutureEtc record from the current period, and so on.

When run with MOH-2, the resulting values are:

```
FEB 17, 1,261.4, 1,312.2
MAR 17, 1,384.4, 1,439.9
APR 17, 1,387.6, 1,439.9
MAY 17, 1,198.3, 1,243.5
JUN 17, 1,135.4, 1,178.1
JUL 17, 1,115.6, 1,158.7
```

Note that the first row of data corresponds to the first future period, and so on.

#### 3.2.2.5 Looping: OrdSelect

In this loop construct, the loop values are again the result of an SQL statement, but the loop variable is an ordinal value (examples: PerOrd for the CalendarDet table and OrdVal for the Period table).

```
(|Meta|BeginLoop|<loopvar>|OrdSelect|<sql-statement>|)
loop body
(|Meta|EndLoop|<loopvar>|)
```

The SQL statement should return a number; the loop variable will run from 0 to that number minus 1.

(The OrdSelectEx loop construct gives us more flexibility, allowing us to start at something other than 0, or to run through the numbers backwards, or both.)

In the following examples, it might be helpful to have the values in the Period table for MOH-2 before us for reference:

| periodid | ordval | enddate    |
|----------|--------|------------|
| 1        | 10     | 2016-04-30 |
| 2        | 9      | 2016-05-31 |
| 3        | 8      | 2016-06-30 |
| 4        | 7      | 2016-07-31 |
| 5        | 6      | 2016-08-31 |
| 6        | 5      | 2016-09-30 |
| 7        | 4      | 2016-10-31 |
| 8        | 3      | 2016-11-30 |
| 9        | 2      | 2016-12-31 |
| 10       | 1      | 2017-01-31 |

As an example, this code with the MOH-2 contract:

```javascript
(| Meta|BeginLoop|ord|OrdSelect|select count (*) from Period where ContrID=cc_id |)
'(| EndDate |(-ord)|) ',
(| Meta|EndLoop|ord|)
```

will result in the following data:

```
JAN 17, DEC 16, NOV 16, OCT 16, SEP 16, AUG 16, JUL 16, JUN 16, MAY 16, APR 16
```

The SQL statement returns 10 (the number of periods in the contract); the loop variable (`ord` in this case) therefore runs from 0 to 9. The `ord` of 0 gives the JAN 17 period (since zero periods back from JAN 17 is JAN 17), `ord = 1` gives the DEC 16 period, and so on.

#### 3.2.2.6 Looping: OrdSelectEx

This variation on the OrdSelect loop allows you to specify an offset and a direction for the loop variable. The general form is:

```
(|Meta|BeginLoop|<loopvar>|OrdSelectEx|<offset>|<dir>|<sql-statement>|)
loop body
(|Meta|EndLoop|<loopvar>|)
```

If the `<dir>` value is positive, the loop moves forward through the values returned by the SQL statement; if negative, the loop moves backward.

In this example, we use an offset of 2, and choose to move forward (the positive 1 – all that matters is that the value is positive). The SQL statement still returns 10 (in our example), but with an offset of 2, the loop variable will run from 2 to 11 (instead of 0 to 9).

```javascript
(| Meta|BeginLoop|ord|OrdSelectEx |2|1| select count (*) from Period where ContrID=cc_id |)
'(| EndDate |(-ord)|) ',
(| Meta|EndLoop|ord|)
```

Here is the result:

```
NOV 16, OCT 16, SEP 16, AUG 16, JUL 16, JUN 16, MAY 16, APR 16, ,
```

Note the two commas at the end. This is because there are no periods for MOH-2 corresponding to 10 and 11 periods back from the current period. The list of values therefore contains two values at the end with blanks. We will see later how to deal with this situation.

Now here is an example of an offset and moving backwards through the loop variable:

```javascript
(| Meta|BeginLoop|ord|OrdSelectEx |3| -1| select count (*) from Period where ContrID=cc_id |)
'(| EndDate |(-ord)|) ',
(| Meta|EndLoop|ord|)
```

Again, the SQL statement returns 10, but since we asked to move backwards and use an offset of 3, the loop values will run from 12 to 3. There are no periods 12, 11, or 10 periods back from the current period, so those values will be returned as blanks, and since we are moving backwards, the blanks occur at the beginning of the list of periods, as the results show:

```
, , ,APR 16, MAY 16, JUN 16, JUL 16, AUG 16, SEP 16, OCT 16
```

## 3.3 User-Defined SQL

SQL is specified by adding a `sql` array to the chart or report template. Any legal SQL select statement (against the Empower database) is allowed. Inserts, updates and deletes are ignored and return an empty array. The report or chart writer should pay whatever attention he or she deems appropriate to the differences in SQL dialects among databases. (Our samples work with Postgres, Oracle and SQL Server.)

As with placeholder loop syntax, `cc_id`, `ce_id`, `cd_id`, `st_id` and `un_id` substitutions can be used (ids of current contract, element, period, structure and unit.)

Additionally, the `cc_ids` substitution can be used for custom charts and reports that should be able to use data from multiple contracts at a time. `cc_ids` contains a comma-separated list of the contract IDs for the current dataset (one, multiple, or all contracts). For this substitution, your SQL condition would look something like `ContrID in (cc_ids)`. Note that you should supply the parentheses around `cc_ids`.

The `ord_id` substitution allows you to use SQL conditions with "OrdVal". This can be useful when designing charts or reports for cross-contract data since you can use OrdVal as your constraint for Period data instead of "PeriodID". Note that "OrdVal = 1" is used for the most recent period of data for each contract, "2" would be the next most recent, etc. For example, to pull data from the prior period to your currently open dataset, you would use something like `Period.OrdVal-1 = ord_id` in your SQL query. When using datasets with shared calendars, custom SQL queries will be automatically updated to use "Period.EndDate" instead of OrdVal since the `ord_id` value will be an EndDate. Keep this substitution in mind if you plan to make your custom item available for datasets that use shared calendars and note that best practice is to include the "Period" table in your custom SQL joins when using this substitution.

When using custom SQL, the `ct_id` substitution is also available. This substitution allows you to use the currently selected TaskID as a SQL constraint in your custom report. Note that in order to have a currently selected TaskID, the Gantt chart must be open. When building a report that uses TaskID in the SQL, we would recommend having some sort of default text that will return should the report be opened when the Gantt chart has not been opened. (e.g. return text that indicates that no task has been selected) When the Gantt chart is opened, a default task will be selected. The current task can then be changed by clicking on a different row of the Gantt chart.

As an example of how you might use user defined SQL, consider the BAC by CAM chart. The unpopulated template is

```javascript
var args = {
  "type": "chart",
  "title": "BAC by CAM",
  "L1": "1",
  "dataset": "(| ContrName |) (| EndDate |) (| Structure|StruName |) (| Unit|UnitName |)",
  "sql": [
    "select ProjOff, sum(Bac) from EarnedValue inner join Element on Element.ElemID = EarnedValue.ElemID inner join Contract on Contract.ContrID = Element.ContrID where ElemType = CaSym and StruID = st_id and PeriodID = cd_id and UnitID = un_id group by ProjOff"
  ],
  "cols": ["CAM", "BAC"]
};
```

(Note the mix of custom SQL and placeholder syntax.) The populated template will look something like this:

```javascript
var args = {
  "type": "chart",
  "cols": ["CAM", "BAC"],
  "dataset": "MOH -2 JAN 17 WBS Dollars",
  "L1": "1",
  "title": "BAC by CAM",
  "sql": [
    [
      ["Brown", "1384600.00000"],
      ["Hall", "127000.00000"],
      ["Smith", "14606400.00000"],
      ["Wayne", "1633000.00000"]
    ]
  ]
};
```

Compare the sql entry in the unpopulated template to the same entry in the populated JSON. You'll see that the SQL in the sql statement has been replaced by the result set of the query. If multiple SQL statements are specified, each is replaced by its individual result set.

Next, consider the BAC by CAM sample report. (NB: report, not chart.)

```javascript
var args = {
  "type": "report",
  "title": "BAC by CAM",
  "L1": "1",
  "dataset": "(| ContrName |) (| EndDate |) (| Structure|StruName |) (| Unit|UnitName |)",
  "header": "This report displays total BAC and key performance indicators by CAM.",
  "sql": [
    {
      "query": "select coalesce(ProjOff, ''), sum(Bac), case when sum(BcwsCum) <> 0 then sum(BcwpCum)/sum(BcwsCum) else 0 end from EarnedValue inner join Element on Element.ElemID = EarnedValue.ElemID inner join Period on Period.PeriodID = EarnedValue.PeriodID inner join Contract on Contract.ContrID = Element.ContrID where ElemType = CaSym and StruID in (st_id, 3) and Period.PeriodID = cd_id and UnitID = un_id group by ProjOff order by ProjOff",
      "format": ["", "cdd", "n3"],
      "scale": ["", "ds", ""]
    }
  ],
  "cols": ["CAM", "BAC", "SPI"],
  "align": ["l", "r", "r"]
};
```

You'll see that the sql array is not composed of simple strings as before, but of objects having the form:

```javascript
{
  "query": "<query string>",
  "format": [<array of strings>],
  "scale": [<array of strings>],
}
```

`format` and `scale` are optional (though there's no point in using this form unless at least one of them is present.) There should be an entry in the `format` and/or `scale` array for each field in the associated SQL statement.

For `format`, valid values are:

- `""` – for strings and integer values, no formatting applied
- `"fmt"` – for dates, use the default date format (as specified by the current calendar)
- `"<date format>"` – for dates, use the specified date format (e.g., `"!%b %Y"`)
- `"c<n>"` – for numbers, a comma-separated value with n decimal places (e.g., `"c1"`)
- `"n<n>"` – for numbers, a non-comma-separated value with n decimal places (e.g., `"n0"`)

In place of `<n>`, `dd` can be used, indicating the DisplayDecimal value for current contract and unit should be used (e.g., `"cdd"`).

For `scale`, valid values are:

- `""` – for non-numeric values, or when no scaling should be applied
- `"ds"` – for numeric values, use the DisplayScale value for the current contract and unit
- `"<n>"` – for numeric values scale to 10^n, e.g. `"3"` indicates that number should be displayed in thousands

**Note:** The preposition matters – scale *to*, not scale *by*. For example, if a number is stored in thousands, it will be returned without change for `scale = "3"`, and multiplied by 1000 for `scale = "0"`. On the other hand, if it is stored in ones, it will be divided by 1000 for `scale = "3"` and returned unchanged for `scale = "0"`.

### 3.3.1 Syncing

When using user-supplied SQL, you can specify an option, `"sync":true`, to indicate that the server should filter and sort returned rows to match the current state of the sort window. (Experiment with the Banded EOC report to see this in action.) To indicate that it should be synced, a SQL statement must include an ElemID column in the first position.

Depending on the demands of the query, it can be `Element.ElemID`, `e.ElemID`, just `ElemID`, whatever is necessary, but it must immediately follow the select keyword. The ElemID field will be returned with the rest of the columns specified (and so should have an entry in `scale` and/or `format`, if used) but the field will usually not be displayed.

For sites hosting Empower on a Windows machine, you may encounter a Windows specific bug with the JSON::XS Perl module related to encoding true/false values. The workaround for this issue is to use `"1"` instead of `true` for the `"sync"` entry.

For example: `"sync": "1"`

When syncing, care should be taken to ensure that the SQL returns all rows of potential interest, to give the user something on which to filter. So, for example:

```sql
select ElemID, WbsNum from Element where ElemID = ce_id
```

would be a poor candidate for syncing, since only one row will be returned in any case.

On the other hand:

```sql
select ElemID, WbsNum from Element where StruID in (st_id, 3) and ContrID = cc_id
```

would allow the user to sync within the current contract and structure, and:

```sql
select ElemID, WbsNum from Element where StruID in (st_id, 3)
```

would allow the user to sync across contracts in the current structure.

Similarly, a where clause like:

```sql
where PeriodID = cd_id and UnitID = un_id
```

would restrict a user to the current period (and hence, contract) while:

```sql
where OrdVal = (select OrdVal from Period where PeriodID = cd_id) and UnitID = un_id
```

would allow the user to sync within a cross-contract dataset, where PeriodIDs will be different but OrdVals the same. This is a useful idiom for cross-contract queries that retrieve period-dependent data.
