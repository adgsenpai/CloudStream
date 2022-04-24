# ADGSTUDIOS - Remove MkDocs Branding

from pathlib import Path

filestochange =  Path('./').rglob('*.html')

for filename in filestochange:
    print(filename)
    with open(filename, 'r',encoding="utf8") as file:
      filedata = file.read()
      branding =     '''Made with
    <a href="https://squidfunk.github.io/mkdocs-material/" target="_blank" rel="noopener">
      Material for MkDocs
    </a>'''
      filedata = filedata.replace(branding, '')
    with open(filename, 'w',encoding="utf8") as file:
        file.write(filedata)

