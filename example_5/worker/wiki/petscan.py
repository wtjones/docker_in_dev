import json
import urllib

def parse_result(jsonResult):
    data = json.loads(jsonResult)

    categories = data['*'][0]['a']['*']
    
    return categories

def get_query_url(category, root):

    baseUrl = 'http://petscan.wmflabs.org/?language=en&depth=4&combination=subset&negcats=&ns%5B0%5D=1&larger=&smaller=&minlinks=&maxlinks=&before=&after=&max_age=&show_redirects=both&edits%5Bbots%5D=both&edits%5Banons%5D=both&edits%5Bflagged%5D=both&templates_yes=&templates_any=&templates_no=&outlinks_yes=&outlinks_any=&outlinks_no=&links_to_all=&links_to_any=&links_to_no=&sparql=&manual_list=&manual_list_wiki=&pagepile=&wikidata_source_sites=&subpage_filter=either&common_wiki=cats&source_combination=&wikidata_item=no&wikidata_label_language=&wikidata_prop_item_use=&wpiu=any&sitelinks_yes=&sitelinks_any=&sitelinks_no=&min_sitelink_count=&max_sitelink_count=&format=json&output_compatability=catscan&sortby=none&sortorder=ascending&regexp_filter=&min_redlink_count=1&doit=Do%20it%21&interface_language=en&active_tab=tab_output'

    wikiCategories = [root, category]
    params = urllib.parse.urlencode({'project': 'wikipedia', 'categories': '\n'.join(wikiCategories)})
    
    url = baseUrl + "&" + params
    print(url)
    return url

def is_category_child_of_root(term, category, root):
    url = get_query_url(category, root)
    f = urllib.request.urlopen(url)
    responseJson = f.read().decode('utf-8')
    print('got response...')
    intersect = parse_result(responseJson)

    return len(list(filter(lambda x: x['title'].replace('_', ' ').lower() == term.lower(), intersect))) > 0 
