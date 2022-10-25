import urllib.request, json

definitions = []
examples = []
synonyms = []
sourceUrl = []


def getMeaning(word):
    queryUrl = ("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    with urllib.request.urlopen(queryUrl) as url:
        data = json.load(url)


        for i in range(len(data)):
            if sourceUrl.__contains__(data[i]['sourceUrls'][0]):
                None
            else:
                sourceUrl.append(data[i]['sourceUrls'][0])
            for j in range(len(data[i]['meanings'])):
                for k in range(len(data[i]['meanings'][j]['definitions'])):
                    definitions.append(data[i]['meanings'][j]['definitions'][k]['definition'])
                    # print('Definition: ' + data[i]['meanings'][j]['definitions'][k]['definition'])
                    if 'example' not in data[i]['meanings'][j]['definitions'][k]:
                        None
                    else:
                        if examples.__contains__(data[i]['meanings'][j]['definitions'][k]['example']):
                            None
                        else:
                            examples.append(data[i]['meanings'][j]['definitions'][k]['example'])
                            # print('Example: ' + data[i]['meanings'][j]['definitions'][k]['example'])

                    for l in range(len(data[i]['meanings'][j]['definitions'][k]['synonyms'])):
                        if data[i]['meanings'][j]['definitions'][k]['synonyms'] == None:
                            None
                        else:
                            if synonyms.__contains__(data[i]['meanings'][j]['definitions'][k]['synonyms'][l]):
                                None
                            else:
                                synonyms.append(data[i]['meanings'][j]['definitions'][k]['synonyms'][l])


name = input("Please enter your name: ")
print("Welcome, %s. Happy learning!" % name)
a = ''
while (a!='q' or a!='Q'):
    print("\nEnter 'Q' or 'q' to exit learning.")
    a = input("Enter the word to find meaning for: ")
    if(a=='q'):
        break
    getMeaning(a)
    print('Total definition count : %d' % (len(definitions)))
    print('Total example count : %d' % (len(examples)))
    print('Total synonyms count : %d' % (len(synonyms)))
    print("Source : %d" % (len(sourceUrl)))
    if len(definitions) == 0:
        None
    else:
        print("\n\nDefinitions:")
        for i in definitions:
            print(i)
    if len(examples) == 0:
        None
    else:
        print("\n\nExamples:")
        for i in examples:
            print(i)
    if len(synonyms) == 0:
        None
    else:
        print("\n\nSynonyms:")
        for i in synonyms:
            print(i)

    if len(sourceUrl) == 0:
        None
    else:
        print("\n\nSource:")
        for i in sourceUrl:
            print(i)
    definitions = []
    examples = []
    synonyms = []
    sourceUrl = []
