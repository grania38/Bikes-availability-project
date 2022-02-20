from elasticsearch import Elasticsearch

elastic = Elasticsearch([{'host': 'localhost', 'port': 9200}])
elastic.indices.create(index='ranii23')
print(elastic.indices.get_alias().keys())
print(elastic.info())
