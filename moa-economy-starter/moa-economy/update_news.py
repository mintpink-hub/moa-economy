"""Daily Moa Economy article updater. Requires OPENAI_API_KEY GitHub secret."""
import datetime as dt
import json
import os
import pathlib
import re
import urllib.request
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).parent
TODAY = dt.datetime.now(ZoneInfo('Asia/Seoul')).date().isoformat()
FEED = 'https://feeds.bbci.co.uk/news/business/rss.xml'

def get_candidates():
    req = urllib.request.Request(FEED, headers={'User-Agent': 'MoaEconomy/1.0'})
    with urllib.request.urlopen(req, timeout=25) as resp:
        root = ET.fromstring(resp.read())
    results = []
    for item in root.findall('./channel/item'):
        title = (item.findtext('title') or '').strip()
        link = (item.findtext('link') or '').strip()
        description = re.sub(r'<[^>]+>', '', item.findtext('description') or '').strip()
        if title and link:
            results.append({'title': title, 'url': link, 'description': description})
    return results[:15]

def main():
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        raise SystemExit('OPENAI_API_KEY secret is missing. No news was changed.')
    path = ROOT / 'news.json'
    data = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'articles': []}
    if any(x.get('date') == TODAY and not x.get('demo') for x in data['articles']):
        print('Already published today.')
        return
    candidates = get_candidates()
    if not candidates:
        raise SystemExit('RSS has no candidates; preserving previous news.')
    from openai import OpenAI
    client = OpenAI(api_key=key)
    prompt = f'''Today in Korea is {TODAY}. Select ONE useful, accessible, freely readable, timely economic news item from the RSS candidates below. Do not fabricate any news facts, claims or quotes. The RSS title and description are the ONLY source facts; do not pretend to have read full article. Write a clearly identified beginner-friendly learning explanation based only on those facts, with general economic context clearly separated from news-specific facts. Avoid unsupported details. Provide exactly 6 short English learning sentences with faithful Korean translations, exactly 5 English vocabulary words with Korean definitions, and exactly 3 multiple-choice comprehension questions in Korean, each with 4 choices, zero-based integer answer and Korean explanation. Make questions answerable using your sentences. Return JSON object with keys date, source, url, title_en, title_ko, sentences (array of {{en,ko}}), words (array of {{en,ko}}), quiz (array of {{question,options,answer,explanation}}). source must be BBC News. date must be {TODAY}. Use the original article URL of the selected item. Do not include copyrighted article text verbatim except the headline if necessary. Candidates: {json.dumps(candidates, ensure_ascii=False)}'''
    response = client.chat.completions.create(model='gpt-4.1-mini', temperature=0.3, response_format={'type':'json_object'}, messages=[{'role':'user','content':prompt}])
    article = json.loads(response.choices[0].message.content)
    article['date'] = TODAY
    article['source'] = 'BBC News'
    urls = {x['url'] for x in candidates}
    if article.get('url') not in urls:
        raise ValueError('Model returned a URL not present in RSS candidates.')
    if len(article.get('sentences',[])) != 6 or len(article.get('words',[])) != 5 or len(article.get('quiz',[])) != 3:
        raise ValueError('Unexpected article schema length.')
    for q in article['quiz']:
        if len(q.get('options', [])) != 4 or not isinstance(q.get('answer'), int) or not 0 <= q['answer'] <= 3:
            raise ValueError('Invalid quiz options.')
    data['articles'] = [article] + [x for x in data['articles'] if x.get('date') != TODAY and not x.get('demo')]
    data['articles'] = data['articles'][:365]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Published', TODAY, article['title_en'])

if __name__ == '__main__':
    main()
