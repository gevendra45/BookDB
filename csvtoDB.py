import csv
from sqlalchemy import create_engine, Table, Column, Integer, MetaData, String

engine = create_engine('sqlite:///book.db', echo=True)

metadata = MetaData()

my_table = Table('Book', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(100)),
    Column('author', String(100)),
    Column('authors', String(100)),
    Column('isbn13', String(100)),
    Column('isbn10', String(100)),
    Column('price', String(100)),
    Column('publisher', String(100)),
    Column('pubyear', String(100)),
    Column('subjects', String(100)),
    Column('lexile', String(100)),
    Column('pages', String(100)),
    Column('dimensions', String(100))
)

metadata.create_all(engine)
insert_query = my_table.insert()

with open('C:\\Users\\verma\\Downloads\\faltuproj\\books1.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)
    engine.execute(
        insert_query,
        [{'id': row[0], 'title': row[1], 'author': row[2], 'authors': row[3], 'isbn13': row[4], 'isbn10': row[5], 'price': row[6], 'publisher': row[7], 'pubyear': row[8], 'subjects': row[9], 'lexile': row[10], 'pages': row[11], 'dimensions': row[12]} 
            for row in csv_reader]
    )
