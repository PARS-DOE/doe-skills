# 16.16 Scripts Submenu

The Scripts submenu has functions for running, editing, importing, exporting, deleting, and reordering user scripts.

## Overview

Scripts are a powerful feature in Empower that allow the user to accomplish specialized tasks that are not available through the normal user interface. Scripts can be used to access the Empower database directly. Here are examples of the kinds of things that can be done with scripts:

- Clear or set the DQI flags (without having to run a full recalculation)
- List all the elements for which a given CAM is responsible
- Search and replace one CAM with another within a contract
- Clear the element or recalculation lock flags

Writing scripts requires a knowledge of SQL and of the Empower database structure, and, of course, of Empower's scripting language. Such knowledge is beyond the scope of this User's Manual. For this reason, we do not normally expect users to be writing their own scripts. If you have a need that you think might be addressed with a script, please contact Encore Analytics support (see Section 23).

Now look at the Global submenu. It is like the Global submenu for all the other custom items in Empower (reports, charts, views, prefilters), in that it displays custom items (scripts, in this case) that are available to all users—that is, they are available globally. However, there is no User menu, since only the Admin user can import scripts.

Of the six operations possible with scripts (run, edit, delete, reorder, import, and export), non-Admin users can perform run and export. All other operations are limited to the Admin user. When a non-Admin user is running Empower, the buttons associated with the Admin-only operations will be disabled (grayed-out).

## 16.16.1 Run/Edit

Clicking on Run/Edit brings up the following dialog, which allows the user to run or edit a script. Here are some examples of scripts and what it looks like to run them.

First we'll consider a script that deletes the Future ETCs for a given contract and period. You select the script ("Delete Future Etc") and click Run.

**Figure 16.154: Run/Edit Script Dialog**

The next screen tells you what the script you just chose will do.

**Figure 16.155: Delete Future Etc Script, Step 1**

Click Next. You will notice that running a script is like running a wizard in many software applications: the wizard presents one page after another, guiding the user through the process and gathering input from the user until it has enough information to perform the desired operation. Now you will see the following screen.

**Figure 16.156: Delete Future Etc Script, Step 2**

Choose the contract and the period for which you want to delete the Future ETCs. At this point, Empower has all the information it needs, as indicated by the presence of the Run button. If you change your mind, you can click the Prev button to go back. We are ready to go, so we press Run.

We are rewarded with the following screen, which tells us the status of the operation and gives us the choice of running another script.

**Figure 16.157: Delete Future Etc Script, Step 3**

Here's an example of a script that uses multiple pages to gather its inputs. Say one of your CAMs has come into a heap of money and has left the world of EVM behind. You need to assign all his accounts to a different CAM. Select "Change CAM" and press Run. You'll see the following screen.

**Figure 16.158: Change CAM, Screen 1**

Press Next. The next screen gets the contract for which you want to change CAMs:

**Figure 16.159: Change CAM, Screen 2**

Press Next, and you will be prompted to enter the name of the lucky CAM:

**Figure 16.160: Change CAM, Screen 3**

Press Next again, and you can specify who will pick up the extra work:

**Figure 16.161: Change CAM, Screen 4**

Now Empower has all the information it needs. Press Run. The changes will be made, and you'll see the usual status screen announcing the result:

**Figure 16.162: Change CAM, Screen 5**

So far, we've seen examples of scripts that changed the database without producing any output (other than status). Now here's an example of a script that does produce some output. Select "Elements for CAM" and press Run. You will see this:

**Figure 16.163: Elements for CAM, Screen 1**

Press Next. The next screen prompts for the CAM's name:

**Figure 16.164: Elements for CAM, Screen 2**

(Apparently, Troop just can't stay away from EVM.)

Press Run. The script will run, producing a status message similar to the ones we've seen before, and Empower will download the output as an Excel spreadsheet. A portion of that spreadsheet is presented below, showing that Troop is the CAM for elements in three contracts in the database: ALPHA, BOOMERANG, and MOH-2, and listing the structures and elements. (We have hidden a number of rows to make the pictures smaller.)

**Figure 16.165: Elements for CAM: Output**

From the Run/Edit dialog, you can also edit the user script. Just as with Custom Reports, editing means changing the name of the script. Here is the Edit dialog:

**Figure 16.166: Editing a Script**

Notice that you can change the name of the script, and you can also have the script shown in the menu or not, depending on whether you check "Show in Menu". (Just like the other custom items, the number of scripts that is shown on the menu is limited by screen real estate, and scripts that aren't shown on the menu can always be accessed via the Run/Edit dialog.)

## 16.16.2 Delete/Reorder

Deleting and reordering of scripts can be accomplished via the dialog of the same name, shown below.

**Figure 16.167: Delete/Reorder Scripts Dialog**

As with the other custom items, scripts that aren't shown on the Global submenu are listed in square brackets.

To delete a script, select it and press Delete.

To change the order in which scripts appear in the menu and in this dialog and the Run/Edit dialog, select the script whose position you want to change, and press the up or down arrow buttons until the script is in the desired place. Then press the Reorder button.
