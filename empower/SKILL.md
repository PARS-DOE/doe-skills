---
name: empower
description: "Empower documentation including User Manual and Tech Notes. Use when asked about Empower concepts, EVMS/earned value management, cost/schedule variance analysis, BAC/EAC/ETC forecasting, publevel logic, data quality indicators (DQIs), VAR narratives, CAM responsibilities, WBS/OBS structures, project reporting, charts, dashboards, data uploads/downloads, recalculation, user administration, SSO/authentication, or system configuration."
---

# Empower Documentation

## Overview

Empower is a server-based analytical tool developed by Encore Analytics for proactive management of complex projects. It combines earned value management (EVM), schedule data, and other key project metrics into an integrated, interactive system. The application runs as a zero-footprint browser-based tool (no client installation required) that provides a rich graphical user interface for project management analytics.

The core interface uses a "Tripane" layout with three primary windows: the Sort Window (top) displays project elements that can be filtered and sorted by various metrics; the Chart Window (bottom-left) shows graphical representations of selected elements; and the Report Window (bottom-right) displays detailed reports. Selecting an element in the Sort Window automatically updates the Chart and Report Windows with relevant data.

Empower is specifically designed to help Control Account Managers (CAMs) understand performance issues driving variances, alert users to potential data anomalies that could trigger audits, provide Program Control with comprehensive anomaly reports, streamline VAR (Variance Analysis Report) narrative generation, and provide insight into EAC (Estimate at Completion) realism and quality. It integrates with external project management data sources and supports databases hosted on Microsoft SQL Server, Oracle, or PostgreSQL.

## When to Use This Skill

- User asks about Empower features, interface, or navigation
- User needs help with earned value management (EVM/EVMS) concepts
- User asks about cost variance (CV), schedule variance (SV), or variance analysis
- User mentions BAC (Budget at Completion), EAC (Estimate at Completion), or ETC (Estimate to Complete)
- User asks about DQIs (Data Quality Indicators) or data quality tests
- User needs help writing or editing VAR narratives or EAC narratives
- User asks about WBS (Work Breakdown Structure) or OBS (Organization Breakdown Structure)
- User mentions CAM (Control Account Manager) responsibilities
- User asks about Empower charts, reports, or dashboards
- User needs help with filtering, sorting, views, or prefilters
- User asks about data uploads, downloads, or recalculation
- User asks about Empower administration or user management
- User mentions SSO, authentication, or security in Empower
- User asks about Empower configuration, installation, or troubleshooting
- User asks about action item tracking or narrative approval workflow
- User asks about element mapping or cross-contract queries
- User mentions publevel, recalc, or data processing in Empower
- User asks about custom charts, custom reports, or dialog templates

## Document Index

### User Manual (user-manual/)

| Chapter | Title | Description |
|---------|-------|-------------|
| 01 | Introduction | Overview of Empower capabilities and Tripane layout |
| 02 | QuickStart | Starting Empower, login/SSO, opening datasets, basic navigation |
| 03 | Sort Window (in more detail) | Column customization, row management, element selection |
| 04 | Filtering Data Interactively | Using filter bar, filter operators, combining filters |
| 05 | Views | Creating, saving, and managing custom views |
| 06 | Filtering Data with Prefilters | Server-side filtering for large datasets, CAM/WBS prefilters |
| 07 | Charts | Standard chart types, Gantt charts, schedule visualization |
| 08 | Custom Charts | Creating and configuring custom chart definitions |
| 09 | Standard Reports | Built-in report types and usage |
| 10 | Custom Reports | Creating custom report templates |
| 11 | Data Quality Indicators | DQI tests, TestSums, removing DQIs from reports |
| 12 | Dashboards | Dashboard creation and configuration |
| 13 | Dialog Templates | Creating templates for dialog boxes |
| 14 | Exporting Data to Other Programs | Excel export, data download options |
| 15 | Editing Narrative Inputs | VAR narratives, EAC narratives, User EAC inputs, VAR categories |
| 16 | Administrator Commands | Data upload/download, recalculation, user management, system admin |
| 17 | Element Mapping Functionality | Mapping elements between structures |
| 18 | Security in Empower | User roles, permissions, access control |
| 19 | Units in Empower | Dollars, hours, units of measure configuration |
| 20 | Narrative Approval Workflow | CAM submission, review cycles, approval process |
| 21 | Action Item Tracking | Creating, managing, and tracking action items |
| 22 | Assumptions and Constraints | System requirements, browser compatibility |
| 23 | Support | Contact information for Encore Analytics support |
| 24 | Frequently Asked Questions (FAQs) | Common questions and troubleshooting |

### Technical Notes

| File | Title | Description |
|------|-------|-------------|
| tn-faq.md | Troubleshooting Guide | Common errors, browser issues, helpful scripts, bulk_data utility |
| tn-auditreports.md | Audit Reports | Configuring and customizing audit reports |
| tn-conffile-1.md | Configuration File | Empower.conf settings and options |
| tn-creatingdatabases.md | Creating Databases | Database setup for SQL Server, Oracle, PostgreSQL |
| custom-charts-reports/ | Custom Charts & Reports | Writing custom charts and reports (10 chapters) |
| tn-emailnotifications.md | Email Notifications | Configuring email alerts and notifications |
| tn-encryption.md | Encryption | Data encryption and security settings |
| tn-headersandfooters.md | Headers and Footers | Customizing report headers and footers |
| tn-incrementalupdate.md | Incremental Update | Incremental data loading vs full recalculation |
| tn-pruning.md | Pruning | Removing old data from the database |
| tn-security.md | Security | Detailed security configuration |

**Note:** Chapter 16 (Administrator Commands) has been split into sections in `user-manual/chapter-16-sections/` for easier navigation.

### Setup & Configuration

| File | Title | Description |
|------|-------|-------------|
| empowerauthentication.md | User Authentication | SSO setup, IIS configuration, SAML, Active Directory |
| empowerwindowsinstallnotes.md | Windows Install Notes | Windows-specific installation guidance |
| empower-roll-out.md | Roll Out Guide | Deployment and rollout procedures |

### Additional Resources

| File | Title | Description |
|------|-------|-------------|
| custom-charts-reports-brittany-hayes.md | Custom Charts & Reports (Training) | Training materials for custom development |
| customreports-additions.md | Custom Reports Additions | Additional custom report features |

## Quick Reference

| Question | Document(s) to Consult |
|----------|------------------------|
| How do I log into Empower? | chapter-02-quickstart.md |
| How do I filter data in the Sort Window? | chapter-04-filteringdatainteractively.md, chapter-06-filteringdatawithprefilters.md |
| What DQI tests are available? | chapter-11-dataqualityindicators.md |
| How do I write VAR narratives? | chapter-15-editingnarrativeinputs.md, chapter-20-narrativeapprovalworkflow.md |
| How do I upload/download data? | user-manual/chapter-16-sections/ |
| How do I set up SSO? | empowerauthentication.md |
| Getting errors or browser issues? | tn-faq.md |
| How do I configure Empower? | tn-conffile-1.md |
| How do I create custom charts? | chapter-08-customcharts.md, custom-charts-reports/ |
| How do I manage users and permissions? | chapter-18-securityinempower.md |
| How do I track action items? | chapter-21-actionitemtracking.md |

## Key Concepts

### Tripane Layout
Empower's main interface with three windows: Sort Window (top, shows project elements), Chart Window (bottom-left, shows graphs), and Report Window (bottom-right, shows reports). Selecting an element updates all windows.

### Dataset
A combination of contract (project), period of data, structure (WBS/OBS/IPT), and unit of measure (Dollars/Hours). Must be opened before working with data.

### DQI (Data Quality Indicator)
Automated tests that check for data anomalies and quality issues. Examples include "No Logic" (schedule activities without predecessors/successors), "BAC not equal to WAD BAC", and various EVMS compliance checks. DQIs can be summed up the WBS tree and color-coded by severity.

### VAR Narrative
Variance Analysis Report narrative explaining cost and schedule variances. Empower provides an enhanced editor with spell check, change tracking, and approval workflow support.

### EAC (Estimate at Completion)
The projected total cost of a project element. Empower supports User EAC inputs with minimum, maximum, and most likely values using various calculation methods (BAC, MovAvg3, CumCpiFc, Analyst-entered).

### CAM (Control Account Manager)
The person responsible for a control account (project element). CAMs use Empower to analyze performance, write narratives, and manage their assigned elements.

### WBS/OBS/IPT
Work Breakdown Structure, Organization Breakdown Structure, and Integrated Product Team. Different ways to organize and view project elements hierarchically.

### Prefilter
Server-side filtering applied when opening a dataset. Reduces network traffic for large projects by limiting which elements are downloaded. Examples: filter by CAM, WBS contains, lowest level only.

### View
A saved configuration of which columns to display and how to filter/sort them. Views can be personal or shared across users.

### Recalculation
Processing that updates derived values, DQI tests, and aggregations. Required after data changes. Can be single-period or multi-period.

### Publevel
The publication level or data processing stage. Related to when data becomes official and available for reporting.

### Action Item
A tracked work item with owner, due date, status, and associated project element. Used for follow-up on issues identified during analysis.
