data = []


with open('jaar2/brela/biodiversity.tsv', 'r') as file:
    for line in file:
        data.append(line.strip().split('\t'))
    data.pop(0)
    file.close()


def insert_row(cursor, row):
    county, sci_name, common_name, year, subtax, tax, status = row
    year = None if year == 'NA' else year  

    cursor.execute("INSERT INTO county (county_name) VALUES (%s) ON CONFLICT DO NOTHING", (county,))
    cursor.execute("INSERT INTO taxonomy (tax_name) VALUES (%s) ON CONFLICT DO NOTHING", (tax,))
    cursor.execute("INSERT INTO status (description) VALUES (%s) ON CONFLICT DO NOTHING", (status,))
    cursor.execute("INSERT INTO subtax (subtax_name, tax_name) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                   (subtax, tax))
    cursor.execute("""INSERT INTO biological_entity (scientific_name, common_name, subtax_name, description)
                      VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING""",
                   (sci_name, common_name, subtax, status))
    cursor.execute("INSERT INTO sighting (county_name, scientific_name, year) VALUES (%s, %s, %s)",
                   (county, sci_name, year))


def insert_all(cursor):
    for row in data:
        insert_row(cursor, row)
