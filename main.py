import myFramework.utils.utils as utils
from sqltostaging.initial.toStaging import ToStaging as toStaging_initial
from sqltostaging.incremental.toStaging import ToStaging as toStaging_incremental
from sqltostaging.full.toStaging import ToStaging as toStaging_full


from myFramework.utils.readYaml import ReadYaml


testread = ReadYaml("/Users/mariammakharadze/DEProject/DEProject/conf/tostaging/dvdrental/full/full.yaml", 'public.category')



# initial
test = toStaging_initial("dvdrental", "public")
tbname_Df = utils.getTbaleList(test.dbname,test.schema)['tablename']
for tbname in tbname_Df:    
    utils.fillstaging(utils.getDF(test.dbname, test.schema,tbname),"DBStaging","dvdrental")
   
   
# full load
test = toStaging_full(testread.path, testread.key)    
utils.fillstaging(utils.getDF(test.getDBName(), test.getTableName(),test.getSchema()),"DBStaging","dvdrental",test.getTableName())


