"""Fetch BBC Business RSS metadata; no full copyrighted article text."""
import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

URL = 'https://feeds.bbci.co.uk/news/business/rss.xml'
req = urllib.request.Request(URL, headers={'User-Agent': 'MoaEconomyStudy/1.0'})
with urllib.request.urlopen(req, timeout=25) as response:
    root = ET.fromstring(response.read())
articles = []
for item in root.findall('.//channel/item')[:12]:
    def get(name):
        node = item.find(name)
        return ''.join(node.itertext()).strip() if node is not None else ''
    articles.append({'title': get('title'), 'description': get('description'), 'link': get('link'), 'published': get('pubDate')})
if not articles:
    raise RuntimeError('RSS feed returned no articles')
Path(__file__).with_name('news.json').write_text(json.dumps({'articles': articles}, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Updated {len(articles)} BBC Business headlines')
