"""
docs strings : helps user to understand all about this file
int.py file is created to practise string slicing datatype
version1 - created by : Sreeni on 15/02/2024
"""

# Index  --> Python index will start with 0 [ String, list, tuple, set, dataframe, series, array]
# when string/list/etc is increasing then index also increases by 1 value
# to do slicing we should use square braces [start pos : end pos : step value]
# when we are slicing we should remember 3 things
#  1. start position # Mandatory
#   2. end positing # optional
#   3. step value # optional default is +1
str = 'ETL' # E-0, T-1, L-2
print("last index ", len(str)-1)
print("str[0]", str[0])
print("str[1]", str[1])
print("str[2]", str[2])
# print("str[3]", str[3])
# print("str[8]", str[8])

str2 = 'ETL AUTOMATION'

print("str2[0:2]", str2[0:3:1]) # string will slice  upto end_pos-1

print("str2[0:5]", str2[0:5:1])

print("str2[6:11]", str2[6:11:1])

print("str2[11:6:1]", str2[11:6:1])

print("str2[11:6:-1]", str2[11:6:-1])

print("str2[9:3:-1]", str2[9:3:-1])

print("str2[9:3:-1]", str2[:])


