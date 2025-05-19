import os

def add_footer_with_gtag_to_all_html(directory, gtag_file):
    # Read the content of gtag.html and wrap it in <footer> tags
    with open(gtag_file, 'r') as gtag:
        footer_tag = f"<footer>\n{gtag.read()}\n</footer>"

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.readlines()

                # Find the closing </body> tag and insert the footer before it
                for i, line in enumerate(content):
                    if "</body>" in line:
                        content.insert(i, footer_tag + "\n")
                        break

                with open(file_path, 'w') as f:
                    f.writelines(content)

# Directory containing the .html files
directory = "/Users/willjasen/GitHub/family-website"

# Path to the gtag.html file
gtag_file = os.path.join(directory, "gtag.html")

# Call the function to add the footer to all .html files
add_footer_with_gtag_to_all_html(directory, gtag_file)