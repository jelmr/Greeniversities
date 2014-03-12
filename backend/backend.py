from flask import Flask
from flask.ext import restful



class UniversityList(restful.Resource):
    def get(self):
        return {'hello': 'world'}

class UniversityScore(restful.Resource):
    def get(self, university_id):
        documents = ['Lago Green IT']
        return {'score': max(university_id%10+5, 6), 'documents': documents }


if __name__ == '__main__':
    app.run(debug=True)
