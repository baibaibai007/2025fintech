import numpy as np
import re
r1 = 'a is 3,b is 6,c is 10,the answer is x'
data = re.findall(r'\d+',r1)
print(data)
data1 =list(map(int,data))
sum = np.sum(data1)
print(sum)
r2=re.sub('x',str(sum),r1)
print(r2)