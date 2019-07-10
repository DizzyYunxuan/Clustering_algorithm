# Clustering Algorithm

* BSAS (Basic Sequential Algorithmic Scheme)
* MBSAS (Modified Basic Sequential Algorithmic Scheme)
* TTSAS (Two-threshold sequential scheme )

####1.BSAS
1. For every `xi` in `unclassified list`, find the l2 min_distance between every `xi` and every class `mean center`. 
2. If `min_distance > threshold`, set `xi` to be a new class, else set `xi` to the closest class.
3.Repeat the above process until `unclassified list` is null.
    
####2.MBSAS
1. For every `xi` in `unclassified list`, find the l2 min_distance between every `xi` and every class `mean center`. 
2. At first traversal, if `min_distance > threshold`, set xi to be a new class.
3. At second traversal, classify every `xi` in `unclassified list` to their closest class respectivly.
####3.TTSAS
1.For every `xi` in `unclassified list`, find the l2 min_distance between every `xi` and every class `mean center`. 
2.At first traversal, If `min_distance` > `threshold2`, set `xi` to be a new class.
else if `min_distance` < `threshold1`, set `xi` to the closest class.
3.At second traversal, classify all `xi` in `unclassify list` to their closest class respectivly.