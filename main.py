import os

# Get the list of HTML files in the folder
html_files = os.listdir("graphs/mae/")

# Create the HTML content
html_content = """<!doctype html>
<html>
  <head>
    <title>Plotly Results</title>
    <meta name="description" content="Plotly results">
  </head>
  <body>
    <h2>a temporary webpage to share interactive graphs</h2>
    <b>Inter-building intra-season (summer) Graphs: Comparison of transfer learning methods</b>
    <ul>"""

# Add links to each HTML file
for filename in html_files:
    if "DS_Store" in filename:
        continue
    _, _, method, building1, season1, _, building2, season2, _ = filename.split("_")
    link = f'<li> Building {building1} {season1} to Building {building2} {season2}: <a href="graphs/mae/{filename}">mae</a> </li>'
    html_content += link

html_content += "</ul></body></html>"

# Save the HTML content to a file
with open("graphs.html", "w") as f:
    f.write(html_content)
