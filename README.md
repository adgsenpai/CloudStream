# ADGDOCS
creates a web app using markdown files

## Installation
fetch the repo using the command

``
git clone https://github.com/ADGSTUDIOS/ADGDOCS/
``

install modules found in `ADGDOCS/requirements.txt` using the command below

``
pip install -r requirements.txt
``

### If you are using GitHub Actions

Change the following in buildblog.yml to your config

![image](https://user-images.githubusercontent.com/45560312/150775275-b827f265-5197-4fea-9e99-34d4fe525ab9.png)
![image](https://user-images.githubusercontent.com/45560312/150775673-4fa3b2bf-9561-4e24-bc40-ef5d8251c479.png)


Also enable GitHub Pages to `gh-pages` branch for you to host the website.

![image](https://user-images.githubusercontent.com/45560312/150775748-a4c29f12-6b87-4b58-8622-39370fd39732.png)


# Configuration

## Changing Metadata

in `mkdocs.yml`


```
site_name: ADGDOCS
copyright: "ADGSTUDIOS"
site_url: https://adgstudios.com
repo_url: https://github.com/ADGSTUDIOS/ADGDOCS
repo_name: ADGSTUDIOS/ADGDOCS
```

you can change all values with appropriate values

## NAV Bar

in `mkdocs.yml`

```
nav:
      - Title:
        - Subtitle: index.md
```

work with the syntax here to add more pages and markup files

## Social Media 
in `mkdocs.yml`

```
  social:
            - icon: fontawesome/brands/github
              link: "https://github.com/ADGSTUDIOS"
            - icon: fontawesome/brands/linkedin
              link: "https://www.linkedin.com/in/adgsenpai/"
```

for icons look up into `fontawesome` docs

change the links to your social media links

## Adding files
add your markdown files in `/docs/`

for example adding `file2.md` and `file3.md`

```
-ADGDOCS
    -docs
        -index.md
        -file2.md
        -file3.md
```

## Changing icons
in `mkdocs.yml`
under `themes`

to change the icons/favicon change the paths down below

```
      favicon: ./static/favicon.png
      logo: ./static/favicon.png
```



# Deployment

To run the web app you can run this command

``
python -m mkdocs serve
``

# Compiling Web Files

To build webfiles you can run

``
python -m mkdocs build
``

you will find your stuff in `ADGDOCS/site`
