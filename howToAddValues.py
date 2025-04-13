res = cur.execute(f"SELECT * FROM RegularCostCat")
print(res.fetchall())

cur.execute("INSERT INTO RegularCostCat (CostID, CostCatName, CreationDate) VALUES (1, \"Gas\", \"1/2/2025\")")
con.commit()

res = cur.execute(f"SELECT * FROM RegularCostCat")
print(res.fetchall())