import yaml
import os


class ReadYaml:

    def __init__(self, path, key):
        self.path = path
        self.key = key
    
    # private mthod
    def __getYaml (self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        yaml_file_path = os.path.join(script_directory, self.path)
        with open(yaml_file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
        return yaml_data[self.key]
    
    def getTableName(self ):
        return self.__getYaml()['TableName']
    
    def getDBName(self ):
        return self.__getYaml()['DBName']
    
    def getSchema(self ):
        return self.__getYaml()['Schema']
    
    def getTableType(self ):
        return self.__getYaml()['TableType']
    
    
testread = ReadYaml("/Users/ramazkapanadze/DEProject/DEProject/conf/tostaging/dvdrental/full/full.yaml", 'public.category')


print(testread.getTableName())
print(testread.getDBName())
print(testread.getSchema())
print(testread.getTableType())
