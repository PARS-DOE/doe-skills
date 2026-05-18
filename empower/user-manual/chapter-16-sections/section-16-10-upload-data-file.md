# 16.10 Upload Data File

Choosing the command Upload Data File brings up the dialog shown in Figure 16.111.

**Figure 16.111: Upload Data, Step 1**

The user presses the Choose File... button and a standard file selection dialog box comes up. The user browses to the location of the Excel file he has earlier downloaded and edited, as described in the previous section. Note that the user can actually open a single Excel file, or a zipped file containing one or more Excel files resulting from the Download Data command. Once the user has chosen a file, the dialog will look like Figure 16.112.

**Figure 16.112: Upload Data, Step 2**

Next the user presses the Upload button. The result will be the dialog shown in Figure 16.113.

**Figure 16.113: Upload Data, Step 3**

If the user selected an Excel file, that file will be shown in the select box. If the user selected a zip file containing a number of Excel files, those files will all be displayed in the select box. Now the user selects the desired file(s).

## Generating Import Messages (Dry Run)

If the user checks the option "Generate import messages only" and then presses the Import button, Empower will not actually upload the data to the database, but it will show a list of the actions it would have taken if the option were not checked. That is, it allows the user to make a dry run to ensure that the upload will do what the user actually intended (keeping in mind the old adage that computers do what you tell them to do, not always what you want them to do). Figure 16.114 shows the result of such a dry run.

**Figure 16.114: Upload Data, Step 3, Generate import messages only (dry run)**

Now, if the dialog says the upload succeeded, but there are no updating, inserting, or deleting lines, you probably forgot to put the codes a, c, or d in the action column (since there would be no point in doing an upload if you didn't want to make changes).

From the figure, we can see that Empower thinks we want to update the contract in row 9 of the spreadsheet and delete the contract on row 10. That's exactly what we wanted to do, so we press Upload Another. That puts us back at the screen where we chose the file to upload. We select the same file, and continue through the steps already described, except that this time we don't check "Generate import messages only." We press Import, and we are rewarded with the dialog of Figure 16.115.

The user will be shown the progress of the import in real time, and the result at the end, as shown in Figure 16.115 below.

**Figure 16.115: Upload Data, Step 4**

## Warnings During Upload

There are two warnings you might encounter during this process:

1. **Warning: Data was downloaded more than N hours ago**
   - This is to remind the user that other changes might have been made to the database between the download and upload that might not be consistent with the changes the administrator is making. For best results, the download-edit-upload cycle should be quite short. (How short will depend on your environment and usage habits.)

2. **Warning: File and current data sources do not match**
   - This means that the spreadsheet was downloaded from one database and uploaded to another database; this is not a best practice for the following reason. It is unlikely that the database id values for a given data item will be the same in both databases. For instance, contract MOH-2 might have ContrID = 2 in one database, and ContrID = 12 in another. Updating or deleting a row in the spreadsheet under these circumstances is likely to fail. Adding a row, on the other hand, will not be affected by downloading from one database and uploading to another.

## Write Permissions Verification

It should also be mentioned at this point that Empower checks to make sure that a user has write permissions to all the contracts he or she is attempting to upload via this command.
