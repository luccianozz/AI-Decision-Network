# Decision network

![alt text](https://github.com/luccianozz/AI-Decision-Network/blob/main/dn.png?raw=true)

This diagram models a decision about whether to cheat at two different time instances.

Suppose 

P(watched)=0.4, 

P(trouble1|cheat1,watched)=0.8, and Trouble1 is true with probability 0 for the other cases.

Suppose the conditional probability P(Trouble2|Cheat2,Trouble1,Watched) is given by the following table:



|Cheat2	| Trouble1 | Watched | P(Trouble2=t)|
| ------- | ------- | ------- | ----------- | 
|t	|t	|t	|1.0|
|t	|t	|f	|0.3|
|t	|f	|t	|0.8|
|t	|f	|f	|0.0|
|f	|t	|t	|0.3|
|f	|t	|f	|0.3|
|f	|f	|t	|0.0|
|f	|f	|f	|0.0|

Suppose the utility is given by

| Trouble2 | Cheat2 | Utility |
| -------- | ------ | ------- |
|t	| t	-| 30|
|t	|f	|70|
|f	|t	|-70|
|f	|f	|100| 
