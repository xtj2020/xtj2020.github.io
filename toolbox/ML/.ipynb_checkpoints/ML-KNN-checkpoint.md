# ML-KNN模型的使用
## 读入数据
```python

path = '/CentOShome/xtjdata/xtjtemp/featuers.csv'
feature_df = pd.read_csv(path)

```

## 对标签进行堆叠

输入为X，标签为Y


## 验证集与测试集的分割

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# Split dataset to 8:2
X_train, X_test, Y_train ,Y_test = train_test_split(X, Y, test_size=0.2)

```
## 对验证集的验证
```
cls = DecisionTreeClassifier()
cls.fit(X_train, Y_train)



```
# 指标

```python



```
