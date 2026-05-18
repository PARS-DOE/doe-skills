# Chapter 1: Introduction

*From the Empower User Manual*

---

## Overview

Encore Analytics Empower is a server-based analytical tool that combines earned value, schedule, and other key information to provide a rich, integrated interactive system for proactive management of complex projects. On the client side, Empower is a zero-footprint browser-based application that requires no installation to provide a rich and intuitive graphical user interface (GUI) for project management analytics. It runs on modern HTML 5/JavaScript-enabled browsers such as Microsoft Internet Explorer (version 9 and above), Firefox, Safari, Edge, and Chrome.

Figure 1.1 shows the Empower application with its standard Tri-panel layout. In this layout, the Empower main window is divided into three subwindows or panes, called the Sort, Chart, and Report Windows.

### Sort Window

Elements of a contract are shown in the Sort Window. The display of these elements can be sorted according to a variety of project metrics or the elements' place in the project hierarchy, and which elements are displayed can be customized by a variety of filters.

### Chart Window

The Chart Window is shown in the lower left, and typically shows a chart illustrating some metric of the project element currently selected in the Sort Window.

### Report Window

The Report Window is shown in the lower right. This window will display a report related either to the entire project, or to the project element currently selected in the Sort Window.

### Window Interaction

Selecting a new element in the Sort Window automatically updates the Chart and Report Windows. In addition, selecting a new chart or report from the menu will replace the existing chart or report in the appropriate window.

---

## Capabilities and Integration

In addition to its own database, Empower has the ability to access a broad range of external project management data sources with its Custom Reports and eNotebook capabilities. When integrated with existing project information sources, Empower can provide a single launch point for all project management information.

### Deployment Options

The Empower application is typically installed on an internal server behind a corporate firewall; however, Empower is also available as a standalone implementation. This can be done either by installing directly on the user's computer or by running Empower with Docker hosted on the user's computer.

Empower uses databases hosted on Microsoft SQL Server, Oracle, or PostgreSQL. These database servers can be hosted on the same server as the Empower application or separately.

---

## Design Objectives

Empower is specifically designed to:

### Enhance CAM Performance Understanding

- Enhanced Element of Cost (EOC) analysis which graphically displays the EOC components of the budget (BAC), forecast (EAC) and cost variance (CV)
- Correlation of work packages to control accounts during analysis and drill-down/up
- Correlation of schedule activities to control accounts of work packages during analysis
- Graphic display of schedule data at control account of work package level (baseline, current plan, progress and relationships)
- Streamlined Assisted Intelligence (AI) narratives that clearly articulate performance issues and the reasonableness of forecasts
- Custom reports, such as Adaptive Touch Reports (ATR), that pull data from other corporate systems (i.e., work authorization, accounting, etc.) and to display key data in Empower's unified interface

### Alert CAMs of Data Anomalies

- Quality of earned value data
- Quality of schedule data
- Quality of the EAC
- Failure to maintain cost and schedule integration

### Provide Program Control

Provide Program Control with a comprehensive set of anomalies for the entire project:

- Current period
- Anomaly trend analysis

### Streamline VAR Narrative Generation

- Enhanced editor with spell check
- Change tracking by user during the VAR generation process
- Acceptance/rejection of changes (all or selected changes)

### Provide EAC Insight

- Provide insight into EAC realism/quality

### Reduce Training and Streamline User Interaction

- Combine earned value, schedule and CAM eNotebook type information in a single unified interface
- Simplify the user interface with interactive filters, views, and single click sorting
- Provide concise data validity and assisted intelligence that explains the condition, rules, and data relationships

---

## Impact and Benefits

With Empower, program management stakeholders no longer require extensive training or a complicated MS Windows desktop client installation to take full advantage of program performance data to assist in the proactive management of complex projects.
