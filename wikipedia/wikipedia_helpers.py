import wikipedia


def get_random_article():
    random_article = wikipedia.random()
    return random_article


def get_article_content(title):
    try:
        page = wikipedia.page(title)
        return page.content
    except wikipedia.DisambiguationError as e:
        print("Title is ambiguous. Trying another random article.")
        return get_article_content(get_random_article())
    except wikipedia.HTTPTimeoutError as e:
        print("Wikipedia request timed out. Please try again later.")
        return None
    except wikipedia.PageError as e:
        print("Page not found on Wikipedia. Please try another random article.")
        return None
