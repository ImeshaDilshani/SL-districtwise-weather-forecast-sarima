"""
Convert Markdown to PDF using Playwright
"""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright
import markdown2

async def markdown_to_pdf(md_file_path, output_pdf_path):
    """Convert markdown file to PDF using Playwright"""
    
    # Read markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Convert to HTML
    html_content = markdown2.markdown(
        markdown_content,
        extras=['tables', 'code-friendly', 'fenced-code-blocks', 'header-ids']
    )
    
    # Create complete HTML with styling
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            
            body {{
                font-family: 'Times New Roman', serif;
                line-height: 1.6;
                color: #333;
                max-width: none;
                margin: 0;
                padding: 0;
            }}
            
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
                margin-top: 30px;
                margin-bottom: 20px;
                page-break-before: always;
            }}
            
            h1:first-of-type {{
                page-break-before: avoid;
            }}
            
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #ecf0f1;
                padding-bottom: 8px;
                margin-top: 25px;
                margin-bottom: 15px;
            }}
            
            h3 {{
                color: #34495e;
                margin-top: 20px;
                margin-bottom: 10px;
            }}
            
            p {{
                text-align: justify;
                margin-bottom: 12px;
            }}
            
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 15px 0;
            }}
            
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
            
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }}
            
            pre {{
                background-color: #f8f8f8;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                overflow-x: auto;
            }}
            
            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: 15px auto;
                border: 1px solid #ddd;
                border-radius: 5px;
            }}
            
            .figure-caption {{
                text-align: center;
                font-style: italic;
                margin-top: 5px;
                color: #666;
            }}
            
            blockquote {{
                border-left: 4px solid #3498db;
                margin: 15px 0;
                padding-left: 15px;
                color: #555;
            }}
            
            ul, ol {{
                margin-bottom: 15px;
            }}
            
            li {{
                margin-bottom: 5px;
            }}
            
            .page-break {{
                page-break-before: always;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Use Playwright to convert HTML to PDF
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Set content and wait for any images to load
        await page.set_content(full_html, wait_until='networkidle')
        
        # Generate PDF with academic formatting
        await page.pdf(
            path=output_pdf_path,
            format='A4',
            margin={
                'top': '2cm',
                'right': '2cm', 
                'bottom': '2cm',
                'left': '2cm'
            },
            print_background=True,
            prefer_css_page_size=True
        )
        
        await browser.close()

async def main():
    # File paths
    project_dir = Path(__file__).parent
    md_file = project_dir / "Weather_Forecasting_Analysis_Report.md"
    pdf_file = project_dir / "Weather_Forecasting_Analysis_Report.pdf"
    
    if not md_file.exists():
        print(f"Error: Markdown file not found at {md_file}")
        return
    
    print(f"Converting {md_file.name} to PDF...")
    
    try:
        await markdown_to_pdf(md_file, pdf_file)
        print(f"✅ PDF successfully created: {pdf_file}")
        print(f"📄 File size: {pdf_file.stat().st_size / 1024 / 1024:.2f} MB")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")

if __name__ == "__main__":
    asyncio.run(main())
