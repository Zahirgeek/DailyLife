# 简明matplotlib api入门(matplotlib_hello)
## 图片和子图 
- 生成一个新的空白图片
	- fig = plt.figure()
## 颜色,标记和线类型

	# ko 黑色凸点
	plt.plot(np.random.randn(30).cumsum(), 'ko--')
- linestyle 线条样式
- drawstyle 修改线类型
## 刻度,标签和图例
### 设置标题,轴标签和刻度标签
- ax.set_xticks 设置x轴刻度
	
		# rotation=30将x轴刻度标签旋转30度,
		labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
		# 设置标题
		ax.set_title

- 批量设置绘图属性

		props = {
    		'title': 'My first matplotlib plot',
    		'xlabel': 'Stages'
		}
		ax.set(**props)

### 添加图例
- label

## 注释与子图加工
- 注释
	- ax.annotate
	- ax.text(x, y, s, fontdict=None, withdash=False, **kwargs)
- 添加图形
	- plt.Rectangle 矩形
	- plt.Circle 圆
	- plt.Polygon 三角形

	ax.add_patch(rect) 加入子图

## 将图片保存到文件
- plt.savefig(*args, **kwargs)

## matplotlib设置
- plt.rc(*args, **kwargs)