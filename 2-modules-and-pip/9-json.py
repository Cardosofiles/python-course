import json

# 1 - Strings para Dicionário 
person =  '{"name": "Rodrigo", "languagens": ["Python", "Javascript"]}' 
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])

# 2 - Convertendo dicionário para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_dict))
print(type(person_json))

# 3 - Formatar o json 
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)