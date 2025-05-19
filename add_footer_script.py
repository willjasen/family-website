import os

def add_footer_with_gtag_to_all_html(directory):
    footer_tag = "<footer>\n  <div id=\"footer_text_id\">\n    <!-- Google tag (gtag.js) -->\n    <script async src=\"https://www.googletagmanager.com/gtag/js?id=G-VGJ94LX338\"></script>\n    <script>\n      window.dataLayer = window.dataLayer || [];\n      function gtag(){dataLayer.push(arguments);}\n      gtag('js', new Date());\n\n      gtag('config', 'G-VGJ94LX338');\n    </script>\n  </div>\n</footer>\n"

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

# Call the function to add the footer to all .html files
add_footer_with_gtag_to_all_html(directory)