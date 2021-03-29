#converts string to "search format"
import requests, json



def drama_link(search):

    urlVar = "https://kuryana.vercel.app/search/q/" + search

    print (urlVar)

    res = requests.get(urlVar)
    dramaData = json.loads(res.text)

    print (dramaData)

    if ( (dramaData['results'][0]['slug']) == False ):
        dramaLink = ('Drama could not be found.')
    else:
        mdlSlug = dramaData['results'][0]['slug']
        print (mdlSlug)
        dramaLink = ('https://mydramalist.com/' + mdlSlug)

    print (dramaLink)
    return dramaLink




"""

def drama_search(search):

    dramaInput = "example here and here"

    dramaInput = dramaInput.split()


    dramaOutput = 'https://mydramalist.com/' + '+'.join(dramaInput)

    return(dramaInput)

"""