import sqlite3


def connect():
    conn = sqlite3.connect("NBA.db")
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

    cur.execute("CREATE TABLE IF NOT EXISTS teams(id INTEGER PRIMARY KEY, "
                "                                   captain_id INTEGER,"
                "                                   coach_id INTEGER, "
                "                                   team_name text,"
                "                                   city text)")

    cur.execute("CREATE TABLE IF NOT EXISTS staffs(id INTEGER PRIMARY KEY, "
                "                                   team_id INTEGER,"
                "                                   role text, "
                "                                   fname text,"
                "                                   lname text,"
                "                                   salary INTEGER,"
                "                                   sex text)")

    cur.execute("CREATE TABLE IF NOT EXISTS dependents(id INTEGER PRIMARY KEY, "
                "                                   dependent_id INTEGER,"
                "                                   fname text, "
                "                                   lname text,"
                "                                   depenpent_fname text,"
                "                                   depenpent_lname text,"
                "                                   relationship text,"
                "                                   sex text)")
    conn.commit()
    conn.close()


def insert_player(team_id, fname, lname, age, salary, position, weight, height, avr_point, avr_asist, avr_rebound):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO players VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?)",
                (team_id, fname, lname, age, salary, position, weight, height, avr_point, avr_asist, avr_rebound))
    conn.commit()
    conn.close()


def view_player():
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM players")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_player(team_id="", fname="", lname="", age="", salary="", position="", weight="", height="", avr_point="", avr_asist="", avr_rebound=""):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM players WHERE team_id=? OR fname=? OR lname=? OR age=? OR salary=? OR position=? OR weight=? OR height=? OR avr_point=? OR avr_asist=? OR avr_rebound=?",
                (team_id, fname, lname, age, salary, position, weight, height, avr_point, avr_asist, avr_rebound))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_player(id):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM players WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update_player(id, team_id, fname, lname, age, salary, position, weight, height, avr_point, avr_asist, avr_rebound):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("UPDATE players SET team_id=?, fname=?, lname=?, age=?, salary=?, position=?, weight=?, height=?, avr_point=?, avr_asist=?, avr_rebound=? WHERE id=?", (id,team_id,fname,lname,age,salary,position,weight,height,avr_point,avr_asist,avr_rebound,id))
    conn.commit()
    conn.close()

#TODO team,staff,dependent için fonkiyonlar eklenecek!

insert_player(1, "berkay", "dindar", 25, 15000, "pg",15,15,15,15,15)
connect()