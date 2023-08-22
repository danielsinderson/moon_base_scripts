"""
script to grab a random Wikipedia article and display the summary
"""


import wikipediaapi

def grab_random_wiki():
    wiki = wikipediaapi.Wikipedia(
        user_agent="Moon Base Books (moonbasebooks@proton.me)", 
        language="en",
        extract_format=wikipediaapi.ExtractFormat.WIKI
        )
    
    #random_page = wiki.page("Special:Random")
    random_page = wiki.page("Tommaso_Catani")
    page = random_page.text
    
    result = f"""
    Here's a random Wikipedia page to use as a story prompt.
    
    {page}
    """
    
    return result


def main():
    page: str = grab_random_wiki()
    print(page)


if __name__ == "__main__":
    main()
    