#!/usr/bin/env python3
"""
Convert Markdown Report to PDF
Converts the Weather Forecasting Analysis Report from Markdown to PDF format
with proper academic styling and image support.
"""

import markdown
from weasyprint import HTML, CSS
import os
import re

def convert_md_to_pdf(md_file_path, output_pdf_path):
    """
    Convert Markdown file to PDF with academic styling
    
    Args:
        md_file_path (str): Path to the input Markdown file
        output_pdf_path (str): Path for the output PDF file
    """
    
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Configure markdown extensions for better formatting
    md = markdown.Markdown(extensions=[
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.meta',
        'markdown.extensions.attr_list'
    ])
    
    # Convert markdown to HTML
    html_content = md.convert(md_content)
    
    # Create complete HTML document with styling
    html_doc = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sri Lanka Weather Forecasting Analysis Report</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm 2.5cm 2cm 2.5cm;
                @top-right {{
                    content: counter(page);
                    font-size: 10pt;
                    color: #666;
                }}
                @bottom-center {{
                    content: "Sri Lanka Weather Forecasting using SARIMA Models";
                    font-size: 9pt;
                    color: #666;
                }}
            }}
            
            body {{
                font-family: "Times New Roman", Times, serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #333;
                max-width: none;
                margin: 0;
                padding: 0;
            }}
            
            h1 {{
                font-size: 18pt;
                font-weight: bold;
                color: #2c3e50;
                text-align: center;
                margin: 30px 0 20px 0;
                page-break-before: always;
            }}
            
            h1:first-of-type {{
                page-break-before: avoid;
                margin-top: 0;
            }}
            
            h2 {{
                font-size: 14pt;
                font-weight: bold;
                color: #34495e;
                margin: 25px 0 15px 0;
                border-bottom: 2px solid #3498db;
                padding-bottom: 5px;
            }}
            
            h3 {{
                font-size: 12pt;
                font-weight: bold;
                color: #2c3e50;
                margin: 20px 0 10px 0;
            }}
            
            h4 {{
                font-size: 11pt;
                font-weight: bold;
                color: #34495e;
                margin: 15px 0 8px 0;
            }}
            
            p {{
                margin: 8px 0;
                text-align: justify;
                text-indent: 0;
            }}
            
            ul, ol {{
                margin: 10px 0;
                padding-left: 25px;
            }}
            
            li {{
                margin: 5px 0;
            }}
            
            strong {{
                font-weight: bold;
                color: #2c3e50;
            }}
            
            em {{
                font-style: italic;
            }}
            
            code {{
                font-family: "Courier New", Courier, monospace;
                background-color: #f8f9fa;
                padding: 2px 4px;
                border-radius: 3px;
                font-size: 10pt;
            }}
            
            pre {{
                background-color: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 5px;
                padding: 15px;
                margin: 15px 0;
                overflow-x: auto;
                font-size: 9pt;
                line-height: 1.4;
            }}
            
            pre code {{
                background-color: transparent;
                padding: 0;
                border-radius: 0;
            }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 15px 0;
                font-size: 10pt;
            }}
            
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
                color: #2c3e50;
            }}
            
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            
            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: 15px auto;
                border: 1px solid #ddd;
                border-radius: 5px;
                page-break-inside: avoid;
            }}
            
            .figure-caption {{
                font-style: italic;
                font-size: 10pt;
                color: #666;
                text-align: center;
                margin: 5px auto 20px auto;
                max-width: 90%;
            }}
            
            blockquote {{
                border-left: 4px solid #3498db;
                margin: 15px 0;
                padding: 10px 20px;
                background-color: #f8f9fa;
                font-style: italic;
            }}
            
            .abstract {{
                background-color: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 5px;
                padding: 20px;
                margin: 20px 0;
                font-style: italic;
            }}
            
            .page-break {{
                page-break-before: always;
            }}
            
            .no-break {{
                page-break-inside: avoid;
            }}
            
            .header-info {{
                text-align: center;
                margin-bottom: 30px;
                color: #666;
                font-size: 10pt;
            }}
            
            .math {{
                font-family: "Times New Roman", Times, serif;
                font-style: italic;
            }}
            
            .references {{
                font-size: 10pt;
            }}
            
            .references ol {{
                padding-left: 20px;
            }}
            
            .references li {{
                margin: 8px 0;
                text-align: justify;
            }}
            
            hr {{
                border: none;
                height: 1px;
                background-color: #ddd;
                margin: 30px 0;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Fix image paths to be relative to the markdown file directory
    base_dir = os.path.dirname(md_file_path)
    
    def fix_image_path(match):
        img_path = match.group(1)
        if not os.path.isabs(img_path):
            full_path = os.path.join(base_dir, img_path)
            if os.path.exists(full_path):
                return f'<img src="file:///{full_path.replace(chr(92), "/")}"'
            else:
                print(f"Warning: Image not found: {full_path}")
                return f'<img src="{img_path}"'
        return match.group(0)
    
    # Fix image paths in HTML
    html_doc = re.sub(r'<img src="([^"]+)"', fix_image_path, html_doc)
    
    # Add figure captions styling
    html_doc = re.sub(
        r'<em>Figure \d+[ab]?:([^<]+)</em>',
        r'<div class="figure-caption"><em>Figure \g<1></em></div>',
        html_doc
    )
    
    # Add abstract styling
    html_doc = html_doc.replace('<h2>Abstract</h2>', '<h2>Abstract</h2><div class="abstract">')
    html_doc = html_doc.replace('<h2>Chapter 1:', '</div><h2 class="page-break">Chapter 1:')
    
    # Convert HTML to PDF
    try:
        HTML(string=html_doc, base_url=base_dir).write_pdf(output_pdf_path)
        print(f"✅ Successfully converted {md_file_path} to {output_pdf_path}")
        return True
    except Exception as e:
        print(f"❌ Error converting to PDF: {str(e)}")
        return False

def main():
    """Main function to convert the report"""
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define file paths
    md_file = os.path.join(current_dir, "Weather_Forecasting_Analysis_Report.md")
    pdf_file = os.path.join(current_dir, "Weather_Forecasting_Analysis_Report.pdf")
    
    # Check if markdown file exists
    if not os.path.exists(md_file):
        print(f"❌ Markdown file not found: {md_file}")
        return False
    
    print(f"📄 Converting {md_file} to PDF...")
    print(f"📍 Output will be saved as: {pdf_file}")
    
    # Perform conversion
    success = convert_md_to_pdf(md_file, pdf_file)
    
    if success:
        print(f"🎉 PDF conversion completed successfully!")
        print(f"📁 Output file: {pdf_file}")
        
        # Check file size
        if os.path.exists(pdf_file):
            file_size = os.path.getsize(pdf_file) / (1024 * 1024)  # Convert to MB
            print(f"📊 File size: {file_size:.2f} MB")
    else:
        print("❌ PDF conversion failed!")
    
    return success

if __name__ == "__main__":
    main()
