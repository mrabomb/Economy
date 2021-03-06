from lxml import html, parse
import scrapy

class QueryTool():
    '''
        Concatonates earch term to the url and runs a search of the terms in
        the list that are passed to it. Returns urls of the correct threads.

        @param urlStart        the first part of the url thats always the same.
        @param searchTermList  list containing the final part of the url to
                               search.
        @return                list containing urls of the threads.
    '''
    def Searcher(urlStart, searchTermList): 
        urlList = []
        for searchTerm in self.searchTermList:

            #initializes url
            urlToVisit = urlStart + searchTerm

            #gos to the url
            page = requests.get('urlToVisit')
            tree = html.fromstring(page.content)

            #xml parser finds the page with the highest int value following the search term
            data = tree.xpath('')   #whatever we are looking through
                                    #now we gotta stick the proper div into a list of lists
                                    #Column 0 contains the title text, column 1 contains the QFC id
        

            #returns list of urls with proper QFC ids to locate the threads
                                    #append proper url to urlList
            return urlList
            
 
urlStart = "http://services.runescape.com/m=forum/searchthreads.ws?search=submit&srcstr="
searchTermList = ["~Discontinued%20Item%20Status", "High%20Level%20Weapon%20Status",
                    "Ability%20Codex%20Status%20Thread", "Treasure%20Trails%20Item%20Status",
                    "SOF/TH%20Item%20Status", "~Third-Age%20Status",
                    "High%20Level%20Gear%20Status", "Nex%20Status"]
QueryTool(urlStart, searchTermList)
