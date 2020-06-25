import sqlite3
#from gists_database.search import search_gists
from tests.fixtures import populated_gists_database
import os
from os.path import dirname as dot

BASE_TESTS_PATH = dot(__file__)
BASE_PROJECT_PATH = dot(dot(__file__))

TESTING_DATABASE_NAME = 'testing_gists_database.db'
TESTING_DATABASE_PATH = os.path.join(BASE_TESTS_PATH, TESTING_DATABASE_NAME)

class Gist(object):
    def __init__(self, gist):
        self.id = gist[0]
        self.github_id = gist[1]
        self.html_url = gist[2]
        self.git_pull_url = gist[3]
        self.git_push_url = gist[4]
        self.commits_url = gist[5]
        self.forks_url = gist[6]
        self.public = gist[7]
        self.created_at = gist[8]
        self.updated_at = gist[9]
        self.comments = gist[10]
        self.comments_url = gist[11]

    def __str__(self):
        return 'Gist: {}'.format(self.github_id)


def search_gists(db_connection, **kwargs):
    if kwargs and 'created_at' in kwargs.keys():
        params=kwargs
        query="""SELECT * FROM gists WHERE datetime(created_at) = datetime(:created_at);"""
        cursor=db_connection.executemany(query, params)
    elif kwargs and 'github_id' in kwargs.keys():
        params=kwargs
        query="""SELECT * FROM gists WHERE github_id = :github_id;"""
        cursor=db_connection.executemany(query, params)
    elif not kwargs:
        #query="""SELECT * FROM gists;"""
        cursor=db_connection.execute('SELECT * FROM gists')
        print('x')
    
    list_gists=[Gist(i) for i in cursor]
    print(list_gists)
    print(len(list_gists))
    return list_gists
    
db2 = sqlite3.connect('tests/populated_gists_database.db')

search_gists(sqlite3.connect('c:/Users/pcrrt/OneDrive/Documents/GitHub/project-gist-databases/tests/populated_gists_database.db'))

'''
db = sqlite3.connect('tests/populated_gists_database.db')
db.row_factory = sqlite3.Row




cursor = db.execute('SELECT * FROM gists')

for gist in cursor:
    print('Id: ', gist['id'])
    print('Github Id: ', gist['github_id'])
    print('Html Url: ', gist['html_url'])
    print('Git Pull Url: ', gist['git_pull_url'])
    print('Git Push Url: ', gist['git_push_url'])
    print('Commits Url: ', gist['commits_url'])
    print('Forks Url: ', gist['forks_url'])
    print('Public: ', gist['public'])
    print('Created At: ', gist['created_at'])
    print('Updated At: ', gist['updated_at'])
    print('Comments: ', gist['comments'])
    print('Comments Url: ', gist['comments_url'])
    print('=' * 60)
'''