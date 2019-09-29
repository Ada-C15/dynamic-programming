# Dynamic Programming

Dynamic programming is a st

## Wave 1 Newman-Conway Sequence

[Newman-Conway sequence] is the one which generates the following integer sequence.  1 1 2 2 3 4 4 4 5 6 7 7….. and follows below recursive formula.

```
P(0) = 0
P(1) = 1
P(2) = 2
for all n > 2
P(n) = P(P(n - 1)) + P(n - P(n - 1))
```

Given a number n then print n terms of Newman-Conway Sequence

Examples:

```
Input : 13
Output : 1 1 2 2 3 4 4 4 5 6 7 7 8

Input : 20
Output : 1 1 2 2 3 4 4 4 5 6 7 7 8 8 8 8 9 10 11 12
```

You should be able to do this in O(n) time complexity.

## 
