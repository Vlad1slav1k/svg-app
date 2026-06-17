from fastapi import FastAPI
import psycopg2
import time

from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
Instrumentator().instrument(app).expose(app)

def get_conn():
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="appdb",
            user="postgres",
            password="postgres",
            connect_timeout=3   # ✅ IMPORTANT
        )
        return conn
    except Exception as e:
        print("❌ DB connection failed:", e)
        return None



@app.post("/click/{button_id}")
def click(button_id: int):
    conn = get_conn()

    if not conn:
        return {"error": "DB not available"}

    try:
        conn.set_session(autocommit=True)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO clicks (button_id, count)
            VALUES (%s, 1)
            ON CONFLICT (button_id)
            DO UPDATE SET count = clicks.count + 1
        """, (button_id,))

        conn.close()

        return {"status": "ok"}

    except Exception as e:
        print("❌ ERROR in click:", e)
        return {"error": str(e)}


@app.get("/stats")
def stats():
    conn = get_conn()

    if not conn:
        return {"error": "DB not available"}

    try:
        conn.set_session(autocommit=True)
        cur = conn.cursor()

        cur.execute("SELECT button_id, count FROM clicks;")
        data = cur.fetchall()

        conn.close()

        return data

    except Exception as e:
        print("❌ ERROR in stats:", e)
        return {"error": str(e)}

