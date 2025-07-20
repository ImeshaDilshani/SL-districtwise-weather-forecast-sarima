#!/usr/bin/env python3
"""
Convert Markdown Report to PDF (Alternative Method)
Uses markdown2 and creates HTML that can be printed to PDF via browser
"""

import markdown2
import os
import re

def create_html_report(md_file_path, output_html_path):
    """
    Convert Markdown file to styled HTML that can be printed to PDF
    
    Args:
        md_file_path (str): Path to the input Markdown file
        output_html_path (str): Path for the output HTML file
    """
    
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Configure markdown2 with extras for better formatting
    html_content = markdown2.markdown(md_content, extras=[
        'tables',
        'fenced-code-blocks',
        'code-friendly',
        'cuddled-lists',
        'metadata',
        'toc'
    ])
    
    # Get base directory for relative image paths
    base_dir = os.path.dirname(md_file_path)
    
    # Create complete HTML document with comprehensive styling
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sri Lanka Weather Forecasting Analysis Report</title>
    <style>
        @media print {{
            @page {{
                size: A4;
                margin: 2cm 2.5cm 2cm 2.5cm;
            }}
            
            body {{
                -webkit-print-color-adjust: exact !important;
                color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            
            .page-break {{
                page-break-before: always !important;
            }}
            
            .no-break {{
                page-break-inside: avoid !important;
            }}
            
            img {{
                page-break-inside: avoid !important;
                max-width: 100% !important;
                height: auto !important;
            }}
            
            h1, h2, h3, h4 {{
                page-break-after: avoid !important;
            }}
            
            table {{
                page-break-inside: avoid !important;
            }}
            
            pre {{
                page-break-inside: avoid !important;
                white-space: pre-wrap !important;
            }}
        }}
        
        body {{
            font-family: "Times New Roman", Times, serif;
            font-size: 12pt;
            line-height: 1.6;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
        }}
        
        h1 {{
            font-size: 20pt;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin: 30px 0 25px 0;
            page-break-before: always;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        
        h1:first-of-type {{
            page-break-before: avoid;
            margin-top: 0;
        }}
        
        h2 {{
            font-size: 16pt;
            font-weight: bold;
            color: #34495e;
            margin: 25px 0 15px 0;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }}
        
        h3 {{
            font-size: 14pt;
            font-weight: bold;
            color: #2c3e50;
            margin: 20px 0 12px 0;
        }}
        
        h4 {{
            font-size: 12pt;
            font-weight: bold;
            color: #34495e;
            margin: 15px 0 10px 0;
        }}
        
        p {{
            margin: 10px 0;
            text-align: justify;
            orphans: 2;
            widows: 2;
        }}
        
        ul, ol {{
            margin: 12px 0;
            padding-left: 30px;
        }}
        
        li {{
            margin: 6px 0;
        }}
        
        strong {{
            font-weight: bold;
            color: #2c3e50;
        }}
        
        em {{
            font-style: italic;
            color: #444;
        }}
        
        code {{
            font-family: "Courier New", Courier, monospace;
            background-color: #f8f9fa;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 10pt;
            border: 1px solid #e9ecef;
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
            font-family: "Courier New", Courier, monospace;
        }}
        
        pre code {{
            background-color: transparent;
            padding: 0;
            border: none;
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
            padding: 8px 12px;
            text-align: left;
            vertical-align: top;
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
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        blockquote {{
            border-left: 4px solid #3498db;
            margin: 15px 0;
            padding: 10px 20px;
            background-color: #f8f9fa;
            font-style: italic;
            border-radius: 0 5px 5px 0;
        }}
        
        .header-info {{
            text-align: center;
            margin-bottom: 30px;
            color: #666;
            font-size: 11pt;
            font-weight: normal;
        }}
        
        .abstract {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 5px;
            padding: 20px;
            margin: 20px 0;
            font-style: italic;
        }}
        
        .figure-caption {{
            font-style: italic;
            font-size: 10pt;
            color: #666;
            text-align: center;
            margin: 5px auto 20px auto;
            max-width: 90%;
            line-height: 1.4;
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
        
        /* Chapter styling */
        h2:contains("Chapter") {{
            page-break-before: always;
        }}
        
        /* Print optimizations */
        @media screen {{
            body {{
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                max-width: 800px;
                padding: 40px;
            }}
        }}
        
        /* Figure and equation numbering */
        .figure {{
            counter-increment: figure;
        }}
        
        .equation {{
            counter-increment: equation;
        }}
        
        /* Better spacing for academic content */
        .methodology, .results, .discussion {{
            margin: 20px 0;
        }}
        
        /* Code block improvements */
        .language-r, .language-python {{
            background-color: #f8f9fa;
            border-left: 4px solid #007acc;
        }}
        
        /* Table of contents styling */
        .toc {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 5px;
            padding: 20px;
            margin: 20px 0;
        }}
        
        .toc ul {{
            list-style-type: none;
            padding-left: 20px;
        }}
        
        .toc li {{
            margin: 5px 0;
        }}
        
        .toc a {{
            text-decoration: none;
            color: #3498db;
        }}
        
        .toc a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
    
    # Fix image paths to be absolute file paths
    def fix_image_path(match):
        img_path = match.group(1)
        if not os.path.isabs(img_path):
            full_path = os.path.join(base_dir, img_path).replace('\\', '/')
            if os.path.exists(os.path.join(base_dir, img_path)):
                return f'<img src="file:///{full_path}"'
            else:
                print(f"Warning: Image not found: {os.path.join(base_dir, img_path)}")
                return f'<img src="{img_path}"'
        return match.group(0)
    
    # Fix image paths in HTML
    html_doc = re.sub(r'<img src="([^"]+)"', fix_image_path, html_doc)
    
    # Add page breaks for chapters
    html_doc = re.sub(r'<h2>Chapter', r'<h2 class="page-break">Chapter', html_doc)
    
    # Style figure captions
    html_doc = re.sub(
        r'<em>Figure \d+[ab]?:([^<]+)</em>',
        r'<div class="figure-caption"><em>Figure \g<1></em></div>',
        html_doc
    )
    
    # Add abstract styling
    if '<h2>Abstract</h2>' in html_doc:
        html_doc = html_doc.replace('<h2>Abstract</h2>', '<h2>Abstract</h2><div class="abstract">')
        # Find the end of abstract (next h2)
        abstract_end = html_doc.find('<h2', html_doc.find('<h2>Abstract</h2>') + 20)
        if abstract_end != -1:
            html_doc = html_doc[:abstract_end] + '</div>' + html_doc[abstract_end:]
    
    # Write HTML file
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_doc)
    
    return True

def main():
    """Main function to convert the report"""
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define file paths
    md_file = os.path.join(current_dir, "Weather_Forecasting_Analysis_Report.md")
    html_file = os.path.join(current_dir, "Weather_Forecasting_Analysis_Report.html")
    
    # Check if markdown file exists
    if not os.path.exists(md_file):
        print(f"❌ Markdown file not found: {md_file}")
        return False
    
    print(f"📄 Converting {md_file} to HTML...")
    print(f"📍 Output will be saved as: {html_file}")
    
    # Perform conversion
    success = create_html_report(md_file, html_file)
    
    if success:
        print(f"✅ HTML conversion completed successfully!")
        print(f"📁 Output file: {html_file}")
        
        # Check file size
        if os.path.exists(html_file):
            file_size = os.path.getsize(html_file) / 1024  # Convert to KB
            print(f"📊 File size: {file_size:.2f} KB")
        
        print(f"\\n🖨️  To create PDF:")
        print(f"1. Open {html_file} in your web browser")
        print(f"2. Press Ctrl+P (or Cmd+P on Mac)")
        print(f"3. Select 'Save as PDF' as destination")
        print(f"4. Choose 'More settings' and:")
        print(f"   - Set margins to 'Default' or 'Custom' (2cm)")
        print(f"   - Check 'Background graphics' for better styling")
        print(f"   - Select A4 paper size")
        print(f"5. Click 'Save' and choose filename ending with .pdf")
        print(f"\\n📝 The HTML file is ready for PDF conversion!")
        
    else:
        print("❌ HTML conversion failed!")
    
    return success

if __name__ == "__main__":
    main()
