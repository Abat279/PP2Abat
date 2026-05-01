import pygame
from pygame.locals import *
import random
import math
import os

# ── Colours ──────────────────────────────────────────────────────
GRAY        = (100, 100, 100)
DARK_ROAD   = (70,  70,  70)
GREEN_GRASS = (55, 160,  40)
RED         = (200,  0,   0)
WHITE       = (255, 255, 255)
YELLOW      = (255, 232,   0)
GOLD_C      = (255, 215,   0)
SILVER_C    = (192, 192, 192)
BRONZE_C    = (205, 127,  50)
ACCENT      = (0,  220, 180)
ACCENT2     = (255, 80,  80)
DARK        = (15,  15,  25)
ORANGE      = (255, 140,   0)
BLUE        = (60,  120, 220)
PURPLE      = (160,  60, 220)

CAR_COLORS = {
    'default': (220,  60,  60),
    'blue':    ( 60, 120, 220),
    'green':   ( 60, 200,  80),
    'yellow':  (255, 220,   0),
    'purple':  (160,  60, 220),
}

DIFF_PARAMS = {
    'easy':   {'base_speed': 2, 'max_vehicles': 2, 'hazard_freq': 300},
    'normal': {'base_speed': 3, 'max_vehicles': 3, 'hazard_freq': 200},
    'hard':   {'base_speed': 4, 'max_vehicles': 4, 'hazard_freq': 120},
}

MAX_HP = 3

# ════════════════════════════════════════════════════════════════
# IMAGE HELPERS
# ════════════════════════════════════════════════════════════════
_BASE = os.path.dirname(os.path.abspath(__file__))

def _abs(p):
    return os.path.join(_BASE, p)

def _scale(img, target_w):
    s = target_w / img.get_width()
    return pygame.transform.scale(img, (int(img.get_width()*s), int(img.get_height()*s)))

def _load(path, target_w=100):
    try:
        return _scale(pygame.image.load(_abs(path)), target_w)
    except Exception:
        return None

# ── Fallback drawn surfaces ──────────────────────────────────────
def _draw_car(color, w=60, h=100):
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (5, 10, w-10, h-20), border_radius=10)
    for wx, wy in [(2,15),(w-12,15),(2,h-35),(w-12,h-35)]:
        pygame.draw.rect(surf, (30,30,30), (wx, wy, 10, 20), border_radius=3)
    wsc = tuple(min(255, c+80) for c in color)
    pygame.draw.rect(surf, wsc, (12, 18, w-24, 22), border_radius=4)
    return surf

def make_oil_surface():
    surf = pygame.Surface((70, 40), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, (20, 20, 20, 180), (0, 0, 70, 40))
    pygame.draw.ellipse(surf, (60, 0, 80, 120), (5, 5, 60, 30))
    return surf

def make_pothole_surface():
    surf = pygame.Surface((50, 30), pygame.SRCALPHA)
    pygame.draw.ellipse(surf, (40, 30, 20, 200), (0, 0, 50, 30))
    pygame.draw.ellipse(surf, (25, 20, 10, 180), (8, 6, 34, 18))
    return surf

def make_barrier_surface():
    surf = pygame.Surface((80, 30), pygame.SRCALPHA)
    for i, c in enumerate([RED, WHITE]*4):
        pygame.draw.rect(surf, c, (i*10, 0, 10, 30))
    return surf

def _pu_surface(color, letter):
    surf = pygame.Surface((44, 44), pygame.SRCALPHA)
    pygame.draw.circle(surf, (*color, 200), (22, 22), 20)
    f = pygame.font.Font(pygame.font.get_default_font(), 16)
    lbl = f.render(letter, True, WHITE)
    surf.blit(lbl, lbl.get_rect(center=(22,22)))
    return surf

def make_coin_surface(weight):
    surf = pygame.Surface((36, 36), pygame.SRCALPHA)
    col = GOLD_C if weight==5 else (SILVER_C if weight==3 else BRONZE_C)
    pygame.draw.circle(surf, col, (18,18), 16)
    pygame.draw.circle(surf, (0,0,0), (18,18), 16, 2)
    return surf

def make_speedbump_surface():
    surf = pygame.Surface((120, 20), pygame.SRCALPHA)
    pygame.draw.rect(surf, YELLOW, (0, 4, 120, 12), border_radius=4)
    return surf

def make_nitro_strip_surface():
    surf = pygame.Surface((120, 20), pygame.SRCALPHA)
    pygame.draw.rect(surf, (0, 220, 180, 200), (0, 4, 120, 12), border_radius=4)
    for i in range(0, 120, 15):
        pygame.draw.rect(surf, (0,160,130,180), (i, 4, 8, 12))
    return surf

# ── Суреттерді жүктеу ────────────────────────────────────────────
_PLAYER_IMG = _load('Car.png', 80)
_CRASH_IMG  = _load('crash.png', 100)
_ENEMY_NAMES = [
    'Mini_truck.png', 'Mini_van.png', 'Police.png', 'truck.png',
    'taxi.png', 'Ambulance.png', 'Audi.png', 'Black_viper.png',
    'mini_truck.png', 'mini_van.png', 'police.png',
    'ambulance.png', 'audi.png', 'black_viper.png',
]
_ENEMY_IMGS = []
_seen = set()
for _n in _ENEMY_NAMES:
    if _n.lower() in _seen: continue
    img = _load(f'Topdown_vehicle_sprites_pack/{_n}', 80)
    if img:
        _ENEMY_IMGS.append(img)
        _seen.add(_n.lower())

# ════════════════════════════════════════════════════════════════
# SPRITES
# ════════════════════════════════════════════════════════════════
class PlayerVehicle(pygame.sprite.Sprite):
    def __init__(self, x, y, color_name='default'):
        super().__init__()
        self.image = _PLAYER_IMG.copy() if _PLAYER_IMG else _draw_car(CAR_COLORS.get(color_name, CAR_COLORS['default']))
        self.rect  = self.image.get_rect(center=(x, y))
        self.hp            = MAX_HP
        self.invincible    = 0
        self.shield_active = False
        self.shield_timer  = 0
        self.nitro_active  = False
        self.nitro_timer   = 0
        self.nitro_bonus   = 0

    def take_damage(self):
        if self.invincible > 0 or self.shield_active:
            if self.shield_active:
                self.shield_active = False
            return False
        self.hp -= 1
        self.invincible = 90
        return self.hp <= 0

    def update_powerups(self, dt):
        if self.invincible > 0:
            self.invincible -= dt
        if self.nitro_active:
            self.nitro_timer -= dt
            if self.nitro_timer <= 0:
                self.nitro_active = False
                self.nitro_bonus  = 0
        if self.shield_active:
            self.shield_timer -= dt
            if self.shield_timer <= 0:
                self.shield_active = False

    def draw_shield(self, surf):
        if self.shield_active:
            t = pygame.time.get_ticks()
            a = 100 + int(60 * math.sin(t / 200))
            s = pygame.Surface((self.rect.w+20, self.rect.h+20), pygame.SRCALPHA)
            pygame.draw.ellipse(s, (100, 100, 255, a), (0, 0, self.rect.w+20, self.rect.h+20), 3)
            surf.blit(s, (self.rect.x-10, self.rect.y-10))

    def draw_hp(self, surf, x, y):
        for i in range(MAX_HP):
            col = (220, 50, 50) if i < self.hp else (60, 60, 80)
            pygame.draw.circle(surf, col, (x + i*28, y), 10)
            pygame.draw.circle(surf, WHITE, (x + i*28, y), 10, 2)


class EnemyVehicle(pygame.sprite.Sprite):
    _FALLBACK = [(80,80,200),(200,80,80),(80,200,80),(180,120,0),(120,0,180)]
    def __init__(self, x, y):
        super().__init__()
        self.image = random.choice(_ENEMY_IMGS).copy() if _ENEMY_IMGS else _draw_car(random.choice(self._FALLBACK))
        self.rect  = self.image.get_rect(center=(x, y))

class CoinSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        c = random.randint(1,100)
        self.weight = 5 if c<=10 else (3 if c<=40 else 1)
        self.image  = make_coin_surface(self.weight)
        self.rect   = self.image.get_rect(center=(x, y))

class OilSpill(pygame.sprite.Sprite):
    slow = True
    def __init__(self, x, y):
        super().__init__()
        self.image = make_oil_surface()
        self.rect  = self.image.get_rect(center=(x, y))

class Pothole(pygame.sprite.Sprite):
    slow = True
    def __init__(self, x, y):
        super().__init__()
        self.image = make_pothole_surface()
        self.rect  = self.image.get_rect(center=(x, y))

class Barrier(pygame.sprite.Sprite):
    slow = False
    def __init__(self, x, y):
        super().__init__()
        self.image = make_barrier_surface()
        self.rect  = self.image.get_rect(center=(x, y))

class SpeedBump(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = make_speedbump_surface()
        self.rect  = self.image.get_rect(center=(x, y))

class NitroStrip(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = make_nitro_strip_surface()
        self.rect  = self.image.get_rect(center=(x, y))

class PowerUp(pygame.sprite.Sprite):
    LIFETIME = 300
    _COLORS  = {'nitro':(0,200,255), 'shield':(80,80,255), 'repair':(60,200,80)}
    _LETTERS = {'nitro':'N', 'shield':'S', 'repair':'R'}
    def __init__(self, x, y, kind):
        super().__init__()
        self.kind  = kind
        self.image = _pu_surface(self._COLORS[kind], self._LETTERS[kind])
        self.rect  = self.image.get_rect(center=(x, y))
        self.timer = self.LIFETIME
    def update_timer(self):
        self.timer -= 1
        if self.timer <= 0:
            self.kill()

# ════════════════════════════════════════════════════════════════
# MAIN GAME
# ════════════════════════════════════════════════════════════════
def run_game(screen, clock, settings, player_name):
    """Returns (final_score, distance, coins_collected)."""
    W, H = screen.get_size()
    FPS  = 60

    # ── Экран өлшеміне қарай координаталарды масштабтау ─────────
    # Барлық координаталар 1000x1000 базасынан есептелген
    SX = W / 1000.0   # горизонталь масштаб
    SY = H / 1000.0   # вертикаль масштаб

    def sx(v): return int(v * SX)   # x координатасы
    def sy(v): return int(v * SY)   # y координатасы

    # Жол геометриясы — экранға бейімделген
    ROAD_X   = sx(200)
    ROAD_W   = sx(600)
    MARKER_W = sx(10)
    MARKER_H = sy(50)

    LEFT_LINE   = sx(300)
    CENTER_LINE = sx(500)
    RIGHT_LINE  = sx(700)
    LANES       = [LEFT_LINE, CENTER_LINE, RIGHT_LINE]

    diff     = settings.get('difficulty', 'normal')
    params   = DIFF_PARAMS[diff]
    speed    = params['base_speed']
    max_v    = params['max_vehicles']
    hz_frq   = params['hazard_freq']
    sound_on = settings.get('sound', True)

    # ── Дыбыс ───────────────────────────────────────────────────
    bg_music = crash_sound = None
    try:
        bg_music    = pygame.mixer.Sound(_abs('bg_music.mp3'))
        crash_sound = pygame.mixer.Sound(_abs('craaash.mp3'))
        if sound_on: bg_music.play(-1)
    except Exception:
        pass

    # ── Спрайт топтары ──────────────────────────────────────────
    player_grp  = pygame.sprite.Group()
    enemy_grp   = pygame.sprite.Group()
    coin_grp    = pygame.sprite.Group()
    hazard_grp  = pygame.sprite.Group()
    event_grp   = pygame.sprite.Group()
    powerup_grp = pygame.sprite.Group()

    # Ойыншыны экранның төменгі ортасына орналастыру
    player = PlayerVehicle(sx(500), sy(820), settings.get('car_color','default'))
    player_grp.add(player)

    score           = 0
    coins_collected = 0
    distance        = 0.0
    FINISH          = 5000.0
    y_move          = 0
    frame           = 0
    last_mile       = 0
    slow_timer      = 0
    gameover        = False
    running         = True
    font            = pygame.font.Font(pygame.font.get_default_font(), max(16, sy(22)))
    lane_danger     = {L: False for L in LANES}

    def safe_to_spawn():
        for grp in (enemy_grp, hazard_grp):
            for sp in grp:
                if sp.rect.top < sy(200):
                    return False
        return True

    def spawn_enemy():
        if safe_to_spawn():
            enemy_grp.add(EnemyVehicle(random.choice(LANES), -80))

    def spawn_hazard():
        if not safe_to_spawn(): return
        kind = random.choices(['pothole','oil','barrier'], weights=[50,30,20])[0]
        lane = random.choice(LANES)
        lane_danger[lane] = True
        if kind == 'oil':       hazard_grp.add(OilSpill(lane, -60))
        elif kind == 'pothole': hazard_grp.add(Pothole(lane, -50))
        else:                   hazard_grp.add(Barrier(lane, -50))

    def spawn_event():
        lane = random.choice(LANES)
        if random.choice([True, False]):
            event_grp.add(SpeedBump(lane, -50))
        else:
            event_grp.add(NitroStrip(lane, -50))

    def spawn_powerup():
        if len(powerup_grp) == 0:
            powerup_grp.add(PowerUp(random.choice(LANES), -60,
                                    random.choice(['nitro','shield','repair'])))

    def draw_hud():
        def lbl(t, y, c=WHITE):
            screen.blit(font.render(t, True, c), (14, y))

        lbl(f'Speed:  {speed}',           14)
        lbl(f'Score:  {score}',           14 + sy(30))
        lbl(f'Coins:  {coins_collected}', 14 + sy(60), GOLD_C)
        lbl(f'Dist:   {int(distance)}m / {int(FINISH)}m', 14 + sy(90), (180,180,255))

        # Қашықтық жолағы
        bar_y = 14 + sy(120)
        bar_w = sx(160)
        pct   = min(distance / FINISH, 1.0)
        pygame.draw.rect(screen, (40,40,60), (14, bar_y, bar_w, sy(12)), border_radius=4)
        pygame.draw.rect(screen, ACCENT,     (14, bar_y, int(bar_w*pct), sy(12)), border_radius=4)

        # HP жүректері
        player.draw_hp(screen, 14, bar_y + sy(32))

        # Power-up таймерлері
        pu_y = bar_y + sy(55)
        if player.nitro_active:
            lbl(f'NITRO  {player.nitro_timer//FPS}s', pu_y, (0,220,255))
            pu_y += sy(24)
        if player.shield_active:
            lbl(f'SHIELD {player.shield_timer//FPS}s', pu_y, (120,120,255))

        # Жол қауіп индикаторлары
        for i, lane in enumerate(LANES):
            pygame.draw.circle(screen, ACCENT2 if lane_danger[lane] else (40,80,40),
                               (lane, sy(14)), 6)

        # Ойыншы аты
        nm = font.render(player_name, True, ACCENT)
        screen.blit(nm, nm.get_rect(topright=(W-14, 14)))

    # ════════════════════════════════════════════════════════════
    # ОЙЫН ЦИКЛІ
    # ════════════════════════════════════════════════════════════
    while running:
        clock.tick(FPS)
        frame += 1

        for ev in pygame.event.get():
            if ev.type == QUIT: running = False
            if ev.type == KEYDOWN and not gameover:
                if ev.key == K_LEFT and player.rect.centerx > LEFT_LINE:
                    player.rect.centerx = LANES[LANES.index(player.rect.centerx) - 1] if player.rect.centerx in LANES else LEFT_LINE
                if ev.key == K_RIGHT and player.rect.centerx < RIGHT_LINE:
                    idx = LANES.index(player.rect.centerx) if player.rect.centerx in LANES else 1
                    if idx < len(LANES)-1:
                        player.rect.centerx = LANES[idx + 1]

        # Пернелер арқылы жылжыту (негізгі)
        keys = pygame.key.get_pressed()
        if not gameover:
            if keys[K_LEFT]  and player.rect.centerx > LEFT_LINE:
                player.rect.x -= sx(5)
                player.rect.centerx = max(player.rect.centerx, LEFT_LINE)
            if keys[K_RIGHT] and player.rect.centerx < RIGHT_LINE:
                player.rect.x += sx(5)
                player.rect.centerx = min(player.rect.centerx, RIGHT_LINE)

        if gameover: break

        # Қиындық өсуі
        mile = int(distance) // 500
        if mile > last_mile:
            speed     = min(speed+1, params['base_speed']+8)
            max_v     = min(max_v+1, params['max_vehicles']+4)
            hz_frq    = max(hz_frq-15, 60)
            last_mile = mile

        eff = speed + player.nitro_bonus
        if slow_timer > 0:
            eff = max(1, eff-2)
            slow_timer -= 1

        # Фон
        screen.fill(GREEN_GRASS)
        pygame.draw.rect(screen, DARK_ROAD, (ROAD_X, 0, ROAD_W, H))
        pygame.draw.rect(screen, YELLOW, (ROAD_X - sx(10), 0, sx(10), H))
        pygame.draw.rect(screen, YELLOW, (ROAD_X + ROAD_W, 0, sx(10), H))

        y_move = (y_move + eff*2) % (MARKER_H*2)
        for y in range(-MARKER_H*2, H, MARKER_H*2):
            pygame.draw.rect(screen, WHITE, (LEFT_LINE + sx(90),   y+y_move, MARKER_W, MARKER_H))
            pygame.draw.rect(screen, WHITE, (CENTER_LINE + sx(90), y+y_move, MARKER_W, MARKER_H))

        player.update_powerups(1)

        # Зақым алғанда жыпылықтау
        if player.invincible > 0 and (frame % 10 < 5):
            pass
        else:
            player_grp.draw(screen)
        player.draw_shield(screen)

        # Спавн
        if len(enemy_grp) < max_v and frame%60==0: spawn_enemy()
        if frame%hz_frq==0:     spawn_hazard()
        if frame%90==0:         hazard_grp.add(Pothole(random.choice(LANES), -50))
        if frame%(hz_frq*2)==0: spawn_event()
        if frame%180==0:        spawn_powerup()
        if frame%80==0 and len(coin_grp)<4:
            coin_grp.add(CoinSprite(random.choice(LANES), -60))
        if frame%300==0:
            lane_danger = {L: False for L in LANES}

        # Барлық спрайттарды жылжыту
        for grp in (enemy_grp, coin_grp, hazard_grp, event_grp, powerup_grp):
            for sp in grp:
                sp.rect.y += eff
                if sp.rect.top > H:
                    if isinstance(sp, EnemyVehicle): score += 1
                    sp.kill()

        for pu in list(powerup_grp): pu.update_timer()

        hazard_grp.draw(screen)
        event_grp.draw(screen)
        enemy_grp.draw(screen)
        coin_grp.draw(screen)
        powerup_grp.draw(screen)

        # Монета жинау
        for coin in pygame.sprite.spritecollide(player, coin_grp, True):
            coins_collected += coin.weight
            score += coin.weight * 2

        # Power-up жинау
        for pu in pygame.sprite.spritecollide(player, powerup_grp, True):
            if pu.kind == 'nitro':
                player.nitro_active = True
                player.nitro_timer  = FPS * 4
                player.nitro_bonus  = 3
            elif pu.kind == 'shield':
                player.shield_active = True
                player.shield_timer  = FPS * 30
            elif pu.kind == 'repair':
                player.hp = min(player.hp + 1, MAX_HP)
                pygame.sprite.spritecollide(player, hazard_grp, True)
                score += 5

        # Жол оқиғалары
        for ev_sp in pygame.sprite.spritecollide(player, event_grp, True):
            if isinstance(ev_sp, SpeedBump):
                slow_timer = FPS * 2
            elif isinstance(ev_sp, NitroStrip):
                player.nitro_active = True
                player.nitro_timer  = FPS * 3
                player.nitro_bonus  = 4

        # Кедергілер
        for haz in pygame.sprite.spritecollide(player, hazard_grp, False):
            if isinstance(haz, Barrier):
                dead = player.take_damage()
                haz.kill()
                if dead:
                    gameover = True
                    if crash_sound and sound_on: crash_sound.play()
                    if bg_music    and sound_on: bg_music.stop()
            else:
                slow_timer = FPS * 2
                haz.kill()

        # Жау көлігімен соқтығысу
        if pygame.sprite.spritecollide(player, enemy_grp, True):
            dead = player.take_damage()
            if dead:
                gameover = True
                if crash_sound and sound_on: crash_sound.play()
                if bg_music    and sound_on: bg_music.stop()

        # Авария суреті
        if gameover and _CRASH_IMG:
            screen.blit(_CRASH_IMG, (player.rect.x-10, player.rect.y-50))

        if not gameover:
            distance += eff * 0.05

        draw_hud()

        if distance >= FINISH:
            score += 500
            running = False

        pygame.display.flip()

    if bg_music:
        try: bg_music.stop()
        except: pass

    return score + int(distance//10), distance, coins_collected