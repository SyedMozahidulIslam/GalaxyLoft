# GalaxyLoft

A medium-large Python/Pygame arcade game — space exploration, bullet-hell combat,
resource trading, asteroid mining, and ship upgrades across a procedural galaxy.

## Quick Start

```bash
pip install pygame-ce
python main.py
```

Requires Python 3.11+ and pygame-ce 2.5+.

---

## Controls

| Key | Action |
|-----|--------|
| W / ↑ | Thrust forward |
| A / ← | Rotate left |
| D / → | Rotate right |
| S / ↓ | Brake |
| SPACE | Fire weapon |
| E (near planet) | Land |
| Hold E (near asteroid) | Mine ore |
| M | Galaxy Map |
| ESC | Pause / back |
| Q / E (on planet) | Switch tabs |

---

## Gameplay Loop

1. **Fly** through a sector using physics-based thrust + inertia
2. **Fight** pirate waves — 4 enemy types + sector boss
3. **Mine** asteroids for resources (Iron, Crystal, Fuel Cells…)
4. **Land** on planets to trade, buy upgrades, and accept missions
5. **Warp** to new sectors on the galaxy map — discover 12 procedural sectors
6. **Upgrade** your ship with 12 modules across 5 stats

---

## Project Structure

```
galaxyloft/
├── main.py                        ← Entry point
├── src/
│   ├── constants.py               ← All tunable values (colors, physics, economy)
│   ├── entities/
│   │   ├── player.py              ← Ship physics, weapons, cargo, upgrades
│   │   ├── enemies.py             ← PirateScout, Gunner, EliteRaider, SectorBoss
│   │   └── objects.py             ← Planets, Asteroids, Pickups
│   ├── scenes/
│   │   ├── sector.py              ← Main flight/combat scene
│   │   ├── galaxy_map.py          ← Procedural star map + warp travel
│   │   ├── planet.py              ← Trade / Upgrade / Missions / Info tabs
│   │   └── menus.py               ← Main menu (save slots) + Game Over
│   ├── systems/
│   │   ├── game_manager.py        ← Main loop + scene router + save/load
│   │   ├── camera.py              ← Smooth follow camera
│   │   ├── starfield.py           ← 3-layer parallax starfield
│   │   ├── particles.py           ← Explosion, thrust, shield, mining FX
│   │   ├── screen_shake.py        ← Trauma-based screen shake
│   │   ├── sound.py               ← Procedural synth audio (no files needed)
│   │   ├── missions.py            ← Procedural mission board (6 mission types)
│   │   └── save_system.py         ← JSON save/load, 3 slots + auto-save
│   └── ui/
│       └── hud.py                 ← HUD overlay, minimap, bars, flash messages
└── saves/                         ← Auto-created on first save
```

---

## Features by Phase

| Phase | Features |
|-------|---------|
| 1 | Physics engine, camera, parallax starfield, particle system |
| 2 | 4 enemy types with AI, 3-phase boss, wave spawner, collision |
| 3 | Procedural 12-sector galaxy map, warp travel, faction territory |
| 4 | 6-resource economy, dynamic pricing, cargo, asteroid mining |
| 5 | 12-module upgrade tree with requirements, mission board foundation |
| 6 | Procedural audio, 6 mission types, screen shake, save slots UI |

**Total: ~3,900 lines across 16 Python files**

---

## Tech Stack

- **Python 3.11+**
- **pygame-ce 2.5** (Community Edition — faster than vanilla pygame)
- No external game frameworks
- Procedural audio synthesis (no audio files)
- Seeded procedural generation (`random.Random(seed)`)
- OOP architecture — all entities extend `pygame.Sprite`
- JSON save system with 3 slots + auto-save
- Trauma-based screen shake, parallax camera, ADSR synth

---

## What You'll Learn

Each system teaches a specific CS concept:

| File | Concept |
|------|---------|
| `player.py` | OOP, physics vectors, ADSR |
| `enemies.py` | Inheritance, state machines, AI behaviors |
| `particles.py` | Data-oriented design, list management |
| `camera.py` | Coordinate transforms, lerp smoothing |
| `starfield.py` | Parallax rendering, modular wrapping |
| `sound.py` | Signal processing, synthesiser math |
| `missions.py` | Observer pattern, serialisation |
| `save_system.py` | JSON I/O, data versioning |
| `game_manager.py` | Scene graph, dependency injection |
