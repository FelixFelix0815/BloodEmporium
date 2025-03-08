import itertools
import os.path
import sqlite3
from itertools import zip_longest

from new_data import *


def cloneDatabase(base_path: str, new_path: str):
    # Connect to the existing SQLite database
    source_conn = sqlite3.connect(base_path)
    source_cursor = source_conn.cursor()

    # Connect to the new SQLite database
    destination_conn = sqlite3.connect(new_path)
    destination_cursor = destination_conn.cursor()

    # Get the list of tables in the source database
    source_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = source_cursor.fetchall()

    # Copy each table from the source database to the destination database
    for table_name in tables:
        table_name = table_name[0]
        source_cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        create_table_sql = source_cursor.fetchone()[0]
        destination_cursor.execute(create_table_sql)

        source_cursor.execute(f"SELECT * FROM {table_name};")
        rows = source_cursor.fetchall()
        for row in rows:
            placeholders = ', '.join(['?'] * len(row))
            destination_cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders});", row)

    # Commit the changes and close the connections
    destination_conn.commit()
    source_conn.close()
    destination_conn.close()


def addSurvivorsTable():
    # Connect to the SQLite database
    conn = sqlite3.connect('assets/new_data.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('CREATE TABLE IF NOT EXISTS survivors (id TEXT PRIMARY KEY, alias TEXT, name TEXT)')

    for survivor in survivorData:
        cursor.execute(
            f'INSERT INTO survivors VALUES (\'{survivor[0].lower()}\', \'{survivor[0]}\', \'{survivor[1]}\')')

    conn.commit()

    # Close the connection
    conn.close()


def listPerks():
    # Connect to the SQLite database
    conn = sqlite3.connect('assets/new_data.db')
    cursor = conn.cursor()

    # Retrieve killer perks
    cursor.execute('SELECT * FROM unlockables WHERE type = "perk" AND "order" IS NOT NULL')
    perks = cursor.fetchall()

    for perk in perks:
        print(perk)

    # Close the connection
    conn.close()


def updatePerkOrder():
    # Connect to the SQLite database
    conn = sqlite3.connect('assets/new_data.db')
    cursor = conn.cursor()

    # Update general killer perks
    sorted_general_killer_perks = general_killer_perks
    sorted_general_killer_perks.sort()
    for perk_id, perk in enumerate(sorted_general_killer_perks):
        cursor.execute(f'UPDATE unlockables SET "order" = {500000 + perk_id} WHERE name = "{perk}"')

    # Update general survivor perks
    sorted_general_survivor_perks = general_survivor_perks
    sorted_general_survivor_perks.sort()
    for perk_id, perk in enumerate(sorted_general_survivor_perks):
        cursor.execute(f'UPDATE unlockables SET "order" = {600000 + perk_id} WHERE name = "{perk}"')

    # Update killer perks
    for killer_id, killer in enumerate(killerPerkMap):
        for perk_id, perk in enumerate(killerPerkMap[killer]):
            if "'" not in perk and '"' not in perk:
                cursor.execute(
                    f'UPDATE unlockables SET "order" = {501000 + killer_id * 10 + perk_id} WHERE name = "{perk}"')
            elif "'" in perk and not '"' in perk:
                cursor.execute(
                    f'UPDATE unlockables SET "order" = {501000 + killer_id * 10 + perk_id} WHERE name = "{perk}"')
            elif '"' in perk and not "'" in perk:
                cursor.execute(
                    f'UPDATE unlockables SET "order" = {501000 + killer_id * 10 + perk_id} WHERE name = \'{perk}\'')
            else:
                print(perk)

    # Update survivor perks
    for survivor_id, survivor in enumerate(survivorPerkMap):
        for perk_id, perk in enumerate(survivorPerkMap[survivor]):
            if "'" not in perk and '"' not in perk:
                cursor.execute(
                    f'UPDATE unlockables SET "order" = {601000 + survivor_id * 10 + perk_id} WHERE name = "{perk}"')
            elif "'" in perk and not '"' in perk:
                cursor.execute(
                    f'UPDATE unlockables SET "order" = {601000 + survivor_id * 10 + perk_id} WHERE name = "{perk}"')
            elif '"' in perk and not "'" in perk:
                cursor.execute(
                    f'UPDATE unlockables SET "order" = {601000 + survivor_id * 10 + perk_id} WHERE name = \'{perk}\'')
            else:
                print(perk)

    conn.commit()

    # Close the connection
    conn.close()


def verifyKillerData():
    # Connect to the SQLite database
    conn = sqlite3.connect('assets/new_data.db')
    cursor = conn.cursor()

    # Retrieve killer perks
    cursor.execute('SELECT * FROM killers')
    killers = cursor.fetchall()

    # iterate over killers and killerData
    for killer in zip_longest(killers, killerData):
        if killer[0] is None or killer[1] is None:
            print(f'Killer mismatch: {killer[0]} vs {killer[1]}')
            continue

        if killer[0][0] != killer[1][0]:
            print(f'Killer mismatch: {killer[0][0]} vs {killer[1][0]}')
        if killer[0][1] != killer[1][1]:
            print(f'Killer mismatch: {killer[0][1]} vs {killer[1][1]}')
        if killer[0][2] != killer[1][2]:
            print(f'Killer mismatch: {killer[0][2]} vs {killer[1][2]}')

    # Close the connection
    conn.close()


def updateWrongKillerPerks():
    conn = sqlite3.connect('assets/new_data.db')
    cursor = conn.cursor()

    # Update Monitor & Abuse
    cursor.execute('UPDATE unlockables SET name = "Monitor & Abuse" where name = "Monitor and Abuse"')

    # Update hangman's trick
    cursor.execute('UPDATE unlockables SET name = "Scourge Hook: Hangman\'s Trick" where name = "Hangman\'s Trick"')

    # Update Awakened Awareness
    cursor.execute('UPDATE unlockables SET name = "Awakened Awareness" where name = "Awakened Awarenesss"')

    conn.commit()
    conn.close()


def updateWrongSurvivorPerks():
    conn = sqlite3.connect('assets/new_data.db')
    cursor = conn.cursor()

    # Update Mettle of Man
    cursor.execute('UPDATE unlockables SET name = "Mettle of Man" where name = "Mettle Of Man"')

    # Update Circle of Healing
    cursor.execute('UPDATE unlockables SET name = "Boon: Circle of Healing" where name = "Boon: Circle Of Healing"')

    # Update Made for This
    cursor.execute('UPDATE unlockables SET name = "Made for This" where name = "Made For This"')

    conn.commit()
    conn.close()


def verify_new_data():
    conn = sqlite3.connect('assets/new_data.db')
    cursor = conn.cursor()

    # Verify killer perks
    cursor.execute('SELECT * FROM unlockables WHERE type = "perk" AND "order" BETWEEN 500000 AND 599999')
    killer_perks = cursor.fetchall()

    if len(killer_perks) != len(general_killer_perks) + len(killerPerkMap) * 3:
        print('Killer perks length mismatch')

    for perk in killer_perks:
        if perk[1] not in general_killer_perks and perk[1] not in itertools.chain(*killerPerkMap.values()):
            print(f'Killer perk not found: {perk[1]}')

    for perk in itertools.chain(*killerPerkMap.values(), general_killer_perks):
        cursor.execute(f'SELECT * FROM unlockables WHERE name = "{perk}"')
        if cursor.fetchone() is None:
            print(f'Killer perk not found: {perk}')

    # Verify survivor perks
    cursor.execute('SELECT * FROM unlockables WHERE type = "perk" AND "order" BETWEEN 600000 AND 699999')
    survivor_perks = cursor.fetchall()

    if len(survivor_perks) != len(general_survivor_perks) + len(survivorPerkMap) * 3:
        print('Survivor perks length mismatch')

    for perk in survivor_perks:
        if perk[1] not in general_survivor_perks and perk[1] not in itertools.chain(*survivorPerkMap.values()):
            print(f'Survivor perk not found: {perk[1]}')

    for perk in itertools.chain(*survivorPerkMap.values(), general_survivor_perks):
        cursor.execute(f'SELECT * FROM unlockables WHERE name = "{perk}"')
        if cursor.fetchone() is None:
            print(f'Survivor perk not found: {perk}')

    # Verify killers
    cursor.execute('SELECT * FROM killers')
    killers = cursor.fetchall()

    if len(killers) != len(killerData):
        print('Killers length mismatch')

    for killer in killers:
        if killer not in killerData:
            print(f'Killer not found: {killer[0]}')

    for killer in killerData:
        cursor.execute(
            f'SELECT * FROM killers WHERE id = "{killer[0]}" AND alias = "{killer[1]}" AND name = "{killer[2]}"')
        if cursor.fetchone() is None:
            print(f'Killer not found: {killer[0]}')

    # Verify killerPerkMap Keys
    if len(killers) != len(killerPerkMap):
        print('Killers length mismatch')

    for killer in killers:
        if killer[0] not in killerPerkMap:
            print(f'Killer not found: {killer[0]}')

    # Verify survivors
    cursor.execute('SELECT * FROM survivors')
    survivors = cursor.fetchall()

    if len(survivors) != len(survivorData):
        print('Survivors length mismatch')

    for survivor in survivors:
        if (survivor[1], survivor[2]) not in survivorData:
            print(f'Survivor not found: {survivor[0]}')

    for survivor in survivorData:
        cursor.execute(
            f'SELECT * FROM survivors WHERE id = "{survivor[0].lower()}" AND alias = "{survivor[0]}" AND name = \'{survivor[1]}\'')
        if cursor.fetchone() is None:
            print(f'Survivor not found: {survivor[0]}')

    # Verify survivorPerkMap Keys
    if len(survivors) != len(survivorPerkMap):
        print('Survivors length mismatch')

    for survivor in survivors:
        if survivor[0] not in survivorPerkMap:
            print(f'Survivor not found: {survivor[0]}')


def updatePerkCategory():
    conn = sqlite3.connect('assets/new_data.db')
    cursor = conn.cursor()

    for killer in killerPerkMap:
        for perk in killerPerkMap[killer]:
            cursor.execute(f'UPDATE unlockables SET category = \'{killer}\' WHERE name = "{perk}"')

    for survivor in survivorPerkMap:
        for perk in survivorPerkMap[survivor]:
            cursor.execute(f'UPDATE unlockables SET category = \'{survivor}\' WHERE name = "{perk}"')

    conn.commit()
    conn.close()


if not os.path.exists('assets/new_data.db'):
    cloneDatabase('assets/data.db', 'assets/new_data.db')

verify_new_data()
