from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://th3khan:Deyvis3110*@localhost:3306/restapi-fastapi")

meta = MetaData()

conn = engine.connect()
