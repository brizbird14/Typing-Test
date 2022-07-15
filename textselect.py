import json

with open('textOptions.json') as json_in: # Opening JSON file
    json_dict = json.load(json_in) # returning as dictionary
    #print(json_dict)

#text_list = []

#for item in json_dict:
#    text_details = {"genre":None, "length":None, "title":None, "raw text":None}
#    text_details['genre'] = item['genre']
#    text_details['length'] = item ['length']
#    text_details['title'] = item['title']
#    text_details['raw text'] = item['raw text']

#for

#text_list = json.loads(json_dict)

#for i in json_dict['textarr_j']:
#    print(i)

# List of dictionaries?

#for i  in json_dict:
#    print("dictionary is ", i)
#    for key in i:
#        print("key is ", key, " value is ", i[key])
#        if (i[key] == "romance"):
#            print("MATCH FOUND: ROMANCE")

#print("---------------------")
#print("dict 1: ", json_dict[0])
#print("key 1 of dict 1: ", json_dict[0].get('genre'))

def retrieve_text (text_length, text_genre):
    with open('textOptions.json') as text_json:
        text_list = json.load(text_json)
    
    for text_dict in text_list:
        if(text_dict.get('length') == text_length and text_dict.get('genre') == text_genre):
            return text_dict.get('raw text'), text_dict.get('title')

json_in.close()