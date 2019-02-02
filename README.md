# Design

This CLI program `report.py` will outputs:

1. The most viewed articles based on a given number
2. The most viewed authors based on a given number
3. Days where requests lead to errors based on a given threshold.

# Usage

This program requires 3 arguments.

```
$ python3 report.py [N] [M] [P]
```

1. An integer **_N_** where **_N_** > 1. This will be used to output the most popular **_N_** articles. 

2. An integer **_M_** where **_M_** > 1. This will be used to output the most popular **_M_** authors. 

3. An integer **_P_** where **_P_** >= 0. This will be used as a percentage rounded to the nearest ones to output days where more than **_P_**% of requests lead to errors.


# Example Usage & Output

```
$ python3 report.py 3 4 1

-----3 Most Popular Articles-----

"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views

-----4 Most Popular Authors-----

"Ursula La Multa" -- 507594 views
"Rudolf von Treppenwitz" -- 423457 views
"Anonymous Contributor" -- 170098 views
"Markoff Chaney" -- 84557 views

-----Days HTTP Error Status Exceeded 1.00%-----

July 17, 2016 -- 2.26% errors
```
