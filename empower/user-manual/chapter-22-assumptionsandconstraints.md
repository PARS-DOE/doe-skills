# Chapter 22: Assumptions and Constraints

*From the Empower User Manual*

---

## 22.1 Data Requirements

Empower provides enhanced analytical features and thus requires that the Empower databases be fully populated with a complete set of earned value and schedule data. In addition, we have added a number of fields to help identify the nomenclature used to identify items such as LOE, CA, WP, PP, etc., for consistency during analysis.

### 22.1.1 Earned Value Data

The following items are recommended for earned value data:

- Standard data elements for performance
- Element of cost (EOC) data (Total $, Labor $, Labor hrs, ODC $, Mat $, etc.)
- Time-Phased future period data (BCWS & ETC)
- Populate at the lowest level where actual costs are interfaced (normally work package). For newer versions of Empower some exceptions can be made to populating data at the lowest level, see section 22.1.3 for more information.
- Fully populate the Elem Type (CA/WP/PP) and EVM columns (EVM method)
- Populate CAM name (Proj of field)

### 22.1.2 Schedule Data

Use the Import EDI function to load scheduling data into the Empower database. Currently the Import EDI function supports, among others, the UN/CEFACT Format 6, IPMDAR JSON SPD, DOE CPP JSON, and C/S Glue XML file types. Many of the DQI flags focus on schedule data and the integration of the earned value and schedule data. Further, the Gantt chart uses this data.

### 22.1.3 Input Data at the Control Account Level

#### 22.1.3.1 Performance Data at Control Account (CA) Level when Work Package (WP) level data also exists

Empower supports the transfer and storing of performance data (BCWS, BCWP, ACWP, Reprogramming Adjustments (Schedule, Cost and Budget), Future BCWS, and Future ETC) at mixed levels between the WP and CA; however, it must be consistent throughout the contract structures. For example, if ACWP is collected at the CA level, it must be that way throughout the entire contract and consistent for all periods. The IPMDAR JSON CPD and Empower optimized files support the mixing of all performance data, but the DOE CPP JSON file only supports ACWP at the CA level with all other data at the WP level. Proper setting of the CaCalcFlag at the contract level is imperative for this to work properly.

On import, Empower will query the IPMDAR JSON CPD dataset configuration.json and set the CaCalcFlag in the Contracts table settings Tab to the appropriate value automatically. For the DOE CPP JSON file, Empower will query the DS07_IPMR_header.json for "is_ACWP_at_CA":"Y" and set CaCalcFlag = 1 in that case. When using an Empower optimized file the end user may need to set the CaCalcFlag prior to running recalculation.

**WARNING:** End users should not change the CaCalcFlag value without a full understanding of the ramifications. Recalculating with an improperly set CaCalcFlag could result in the loss of data at the CA level.

**Ground Rules**

1. This feature only works with Empower optimized, DoD IPMDAR JSON CPD, and the DOE CPP JSON files. It is not backward compatible with other EDI formats.

2. Per the DoD IPMDAR JSON CPD and the DOE CPP JSON specifications, WPs/PPs must be direct descendants of a CA or SLPP.

3. The level at which the performance data is transmitted must be consistent throughout the entire contract. For example, if ACWP is collected at the CA level, it must be that way throughout the contract. In other words, no actuals at the WP level for any account.

4. The data must be consistent month-to-month. For example, you cannot have actuals report at the CA level one month and then at the WP level in another month.

5. If ACWP is at the CA level, the WP EACs will represent the sum of the future ETC. The ACWP plus future ETC total will be displayed at the CA level and above.

6. When running audit metrics with mixed levels for performance data, please ensure the correct audit report is selected for your contract.

#### 22.1.3.2 Data Downloads for CA Level Data

The "Earned Value" data download has a CA tab where the data for your control accounts can be viewed and edited.

**Figure 22.1: Data Download for Earned Value, CA tab**

Similarly, the "Future Period" data download also has a CA tab where you can view the future period data for your control accounts.

**Figure 22.2: Data Download for Future Etc, CA tab**

#### 22.1.3.3 Setting CaCalcFlag

The CaCalcFlag setting in the "Settings" tab of the Contracts data download controls which data fields for a contract are calculated from the Control Account level instead of the lowest level. CaCalcFlag can be set via data download/upload of Contracts.

**Fields that can have data input at the CA level are listed below:**

**Table 22.1: CaCalcFlag**

| Flag Value | Fields |
|------------|--------|
| 0 | None (fields calculated from lowest level) |
| 1 | AcwpCur, AcwpCum, AcwpAdj |
| 2 | ReprogCost, ReprogBudg, ReprogSch |
| 4 | BcwpCur, BcwpCum, BcwpAdj |
| 8 | BcwsCur, BcwsCum, BcwsAdj |
| 16 | FuturePeriodBcws |
| 32 | FuturePeriodEtc |

To designate that a field (or group of fields) should be reported at the CA level, add the corresponding value from the table above to your CaCalcFlag. Notice that some values correspond to a group of fields; in these cases adding the value will indicate that all fields in the group should be calculated from the CA level.

**Example Entries**

- If ACWP only at CA: CaCalcFlag = 1

- If Repro only at CA: CaCalcFlag = 2 (Note that the IPMDAR only accepts Repro at CA. This is the default for IPMDAR if all other items are at WP.)

- If Repro and ACWP at CA:
  - CaCalcFlag = 1 + 2
  - = 3

- If ACWP and Future ETC at CA:
  - CaCalcFlag = 1 + 32
  - = 33

- If ACWP, Repro, and Future ETC at CA:
  - CaCalcFlag = 1 + 2 + 32
  - = 35

After setting the CaClacFlag, make sure to recalculate your data to ensure that your calculated values are up-to-date.

#### 22.1.3.4 CaCalcFlag for IPMDAR CPD Imports

Importing a file in the IPMDAR CPD format will automatically populate your CaCalcFlag value based on the Dataset Configuration settings in the imported file. If the corresponding entry is set to false for a field (or group of fields), that field will be calculated from the CA level. For example, if your ACWP_ToDate_ByWorkPackage entry is set to false in your DatasetConfiguration file, your ACWP values will be calculated from the CA level instead of the lowest level.

As a reference, here are the DatasetConfiguration entries that can impact which fields are input at the CA level:

- ACWP_ToDate_ByWorkPackage; corresponds to Earned Value ACWP fields
- BCWP_ToDate_ByWorkPackage; corresponds to Earned Value BCWP fields
- BCWS_ToDate_ByWorkPackage; corresponds to Earned Value BCWS fields
- BCWS_ToComplete_ByWorkPackage; corresponds to Future Etc BCWS field
- EST_ToComplete_ByWorkPackage; corresponds to Future Etc ETC field

#### 22.1.3.5 Exporting Data with mixed levels of Performance Data for the DoD IPMDAR CPD JSON

Empower supports exporting the IPMDAR CPD JSON file with performance data at mixed levels between the CA and WP. For example, if the contract has CaCalcFlag = 3 and data is exported to the WP level, ACWP and reprograming adjustments will be exported at the CA level and the datasetconfiguration.json will be generated to reflect that condition (e.g. "ACWP_ToDate_ByWorkPackage" : false). Note, there is no parameter in the datasetconfiguration.json for reprogramming adjustments at the CA level since it is the only option supported; however, Empower must be told to export the Reprogramming Adjustments and ACWP at the CA (CaCalcFlag = 3).

## 22.2 Scheduling Units

Empower assumes that all schedule planning units (durations, leads, lags, slips, float, etc.) are in days. You must ensure that when you export from the underlying scheduling tool (MS Project, Open Plan or P6) that the schedule units are in days.

## 22.3 Database Servers

Empower supports databases hosted on Microsoft SQL Server, Oracle, and PostgreSQL. Supported versions include:

- SQL Server 2012 and newer
- Oracle 11 and newer
- Postgres 9 and newer

## 22.4 Browser Compatibility

The Empower application requires a modern browser, meaning one that implements HTML5 and JavaScript. We have tested the following so any version newer than those listed below should be compatible:

### MS Windows

- IE 8.0, 9.0, 10.0, 11.0
- Firefox 32.0
- Chrome 37.0
- Edge 102.0.1245.41

### Mac OS X

- Safari 7.0
- Firefox 25.0
- Chrome 31.0
- Edge 102.0.1245.41

### Linux

- Firefox 24.0
- Chrome 31.0

### Apple iPad

- Safari 6.0 (with some limitations)
- Chrome 23.0 (with some limitations)
