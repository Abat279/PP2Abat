# ── Экран ────────────────────────────────────────────────────────
WIDTH  = 600
HEIGHT = 600
CELL   = 30

# ── Ойын ────────────────────────────────────────────────────────
BASE_FPS   = 5
MAX_LEVEL  = 20

# ── PostgreSQL (қажет болса толтыр) ─────────────────────────────
DB_CONFIG = {
    'host':     'localhost',
    'port':     5432,
    'database': 'snake_db',
    'user':     'postgres',
    'password': '1234',   # өз паролін жаз
}

# ── Файлдар ──────────────────────────────────────────────────────
SETTINGS_FILE    = 'TSIS/TSIS4/settings.json'
LEADERBOARD_FILE = 'TSIS/TSIS4/leaderboard.json'

# ── Түстер (settings.json-нан қайта жазылады) ───────────────────
DEFAULT_SETTINGS = {
    'sound':       True,
    'snake_color': 'red',      # red | green | blue | yellow
    'bg_color':    'black',    # black | dark_green | navy
}

SNAKE_COLORS = {
    'red':    (220,  50,  50),
    'green':  ( 50, 200,  50),
    'blue':   ( 50, 100, 220),
    'yellow': (220, 200,  50),
}

BG_COLORS = {
    'black':      (  0,   0,   0),
    'dark_green': (  0,  30,   0),
    'navy':       (  0,   0,  40),
}
