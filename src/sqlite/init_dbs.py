"""
This file contains all init functions to be run once only.
"""


def init_character_db(char_db_filename):
    """initializes the character database"""
    import connection

    conn = connection.create_connection(char_db_filename)
    cur = conn.cursor()

    create_char_table = 'CREATE TABLE "Characters" (Name TEXT PRIMARY KEY, Class TEXT, Level INTEGER, ' \
                        'Background TEXT, NPC INTEGER, Race TEXT, Alignment TEXT, Proficiency INTEGER, ' \
                        'Strength INTEGER, Dexterity INTEGER, Constitution INTEGER, Intelligence INTEGER, ' \
                        'Wisdom INTEGER, Charisma INTEGER, ProficientIn TEXT, DoublyProficientIn TEXT, ' \
                        'WornACBonus INTEGER, TotalAC INTEGER, Initiative INTEGER, Speed INTEGER, MaxHP INTEGER, ' \
                        'CurrHP INTEGER, TempHP INTEGER, Backstory TEXT, SpellSlots TEXT, SpellsKnown TEXT, ' \
                        'Equipment TEXT, CurrentLocation TEXT, Loot TEXT, Tags TEXT)'

    cur.execute(create_char_table)
    conn.commit()
    conn.close()