# Read MeinaMix summary.html
$content = Get-Content 'd:\git_repos\comfyui_expression_demo\docs\MeinaMix_demo\summary.html' -Raw

# Replace the style section
$content = $content -replace '\<style\>.*?\</style\>', @'
<meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>MeinaMix - Expression Demo</title>
  <link rel="stylesheet" href="../common.css" />
  <style>
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
  </style>
'@

# Save updated file
$content | Set-Content 'd:\git_repos\comfyui_expression_demo\docs\MeinaMix_demo\summary.html' -NoNewline

# Read Counterfeit summary.html
$content = Get-Content 'd:\git_repos\comfyui_expression_demo\docs\Counterfeit_demo\summary.html' -Raw

# Replace the style section
$content = $content -replace '\<style\>.*?\</style\>', @'
<meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Counterfeit - Expression Demo</title>
  <link rel="stylesheet" href="../common.css" />
  <style>
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
  </style>
'@

# Save updated file
$content | Set-Content 'd:\git_repos\comfyui_expression_demo\docs\Counterfeit_demo\summary.html' -NoNewline

Write-Host "Successfully updated both summary.html files!"
