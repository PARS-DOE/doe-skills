# CustomReports additions

*Source: CustomReports_additions.pdf*

---

## What's New

This note provides preliminary documentation of new custom chart and report capabilities available in Empower 3.6.2.53 and later.

- Custom charts can now be generated in an manner analagous to "new-style" custom reports. Where custom reports define an anonymous function that returns HTML in the format expected by Empower's Report pane, custom charts define an anonymous function that returns a JSON object in the format expected by Empower's Chart pane. (Ref BAC by CAM chart, Target Price vs. Forecast chart.)

- Custom charts and "new-style" custom reports can now retrive data from Empower's database with one or more user-defined SQL statements, in addition to or instead of using placeholders. Fields returned by SQL statements can optionally be formatted and scaled on the server (as with placeholders) or returned directly from the database for processing on the client. (Ref BAC by CAM report.)

- Adaptive Touch (AT) charts are now supported, in addition to AT reports. (As with AT reports, the intended use is to combine data from Empower with data from other sources.) User-defined SQL is available to both AT charts and AT reports. Just as an AT report directly returns HTML as expected by Empower's Report pane, so an AT chart directly returns JSON as expected by Empower's Chart pane. (Ref Who Charged chart.)

- An optional parameter, 'sync', if set to true, tells Empower to filter and sort the data returned by the SQL statements to match the state of the sort window. (Ref Banded EOC report.)

- In Empower 3.6.3.54 and later it is possible to make asynchronous calls to local or remote web services from the Javascript that defines a custom chart or report. This provides Adaptive Touch capabilities to custom client-side charts and reports, but uses existing web services and allows the chart or report itself to be defined entirely on the client side.

## Testing with JSFiddle

Follow the steps below to set up a JSFiddle page for experimenting with custom charts and reports.

1. Navigate to https://jsfiddle.net

2. Click External Resources

3. Where you see JavaScript/CSS URI, enter https://dev.encore-analytics.com/dev-empower/chrp-min.js, click +, then click the newly added link chrp-min.js. You should see the contents of chrp-min.js (which won't be pretty.)

4. Repeat for https://dev.encore-analytics.com/dev-empower/report-min.css and https://code.highcharts.com/highcharts.js and verify the links.

5. In the top left pane, enter `<div id="container"></div>`

6. In the bottom left pane, enter:

```javascript
if(0) {
Highcharts.chart("container", options);
} else if (args.type === "chart") {
Highcharts.chart("container", test());
} else {
document.getElementById("container").innerHTML =
test();
}
```

7. In Empower, open the Options > Show Raw Data window, then the BAC by CAM custom chart.

8. Copy the entire line beginning `var extra =` from the raw data window and paste it into the bottom left pane of the jsfiddle page, above the code block you just entered.

9. Convert the anonymous function to a named function, test:
   - At the beginning of the anonymous function, change `(function()` to `function test()`.
   - At the end of the anonymous function, delete the trailing parenthesis and semicolon `)();`.

10. Click the Run toolbar button. The chart should display. If it does not, open the debug console and look for errors.

11. Save the fiddle and bookmark it for future use.

The above procedure should work for any "new-style" custom report or chart. For an AT chart, the procedure is slightly different. For example:

1. In Empower, open the Options > Show Raw Data window, then the Who Charged custom chart.

2. Copy the entire line beginning with `{` from the raw data windows and paste it into the bottom left page of the jsfiddle page. (Replace any existing code, except the code block at the bottom.)

3. Click Tidy. (Note the absence of an anonymous function; this is the defining characteristic of AT-style charts and reports.)

4. At the top of the page, enter `var options =` in front of the opening brace, `{`.

5. Change `if(0)` to `if(1)` in the first line of the code block at bottom.

6. (Optional) Enter a semicolon after the closing brace, `}`.

7. Click Run. The chart should display.

## New-Style Custom Charts

A "new-style" custom chart uses an anonymous JavaScript function to create and return a JSON object in the format expected by Empower's Chart pane. That format, in turn, is defined by the Highcharts charting tool that Empower uses, see https://highcharts.com/demo for many examples.

Consider the Target Price vs. Forecasts sample. (Download the chart definition using File > Export User Items.) The first section, beginning `var args = {` defines a JSON structure that should be familar from writing custom reports. The first entry, `"type":"chart"`, identifies this as a chart. (If omitted, the object is treated as a report.) NB: Notice the consistent use of double-quotes around the text elements in the JSON. This is required for chart and reports containing user-defined SQL (due to an intermediate JSON-decode now in the mix) and should be adopted as a best-practice for all future charts and reports.

The remainder of the JSON uses placeholder syntax to gather data for the chart, and should look familiar. The second section, the anonymous JavaScript function, takes the data and populates and returns the options object. The details of the options object are defined by Highcharts according to chart type, and are best learned by (js)fiddling with their demos.

Next, consider the BAC by CAM sample chart. (Again, download with File > Export User Items.) Again, you see the `"type":"chart"` entry. The L1 entry is used as a flag to select (or not) a title that doesn't change unless a new dataset is selected. In the function, notice the different character of the options object returned, reflecting differences between line and pie charts.

## User-Defined SQL

SQL is specifed by adding a sql array to the chart or report template. Any legal SQL select statement (against the Empower database) is allowed. Inserts, updates and deletes are ignored and return an empty array. The report or chart writer should pay whatever attention he or she deems appropriate to the differences in SQL dialects among databases. (Our samples work with Postgres, Oracle and SQL Server.) As with placeholder loop syntax, `cc_id`, `ce_id`, `cd_id`, `st_id` and `un_id` substitutions can be used (ids of current contract, element, period, structure and unit.)

For example, consider the BAC by CAM chart. The unpopulated template is:

```javascript
var args = {
"type": "chart",
"title": "BAC by CAM",
"L1": true,
"dataset" : "(|ContrName|) (|EndDate|)
(|Structure|StruName|) (|Unit|UnitName|)",
"sql" : [
"select ProjOff, sum(Bac) from EarnedValue
inner join Element on Element.ElemID =
EarnedValue.ElemID inner join Contract on
Contract.ContrID = Element.ContrID where
ElemType = CaSym and StruID = st_id and
PeriodID = cd_id and UnitID = un_id group by
ProjOff"
],
"cols": ["CAM", "BAC"]
};
```

(Note the mix of custom SQL and placeholder syntax.) The populated template will look something like this:

```javascript
var args = {
"type": "chart",
"cols": ["CAM", "BAC"],
"dataset": "MOH-2 JAN 17 WBS Dollars",
"L1": true,
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
"L1": true,
"dataset" : "(|ContrName|) (|EndDate|)
(|Structure|StruName|) (|Unit|UnitName|)",
"header": "This report displays total BAC and key
performance indicators by CAM.",
"sql" : [
{
"query": "select coalesce(ProjOff, ''),
sum(Bac), case when sum(BcwsCum) <> 0 then
sum(BcwpCum)/sum(BcwsCum) else 0 end from
EarnedValue inner join Element on
Element.ElemID = EarnedValue.ElemID inner
join Period on Period.PeriodID =
EarnedValue.PeriodID inner join Contract on
Contract.ContrID = Element.ContrID where
ElemType = CaSym and StruID in (st_id, 3) and
Period.PeriodID = cd_id and UnitID = un_id
group by ProjOff order by ProjOff",
"format": ["", "cdd", "n3"],
"scale": ["", "ds", ""]
}
],
"cols": ["CAM", "BAC", "SPI"],
"align": ["l", "r", "r"],
};
```

You'll see that the sql array is not composed of simple strings as before, but of objects having the form:

```javascript
{
"query" : "<query string>",
"format" : [<array of strings>],
"scale" : [<array of strings>],
}
```

`format` and `scale` are optional (though there's no point in using this form unless at least one of them is present.) There should be an entry in the format and/or scale array for each field in the associated SQL statement.

For format, valid values are:

- `""` – for strings and integer values, no formatting applied.
- `"fmt"` – for dates, use the default date format (as specified by the current calendar)
- `"<date format>"` – for dates, use the specified date format (e.g., `"!%b %Y"`).
- `"c<n>"` – for numbers, a comma-separated value with n decimal places (e.g., `"c1"`).
- `"n<n>"` – for numbers, a non-comma-separated value with n decimal places (e.g., `"n0"`).

In place of `<n>`, `dd` can be used, indicating the DisplayDecimal value for current contract and unit should be used (e.g., `"cdd"`).

For scale, valid values are:

- `""` – for non-numeric values, or when no scaling should be applied.
- `"ds"` – for numeric values, use the DisplayScale value for the current contract and unit.
- `"<n>"` – for numeric values scale to 10^n, e.g. `"3"` indicates that number should be displayed in thousands.

NB: The preposition matters – scale to, not scale by. For example, if a number is stored in thousands, it will be returned without change for `scale = "3"`, and multiplied by 1000 for `scale = "0"`. On the other hand, if it is stored in ones, it will be divided by 1000 for `scale = "3"` and returned unchanged for `scale = "0"`.

## Syncing

When using user-supplied SQL, you can specify an option, `"sync":true`, to indicate that the server should filter and sort returned rows to match the current state of the sort window. (Experiment with the Banded EOC report to see this in action.) To indicate that it should be synced, a SQL statment must include an ElemID column in the first position. Depending on the demands of the query, it can be `Element.ElemID`, `e.ElemID`, just `ElemID`, whatever is necessary, but it must immediately follow the select keyword. The ElemID field will be returned with the rest of the columns specified (and so should have an entry in scale and/or format, if used) but the field will usually not be displayed.

When syncing, care should be taken to ensure that the SQL returns all rows of potential interest, to give the user something on which to filter. So, for example,

```sql
select ElemID, WbsNum from Element where ElemID = ce_id
```

would be a poor candidate for syncing, since only one row will be returned in any case. On the other hand

```sql
select ElemID, WbsNum from Element where StruID in (st_id, 3) and ContrID = cc_id
```

would allow the user to sync within the current contract and structure, and

```sql
select ElemID, WbsNum from Element where StruID in (st_id, 3)
```

would allow the user to sync across contracts in the current structure.

Similarly, a where clause like

```sql
where PeriodID = cd_id and UnitID = un_id
```

would restrict a user to the current period (and hence, contract) while

```sql
where OrdVal = (select OrdVal from Period where PeriodID = cd_id)
and UnitID = un_id
```

would allow the user to sync within a cross-contract dataset, where PeriodIDs will be different but OrdVals the same. This is a useful idiom for cross-contract queries that retrieve period-dependent data.

## Asynchronous Calls to Web Services

To make an asynchronous call to a local or remote web service, include code like the following somewhere in the anonymous function defining your custom chart or report.

```javascript
if( extra.lines ) {
lines = extra.lines;
}
else {
var svc =
'https://dev.encore-analytics.com/dev-empower/vcd.cgi',
s = svc + encodeURIComponent('?projectName=' +
args.cc + '&WBS=' + args.ce);
var ret = {
"url" : s,
"name" : "lines"
};
return JSON.stringify(ret);
}
```

The code checks first for the existence of a specified object in the default extra object. If not found, the code returns a JSON object defining a call to a local or remote web service (with any necessary parameters), and a name to be assigned to the data returned from the service (in this case, `'lines'`). Empower will call the service and inject the result into the extra object under the name provided. Note that the anonymous function is called (at least) twice. On the first call, the named object will be undefined, signally the code to return a request for the object; on the next call, that object will be available for use. Some other things to note:

- Multiple service calls may be made by assigning their results to different names. The report or chart Javascript code would simply keep returning service requests to Empower until all the required data had been gathered, before finally returning the report HTML or chart JSON as usual.

- The remote service should return data in a text-based format such as JSON, XML, HTML, or plain text. If the returned text is not a JSON string, it will be stored line-by-line in a JSON array.

- Remote services should support Cross-Origin Resource Sharing. See https://enable-cors.org for details.

- Remote services should allow anonymous access, or be configured to allow access to the service account under which Empower is running.

The Who Charged AT sample chart and report have also been implemented using client-side call to a remote web service as discussed here, and are available on request or from Empower's Freshdesk support portal.

## Sample Notes

- The Banded EOC report is an example using multiple queries. The first query gets EOC units, the second gets Element information, the third gets the associated EV data. Lookup tables are built in memory in the Javascript code to tie everything together.

- The BAC by CAM report is intended to be reused – results from any query can be presented in tabular form by modifying the args object alone; the JavaScript should work without change.

- The Cross-Contract Sample report was created in just this way. It illustrates some of the subtleties of cross-contract reports and provides a good template for experimenting with formatting numbers and dates. It also shows what happens to a delete query (in a word, nothing), though you'll need to fiddle to see this. For best results, at least one contract in your database should have different `Contract.DateFmt`, `ContrUnit.DisplayScale`, and `ContrUnit.DisplayDecimal` values than the rest.

- The BAC by CAM chart and Target Price vs. Forecasts are examples of pie and line charts, respectively. Note that both make a call to `scale_chart_data()`, a function defined in `chrp-min.js` that scales data the way our built-in charts do. The interested user can view this file by clicking the link created to it in JSFiddle. (A JavaScript beautifier will help, e.g. http://jsbeautifier.org). Of course, any function defined in `chrp-min.js` is available for use in user-defined custom charts and reports.

- When table names are required, the SQL in the samples use full table names with capitalization matching the Empower schema, and avoid the SQL-standard using construct for join. For example, the samples will use:

```sql
select Element.ElemID, Bac from EarnedValue inner join
Element on Element.ElemID = EarnedValue.ElemID where
Element.ElemID = ce_id
```

rather than

```sql
select e.ElemID, Bac from EarnedValue ev inner join
Element e on e.ElemID = ev.ElemID where e.ElemID = ce_id
```

or

```sql
select ElemID, Bac from EarnedValue inner join Element
using (ElemID) where ElemID = ce_id
```

- the samples avoid using because SQL Server does not support it;
- samples follow the capitalization used in the Empower schema to prevent errors in SQL Server databases created with a case-sensitive collation
- samples provide full table names to allow SQL from the Column table to be inserted without change.
