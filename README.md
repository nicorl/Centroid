# Information

The script `cluster_points.py` is able to take pairs of values (x,y) and return back an array where points are agrupped according to a limit value.

## Using the script

Open the file `cluster_points.py` and modify next parameters:

* **muestra**: array with the _x_,_y_ coords.
* **limite**: value limit to gather them.

## Example of use

1. Open a terminal

2. Go to the path where `cluster_points.py` is saved

3. type `python cluster_points.py` as follows

> _(nico) \home\nico\centroid>_ python cluster_points.py

Being `muestra`

```python
muestra = [[1,10],[1,15],[20,20],[20,25],[30,80],[4,18],[3,18],[2,18],[30,30],[80,80],[30,75],[85,85],[85,85]]
```
Result
> _(nico) \home\nico\centroid>_ [0, 0, 2, 2, 4, 0, 0, 0, 8, 9, 4, 9, 9]

Index | Value | Index of similar values
----- | ----- | -----
0 | [1,10] | 1,5,6,7
1 | [1,15] | 0,5,6,7
2 | [20,20] | 3
3 | [20,25] | 4
4 | [30,80] | 10
5 | [4,18] | 0,1,6,7
6 | [3,18] | 0,1,5,7
7 | [2,18] | 0,1,5,6
8 | [30,30] | -
9 | [80,80] | 11,12
10 | [30,75] | 4
11 | [85,85] | 9,12
12 | [85,85] | 9,11
