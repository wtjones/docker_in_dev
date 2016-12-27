import wikipedia

def categorize_term(term):
    categories = wikipedia.page(term).categories
    print(categories)
    print ('.......')
    filtered = filter(lambda x: 
        not x.startswith('All articles') 
        and not x.startswith('Articles')
        and not x.startswith('Products')
        and not x.startswith('Pages')
        and not x.startswith('Commons category')
        and not x.startswith('Webarchive template wayback links')
        and not 'disestablishments' in x, categories)
    
    return filtered
