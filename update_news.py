"""Fetch one BBC Business RSS item daily; no AI, API key, or third-party package."""
import json
import pathlib
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

ROOT = pathlib.Path(__file__).resolve().parent
DEST = ROOT / 'news.json'
FEED = 'https://feeds.bbci.co.uk/news/business/rss.xml'
KST = timezone(timedelta(hours=9))

def main():
    today = datetime.now(KST).date().isoformat()
    data = {'articles': []}
    if DEST.exists():
        try:
            data = json.loads(DEST.read_text(encoding='utf-8'))
        except (ValueError, OSError):
            pass
    articles = data.get('articles', [])
    if any(a.get('date') == today for a in articles):
        print('Already has an article for', today)
        return
    req = urllib.request.Request(FEED, headers={'User-Agent': 'MoaEconomy/1.0 (+personal learning; RSS reader)'})
    with urllib.request.urlopen(req, timeout=25) as response:
        root = ET.fromstring(response.read())
    items = root.findall('./channel/item')
    if not items:
        raise RuntimeError('BBC RSS returned no items')
    existing_links = {a.get('url') for a in articles}
    chosen = next((item for item in items if (item.findtext('link') or '').strip() not in existing_links), items[0])
    title = (chosen.findtext('title') or '').strip()
    link = (chosen.findtext('link') or '').strip()
    description = (chosen.findtext('description') or '').strip()
    if not (title and link.startswith('https://')):
        raise RuntimeError('RSS article lacks title or link')
    entry = {'date': today, 'source': 'BBC News · Business', 'title': title,
             'summary': description, 'url': link, 'published': (chosen.findtext('pubDate') or '').strip()}
    articles.insert(0, entry)
    data['articles'] = articles[:365]
    DEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Saved', today, title)

if __name__ == '__main__':
    main()
