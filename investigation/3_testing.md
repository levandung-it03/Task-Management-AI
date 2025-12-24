# Split Test/Train
If we split it in a normal way that take `0.1` or `0.2` the size of `dataset`, it may fail when we use it to calculate
the testing-output-score, because we made the model have to recognize
> This input of (level, prior, free, used, is_on_time) belongs to which user?

not our problem
> This input can be done by which users in a ranked list?

