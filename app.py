from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Configuración obtenida desde variables de entorno
APP_NAME = os.getenv("APP_NAME", "Inventario API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0") 
DB_NAME = os.getenv("DB_NAME", "inventario")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


@app.route("/")
def home():

    try:
        conn = get_connection()
        conn.close()
        estado = "Conectado"
    except Exception:
        estado = "Error de conexión"

    return jsonify({
        "aplicacion": APP_NAME,
        "version": APP_VERSION,
        "postgresql": estado
    })


@app.route("/productos")
def productos():

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, nombre, precio, stock
            FROM productos
            ORDER BY id
        """)

        rows = cur.fetchall()

        resultado = []

        for row in rows:
            resultado.append({
                "id": row[0],
                "nombre": row[1],
                "precio": float(row[2]),
                "stock": row[3]
            })

        cur.close()
        conn.close()

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)