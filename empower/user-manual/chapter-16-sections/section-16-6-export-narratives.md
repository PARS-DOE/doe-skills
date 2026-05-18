# 16.6 Export Narratives

Recall that on the Reports menu, there are functions to show the VAR narrative, the User narrative, the EAC narrative, and the Scope of Work narrative in the Report Window. The Export Narratives functionality allows the user to export these narratives for a selected dataset to an HTML, text, EDI file, or a PARS JSON file format.

On the Admin menu, select Export Narratives. The following dialog will appear, which allows you to select the contract, period, structure, and unit. It also allows you to choose which narratives to export (one, several, or all four), and the target format (HTML, EDI, PARS or plain text). Finally, you can choose to export all elements, sync to the sort window, export to the control account level, or just export to the reporting level (see Section 16.9.1 for how to set the reporting level). Note that the "sync to sort window" option is not available for EDI exports.

The EDI export option will produce a minimal Empower-optimized zip file that can be imported via the menu option "Admin > Import EDI File". This format can be useful for porting narrative data between databases or creating narrative-only contracts. Note that narrative role information will not be included.

## Figure 16.40: Export Narrative Selections

Once you make your selections and press Export, you'll see the status dialog below and an export file will be written to your computer in the usual fashion.

## Figure 16.41: Export Narratives Status Dialog

Here is the beginning of an exported VAR narrative in HTML format:

## Figure 16.42: Exported Narrative (partial)
