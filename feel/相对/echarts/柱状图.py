from pyecharts.charts import Bar
bar=Bar();
bar.add_xaxis(['衬衫','羊毛衫','裤子','高跟鞋','袜子'])
bar.add_yaxis('销量',[5,20,36,10,10,20])
bar.render('p1.html')