import pandas as pd

input_path = "assets/data/glossary.xls"
output_path = "_posts/2019-06-25-glossary-for-nlp.md"

header = [
				'---',
				'layout: post',
				'title: "glossary"',
				'comments: true',
				'description: "glossary for nlp"',
				'showtags: true',
				'tags: nlp glossary',
				'---'
		]
space = "   "
next_line = "\n"
excel_header = ["Name", "Description", "Example"]
table_line = "--- | --- | ---:"
df = pd.read_excel(input_path)
with open(output_path, 'w') as f:
	for ele in header:
		f.write(ele);
		f.write(next_line)
	
	f.write("#### NLP glossary")
	f.write(next_line)
	f.write(next_line)
	f.write(' | '.join(excel_header))
	f.write(next_line)
	f.write(table_line)
	f.write(next_line)
	for idx, row in df.iterrows():
		f.write(' | '.join(row))
		f.write(next_line)
