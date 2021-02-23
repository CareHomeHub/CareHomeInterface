# py2neo

from py2neo import Graph

graph = Graph("bolt://localhost:7687")

graph.run("MERGE (n:Person {name:'Bob', gender: 'M'})")
graph.run("MERGE (n:Person {name:'Betty', gender: 'F'})")
data = []
result = graph.run("MATCH (n:Person)  RETURN n").data()
for record in result:
    print("THIS is the record: {}".format(record["n"]["gender"]))
    data.append(record["n"]["person"])

# print (data)

# result = graph.run( "WITH date({ year:1984, month:10, day:11 }) AS d\
# RETURN [d.year, d.quarter, d.month, d.week, d.weekYear, d.day, d.ordinalDay, \
#                    d.dayOfWeek, d.dayOfQuarter] as dated").data()
# for record in result:
#     print("DATE = {}".format(record["dated"]))


