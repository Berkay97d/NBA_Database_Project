import sqlite3


def connect():
    conn = sqlite3.connect("players.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS players(id INTEGER PRIMARY KEY, "
                "                                   team_id INTEGER,"
                "                                   fname text, "
                "                                   lname text,"
                "                                   age INTEGER,"
                "                                   salary INTEGER,"
                "                                   position text,"
                "                                   weight INTEGER,"
                "                                   height INTEGER,"
                "                                   avr_point INTEGER,"
                "                                   avr_asist INTEGER,"
                "                                   avr_rebound INTEGER )")
    conn.commit()
    conn.close()


def insert(team_id, fname, lname, age, salary, position, weight, height, avr_point, avr_asist, avr_rebound):
    conn = sqlite3.connect("players.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO players VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?)",
                (team_id, fname, lname, age, salary, position, weight, height, avr_point, avr_asist, avr_rebound))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("players.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM players")
    rows = cur.fetchall()
    conn.close()
    return rows


connect()
