I fixed given clauses like this:

(bold is wrong)

- outside_power => w5
- -outside_power => -w5

- (w5 & cb1) => w3  
- **(w3 & cb1) => w5**  (w5 & cb1) => w3 
- w6 => p2
- w3 => p1
- (w3 & -s1) => w2  
- s1 => -w2
- **-s1 => w1 **  s1=> w1
- **(w1 & s1) => w3**  (w3 & s1 ) => w1
- **(w2 & -s1) => w3**   (w3 & -s1) => w2
- **(-w2 & -s2) => w0**   (-w2 & -s2) => -w0
- (w1 & s2) => w0
- (w0 & -s2) => w2
- (w0 & s2) => w1
- w0 => l1
- l1 => w0
- w4 => l2
- (w3 & s3) => w4
- l2 => w4
- -s3 => -w4


All clauses I was working with were:
- ["-op", "w5"]
- ["-w3", "-s3", "w4"]
- ["op", "-w5"]
- ["-w5", "-cb1", "w3"]
- ["-w5", "-cb2", "w6"]
- ["-w0", "l1"]
- ["w0", "-l1"]
- ["-w6", "p2"]
- ["w6", "-p2"]
- ["-w3", "p1"]
- ["w3", "-p1"]
- ["-w4", "l2"]
- ["w4", "-l2"]
- ["-w2", "-s2", "-w0"]
- ["-w3", "-s1", "w1"]
- ["-w3", "s1", "w2"]
- ["-w1", "-s2", "w0"]
- ["-w2", "s2", "w0"]
>     For the first question:
>     KB1 = [["op"], ["cb2"]]
>     neg_alpha1 = ["-p2"]
> 
>     For the second question:
>     KB2 = [["op"], ["cb1"], ["-s1"], ["s2"]]
>     neg_alpha2 = ["l1"]
> 
>     For the third question:
>     KB3 = [["op"], ["-l1"], ["s1"], ["s2"]]
>     neg_alpha3 = ["cb1"]


