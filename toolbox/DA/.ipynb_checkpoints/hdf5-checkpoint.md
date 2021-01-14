# 使用p

```python

import pickle

with open('staytim_li.pkl', 'wb') as f:
    pickle.dump(staytim_li, f)
        
pkl_file = open('staytim_li.pkl', 'rb')
data1 = pickle.load(pkl_file)



```
