I fixed given clauses like this:

outside_power => w5
-outside_power => -w5

(w5 & cb1) => w3  
**(w3 & cb1) => w5**  (w5 & cb1) => w3 
w6 => p2
w3 => p1
(w3 & -s1) => w2  
s1 => -w2
**-s1 => w1 **  s1=> w1
**(w1 & s1) => w3**  (w3 & s1 ) => w1
**(w2 & -s1) => w3**   (w3 & -s1) => w2
**(-w2 & -s2) => w0**   (-w2 & -s2) => -w0
(w1 & s2) => w0
(w0 & -s2) => w2
(w0 & s2) => w1
w0 => l1
l1 => w0
w4 => l2
(w3 & s3) => w4
l2 => w4
-s3 => -w4
