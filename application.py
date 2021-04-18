from flask import Flask, request, flash, url_for, redirect, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from collections import OrderedDict

app = Flask(__name__)

engine = create_engine("sqlite:///book.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session=Session()

Base = automap_base()
Base.prepare(engine, reflect=True)
Book = Base.classes.Book

@app.route('/')
def home():
    result = { 
        "Documentation":[
            {
                "Link" : "https://remoteproject.hauntedvideosvi.repl.co/show?count=50",
                "Request Type":"GET",
                "Description" : "To get the first n records from the data base",
                "Parameter" : "count is to be given as show in Link",
                "Body" : "Not Applicable"
                },
            {
                "Link" : "https://remoteproject.hauntedvideosvi.repl.co/find",
                "Request Type":"GET",
                "Description" : "to get the applicable result from database as column name and column data are provided in example",
                "Parameter" : "Not Applicable",
                "Body" : "{'author':'Bayo Ogunjimi'}"
                }
        ]
    }

    return(jsonify(result))

@app.route('/show')
def show_all():
    if 'count' in request.args:
        temp = request.args['count']
        records=session.query(Book).limit(temp).all()
        result={"books":[]}

        for record in records:
            recordObject = OrderedDict()
            recordObject = {
                'id': record.id,
                'title': record.title,
                'author': record.author,
                'authors': record.authors,
                'isbn13': record.isbn13,
                'isbn10': record.isbn10,
                'price': record.price,
                'publisher': record.publisher,
                'pubyear': record.pubyear,
                'subjects': record.subjects,
                'lexile': record.lexile,
                'pages': record.pages,
                'dimensions': record.dimensions
            }
            result["books"].append(recordObject)
        return(jsonify(result))
    else:
        return({'msg':'Paramater is missing from the request'})

@app.route('/find', methods = ['POST'])
def find():
     if request.method == 'POST':
        if not request.data:
             return({'msg':'Paramater is missing from the request'})
        else:
            try:
                (col_name, col_val), = (dict(json.loads(request.data))).items()
            except Exception as e:
                return({'msg':'Invalid Parameter is provided.'})
            else:
                try:
                    records = session.query(Book).filter(Book.__table__.c[col_name]==col_val).all()
                except Exception as e:
                    return({'msg':'No such column exists in table.'})
                else:
                    result={"books":[]}
                    for record in records:
                        recordObject = OrderedDict()
                        recordObject = {
                            'id': record.id,
                            'title': record.title,
                            'author': record.author,
                            'authors': record.authors,
                            'isbn13': record.isbn13,
                            'isbn10': record.isbn10,
                            'price': record.price,
                            'publisher': record.publisher,
                            'pubyear': record.pubyear,
                            'subjects': record.subjects,
                            'lexile': record.lexile,
                            'pages': record.pages,
                            'dimensions': record.dimensions
                        }
                        result["books"].append(recordObject)
                    return(jsonify(result))
             
if __name__ == '__main__':
    app.run(debug = True)