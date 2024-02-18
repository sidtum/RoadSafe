
def generatePage(table_rows):
    output_file = 'output.html'

    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RoadSafe</title>
        <style>
            body {{ 
            background-image: url('Intersection.jpg');
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;  
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            }}

            .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            }}

            table {{
            width: 100%;
            border-collapse: collapse;
            }}

            th,
            td {{
            border: 1px solid #ddd;
            padding: 15px;
            text-align: left;
            }}

            th {{
            background-color: lightgrey;
            color: black;
            font-size: 1.2em;
            font-weight: normal;
            }}

            tr:nth-child(even) {{
            background-color: lightslategrey;
            }}

            tr:nth-child(odd) {{
            background-color: lightblue;
            }}

            tr:first-child {{
            border-top: 2px solid white;
            }}

            tr:last-child {{
            border-bottom: 2px solid white;
            }}

            th:first-child,
            td:first-child {{
            width: 40%;
            }}

            th:last-child,
            td:last-child {{
            width: 60%;
            }}
        </style>
        </head>
        <body>
        <div class="container">
            <center><h1 style="color: white;">RoadSafe Accident Log</h1></center>
            <table>
            <tr>
                <th>Detections</th>
                <th>Dates and Times</th>
            </tr>
            {','.join(table_rows)}
            </table>
        </div>
        </body>
        </html>
        """
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)