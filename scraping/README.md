# Diamond Web Scraping

You can scrape Brilliant Earth for their diamond data without any fancy configuration. They do seem to do some rate limiting but will not block your requests.

## Set Up

1. Create a virutal conda environment
```
conda create --name diamond python=3.8
conda activate diamond
```

2. Install Packages
```
python -m pip install beautifulsoup4 requests
```

3. Scrape, ex:
```
python diamonds.py
```