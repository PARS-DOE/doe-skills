# 16.3 Check Queue

This option allows the user to check the streaming status of currently queued imports or recalculations. The "Check Queue" option will only appear on the menu if queueing is enabled for Empower. For more information on queueing, see the technical note "The Empower Watchdir Import Facility" available on the support website at http://encoreanalyticsllc.freshdesk.com/support/solutions.

## Check Queue Window

The "Check Queue" window displays items listed in the watch queue, as well as any items currently in your "batch" directory. Items are queued alphabetically and list the data source that they will be imported into in parentheses. Items queued via the UI also indicate the type of operation that has been queued: "recalc" or "import".

Notice the button labeled "Refresh" at the bottom of the window. Toggling this button on will refresh the streaming status in the "Log Tail" portion of the window. While "Refresh" is toggled on, the "Log Tail" will periodically check for updates to the status of the currently running item. Note that while "Refresh" is active, the "Log Tail" will auto-scroll to the bottom whenever it updates. To stop refreshing, click "Stop".
