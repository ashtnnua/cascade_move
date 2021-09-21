# cascade_move

Wrapper function to sort a DataFrame at a series level by moving NULLS around, and retaining the preference order of non-NULLS.

As an example, I am creating a 8x20 table. 
This table represents 8 options chosen by 20 people listed in the order of their preferences.
The columns p1 to p8 correspond to the preference for the chosen option. (p1-p8 arranged from the highest to lowest or vice-versa)

df.head()
 	
|  |p1   |p2 	|p3 	|p4 	|p5 	|p6 	|p7 	|p8 |
|---|---|---|---|---|---|---|---|---|
|0	|Opt3 |Opt8 |Opt7 |Opt2 |Opt5 |Opt4 |Opt10|Opt9|
|1	|Opt9 |Opt5 |Opt10|Opt7 |Opt4 |Opt6 |Opt1 |Opt3|
|2	|Opt8 |Opt5 |Opt2 |Opt10|Opt1 |Opt4 |Opt6 |Opt7|
|3	|Opt2 |Opt7 |Opt5 |Opt8 |Opt10|Opt6 |Opt3 |Opt4|
|4	|Opt6 |Opt5 |Opt3 |Opt8 |Opt2 |Opt1 |Opt7 |Opt10|

In a scenario where some of these options have to be dropped, the preference list for each record has to be readjusted
(eg: A personal shopper pooling orders for multiple customers has to update the preference list based on the in-store availability)

Dropping "opt3", "opt5", "opt7"

df.head()

|  |p1   |p2 	|p3 	|p4 	|p5 	|p6 	|p7 	|p8 |
|---|---|---|---|---|---|---|---|---|
|0	|   |Opt8 |  |Opt2 |  |Opt4 |Opt10|Opt9|
|1	|Opt9 |  |Opt10|   |Opt4 |Opt6 |Opt1 |  |
|2	|Opt8 |  |Opt2 |Opt10|Opt1 |Opt4 |Opt6 |  |
|3	|Opt2 |  |  |Opt8 |Opt10|Opt6 |  |Opt4|
|4	|Opt6 |  |   |Opt8 |Opt2 |Opt1 |   |Opt10|


This function attempts to shuffle and sort the dataframe such that all the non-NULL options are moved to the front(or back) of the preference list.

As an added functionality, the non-NULLs can be moved around axis=0 as well.


df.head()

|  |p1   |p2 	|p3 	|p4 	|p5 	|p6 	|p7 	|p8 |
|---|---|---|---|---|---|---|---|---|
|0	|Opt8 |Opt2 |Opt4 |Opt10|Opt9|    |     |     |
|1	|Opt9 |Opt10|Opt4 |Opt6 |Opt1 |  |   |     |
|2	|Opt8 |Opt2 |Opt10|Opt1 |Opt4 |Opt6 |  |
|3	|Opt2 |Opt8 |Opt10|Opt6 |Opt4|    |   |   |
|4	|Opt6 |Opt8 |Opt2 |Opt1 |Opt10|   |   |     |
