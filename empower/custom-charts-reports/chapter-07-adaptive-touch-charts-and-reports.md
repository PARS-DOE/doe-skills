# Chapter 7: Adaptive Touch Charts and Reports

*From TN-CustomChartsReports*

---

## Overview

Adaptive Touch (AT) charts are supported in Empower, in addition to AT reports. As with AT reports, the intended use of AT charts is to combine data from Empower with data from other sources. User-defined SQL is available to both AT charts and AT reports. Just as an AT report directly returns HTML as expected by Empower's Report pane, an AT chart directly returns JSON as expected by Empower's Chart pane. For an example of an AT chart, see the Who Charged chart.

In order to accommodate restrictions at some sites, AT charts and reports are NOT enabled by default when installing Empower. If allowed at your site, you can enable AT charts and reports by creating a cgi directory in your Empower home directory (C:\encore-analytics\empower in the default Windows installation), then copying the contents of the empower/setup/at/cgi folder into the empower/cgi folder that you just created. The files will include sample AT chart and report. After the cgi folder is in place, you will still need to import a chart and/or report useritem into Empower before you will be able to see the chart/report in Empower. Later sections will describe this useritem in more detail.

AT charts and reports use a server-side file to generate either a valid JSON string (for charts) or standard HTML (for reports). Any server-side language can be used, as long as it follows CGI protocol. In our examples, we will use Perl.

Data used in AT charts and reports can come from any source, as long as it can be accessed from your Empower application server. External data can be accessed in different ways, including parsing a .txt file or querying a (non-Empower) database.

## 7.1 AT Chart Example

AT charts must return a valid JSON string that can be accepted by Empower's chart plugin. When developing your own AT Charts, JSONLint.com can be a useful tool for checking the validity of your JSON string.

The "Who Charged" chart is a bar chart showing the hours charted by different resources for an element over the periods of a contract. For this chart, we will use external data from a .txt file, so this is an AT chart.

**Figure 7.1: Who Charged Chart**

For this chart we will need three files:

- A .txt file containing the external data
- A .txt file containing the information that Empower will need to create the chart, such as the location and name of the script that will return the JSON string
- A .cgi file containing our Perl script that will generate a JSON string

The .txt file containing our external data is a tab-delimited file with these fields:

- **Contract**: the contract name in Empower
- **WBS**: the WBS number in the contract
- **Name**: Who or What charged
- **ID**: a unique ID assigned to each name. This field could be omitted if Name is unique
- **Date**: the period end date of the charge
- **Hours**: the actual hours charged in the period

Some fields, such as "Contract" and "Date" will be used to tie the external data to data from Empower.

**Figure 7.2: External Data File**

Next, we will need a plain text file containing information defining the chart. This file will be imported into Empower on the client side with "File > Import User Items" and can be used to tell Empower which file contains the code to generate the JSON string for the chart as well as to specify any data that we want to use from the Empower database.

```json
{
  "type": "chart",
  "title": "Who Charged",
  "url": "ch_getcharge.cgi",
  "input": "Who-Charged",
  "contr": "(| ContrName |)",
  "stru": "(| Structure|StruName |)",
  "wbs": "(| WbsNum |)",
  "date": "(| EndDate |[%Y-%m-%d]|)",
  "dmap": {
    "(|Meta|BeginLoop|cd|IDSelect|select PeriodID from Period where ContrID = cc_id order by OrdVal desc |)":
    "(| EndDate |[%Y-%m-%d]|#cd#|): (| EndDate |#cd#|)",
    "(|Meta|EndLoop|cd|)": null
  }
}
```

The contents:

- `url` contains the name of our chart script that will generate the JSON string
- `input` tells us the name of the .txt file containing our external data
- We use placeholder syntax to specify the data that we want from Empower. For example:
  - `|ContrName|` returns the name of the currently selected contract
  - `|WbsNum|` returns the WbsNum of the currently selected element
  - The `|Meta|BeginLoop|cd|` construct loops over the periods in the selected contract, returning the EndDate for each period

Note that we could use user-defined SQL instead of or in addition to placeholders to get the data from Empower.

### 7.1.1 Chart Code

Finally, we will need a file containing the code to generate the JSON string for our chart. For this example, we will be using a file called ch_getcharge.cgi, which can be found in the empower/cgi/ folder.

First, the script will get the parameters passed from Empower:

**Figure 7.3: Getting Parameters from Empower**

Next, we parse the input file containing our external data, skipping any lines that are not relevant for our chart:

**Figure 7.4: Parse the Input File**

Now the script will rearrange the data to be in a format that the Empower chart plugin, Highcharts, expects:

**Figure 7.5: Format Data**

We will also set the chart title and subtitle that we want to use for this chart, using values that were passed from Empower. Note that we are using a title from the extra variable, which is available to all charts and reports. This variable contains helpful information like the current unit, display scale, a preformatted title, etc.

**Figure 7.6: Chart Title**

Constructing the "options" object is the final reformatting step that we will take before encoding our JSON string and returning it to Empower to be processed by the charting tool.

**Figure 7.7: Options Object**

The "options" object has many options for customization. For details on the available "options" settings, see https://www.highcharts.com.

Once you have an "options" object, you can paste it into JSFiddle to see how it will look. JSFiddle can also be useful for testing out different Highcharts settings before adding them to your code. (see 6.1 for an example of how to use JSFiddle.)

Finally, ch_whocharged.cgi returns our JSON string.

**Figure 7.8: Return the JSON Object**

## 7.2 AT Report Example

The "Who Charged" report serves as an example of an AT Report. Recall that AT Reports must return standard HTML. This report will use the same file containing data external to Empower that we used in the "Who Charged" chart.

**Figure 7.9: Who Charged Report**

The "Who Charged" report compares current and cumulative ACWP from Empower with the data from our external data file. As with the AT chart in the previous section, we will need three files:

- A .txt file containing the external data
- A .txt file containing the information that Empower will need to create the report, such as the location and name of the script that will return the report HTML
- A .cgi file containing our Perl script that will generate the report HTML. In this case, the file is getcharge.cgi

See 7.1 for details on the fields and structure of the external data file.

The plain text file that we will import into Empower to define the report contains the name of our .cgi file as well as some placeholders that we will use to pull data from Empower for use in the report.

```json
{
  "url": "getcharge.cgi",
  "title": "Who Charged",
  "header": "This report compares current and cumulative ACWP (hours) from an Empower database to data from an external source. Sample data are available for MOH-2 elements 2100, 2200, 3200 and 3600.",
  "input": "Who-Charged",
  "contr": "(| ContrName |)",
  "stru": "(| Structure|StruName |)",
  "wbs": "(| WbsNum |)",
  "date": "(| EndDate |[%Y-%m-%d]|)",
  "desc": "(| ElemDesc |)",
  "ds": "(| ContrUnit|DisplayScale |%2%|[n0]|)",
  "us": "(| Unit|Scale |%2%|[n0]|)",
  "acum": "(| AcwpCum |[n5]|%2%|)",
  "acur": "(| AcwpCur |[n5]|%2%|)"
}
```

This file gets data from Empower using placeholders, including:

- `|ContrName|` returns the name of the currently selected contract
- `|EndDate|[%Y-%m-%d]` returns the End Date of the currently selected period in the format "yyyy-mm-dd"
- `|AcwpCum|[n5]|%2%|` returns the cumulative Acwp in hours, using a numeric format with five decimal places

### 7.2.1 Report Code

The code to generate the Who Charged Report HTML follows an outline similar to the script we used for the Who Charged Chart (see 7.1).

First, we get the parameters that were passed from Empower:

**Figure 7.10: Report Parameters**

If necessary, we convert the input file into a tab-delimited text file. This section of the code serves as an example that you can use when developing your own AT charts and reports.

**Figure 7.11: Convert Input**

Now we parse the input file, looping over the data and calculating the cumulative values.

**Figure 7.12: Parse Input**

Next we dynamically generate the rows that will be in the HTML table in our report.

**Figure 7.13: Generate Report Rows**

Before putting the HTML together, we do some more formatting:

**Figure 7.14: Format Report Data**

Finally, we put our HTML together, inserting our dynamically generated rows.

**Figure 7.15: Report HTML**

## 7.3 Integrating AI with Empower

AI tools can be integrated with Empower via Adaptive Touch custom reports. For example, you could supply information from Empower (such as a VAR narrative report) and have the AI tool provide a summary of the report.

### 7.3.1 Important Notes: Please Read Before Implementing

- Connections to AI tools are not automatic and only work if Empower is configured to connect to an AI tool
- When sending data to an external AI tool you are responsible for meeting any data security requirements
- Reports that connect to AI tools may take a long time to load. This is dependent on the amount of time that the AI tool takes to generate the response
- Results from these types of AI tools may not always be consistent, even when using the same data. Encore Analytics is not responsible for differences, errors, or inaccuracies in the results from these AI tools
- The quality of your results will greatly depend on the prompt that you choose to use. While we provide some examples of prompts that could be used, evaluating prompt quality or providing custom prompts is beyond the scope of Encore Analytics support
- Calculations done by an AI tool are not guaranteed to be correct. As mentioned previously, results may not be consistent
- Occasionally the AI tool may return unusual characters or formatting. This is not a problem with Empower
- Our examples will use OpenAI ChatGPT; naturally if you are using a different tool then the connection information and/or method may be different. The AI tool used in our examples is not included with Empower. Providing correct connection information is necessary in order for the report to work
- Our sample code is intended as an example of how you might connect to an AI tool in Empower. Determining the correct connection code and parameters for your chosen tool is up to you

### 7.3.2 Examples

Just like other AT reports, this example will use a JSON import file and a CGI server-side file, and will return HTML to be displayed in the report pane. Unlike our other AT reports however, we will be pulling data to integrate with data from Empower from an AI tool instead of a file on the server. In this example we'll provide the Empower VAR narrative to OpenAI and ask it to summarize the VAR, including a few more specific requests in the prompt.

#### 7.3.2.1 Example 1

**Figure 7.16 shows an excerpt of the JSON import file. This is the file that would be imported into Empower via "Import User Items."**

**Figure 7.16: OpenAI Gen VAR Import**

This import file includes a few key items:

- `url`: indicates the server-side file that will be used to generate the report
- `title`: the report name
- `header`: text that will be included at the top of the report and is not passed to the AI tool. This text can be used to insert any required disclaimer text for AI generated content
- `data`: use to indicate the chart or report data that should be passed to OpenAI. In this example, we'll use rp_var, which is the VAR narrative report
- `prompt`: the prompt to pass to the AI tool. In this example, we use the following prompt:

> "The following input is a JSON string. The 'title' value is plain text and identifies the active element. The 'narr' value is HTML and provides a detailed variance analysis. You are an earned value analyst preparing a report for the program manager. A professional tone is essential in the response. Summarize the following 'narr' value. Including the following: 1. an analysis of the cost and schedule variances with dollar values and key drivers, 2) the range of EACs (best case, worst case and most likely) with drivers for each, 3) a summary of the integrated master schedule (IMS) status, 4) management reserve usage this period, and a brief summary of corrective actions being taken. Also, provide recommendations and potential questions for the PM to ask at our meeting with the contractor."

This import file can also be used to pass other information to the server-side code. For example, you might pass an as_html flag to tell the AI tool to return information as HTML or as plain text.

Next we'll give an overview of some key components in the server-side code. For this example we'll use excerpts from openai_gen.cgi. Figure 7.17 shows sample connection information for connecting to ChatGPT. As a reminder, you would customize this information for your own site; you would need to use your own api_key and adjust the engine name and URL as necessary.

**Figure 7.17: OpenAI Gen Connection Code**

In our example code we include some options that can be passed, such as whether we want the AI tool to return HTML or plain text or how to wrap text.

**Figure 7.18: OpenAI Gen Code**

We pass the report data from Empower to the AI tool in JSON format and get a response. Note that this response may take some time to complete.

**Figure 7.19: OpenAI Gen Code**

Our sample code does some checks on the response for formatting, then similarly to other AT reports, the last thing we'll do in our server-side code is return the HTML to Empower.

**Figure 7.20: OpenAI Gen Code**

Figure 7.21 shows an excerpt of what this report might look like in the Empower report pane. Keep in mind that the results for this report may not be consistent.

**Figure 7.21: OpenAI Gen Report**

The sample openai_gen.cgi server-side code is designed to be flexible for use with other import files; the following examples will all use the same server-side code as the previous example.

While our examples will focus on the openai_gen.cgi server-side file in this document, there is an additional server-side file called asst_openai_gen.cgi available. This sample file is very similar to openai_gen.cgi, but contains adjusted connection information to allow for the use of an "assistant ID" key with your AI tool.

**Figure 7.22: OpenAI Gen with Assistant Connection Code**

At the time of writing, the use of "assistant IDs" is experimental. Assistant IDs could help achieve more consistent results for requests that rely on the same background information.

#### 7.3.2.2 Example 2

As another example, we could have an import file that looked like figure 7.23

**Figure 7.23: OpenAI Gen BAC Delta Import**

This import file uses the same server-side code as our first example, but this time we'll use the "BAC Delta" report and a new prompt.

This time, note a few items in the import file:

- `data`: this time we're using a custom report, so the function name is rp_custom
- `rid`: since we're using a custom report, we use the name of the report to indicate which custom report we want to use
- `prompt`: "What follows are the contents of a Javascript file. They begin with 'var extra', which defines a Javascript string, followed by 'var args', another Javascript string, is followed by a Javascript anonymous function that uses those variables. Please evaluate the Javascript and identify the WBS elements with non zero values in Dec 10 column. If an element has a non zero value that means there has been a budget change from the prior period. Write a memo asking the contractor to justify the budget changes in Dec 10. Do not emit the evaluated Javascript."

This time we're asking the AI tool to write a memo for a contractor; the resulting report in Empower might look something like 7.24.

**Figure 7.24: OpenAI Gen BAC Delta Report**

#### 7.3.2.3 Example 3

In our third example, we pass the BAC by CAM report to the AI tool and ask it to write a report that shows which CAM has the highest and lowest SPI, as well as which CAM has the best performance.

Our import file looks like 7.25.

**Figure 7.25: OpenAI Gen BAC by CAM Import**

The resulting report might look like 7.26.

**Figure 7.26: OpenAI Gen BAC by CAM Report**

#### 7.3.2.4 Example 4

Our sample code is also designed to accept chart inputs from Empower. Consider the import file displayed in figure 7.27.

**Figure 7.27: OpenAI Gen EAC Chart Import**

Notice that the "data" is from ch_eac, which is an Empower chart function. This time our prompt is: "The following input is a JSON string intended for the Highcharts charting tool. For each line, identify the legend and the values, and describe the trend over time."

The resulting report might look like 7.28.

**Figure 7.28: OpenAI Gen EAC Chart Report**
