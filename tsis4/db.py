import psycopg2
from config import params

def get_connection():
    return psycopg2.connect(**params)

def init_db():
   
    conn = get_connection()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id),
            score INTEGER NOT NULL,
            level_reached INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def save_result(username, score, level):
   
    conn = get_connection()
    cur = conn.cursor()
   
    cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT DO NOTHING", (username,))
    conn.commit()
    
   
    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    p_id = cur.fetchone()[0]
    
   
    cur.execute("""
        INSERT INTO game_sessions (player_id, score, level_reached) 
        VALUES (%s, %s, %s)
    """, (p_id, score, level))
    
    conn.commit()
    cur.close()
    conn.close()

def get_personal_best(username):
   
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT MAX(score) FROM game_sessions 
        JOIN players ON players.id = game_sessions.player_id
        WHERE players.username = %s
    """, (username,))
    res = cur.fetchone()[0]
    cur.close()
    conn.close()
    return res if res else 0


def get_top_10():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.username, s.score, s.level_reached, s.played_at 
        FROM game_sessions s
        JOIN players p ON p.id = s.player_id
        ORDER BY s.score DESC
        LIMIT 10
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows