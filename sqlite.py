from coverage import Coverage

cov = Coverage()
cov.load()

total_stmts = 0
total_miss = 0

for file in cov.get_data().measured_files():
    _, stmts, _, miss, _ = cov.analysis2(file)
    total_stmts += len(stmts)
    total_miss += len(miss)

coverage_percent = 100.0 * (total_stmts - total_miss) / total_stmts
print(f"合并后的总覆盖率: {coverage_percent:.2f}%")