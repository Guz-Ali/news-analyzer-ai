import re
from datetime import datetime

def newsParser(text_block):
    print("DEBUG: Full text block received:")
    print(repr(text_block))

    pattern = (
        r"(?P<title>.*?)\s*\n"                
        r"(?P<source>.*?)\s*\n"               
        r"(?P<date>\d{2}/\d{2}/\d{4})\s*\n"   
        r"(?P<content>.*?)\s*\n"              
        r"(?P<link>https?://[^\s]+)\s*\n\n?"
    )
    
    news_items = []
    matches = list(re.finditer(pattern, text_block, re.DOTALL))
    print(f"DEBUG: Number of matches found: {len(matches)}")

    for match in matches:
        title = match.group("title").strip()
        source = match.group("source").strip()
        date_str = match.group("date").strip()
        content = match.group("content").strip()
        link = match.group("link").strip()

        try:
            date = datetime.strptime(date_str, "%m/%d/%Y").date()
        except ValueError:
            date = None 
            
        news_items.append({
            'title': title,
            'source': source,
            'date': date,
            'content': content,
            'link': link
        })
        
    return news_items