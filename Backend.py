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
    cur.execute("UPDATE players SET team_id=?, fname=?, lname=?, age=?, salary=?, position=?, weight=?, height=?, avr_point=?, avr_asist=?, avr_rebound=? WHERE id=?", (id,team_id,fname,lname,age,salary,position,weight,height,avr_point,avr_asist,avr_rebound))
    conn.commit()
    conn.close()


def insert_team(captain_id, coach_id, team_name, city):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO teams VALUES(NULL,?,?,?,?)",
                (captain_id, coach_id, team_name, city))
    conn.commit()
    conn.close()


def view_team():
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM teams")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_team(captain_id ="", coach_id="", team_name="", city=""):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM teams WHERE captain_id=? OR coach_id=? OR team_name=? OR city=?",
                (captain_id, coach_id, team_name, city))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_team(id):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM teams WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update_team(id, captain_id, coach_id, team_name, city):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("UPDATE teams SET captain_id=?, coach_id=?, team_name=?, city=? WHERE id=?", (id,captain_id,coach_id,team_name,city))
    conn.commit()
    conn.close()


def insert_staff(team_id, role, fname, lname, salary, sex):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO staffs VALUES(NULL,?,?,?,?,?,?)",
                (team_id, role, fname, lname, salary, sex))
    conn.commit()
    conn.close()


def view_staff():
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM staffs")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_staff(team_id="", role="", fname="", lname="", salary="", sex=""):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM staffs WHERE team_id=? OR role=? OR fname=? OR lname=? OR salary=?, OR sex=?",
                (team_id, role, fname, lname, salary, sex))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_staff(id):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM staffs WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update_staff(id, team_id, role, fname, lname, salary, sex):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("UPDATE teams SET team_id=?, role=?, fname=?, lname=?, salary=?, sex=? WHERE id=?", (id,team_id,role,fname,lname,salary,sex))
    conn.commit()
    conn.close()


def insert_dependent(depent_id, fname, lname, relationship, sex):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO dependents VALUES(NULL,?,?,?,?,?)",
                (depent_id, fname, lname, relationship, sex))
    conn.commit()
    conn.close()


def view_dependent():
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dependents")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_dependent(depent_id="", fname="", lname="", relationship="", sex=""):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM players WHERE depent_id=? OR fname=? OR lname=? OR relationship=? OR sex=? ",
                (depent_id, fname, lname, relationship, sex))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_dependent(id):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM dependents WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update_dependent(id, depent_id, fname, lname, relationship, sex):
    conn = sqlite3.connect("NBA.db")
    cur = conn.cursor()
    cur.execute("UPDATE dependents SET depent_id=?, fname=?, lname=?, relationship=?, sex=? WHERE id=?", (id,depent_id,fname,lname,relationship,sex))
    conn.commit()
    conn.close()


connect()