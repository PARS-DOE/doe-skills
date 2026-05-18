# PARS CPP JSON Schema Compact Reference

This is a compact version of the PARS CPP JSON Schema v5.0.3 specification intended for quick reference or LLM context. For complete details, validation rules, and formal requirements, consult the full DID and schema files.

---

# DS01

This data set contains the project's contractor WBS identifiers in a hierarchical structure from project level down to work package level.

## Fields

WBS_ID: Unique contractor WBS identifier.
title: WBS identifier title.
level: Hierarchical level relative to the project.
 Starting with 1 at project level, incrementing by 1.
 Only one level 1 WBS identifier representing the entire project.
parent_WBS_ID?: WBS identifier of immediate hierarchical parent.
 Required unless level = 1.
type:WBS|SLPP|CA|PP|WP: WBS type
OBS_ID?: OBS identifier associated with this WBS. Aligns with DS02.
CAM?: Control Account Manager name.
WPM?: Work Package Manager.
subproject_ID?: Unique subproject identifier. Required if external = Y.
IMP_ID?: Integrated Master Plan identifier.
external:Y|N: WBS is external to the project.
exit_criteria?: Criteria to determine WBS scope completion.
 Required for CA or SLPP types.
narrative: WBS scope description from EVMS cost tool.
K_ref?: Contract reference: number, sections, paragraphs. Aligns with DS07.
BWC_ID?: Base work construct identifier. Examples: W.01.01 project, W.02.03 preliminary, W.04.04 construction.
---

# DS02

This data set contains the project's contractor OBS identifiers in a hierarchical structure from project level down to control account level.

## Fields

OBS_ID: Unique contractor OBS identifier.
title: OBS identifier title.
level: Hierarchical level relative to the project.
 Starting with 1 at contractor head level, incrementing by 1.
 Only one level 1 OBS identifier.
parent_OBS_ID?: OBS identifier of immediate hierarchical parent.
 Required unless level = 1.
external:Y|N: OBS is external to the project.
narrative?: OBS description from EVMS cost tool.
---

# DS03

This data set contains the project's contractor EVMS cost tool time-phased data at WP/PP level by EOC.

## Fields

period_date: Time-phased period end date. Aligns with CPP_status_date.
WBS_ID_WP?: WBS identifier when data is reported at WP or PP level.
WBS_ID_CA: Control Account WBS identifier.
 If data at CA level, the CA where reported.
 If data at WP/PP level, the parent CA.
EOC:labor|material|subcontract|ODC|indirect: Element of cost.
EVT?:A|B|C|D|E|F|G|H|J|K|L|M|N|O|P|NA: Earned value technique. Required for WP, PP, or SLPP.
justification_EVT?: Justification for EVT = B, G, H, J, L, M, N, O, or P.
EVT_J_to_WBS_ID?: WBS_ID apportioned to, if EVT = J or M.
EVT_J_pct?: Percent apportioned from another WBS.
BCWSi_dollars: BCWS incremental (dollars).
BCWPi_dollars: BCWP incremental (dollars).
ACWPi_dollars: ACWP incremental (dollars).
ETCi_dollars: ETC incremental (dollars).
is_indirect?:Y|N: Represents indirect costs only.
BCWSi_hours: BCWS incremental (hours) for labor EOC only.
BCWPi_hours: BCWP incremental (hours) for labor EOC only.
ACWPi_hours: ACWP incremental (hours) for labor EOC only.
ETCi_hours: ETC incremental (hours) for labor EOC only.
BCWSi_FTEs: BCWS incremental (FTE) for labor EOC only.
BCWPi_FTEs: BCWP incremental (FTE) for labor EOC only.
ACWPi_FTEs: ACWP incremental (FTE) for labor EOC only.
ETCi_FTEs: ETC incremental (FTE) for labor EOC only.
CV_rpg: Reprogramming cost variance adjustment.
SV_rpg: Reprogramming schedule variance adjustment.
BAC_rpg: Reprogramming BAC adjustment.
CC_ID?: Charge code identifier.
CC_description?: Charge code description.
---

# DS04

This data set contains the project's contractor BL and FC IMS tool data by task.

## Fields

schedule_type:BL|FC: Baseline or forecast schedule.
task_ID: Task identifier.
type:TD|RD|LOE|SM|FM|WS: Task type.
description: Task description. Should include a verb.
subtype?:SVT|ZBA: Task subtype for non-PMB or zero budget activities.
milestone_level?: Milestone level for SM/FM tasks. 3 digit code specifies milestone type.
milestone_level_description?: Milestone description.
WBS_ID: WBS identifier associated with this task.
justification_WBS?: Justification if not WP, PP, or SLPP.
CAM?: Control Account Manager name.
EVT?:A|B|C|D|E|F|G|H|J|K|L|M|N|O|P: Earned value technique. Aligns with DS03.EVT.
justification_EVT?: Justification for EVT = B, G, H, J, L, M, N, O, or P.
EVT_J_to_task_ID?: Task ID apportioned to, if EVT = J.
EVT_J_pct?: Percent apportioned from another task.
ES_date: Early start date.
EF_date: Early finish date.
LS_date: Late start date.
LF_date: Late finish date.
AS_date?: Actual start date.
AF_date?: Actual finish date.
duration_original_days: Original duration (work days).
duration_remaining_days: Remaining duration (work days).
duration_actual_days: Actual duration (work days).
float_free_days: Free float (work days).
float_total_days: Total float (work days).
justification_float_high?: Justification for high float.
justification_lag?: Justification for lag with predecessor.
driving_path:Y|N: Task is on the driving path.
RMT_ID?: Risk mitigation task ID. Aligns with DS15.risk_ID.
PC_type:duration|physical|units: Percent complete type for BCWP calculation.
PC_duration: Duration percent complete (0.00 to 1.00).
PC_physical: Physical percent complete (0.00 to 1.00).
PC_units: Units percent complete (0.00 to 1.00).
constraint_type?:CS_ASAP|CS_MANDSTART|CS_MSO|CS_MSOA|CS_MSOB|CS_ALAP|CS_MANDFIN|CS_MEO|CS_MEOA|CS_MEOB: Schedule constraint.
constraint_date?: Constraint date.
justification_constraint_hard?: Justification for hard constraints.
justification_constraint_soft?: Justification for soft constraints.
justification_constraint_secondary?: Secondary constraint description.
HDV_CI_ID?: High dollar value critical item ID. Aligns with DS14.
RPG:Y|N: Task is for reprogramming effort.
calendar_name?: Calendar for task. Aligns with DS19/DS20.
subproject_ID?: Subproject identifier for external or out-of-scope tasks.
---

# DS05

This data set contains the project's contractor BL and FC IMS tool task relationship data.

## Fields

schedule_type:BL|FC: Baseline or forecast schedule.
task_ID: Task identifier.
predecessor_task_ID: Predecessor task identifier. Aligns with DS04.task_ID.
type:FS|SS|SF|FF: Task relationship type.
lag_days: Lag (positive) or lead (negative) in work days.
subproject_ID?: Subproject identifier.
predecessor_subproject_ID?: Predecessor task's subproject identifier.
---

# DS06

This data set contains the project's contractor BL and FC IMS tool task resource data. Entries should represent either a resource or a role.

## Fields

schedule_type:BL|FC: Baseline or forecast schedule.
task_ID: Task identifier.
resource_ID?: Resource identifier.
resource_name?: Resource name.
role_ID?: Role identifier.
role_name?: Role name.
type:labor|nonlabor|material: Resource type.
EOC?:labor|material|subcontract|ODC|indirect: Element of cost.
start_date: Resource start date.
finish_date: Resource finish date.
budget_dollars: Total budget (dollars) aligned with BCWS.
actual_dollars: Total actual (dollars) aligned with BCWP.
remaining_dollars: Total remaining (dollars) aligned with ETC.
budget_units: Total budget units aligned with BCWS.
actual_units: Total actual units aligned with BCWP.
remaining_units: Total remaining units aligned with ETC.
UOM: Unit of measure. Hours for labor/nonlabor, string for material.
lag_remaining_days: Remaining lag (positive) or lead (negative) in work days.
lag_planned_days: Planned lag (positive) or lead (negative) in work days.
subproject_ID?: Subproject identifier.
calendar_name: Calendar name for resource. Aligns with DS19/DS20.
---

# DS07

This object contains the project's contractor IPMR header data. Single object, not an array.

## Fields

K_ID: DOE contract number and CLIN(s) if applicable.
type?:FFP|FPE|FPI|CPIF|CPAF|CPDS|CPE|CPP: Contract type.
UB_bgt_days: UB budget (work days).
UB_est_days: EAC for UB scope (work days).
UB_bgt_dollars: UB budget (dollars).
UB_est_dollars: EAC for UB scope (dollars).
MR_bgt_dollars: MR excluding OTB and OTS.
MR_rpg_dollars: MR reprogramming adjustment.
AUW_dollars: Authorized unpriced work. Excludes fee and profit.
NCC_dollars: Negotiated contract cost. Excludes fee and profit.
CBB_dollars: Contract budget base (NCC plus AUW).
OTB_OTS_date?: Date last OTB or OTS approved by DOE.
TAB_dollars: Total allocated budget. Excludes fee and profit.
profit_fee_dollars?: Target profit or fee.
EAC_PM_best_dollars?: Contractor's best case EAC. Excludes fee and profit.
EAC_PM_likely_dollars: Contractor's most likely EAC. Excludes fee and profit.
EAC_PM_worst_dollars?: Contractor's worst case EAC. Excludes fee and profit.
EAC_PM_best_date: Contractor's best case completion date.
EAC_PM_likely_date: Contractor's most likely completion date.
EAC_PM_worst_date: Contractor's worst case completion date.
escalation_rate_pct: Escalation rate for TAB.
QRA_CL_cost_pct: QRA confidence level for cost.
QRA_CL_schedule_pct: QRA confidence level for schedule.
threshold_cost_cum_dollar_fav: Cost threshold cumulative favorable (dollars).
threshold_cost_cum_dollar_unfav: Cost threshold cumulative unfavorable (dollars).
threshold_cost_cum_pct_fav: Cost threshold cumulative favorable (percent).
threshold_cost_cum_pct_unfav: Cost threshold cumulative unfavorable (percent).
threshold_cost_inc_dollar_fav: Cost threshold incremental favorable (dollars).
threshold_cost_inc_dollar_unfav: Cost threshold incremental unfavorable (dollars).
threshold_cost_inc_pct_fav: Cost threshold incremental favorable (percent).
threshold_cost_inc_pct_unfav: Cost threshold incremental unfavorable (percent).
threshold_cost_VAC_dollar_fav: VAC threshold favorable (dollars).
threshold_cost_VAC_dollar_unfav: VAC threshold unfavorable (dollars).
threshold_cost_VAC_pct_fav: VAC threshold favorable (percent).
threshold_cost_VAC_pct_unfav: VAC threshold unfavorable (percent).
threshold_schedule_cum_dollar_fav: Schedule threshold cumulative favorable (dollars).
threshold_schedule_cum_dollar_unfav: Schedule threshold cumulative unfavorable (dollars).
threshold_schedule_cum_pct_fav: Schedule threshold cumulative favorable (percent).
threshold_schedule_cum_pct_unfav: Schedule threshold cumulative unfavorable (percent).
threshold_schedule_inc_dollar_fav: Schedule threshold incremental favorable (dollars).
threshold_schedule_inc_dollar_unfav: Schedule threshold incremental unfavorable (dollars).
threshold_schedule_inc_pct_fav: Schedule threshold incremental favorable (percent).
threshold_schedule_inc_pct_unfav: Schedule threshold incremental unfavorable (percent).
is_ACWP_at_CA?:Y|N: Whether ACWP is collected at control account level.
---

# DS08

This data set contains the project's contractor WAD data for all approved work authorization documents.

## Fields

WAD_ID: Unique WAD identifier.
revision?: WAD version.
title: WAD title.
WBS_ID: CA or SLPP WBS identifier.
WBS_ID_WP?: WP or PP WBS identifier.
auth_PM_date?: Date WAD last signed by project manager.
auth_CAM_date?: Date WAD last signed by CAM.
auth_WPM_date?: Date WAD last signed by WPM.
initial_auth_date?: Date WAD initially signed by project manager.
EVT?:A|B|C|D|E|F|G|H|J|K|L|M|N|O|P|NA: Earned value technique if WBS_ID_WP provided.
budget_labor_dollars: Total budget for labor (dollars).
budget_material_dollars: Total budget for material (dollars).
budget_subcontract_dollars?: Total budget for subcontract (dollars).
budget_ODC_dollars: Total budget for ODC (dollars).
budget_indirect_dollars: Total budget for indirect (dollars).
budget_labor_hours: Total labor budget (hours).
POP_start_date: Period of performance start date.
POP_finish_date: Period of performance finish date.
CAM: CAM who signed WAD.
WPM?: WP manager if applicable.
PM: Contractor project manager.
narrative: CA scope statement from WAD.
---

# DS09

This data set contains the project's contractor change control log data.

## Fields

CC_log_ID: CC identifier.
CC_log_ID_supplement?: Supplemental CC_log_ID for revisions.
CC_log_ID_original_UB?: Original CC_log_ID for UB distribution changes.
type:BCP|BCR|Funding: Change type.
K_mod_ID?: Contract modification ID when applicable.
description: Scope description of approved change.
approved_date: Approval date.
implementation_date: Date implemented in contractor systems.
dollars_delta?: Total budgeted dollars change. Sum of DS10 transactions.
hours_delta?: Total budgeted hours change. Sum of DS10 transactions.
PM?: Contractor project manager.
risk_ID?: Risk IDs addressed. Semicolon separated. Aligns with DS15.
---

# DS10

This data set contains the project's contractor change control log transaction details for DS09. Transactions should zero-sum unless new budget is added to CBB.

## Fields

transaction_ID: Unique transaction identifier.
category:CNT|DB|UB|MR|OTB|OTS|OTB-OTS|funding|profit-fee: Transaction category.
CC_log_ID: CC identifier from DS09.
description?: Transaction summary.
WBS_ID?: WBS identifier. Project level for UB/MR/CNT, CA or lower for DB.
dollars_delta?: Dollar change to the balance.
hours_delta?: Hours change to the balance.
AUW:Y|N: Transaction is for AUW.
NTE_dollars_delta?: Not to exceed for AUW transactions.
POP_start_date?: Modified POP start date if applicable.
POP_finish_date?: Modified POP finish date if applicable.
---

# DS11

This data set contains the project's contractor variance data and narratives.

## Fields

WBS_ID: WBS identifier. Use project level WBS for project-level narratives.
narrative_type?:100|110|120|130|140|150|160|170|200|300|400|500: Narrative type.
 100-170 = project level types
 200 = SLPP
 300 = control account
 400 = planning package
 500 = work package
narrative_overall?: Overall narrative for types < 200.
narrative_RC_SVi?: Root cause for incremental schedule variance.
narrative_RC_CVi?: Root cause for incremental cost variance.
narrative_RC_SVc?: Root cause for cumulative schedule variance.
narrative_RC_CVc?: Root cause for cumulative cost variance.
narrative_impact_technical?: Technical impact narrative.
narrative_impact_schedule?: Schedule impact narrative (cumulative).
narrative_impact_cost?: Cost impact narrative (cumulative).
narrative_impact_schedule_inc?: Schedule impact narrative (incremental).
narrative_impact_cost_inc?: Cost impact narrative (incremental).
CAL_ID?: Corrective action log IDs. Semicolon separated.
approved_date?: CAM approval date.
---

# DS12

This data set contains the project's contractor corrective action data for DS11 variances.

## Fields

CAL_ID: Corrective action log identifier.
transaction_ID?: Unique transaction identifier.
narrative_schedule?: Corrective action for schedule variance.
narrative_cost?: Corrective action for cost variance.
POC: Person responsible for closing action.
status:open|closed: Current status.
initial_date: Date of initial corrective action.
original_due_date: Original due date.
forecast_due_date: Expected closure date. Equals closed_date if closed.
closed_date?: Actual closure date.
---

# DS13

This data set contains the project's subcontract work data as reported to the contractor.

## Fields

subK_ID: Subcontract identifier.
subK_task_ID: Task ID from subcontract schedule.
task_ID: Associated DS04.task_ID.
BCWSc_dollars?: BCWS cumulative (dollars).
BCWPc_dollars?: BCWP cumulative (dollars).
ACWPc_dollars?: ACWP cumulative (dollars).
BAC_dollars?: BAC (dollars).
BAC_initial_dollars?: Initial BAC (dollars).
EAC_dollars?: EAC (dollars).
BL_start_date?: Baseline start date.
BL_finish_date?: Baseline finish date.
FC_start_date?: Forecast start date.
FC_finish_date?: Forecast finish date.
AS_date?: Actual start date.
AF_date?: Actual finish date.
MR_dollars?: MR remaining (dollars).
MR_initial_dollars?: Initial MR (dollars).
profit_fee_dollars?: Profit fee remaining (dollars).
profit_fee_earned_dollars?: Profit fee earned (dollars).
profit_fee_initial_dollars?: Initial profit fee (dollars).
subK_PO_ID?: Purchase order identifier.
flow_down:Y|N: DOE Order 413.3B CRD flow down required.
---

# DS14

This data set contains the project's contractor HDV-CI data.

## Fields

HDV_CI_ID: HDV-CI identifier. Aligns with DS04.HDV_CI_ID.
description: HDV-CI description.
subK_ID?: Subcontract identifier.
subK_PO_ID?: Purchase order identifier.
equipment_ID?: Equipment identifier.
---

# DS15

This data set contains the project's contractor risk log.

## Fields

risk_ID: Unique risk identifier.
revision?: Current revision number.
description: Risk description. Format: if/then statement.
type:T|O: Threat or opportunity.
manager: Risk manager name.
owner:federal|contractor: Risk owner.
approved_date?: Date risk handling approved.
realized_date?: Date risk realized.
closed_date?: Date risk closed (no longer tracked but remains on log).
probability_schedule_min_pct: Schedule probability min (percent).
probability_schedule_max_pct: Schedule probability max (percent).
probability_cost_min_pct: Cost probability min (percent).
probability_cost_max_pct: Cost probability max (percent).
risk_handling:avoid|mitigate|transfer|accept: Risk handling approach.
basis?: Notes.
---

# DS16

This data set contains the project's contractor risk log tasks.

## Fields

risk_ID: Risk identifier. Aligns with DS15.risk_ID.
risk_task_type: Task type - event (trigger) or impact.
task_ID: Event or impact task ID. Aligns with DS04.task_ID.
impact_schedule_min_days?: Schedule impact min (calendar days) if type = impact.
impact_schedule_likely_days?: Schedule impact likely (calendar days) if type = impact.
impact_schedule_max_days?: Schedule impact max (calendar days) if type = impact.
impact_cost_min_dollars?: Cost impact min (dollars) if type = impact.
impact_cost_likely_dollars?: Cost impact likely (dollars) if type = impact.
impact_cost_max_dollars?: Cost impact max (dollars) if type = impact.
---

# DS17

This data set contains the project's contractor WBS EU data.

## Fields

WBS_ID: WP or PP WBS identifier.
EOC:labor|material|subcontract|ODC: Element of cost.
EU_min_dollars: EU min (dollars) work remaining.
EU_likely_dollars: EU most likely (dollars) work remaining.
EU_max_dollars: EU max (dollars) work remaining.
time_dependent:Y|N: WBS has time-dependent tasks.
justification_EU?: Basis for non-triangular distribution.
subproject_ID?: Unique subproject identifier.
---

# DS18

This data set contains the project's contractor task EU data.

## Fields

schedule_type:BL|FC: Baseline or forecast schedule.
task_ID: Unique task identifier.
EU_min_days: EU min (work days) remaining.
EU_likely_days: EU most likely (work days) remaining.
EU_max_days: EU max (work days) remaining.
justification_EU?: Basis for non-triangular distribution or incomplete task.
subproject_ID?: Unique subproject identifier.
---

# DS19

This data set contains the project's contractor IMS standard work week calendar data.

## Fields

calendar_name: Unique calendar name.
hours_per_day: Hours per day.
std_01_Mon_shift_A_start_time?: Monday shift A start time.
std_01_Mon_shift_A_stop_time?: Monday shift A stop time.
std_01_Mon_shift_B_start_time?: Monday shift B start time.
std_01_Mon_shift_B_stop_time?: Monday shift B stop time.
std_01_Mon_shift_C_start_time?: Monday shift C start time.
std_01_Mon_shift_C_stop_time?: Monday shift C stop time.

[Pattern repeats for days 02-07 (Tue-Sun) with fields]:
std_[##]_[Day]_shift_[A|B|C]_[start|stop]_time?

subproject_ID?: Unique subproject identifier.

Note: Maximum 3 shifts per day (A, B, C) in half-hour increments with no overlaps.
---

# DS20

This data set contains the project's contractor IMS calendar exception data.

## Fields

calendar_name: Calendar name.
exception_date: Date of exception.
exception_work_day:Y|N: Exception is a work day.
 If Y, entire day is exception (shift times not needed).
 If N, provide shift times below.
exception_shift_A_start_time?: Exception shift A start time.
exception_shift_A_stop_time?: Exception shift A stop time.
exception_shift_B_start_time?: Exception shift B start time.
exception_shift_B_stop_time?: Exception shift B stop time.
exception_shift_C_start_time?: Exception shift C start time.
exception_shift_C_stop_time?: Exception shift C stop time.
subproject_ID?: Unique subproject identifier.

Note: Maximum 3 shifts (A, B, C) in half-hour increments with no overlaps.
---

# DS21

This data set is deprecated and should not be used.
---

# DS22

This data set contains the project's contractor financial calendar.

## Fields

calendar_name: Unique calendar name.
period_date: Period end date. Aligns with CPP_status_date.
period_ID: Period identifier. Sequential starting from 1.
---

# Acronyms

ACWP: Actual Cost of Work Performed
AF: Actual Finish
AS: Actual Start
AUW: Authorized Unpriced Work
BAC: Budget At Complete
BCP: Baseline Change Proposal
BCR: Baseline Change Request
BCWP: Budgeted Cost of Work Performed
BCWS: Budgeted Cost of Work Scheduled
BL: Baseline
BWC: Base Work Construct
CA: Control Account
CAL: Corrective Action Log
CAM: Control Account Manager
CBB: Contract Budget Base
CC: Charge Code
CD: Critical Decision
CL: Confidence Level
CLIN: Contract Line Item Number
CNT: Contingency
CPAF: Cost Plus Award Fee
CPDS: Cost Plus Fixed Fee
CPE: Cost Plus Expenses
CPIF: Cost Plus Incentive Fee
CPP: Contractor Project Performance
CPP Status Date: The "as-of" data export date for a given PARS CPP Upload file
CRD: Contract Requirements Document
CS: Constraint
CV: Cost Variance
DB: Distributed Budget
DOE: Department of Energy
DS: Data Set
EAC: Estimate At Completion
EF: Early Finish
EOC: Elements of Cost
ES: Early Start
ETC: Estimate To Complete
ETCc: Cumulative Estimate to Complete (total work remaining)
ETCi: Incremental Estimate to Complete (work remaining to be done in this month)
EU: Estimate Uncertainty
EVT: Earned Value Technique
EVMS: Earned Value Management System
FC: Forecast
FF: Finish to Finish
FFP: Firm Fixed Price
FM: Finish Milestone
FPE: Fixed Price Escalation
FPI: Fixed Price Incentive
FS: Finish to Start
FTE: Full-Time Equivalent
FY: Fiscal Year
HDV-CI: High Dollar Value - Critical Item
IMP: Integrated Master Plan
IMS: Integrated Master Schedule
IPMR: Integrated Program Management Report
IPMR F1: Integrated Program Management Report Format 1 (WBS)
IPMR F2: Integrated Program Management Report Format 2 (OBS)
IPMR F3: Integrated Program Management Report Format 3 (Changes)
IPMR F4: Integrated Program Management Report Format 4 (Staffing)
LF: Late Finish
LOE: Level of Effort
LS: Late Start
MR: Management Reserve
NA: Not Applicable
NCC: Negotiated Contract Cost
NTE: Not To Exceed
OBS: Organizational Breakdown Structure
ODC: Other Direct Costs
OTB: Over Target Baseline
OTS: Over Target Schedule
PARS: Project Assessment and Reporting System
PC: Percent Complete
PM: Project Manager, or DOE Office of Project Management
PMB: Performance Measurement Baseline
PO: Purchase Order
POC: Point of Contact
POP: Period of Performance
PP: Planning Package
QRA: Quantitative Risk Analysis
RAM: Responsibility Assignment Matrix
RC: Root Cause
RD: Resource Dependent
RMT: Risk Mitigation Task
RPG: Reprogramming
SF: Start to Finish
SLPP: Summary Level Planning Package
SM: Start Milestone
SS: Start to Start
subK: Subcontract
SV: Schedule Variance
SVT: Schedule Visibility Task
TAB: Total Allocated Budget
TD: Task Dependent
UB: Undistributed Budget
UOM: Unit of Measure
VAC: Variance At Completion
WAD: Work Authorization Document
WBS: Work Breakdown Structure
WP: Work Package
WPM: Work Package Manager
WS: WBS Summary
ZBA: Zero Budget Activity