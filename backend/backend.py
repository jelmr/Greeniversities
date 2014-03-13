from flask import Flask
from flask.ext import restful

from app import models, db


class UniversityList(restful.Resource):
    def get(self):
        universities = models.University.query.all()
        university_list = [{u.id : u.name} for u in universities]
        return {'universities': university_list}

class UniversityScore(restful.Resource):
    def get(self, university_id):
        documents = ['Lago Green IT']
        name = models.University.query.get(university_id).name
        return {'name': name, 'score': max(university_id%10+5, 6), 'documents': documents }


if __name__ == '__main__':
    app.run(debug=True)
