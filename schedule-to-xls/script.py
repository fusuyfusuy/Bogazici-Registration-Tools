import pandas as pd

def html_to_excel(html_file, excel_file):
    # Read HTML file
    with open(html_file, 'r', encoding='iso8859-9') as file:
        html_content = file.read()

    # Convert HTML to DataFrame
    dfs = pd.read_html(html_content)

    # Assuming the first table is the one you want
    if dfs:
        schedule_table = dfs[2]
        print("Extracted Table:")
        print(schedule_table)

        # Save the DataFrame to an Excel file
        schedule_table.to_excel(excel_file, index=False)
        print(f"Data saved to {excel_file}")
    else:
        print("No tables found in HTML file.")

# Specify the HTML file and the desired output Excel file
html_file_path = 'schedule.html'
excel_file_path = 'schedule.xlsx'

# Call the function
html_to_excel(html_file_path, excel_file_path)
