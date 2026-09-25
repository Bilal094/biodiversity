def create_county():
    return """ CREATE TABLE IF NOT EXISTS county
                (
                    county_name VARCHAR(50) PRIMARY KEY
                )
            """

def create_sighting():
    return """ CREATE TABLE IF NOT EXISTS sighting
                (
                    county_name VARCHAR(50),
                    scientific_name VARCHAR(50),
                    year DATE,

                    FOREIGN KEY (county_name) REFERENCES county(county_name),
                    FOREIGN KEY (scientific_name) REFERENCES biological_entity(scientific_name)
                )
            """

def create_biological_entity():
    return """ CREATE TABLE IF NOT EXISTS biological_entity
            (
                scientific_name VARCHAR(50) PRIMARY KEY,
                common_name VARCHAR(50),
                subtax_name VARCHAR(50),
                description VARCHAR(50),

                FOREIGN KEY (subtax_name) REFERENCES subtax(subtax_name),
                FOREIGN KEY (description) REFERENCES status(description)
            )
        """

def create_status():
    return """ CREATE TABLE IF NOT EXISTS status
            (
                description VARCHAR(50) PRIMARY KEY
            )
        """

def create_subtax():
    return """ CREATE TABLE IF NOT EXISTS subtax
            (
                subtax_name VARCHAR(50) PRIMARY KEY,
                tax_name VARCHAR(50),

                FOREIGN KEY (tax_name) REFERENCES taxonomy(tax_name)
            )
        """

def create_taxonomy():
    return """ CREATE TABLE IF NOT EXISTS taxonomy
            (
                tax_name VARCHAR(50) PRIMARY KEY
            )
        """

def execute_queries(cursor):
    queries = [
        create_county(),
        create_status(),
        create_taxonomy(),
        create_subtax(),
        create_biological_entity(),
        create_sighting()
    ]

    for query in range(len(queries)):
        cursor.execute(queries[query])