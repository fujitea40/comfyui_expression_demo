from bs4 import BeautifulSoup

# Process MeinaMix summary.html
with open(r'd:\git_repos\comfyui_expression_demo\docs\MeinaMix_demo\summary.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# Update head section
head = soup.find('head')
if head:
    # Remove existing style tag
    style_tag = head.find('style')
    if style_tag:
        style_tag.decompose()
    
    # Add meta tags and link to common.css
    head.clear()
    head.append(soup.new_tag('meta', charset='utf-8'))
    head.append(soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}))
    head.append(soup.new_tag('title'))
    head.title.string = 'MeinaMix - Expression Demo'
    
    link = soup.new_tag('link', rel='stylesheet', href='../common.css')
    head.append(link)
    
    # Add table-specific styles
    style = soup.new_tag('style')
    style.string = '''
    body { padding-top: 80px; }
    h1 { text-align: center; margin-bottom: 20px; }
    table { border-collapse: collapse; width: 100%; max-width: 1400px; margin: 0 auto; }
    th, td { border: 1px solid var(--border); padding: 8px; text-align: center; }
    th { background: var(--panel); position: sticky; top: 0; z-index: 10; }
    .row-header { position: sticky; left: 0; text-align: left; min-width: 150px; background: var(--panel); z-index: 5; }
    th.row-header { z-index: 20; }
    .img-container { display: flex; flex-direction: column; align-items: center; gap: 5px; }
    .img-box { text-align: center; }
    img { max-width: 150px; border: 1px solid var(--border); border-radius: 4px; }
    img:hover { transform: scale(3); z-index: 100; position: relative; border-color: var(--link); }
    .label { font-size: 0.8rem; color: var(--muted); margin-bottom: 2px; }
    .expr-sub { font-size: 0.8rem; color: var(--muted); font-weight: normal; display: block; margin-top: 4px; }
    '''
    head.append(style)

# Write formatted HTML
with open(r'd:\git_repos\comfyui_expression_demo\docs\MeinaMix_demo\summary.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# Process Counterfeit summary.html
with open(r'd:\git_repos\comfyui_expression_demo\docs\Counterfeit_demo\summary.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# Update head section
head = soup.find('head')
if head:
    # Remove existing style tag
    style_tag = head.find('style')
    if style_tag:
        style_tag.decompose()
    
    # Add meta tags and link to common.css
    head.clear()
    head.append(soup.new_tag('meta', charset='utf-8'))
    head.append(soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}))
    head.append(soup.new_tag('title'))
    head.title.string = 'Counterfeit - Expression Demo'
    
    link = soup.new_tag('link', rel='stylesheet', href='../common.css')
    head.append(link)
    
    # Add table-specific styles
    style = soup.new_tag('style')
    style.string = '''
    body { padding-top: 80px; }
    h1 { text-align: center; margin-bottom: 20px; }
    table { border-collapse: collapse; width: 100%; max-width: 1400px; margin: 0 auto; }
    th, td { border: 1px solid var(--border); padding: 8px; text-align: center; }
    th { background: var(--panel); position: sticky; top: 0; z-index: 10; }
    .row-header { position: sticky; left: 0; text-align: left; min-width: 150px; background: var(--panel); z-index: 5; }
    th.row-header { z-index: 20; }
    .img-container { display: flex; flex-direction: column; align-items: center; gap: 5px; }
    .img-box { text-align: center; }
    img { max-width: 150px; border: 1px solid var(--border); border-radius: 4px; }
    img:hover { transform: scale(3); z-index: 100; position: relative; border-color: var(--link); }
    .label { font-size: 0.8rem; color: var(--muted); margin-bottom: 2px; }
    .expr-sub { font-size: 0.8rem; color: var(--muted); font-weight: normal; display: block; margin-top: 4px; }
    '''
    head.append(style)

# Write formatted HTML
with open(r'd:\git_repos\comfyui_expression_demo\docs\Counterfeit_demo\summary.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

print("Successfully updated both summary.html files with common.css!")
