def google_search(query):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    links = []
    for i in search(query, tld='com', lang='en', tbs='0', safe='off', num=100, start=0, stop=100, pause=2.0, country='',
                    extra_params=None, user_agent=None):
        if i not in links:
            links.append(i)
    return links