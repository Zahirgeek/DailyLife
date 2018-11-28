# 分类问题
## [iris_sample](https://github.com/Zahirgeek/DailyLife/blob/master/Machine_Learning/KNN/iris_sample.ipynb)(机器学习案例:鸢尾属植物数据集)
- 机器学习框架 sklearn
	- 导包

			from sklearn.neighbors import KNeighborsClassifier

- 读取数据

		iris = datasets.load_iris()
		# 两个属性data(数据), target(目标值)
		# data: 花萼长度，花萼宽度，花瓣长度，花瓣宽度
		# target: 三类不同的鸢尾属植物：Iris Setosa，Iris Versicolour，Iris Virginica
- 定义训练数据

		X_train = X[: 105]
		y_train = y[: 105]

- 定义测试数据

		X_test = X[105: ]
		y_test = y[105: ]

- 定义knn分类器

		knn = KNeighborsClassifier(n_neighbors=5)
- 第一步进行训练
	
		knn.fit(X_train, y_train)
- 第二步进行测试

		y_ = knn.predict(X_test)

## [手写数字识别](https://github.com/Zahirgeek/DailyLife/blob/master/Machine_Learning/KNN/%E6%89%8B%E5%86%99%E6%95%B0%E5%AD%97%E8%AF%86%E5%88%AB.ipynb)

## [癌症检测](https://github.com/Zahirgeek/DailyLife/blob/master/Machine_Learning/KNN/%E7%99%8C%E7%97%87%E6%A3%80%E6%B5%8B.ipynb)
- 归一化

## [movement identification](https://github.com/Zahirgeek/DailyLife/blob/master/Machine_Learning/KNN/movement%20identification.ipynb) 人类动作识别

## [Salary](https://github.com/Zahirgeek/DailyLife/blob/master/Machine_Learning/KNN/Salary.ipynb) 预测年收入是否大于50K美元
- 将str转换为可以计算的值
# 回归问题
## [KNN回归问题](https://github.com/Zahirgeek/DailyLife/blob/master/Machine_Learning/KNN/KNN%E5%9B%9E%E5%BD%92%E9%97%AE%E9%A2%98.ipynb)
- 基础: 预测正弦波
