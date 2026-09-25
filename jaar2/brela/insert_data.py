data = []


with open('biodiversity.tsv', 'r') as file:
    for line in file:
        data.append(line.strip().split('\t'))
    data.pop(0)
    file.close()


counties = set()
for row in range(len(data)):
    counties.add(data[row][0])


def insert_county(cursor):
    for county in counties:
        cursor.execute("INSERT INTO county (county_name) VALUES (%s) RETURNING county_id", (county,))
    county_id = cursor.fetchone()[0]
    return county_id
