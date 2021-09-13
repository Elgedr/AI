**The aim of this task was to implement 3 path search algorithms: Breadth First Seach, Greedy search,  A* ; and examine how effective they are.**

I tested all 3 algorithms in ASCII-art cards of different sizes:
300X300;
600X600;
900X900;

I measured the number of iterations and and the path length for all algorithms.

There are my results:

BFS: 
	300 x 300 {iterations: 61438, path length: 555}
	600 x 600 {iterations: 256493, path length: 1248}
	900 x 900 {iterations: 582466, path length: 1844}

Greedy:
	300 x 300 {iterations: 3048, path length: 831}
	600 x 600 {iterations: 14255, path length: 2356}
	900 x 900 {iterations: 16967, path length: 3088}

A*:
	300 x 300 {iterations: 10078, path length: 555}
	600 x 600 {iterations: 77392, path length: 1248}
	900 x 900 {iterations: 119027, path length: 1844}

Based on measurement results It is seen, that the fastest algorithm is Greedy's Best First Search algorithm. Compared to other algorithms Its has the smallest amount of iterations, but its path lengths are the largest so this means, that this algorithm can't find
the shortest path. 

The path lengths found by the Greedy and A * algorithms are similar and much shorter than
The paths found by the Greedy algorithm. 

However, in terms of iterations, the algorithm A* coped faster.
Greedy typically runs faster than A* and BFS Algorithms but doesn’t produce optimal paths. A* is a good choice for most pathfinding needs
