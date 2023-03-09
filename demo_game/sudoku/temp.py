"""

input4 = [None, None,   None,   None,   None,   None,   None,   None,   None]


# input0 = [None, 9,      4,      None,   3,      None,   1,      None,   None]
# input1 = [8,    1,      2,      7,      None,   None,   None,   9,      6]
# input2 = [3,    None,   None,   1,      9,      None,   None,   None,   None]
# input3 = [None, 3,      None,   9,      None,   4,      6,      None,   None]
# input4 = [None, None,   8,      6,      1,      3,      None,   4,      9]
# input5 = [None, None,   6,      2,      None,   None,   None,   None,   1]
# input6 = [4,    None,   3,      5,      None,   None,   None,   None,   8]
# input7 = [5,    None,   None,   None,   2,      None,   7,      None,   None]
# input8 = [None, 6,      None,   None,   None,   8,      4,      1,      5]
"""

"""
origin
0	0	0	 	5	0	0	 	3	0	0	 	
0	7	0	 	0	3	2	 	0	0	5	 	
0	3	0	 	7	6	0	 	0	0	9	 	

0	0	0	 	4	0	7	 	0	0	8	 	
0	0	0	 	0	0	0	 	0	3	0	 	
2	5	0	 	0	0	0	 	9	0	7	 	

7	2	0	 	3	0	9	 	5	0	0	 	
8	9	0	 	2	0	0	 	0	0	0	 	
0	0	5	 	0	0	0	 	0	0	6

rule 2
0	0	2	 	5	9	0	 	3	7	0	 	
0	7	9	 	0	3	2	 	0	0	5	 	
5	3	0	 	7	6	0	 	0	2	9	 	

9	0	3	 	4	2	7	 	0	5	8	 	
0	0	7	 	9	0	5	 	0	3	2	 	
2	5	0	 	0	0	3	 	9	0	7	 	

7	2	6	 	3	0	9	 	5	0	0	 	
8	9	0	 	2	5	6	 	7	0	3	 	
3	0	5	 	0	7	0	 	2	9	6


before rule 1
0	0	2	 	5	9	0	 	3	7	0	 	
0	7	9	 	0	3	2	 	0	0	5	 	
5	3	0	 	7	6	0	 	0	2	9	 	

9	0	3	 	4	2	7	 	0	5	8	 	
0	0	7	 	9	0	5	 	0	3	2	 	
2	5	0	 	0	0	3	 	9	0	7	 	

7	2	6	 	3	0	9	 	5	0	0	 	
8	9	0	 	2	5	6	 	7	0	3	 	
3	0	5	 	0	7	0	 	2	9	6

"""