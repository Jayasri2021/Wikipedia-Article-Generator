from wikipedia_helpers import get_random_article, get_article_content


def generate_random_article():
    random_article_title = get_random_article()
    print("Random article title:", random_article_title)

    choice = input("Do you want to see the article? (yes/no): ").lower()
    if choice == "yes":
        article_content = get_article_content(random_article_title)
        if article_content:
            print("Article Content:")
            print(article_content)
    else:
        print("Okay, fetching another random article.")
