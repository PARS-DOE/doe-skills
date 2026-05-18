# TN Headers and Footers

*Source: TN-HeadersandFooters.pdf*

---

## Technical Note: Custom Headers and Footers

© 2013 Encore Analytics, LLC
January 19, 2022

## 1 Implementing Custom Headers and Footers

Empower supports the implementation of custom headers and footers for the Empower login screen, main page, and charts or reports opened in external windows. To implement custom headers and footers, add entries for each desired header or footer to empower.conf.

```
LOGIN_HEADER=<div id="my_login_header"><img src="ea.svg" height="40"></img></div>
Login_Header_Height=50
LOGIN_FOOTER=<div id="my_login_footer">Encore Analytics LLC Proprietary Data</div>
INDEX_HEADER=<div id="my_index_header">I'm an index header.</div>
INDEX_FOOTER=<div id="my_index_footer">I'm an index footer.</div>
REPORT_HEADER=<div id="my_report_header">I'm a report header.</div>
REPORT_FOOTER=<div id="my_report_footer">I'm a report footer.</div>
CHART_HEADER=<div id="my_chart_header">I'm a chart header.</div>
CHART_FOOTER=<div id="my_chart_footer">I'm a chart footer.</div>
EXPORT_CHART_HEADER=I'm an export chart header
EXPORT_CHART_FOOTER=I'm an export chart footer
EXPORT_HEADER=I'm an export header
```

Note that some lines in this document are wrapped to fit the page.

### 1.1 Login Page

The LOGIN_* entries in the sample define headers/footers for login.html, the login page.

```
LOGIN_HEADER=<div id="my_login_header"><img src="ea.svg" height="40"></img></div>
Login_Header_Height=50
LOGIN_FOOTER=<div id="my_login_footer">Encore Analytics LLC Proprietary Data</div>
```

Note that you can specify a height for your headers and footers. For example, see the entry for LOGIN_HEADER_HEIGHT above, where the header for the login screen is set to have a height of 50px. The height can be specified for any of the headers/footers mentioned in this document except for EXPORT_HEADER. If omitted, the height defaults to 30px.

### 1.2 Empower main page

Entries with INDEX_* define headers/footers for index.html, the main page for Empower.

```
INDEX_HEADER=<div id="my_index_header">I'm an index header.</div>
INDEX_FOOTER=<div id="my_index_footer">I'm an index footer.</div>
```

### 1.3 External Reports

Entries beginning with REPORT_* define headers/footers for xrpt.html, which is used for reports opened in external windows.

```
REPORT_HEADER=<div id="my_report_header">I'm a report header.</div>
REPORT_FOOTER=<div id="my_report_footer">I'm a report footer.</div>
```

### 1.4 External Charts

Entries beginning with CHART_* define headers/footers for xchrt.html, which is used for charts opened in external windows.

```
CHART_HEADER=<div id="my_chart_header">I'm a chart header.</div>
CHART_FOOTER=<div id="my_chart_footer">I'm a chart footer.</div>
```

### 1.5 Exported Charts

Entries beginning with EXPORT_CHART_* define headers/footers for charts exported as PDFs, PNGs, and SVGs. Note that these entries should be plain text, and that the exported file will not retain any html styles, only the plain text.

```
EXPORT_CHART_HEADER=I'm an export chart header
EXPORT_CHART_FOOTER=I'm an export chart footer
```

### 1.6 Excel Exports

The entry EXPORT_HEADER defines a header that will appear in all Excel exports. This header must be plain text, and will apply to all exported Excel files. Note that this does not apply to Excel files downloaded using "Download Data File." The header text will appear in the first row of the exported file without any formatting, as shown in Figure 1.

**Figure 1: Excel export header**

## 2 Custom CSS styles

Custom CSS styles for headers and footers can be defined in the file banner.css if desired. This allows you to change the background color, text alignment, border, etc. of your custom headers and footers. Our sample CSS file, sample-banner.css, can be found in \empower\setup. Simply copy sample-banner.css into the www directory (C:\encore-analytics\empower\www in the default installation) and rename it banner.css to implement the custom styles in the file.

Headers or footers referenced in banner.css follow a naming convention, for example, #my_index_header refers to the header for Empower's main page. Referencing other headers or footers in this file follows the same pattern: #my_<type of header/footer>_<header/footer>.

Styles can be set for multiple headers and footers at once by listing the headers and footers that you want the style to apply to separated by commas before the declaration block with the CSS properties you want to set for those elements.

**Sample banner.css:**

```css
#my_index_header, #my_index_footer,
#my_login_header, #my_login_footer,
#my_chart_header, #my_chart_footer,
#my_report_header, #my_report_footer
{
  background-color: white;
  padding: 5px 5px;
}

#my_index_header {
  border-bottom: 1px solid silver;
}

#my_login_header, #my_report_header, #my_chart_header {
  border-bottom: 1px solid silver;
}

#my_login_footer, #my_report_footer, #my_chart_footer {
  border-top: 1px solid silver;
}
```

## 3 Per-Contract Banners

Custom banners can also be assigned on a per-contract basis. This can be useful, for example, if you have different levels of confidentiality for different contracts and users need to be notified of the level of their current data. With custom banners you could display the appropriate level for the current dataset in the header or footer.

If you plan to use banners, make sure to set the HIDE_PRINT_CHART config option should be set to 1 in empower.conf. Since banners are not available for printed charts, this option will disable the chart printing option.

### 3.1 Default Banners

When using custom per-contract banners, you should set a default index header and footer in empower.conf for contracts that do not have a banner assigned to them unless you plan to have a banner entry for each contract. For example, you could set a blank header and footer as your default banners in empower.conf:

```
INDEX_HEADER=<div class="empty"></div>
INDEX_FOOTER=<div class="empty"></div>
```

### 3.2 Creating Banners

To create a banner that can be used on a per-contract basis, use "Download Data File" to download "Banners." Add rows as desired, putting an 'a' in the "action" column. Save your changes, then upload your file with "Upload Data File."

**Figure 2: Data Download: Banners**

Banner Text should be HTML for the banner, including whatever text you want to display.

Banner Priority indicates the priority with which each banner should be displayed over other banners. If multiple contracts are open, the sort window will display the banner with the lowest Banner Priority value. Note that external items that have banners set (e.g. external charts and reports) will display the banner of the contract that they are displaying data for.

Banner Type ID indicates what type of banner you want to create. Valid entries are:

| ID | Meaning |
|----|---------|
| 1 | Index_Header |
| 2 | Index_Footer |
| 3 | Report_Header |
| 4 | Report_Footer |
| 5 | Chart_Header |
| 6 | Chart_Footer |
| 7 | Export_Chart_Header |
| 8 | Export_Chart_Footer |
| 9 | Export_Header |

The meanings of these types are discussed earlier in this document. This list is also available on the "Notes" tab of the "Banners" data download.

As an example, we could create banners that look like the image below.

**Figure 3: Banners**

This would create banner entries that we could then assign to specific contracts.

### 3.3 Assigning Banners

To assign banners to contracts, use the Contract Banners data download.

**Figure 4: Data Download: Contract Banners**

Add lines to the resulting xlsx file as desired, then save and upload with "Upload Data File." For example, we could use the following to add Contract Banner entries for the "Jeep" sample data:

**Figure 5: Contract Banners Upload**

After creating our sample banners, we will see something like this in the sort window when MOH-2 is open:

**Figure 6: MOH-2 Banners**

### 3.4 Banner Styles

As discussed earlier in this document, you can use the banner.css file to create styles that can be used with your banners. For example, banner.css might look like this:

```css
div.notice {
  background-color: red;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 24px;
}

div.empty {
  display: flex;
  height: 24px;
}
```

Notice that we used the empty class for our default INDEX_HEADER and INDEX_FOOTER entries in empower.conf.
