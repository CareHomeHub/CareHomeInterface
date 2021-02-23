from neo4j import GraphDatabase
# point = point({ x: 2.3, y: 4.5, crs: 'cartesian' })


driver = GraphDatabase.driver("bolt://192.0.0.1:7687")


sessionObj = driver.session()


result = sessionObj.run( "WITH date({ year:1984, month:10, day:11 }) AS d RETURN [d.year, d.quarter, d.month, d.week, d.weekYear, d.day, d.ordinalDay, d.dayOfWeek, d.dayOfQuarter] as dated")
for record in result:
    print("DATE = {}".format(record["dated"]))

result = sessionObj.run("MATCH (n:Person) where n.name = 'Betty' RETURN [n.name, n.gender] AS name")
for record in result:
    print(record["name"][1])
sessionObj.close()
