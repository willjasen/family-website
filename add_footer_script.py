import os

def add_footer_with_gtag(file_path, gtag_script):
    with open(file_path, 'r') as file:
        content = file.readlines()

    footer_tag = "<footer>\n  <div id=\"footer_text_id\">\n    <!-- Google tag (gtag.js) -->\n    <script async src=\"https://www.googletagmanager.com/gtag/js?id=G-VGJ94LX338\"></script>\n    <script>\n      window.dataLayer = window.dataLayer || [];\n      function gtag(){dataLayer.push(arguments);}\n      gtag('js', new Date());\n\n      gtag('config', 'G-VGJ94LX338');\n    </script>\n  </div>\n</footer>\n"

    # Find the closing </body> tag and insert the footer before it
    for i, line in enumerate(content):
        if "</body>" in line:
            content.insert(i, footer_tag + "\n")
            break

    with open(file_path, 'w') as file:
        file.writelines(content)

# File path to the index.html
file_path = "/Users/willjasen/GitHub/family-website/Brandon's Family Tree/index.html"

# Call the function to add the footer
add_footer_with_gtag(file_path, gtag_script=None)