import myFramework.source.posgresql.connect as conn
# from myFramework.utils.Yaml import yaml
import pandas as pd



def getTbaleList(dbname, schema):
        return pd.read_sql(f"select tablename  from pg_catalog.pg_tables where schemaname = '{schema}'"
                        ,conn.getConnection(dbname))


def fillstaging(df, dst_dbname, schema, tablename):
        df.to_sql(tablename, conn.getConnection(dst_dbname)
                , schema=f"{schema}", if_exists='replace', index=False)
        

def getDF( source_dbname, tablename, schema):
        return pd.read_sql(f"select * from {schema}.{tablename}"
                ,conn.getConnection(source_dbname))


# def getDF( source_dbname, tablename,schema,colName, dateFrom, dateTo):
#         return pd.read_sql(f"select * from {schema}.{tablename} where {dateFrom}>= {colName} and {dateTo} < {colName}"
#                 ,conn.getConnection(source_dbname))


