# 16.8 Prune To Range

This utility provides a faster alternative to "Export From Range" by pruning the selected contracts so that it begins in the selected 'From' period and ends in the 'To' period. This eliminates the import step required by "Export From Range."

## Figure 16.46: Prune To Range Dialog

Note that pruning the contract will delete period data prior to the 'From' date, as well as time-phased future-period data after the 'To' date. The newly pruned contract will have correct BCWS, BCWP, and ACWP values, but will need to be recalculated in order for other calculated metrics to be correct.

This method is much quicker than the "Export From Range" method, but also permanently deletes data, so caution is advised.
