from py2neo import Graph

graph = Graph("bolt://graph_db:7687")

queryStr = """
merge (a :CELL { cell_ref:'REF_0001'})
merge (b :LOC {loc_ref:'REF_L0002'} )
merge (a)-[:CURRENT_STATE]->(b)  
RETURN a
"""

queryStr1 = """
MATCH (a:CELL)-[:CURRENT_STATE]->()  
RETURN a.cell_ref
"""

def executeQry_df1(queryStr):
    dat = graph.run(queryStr).to_data_frame()
    print(f"dat: \n{dat}\n")
    return dat

tbl_qry = "UNWIND range(1, 3) AS n RETURN n, n * n as n_sq"

def executeQry_tbl1(queryStr):
    tbl = graph.run(queryStr).to_table()
    print(f"tbl \n{tbl}\n")
    return tbl




executeQry_df1(queryStr)
executeQry_df1(queryStr1)

executeQry_tbl1(tbl_qry)
