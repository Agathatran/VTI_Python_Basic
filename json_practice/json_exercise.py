#Exercise 1: Convert a dictionary to json format
import json
'''def convert_dic_to_json():
    data ={'key1':'value1', 
           'key2': 'value2', 
           'key3':'value3'}
    json_data = json.dumps(data)
    print(json_data)
convert_dic_to_json()

# Exercise 2: Access to the value ò a key from a json object
def access_to_value():
    json_str = """{"key1":"value1", "key2":"value2", "key3":"value3"}"""
    json_data = json.loads(json_str)
    print(f'Value with key key2 is {json_data["key2"]}')
access_to_value()

#Exercise 3: Pretty print json data
def pretty_json_data():
    json_data={'key1':'value1', 
           'key2': 'value2', 
           'key3':'value3'}
    pretty_json = json.dumps(json_data, indent=2, separators = (",","="))
    print(pretty_json)
#test function
pretty_json_data()

#Exercise 4:Write data to json file
def write_json():
    json_data = {"id":10, "name": "Pham Van Manh", "age":31, "address":"Hanoi"}
    # open json file to write
    with open('sample_json.json','w') as json_file:
        json.dump(json_data, json_file, indent=4 , sort_keys=True)
    #test function
write_json()
'''
#Exercise 5: Access the key "salary" from a nested json
def json_nested_access():
    json_str = """{
        "company":{
            "employee1":{
             "name":"Pham Van Nam", 
             "payable": {
                "salary":"1200$",
                "bonus":"300$"
            },
            "position":"Leader"
            }
        }
    }
    """
    json_data = json.loads(json_str)
    # print(json_data)
    salary_emp1=json_data['company']['employee1']['payable']['salary']
    print(f'Salary of employee 1 is: {salary_emp1}')
    #save to json file
    with open('company.json','w') as json_file:
        json.dump(json_data, json_file, indent=4, sort_keys=True )
json_nested_access()
