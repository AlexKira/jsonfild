import json
import pandas as pd

with open(input("Input names Json: ")) as f:
    data_listofdict = json.load(f)
    print(pd.DataFrame(data_listofdict))
# We can do the same thing with pandas
data_df = pd.read_json(input("Input names Json: "), orient='records')

print(pd.DataFrame(data_df))

with open('new_file.json', 'w+') as json_file:
    json.dump(data_listofdict, json_file, indent=4, sort_keys=True)

# And again the same thing with pandas
export = data_df.to_json('new_file.json', orient='records')
print(pd.DataFrame(export))

with open('new_file.json') as fp:
    obj = json.load(fp)
    print(obj)
