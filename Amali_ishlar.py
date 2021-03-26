import pygal

line_chart = pygal.Line()
line_chart.title = 'Statistika'
line_chart.x_labels = ['Fevral', 'Mart', 'Aorel', 'May']
line_chart.add('Fezbuk',[9.24,13.7,16.24,18.07])
line_chart.add('Instagram',[24.03, 26.81,21.03,22.77])
line_chart.add('Youtube',[8.95,15.81,19.19,22.67])
line_chart.render_in_browser()