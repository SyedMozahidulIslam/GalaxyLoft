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


# Player Manual

> *"Space is not empty. It is full of pirates, minerals, and opportunity."*

---

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [The Core Loop](#2-the-core-loop)
3. [Controls Reference](#3-controls-reference)
4. [Flying Your Ship](#4-flying-your-ship)
5. [Combat](#5-combat)
6. [The Galaxy Map](#6-the-galaxy-map)
7. [Planets — Trade, Upgrade, Missions](#7-planets--trade-upgrade-missions)
8. [Mining Asteroids](#8-mining-asteroids)
9. [Resources & Economy](#9-resources--economy)
10. [Ship Upgrades](#10-ship-upgrades)
11. [Missions](#11-missions)
12. [Enemies](#12-enemies)
13. [Scoring](#13-scoring)
14. [Save System](#14-save-system)
15. [HUD Guide](#15-hud-guide)
16. [Tips & Strategy](#16-tips--strategy)
17. [Full Stats Reference](#17-full-stats-reference)

---

## 1. Getting Started

### First Launch
When you open the game you land on the **Main Menu**. You have two options:

- **NEW GAME** — Start a fresh run with 1,500 credits in Sector A-1
- **LOAD GAME** — Open the save slot screen to continue a previous run

Click **NEW GAME** and you will be dropped directly into your first sector. A controls reminder fades in for the first 5 seconds — read it before the pirates arrive.

---

## 2. The Core Loop

GalaxyLoft has one repeating loop. Every session looks like this:

```
Sector Flight
    │
    ├─► Fight waves of pirates
    ├─► Mine nearby asteroids
    ├─► Approach a planet  ──► Land
    │                              │
    │                              ├─► Trade resources
    │                              ├─► Buy upgrades
    │                              ├─► Accept / claim missions
    │                              └─► Repair ship (free)
    │
    └─► Open Galaxy Map ──► Warp to next sector ──► repeat
```

You never have to do all of these. A pure combat run works. A pure trader run works. Mixing them all together is where the game gets interesting.

---

## 3. Controls Reference

| Action | Keys |
|--------|------|
| Thrust forward | `W` or `↑` |
| Rotate left | `A` or `←` |
| Rotate right | `D` or `→` |
| Brake / slow down | `S` or `↓` |
| Fire weapon | `SPACE` |
| Land on planet | `E` (when close to a planet) |
| Mine asteroid | Hold `E` (when close to an asteroid) |
| Open Galaxy Map | `M` |
| Pause game | `ESC` |
| Switch planet tabs | `Q` / `E` or `←` / `→` |
| Scroll Galaxy Map | `W A S D` or arrow keys |

> **Tip:** You can hold multiple keys at once — rotate and thrust simultaneously to strafe in any direction.

---

## 4. Flying Your Ship

Your ship uses **Newtonian physics** — not arcade steering. Understanding this is the difference between dying on wave 1 and clearing a boss sector.

### Thrust and Inertia
- Pressing `W` fires your engine and accelerates in the direction your nose is pointing.
- Releasing `W` does **not** stop you. You keep moving (space has no air resistance).
- Your ship has a **friction value of 0.985** — very slight drag that slowly bleeds off speed.
- Top speed is **7.0 pixels/frame** (upgradeable to 12.5 with both engine upgrades).

### Rotating
- `A` and `D` rotate the ship's nose left and right at **3.5 degrees per frame**.
- The ship rotates around its own centre — you are not turning a car.

### Braking
- Holding `S` applies a **strong brake multiplier (0.92)** that rapidly kills your velocity.
- This is your most important survival tool — use it to stop quickly when enemies surround you.

### The World Wraps
The sector is **3,200 × 3,200 pixels**. If you fly off the right edge you reappear on the left. Same for top and bottom. You can never get stuck at a wall.

### Thrust Particles
When your engine fires you will see a blue exhaust trail behind you. This is a visual cue — if you see no particles behind you, you are not thrusting.

### Shield Bubble
When your shield is above 30% of maximum, a faint blue circle appears around your ship. When it disappears, your hull is exposed. Take cover.

---

## 5. Combat

### Firing
Press `SPACE` to fire. The cooldown between shots is **18 frames** (0.3 seconds) by default. Each bullet travels at **14 pixels/frame** and disappears after **55 frames**.

Bullets are fired from your ship's nose. You must be facing your target to hit it.

### Damage Model
Your ship has two protective layers:

| Layer | Default | What it does |
|-------|---------|-------------|
| **Shield** | 80 SP | Absorbs incoming damage first. Regenerates automatically after 3 seconds of not being hit |
| **Hull** | 100 HP | The real health bar. If this reaches zero, your ship is destroyed |

Shield regenerates at **0.08 SP per frame** (about 4.8 SP per second). Hull does **not** regenerate in space — land on a planet for free repairs.

### Invincibility Frames
After taking a hit you are **invincible for 1 second**. Your ship blinks to show this. Use this window to reposition — do not waste it flying into more bullets.

### Hit Indicators
- **Blue sparks** — Shield absorbed the hit
- **Red sparks** — Hull took damage (bad)
- **Screen shakes** — Something exploded near you

### Winning a Sector
Each sector has **3 + difficulty** waves. After the last wave, if the sector has a boss, the boss spawns. Defeat the boss to mark the sector **CLEARED** (shown as a green ring on the Galaxy Map).

You do not have to clear sectors to progress — you can warp away any time by pressing `M`. Cleared sectors give better pickup drops and are safer for trading.

---

## 6. The Galaxy Map

Press `M` at any time (in-sector or paused) to open the Galaxy Map.

### Reading the Map
Each circle is a **sector node**. The galaxy has **12 sectors** total.

| Visual element | Meaning |
|---------------|---------|
| Gold ring | Your current sector |
| Cyan ring | Hovered sector |
| Green ring | Cleared sector (boss defeated) |
| `?` grey dot | Undiscovered sector |
| Coloured dots below node | Difficulty (green=easy → red=brutal) |
| `*BOSS*` label | This sector has a sector boss |
| Lines between nodes | Travel connections |

### Difficulty Stars
Every sector has a difficulty from 1 to 5, shown as coloured dots:

| Dot colour | Difficulty | What to expect |
|-----------|-----------|---------------|
| 🟢 Green | 1 | Scouts only, small waves |
| 🔵 Cyan | 2 | Scouts + first Gunners |
| 🟡 Gold | 3 | All basic types, more enemies per wave |
| 🟠 Orange | 4 | Elite Raiders appear, waves are large |
| 🔴 Red | 5 | Mostly Elites, brutal wave count |

### Travelling
- **Click a discovered sector** to warp to it.
- Adjacent sectors to any sector you have visited become **discovered** (revealed on the map).
- Warping triggers an **auto-save** — you never lose progress between sectors.

### Scrolling
Use `WASD` or arrow keys to scroll the map. The galaxy is **2,400 × 1,600** — larger than the screen. Pan around to see undiscovered sectors at the edges.

### Faction Territory
Each sector belongs to a faction. The faint coloured glow behind sector nodes shows whose space you are in. Hover over a node to see the tooltip with faction name.

---

## 7. Planets — Trade, Upgrade, Missions

When you are close enough to a planet, a prompt appears at the bottom of the screen:

```
[E] Land on Veridian
```

Press `E` to land. Each sector has **2 to 5 planets** with unique names, factions, and prices.

Landing gives you a **free 25% shield top-up** automatically.

The planet screen has **four tabs**. Navigate with `Q` / `E` or `←` / `→`.

---

### Tab 1 — Trade

The market table shows all 6 resources with two prices per planet:

| Column | Meaning |
|--------|---------|
| **BASE** | The universe baseline price |
| **BUY@** | What you pay the planet (planet sells to you) |
| **SELL@** | What the planet pays you (you sell to planet) |
| **HELD** | How many you currently carry |

Prices vary **±20 to ±40%** from the base depending on the planet. A planet with a high BUY@ price is bad to buy from. A planet with a high SELL@ price is great to sell at.

**Profit strategy:** Buy low at one planet, warp to another, sell high. The bigger the spread between what you paid and what the new planet offers, the more profit.

> **Example:** Buy Iron at 32 cr (below base of 40), sell at another planet for 54 cr. Profit: 22 cr per unit.

Each planet also has a **stock count**. If stock is 0, you cannot buy that resource there.

---

### Tab 2 — Upgrades

All 12 ship upgrades are bought here. Some require a prerequisite upgrade first.

> See **Section 10 — Ship Upgrades** for the full upgrade tree.

The buy button shows `INSTALL` when you can afford it and meet requirements, and dims when you cannot. Already-installed upgrades show a `✓` prefix.

---

### Tab 3 — Missions

The mission board shows up to **4 active missions**. Each mission has:

- A **title** and **description** showing what to do
- A **progress bar** tracking how far you are
- A **reward** in credits (shown top-right of the mission card)

When a mission is complete the progress bar turns green and a **CLAIM REWARD** button appears. Click it to collect your credits and bonus score.

Missions **refresh** every time you land on a planet. In-progress missions carry over; completed unclaimed ones stay until you claim them.

> See **Section 11 — Missions** for all 6 mission types.

---

### Tab 4 — Info

Shows a summary of:
- Planet name, faction, and physical data
- Your current ship stats (hull, shield, speed, fire rate, cargo)
- Your credits and score
- A **REPAIR SHIP (FREE)** button — fully restores hull and shield at no cost

**Always visit Info before leaving a difficult sector** — the free repair can save your run.

---

## 8. Mining Asteroids

Asteroids drift slowly through every sector. Each one contains a specific resource type and between **3 and 12 units** of ore.

### How to Mine
1. Fly close to an asteroid — a label appears showing the resource type and ore count
2. When you see the prompt `[Hold E] Mine Crystal (8 ore)`, hold `E`
3. You extract **1 unit every 20 frames (0.33 seconds)**
4. Mining sparks in the resource's colour spray from the asteroid
5. When ore runs out, the asteroid **explodes** and disappears

### Mining Limits
- You can only mine if your **cargo bay has free space**
- If cargo is full, mining does nothing — sell or use resources first
- Mined ore goes directly into your cargo

### Which Resources to Mine
Not all resources are equal. Mine by value per slot:

| Resource | Base Price | Worth mining? |
|----------|-----------|--------------|
| Iron | 40 cr | Only if cargo is empty |
| Fuel Cell | 80 cr | Decent early game |
| Bio-Matter | 95 cr | Good general filler |
| Crystal | 120 cr | Yes — high value, common |
| Nano-Chips | 160 cr | High priority |
| Dark Ore | 200 cr | Mine every unit you find |

---

## 9. Resources & Economy

### The 6 Resources

| Resource | Base Price | Colour | Notes |
|----------|-----------|--------|-------|
| **Iron** | 40 cr | Grey-brown | Most common in asteroids, lowest value |
| **Crystal** | 120 cr | Light blue | Common asteroid drop, good mid-value |
| **Fuel Cell** | 80 cr | Yellow-orange | Frequent pirate drop |
| **Bio-Matter** | 95 cr | Green | Good all-rounder |
| **Dark Ore** | 200 cr | Purple | Rarest, highest value — always sell high |
| **Nano-Chips** | 160 cr | Cyan | High value, look for sell@ above 190 |

### Cargo System
- Default cargo capacity: **50 units** (total across all resources)
- Each unit of any resource takes 1 cargo slot
- Cargo Bay I adds 20 slots, Cargo Bay II adds another 30 (total 100 slots)
- The cargo bar in the top-right of the HUD turns orange near full, red at 95%

### Price Variation
Prices vary **±20% to ±40%** from base at each planet. Planets with a dominant faction may favour resources that faction produces. Always check the BUY@ vs base before filling your hold — you want to buy below base and sell above.

### Enemy Drops
Killing enemies has a **50% chance** of dropping credits (20–80 cr) and a **25% chance** of dropping 1 unit of a random resource. These appear as floating orbs — fly through them to collect automatically.

---

## 10. Ship Upgrades

Upgrades are permanent and carry across sectors. Buy them at any planet's **Upgrades tab**. Some require a prerequisite.

### Full Upgrade Tree

```
Engine Boost I (800 cr)
    └── Engine Boost II (2,000 cr)

Heavy Shields I (600 cr)
    ├── Heavy Shields II (1,800 cr)
    └── Shield Regen I (900 cr)

Rapid Fire I (700 cr)
    ├── Rapid Fire II (1,900 cr)
    └── Twin Cannons (2,500 cr)

Cargo Bay I (500 cr)
    └── Cargo Bay II (1,200 cr)

Hull Armor I (650 cr)
    └── Hull Armor II (1,600 cr)
```

### What Each Upgrade Does

| Upgrade | Cost | Effect |
|---------|------|--------|
| **Engine Boost I** | 800 cr | +1.5 to max speed (7.0 → 8.5) |
| **Engine Boost II** | 2,000 cr | +2.5 more (8.5 → 11.0) |
| **Heavy Shields I** | 600 cr | +30 max shield (80 → 110 SP) |
| **Heavy Shields II** | 1,800 cr | +60 more (110 → 170 SP) |
| **Rapid Fire I** | 700 cr | −5 frames fire cooldown (18 → 13) |
| **Rapid Fire II** | 1,900 cr | −8 more (13 → 5 frames) |
| **Cargo Bay I** | 500 cr | +20 cargo slots (50 → 70) |
| **Cargo Bay II** | 1,200 cr | +30 more (70 → 100 slots) |
| **Hull Armor I** | 650 cr | +50 max hull (100 → 150 HP) |
| **Hull Armor II** | 1,600 cr | +80 more (150 → 230 HP) |
| **Twin Cannons** | 2,500 cr | Fires 3 bullets per shot (spread) |
| **Shield Regen I** | 900 cr | +0.04 regen/frame (0.08 → 0.12) |

### Recommended Build Orders

**Combat focus (early aggression):**
Rapid Fire I → Heavy Shields I → Hull Armor I → Rapid Fire II → Twin Cannons

**Trader focus (maximise income):**
Cargo Bay I → Cargo Bay II → Engine Boost I → Hull Armor I → Heavy Shields I

**Survivalist (tank everything):**
Heavy Shields I → Hull Armor I → Heavy Shields II → Shield Regen I → Hull Armor II

**All-rounder:**
Cargo Bay I → Rapid Fire I → Heavy Shields I → Engine Boost I → Hull Armor I → Twin Cannons

---

## 11. Missions

The mission board refreshes every time you land on a planet. You can hold up to **4 active missions** at once. Completed missions from a previous refresh stay until you claim them.

### The 6 Mission Types

| Type | Title format | What to do | Base reward |
|------|-------------|------------|------------|
| **Bounty** | Bounty: [Faction] Raiders | Destroy X enemy ships of any type | 400 cr |
| **Elite Takedown** | Elite Takedown | Destroy X Elite Raiders specifically | 700 cr |
| **Supply Run** | Supply Run: [Resource] | Sell X units of a specific resource at any market | 300 cr |
| **Mining Contract** | Mining Contract: [Resource] | Extract X units of a specific resource by mining | 250 cr |
| **Survey Mission** | Survey Mission | Discover X new sectors on the Galaxy Map | 500 cr |
| **Gauntlet** | Gauntlet: [Faction] Onslaught | Survive X enemy waves without leaving the sector | 600 cr |

### How Progress Works
Mission counters are **cumulative and global** — they track everything you do across all sectors, not just the current one. If a Bounty mission asks for 8 kills and you have already killed 3 enemies this session, it starts at 3/8.

This means:
- Kill missions fill up naturally as you play
- Trade missions fill up as you sell resources (not buy)
- Mining missions fill as you extract ore from asteroids
- Survey missions fill when you warp to undiscovered sectors
- Gauntlet missions count each full wave you survive in a single sector stay

### Claiming Rewards
- Go to any planet's **Missions tab**
- Completed missions show a green bar and a **CLAIM REWARD** button
- Click it to receive credits and bonus score points
- Claimed missions are archived (shown at the bottom of the tab)

### Reward Scaling
Rewards scale with the sector **difficulty** you are in when the mission was generated. A Bounty mission generated in a difficulty-5 sector pays significantly more than one from difficulty-1. Warp to harder sectors before landing to get higher-paying mission boards.

---

## 12. Enemies

### Pirate Scout
- **HP:** 30 — goes down in 2–3 direct hits
- **Speed:** 2.8 (fast)
- **Behaviour:** Dives straight at you. Always moving toward you.
- **Attack:** Fires single shots when within range 380
- **Score:** 150 points
- **Weakness:** Brake hard and shoot as it approaches — it flies into your bullets

### Pirate Gunner
- **HP:** 55 — moderate
- **Speed:** 1.5 (slow)
- **Behaviour:** Tries to maintain distance of ~320 pixels. Strafes if you get too close.
- **Attack:** Fires **burst of 3 shots** every ~80 frames
- **Score:** 250 points
- **Weakness:** Charge it aggressively — inside its ideal range it can't strafe fast enough

### Elite Raider
- **HP:** 90 — takes sustained fire
- **Speed:** 2.4
- **Behaviour:** Chases at long range, switches to strafing circles up close
- **Attack:** Fast single shots every ~55 frames
- **Score:** 300 points
- **Weakness:** Most dangerous enemy. Keep moving — never fly in a straight line near one

### Sector Boss *(appears in every 4th sector)*
- **HP:** 600
- **Speed:** 1.0 but orbits you constantly
- **Score:** 1,000 points
- **Three attack phases:**

| Phase | HP threshold | Attack pattern |
|-------|-------------|---------------|
| **Phase 1** | 100% → 50% | 5-way spread shot while orbiting |
| **Phase 2** | 50% → 25% | 8-way ring shot + aimed centre shot |
| **Phase 3** | Below 25% | Full 12-bullet rotating spiral — frantic |

- **Strategy:** Orbit the boss from just outside its orbit radius. In Phase 1 the 5-way spread has gaps — fly through them. In Phase 3 the spiral rotates, so keep circling in the same direction as the pattern to chase the gaps rather than running into them.

### Wave Composition by Difficulty

| Difficulty | Wave pool |
|-----------|----------|
| 1 | Scouts only |
| 2 | Scouts + occasional Gunner |
| 3 | Scouts, Gunners, first Elites |
| 4 | Gunners and Elites dominate |
| 5 | Mostly Elites + Gunners, large waves |

---

## 13. Scoring

Your score is shown at the top-left of the HUD and on the game-over screen.

| Action | Points |
|--------|--------|
| Kill Pirate Scout | 150 |
| Kill Pirate Gunner | 250 |
| Kill Elite Raider | 300 |
| Kill Sector Boss | 1,000 |
| Trade transaction (buy or sell) | 10 per credit of profit |
| Complete a mission | 2× the credit reward |

Score does not affect gameplay — it is your personal measure of a good run. Try to beat your previous score on the save slot screen.

---

## 14. Save System

### Auto-Save
The game auto-saves every time you:
- Warp between sectors on the Galaxy Map
- Leave a planet and return to the sector

You never lose progress mid-sector — the worst case is replaying the current sector if you quit mid-fight.

### Manual Save Slots
There are **3 save slots**. On the Main Menu, choose **LOAD GAME** to see all three slots with:
- Timestamp of last save
- Score and credits at time of save
- Sector number

To save to a specific slot, start a new game via slot selection from the Load screen. Each new game uses that slot for all future auto-saves.

### What Is Saved
- Player stats (hull, shield, speed, fire rate, cargo)
- Credits, cargo contents, score
- All purchased upgrades
- Active and completed missions with progress
- Galaxy map — discovered and cleared sectors
- Current sector

---

## 15. HUD Guide

```
┌─────────────────────────────────────────────────────────────────────────┐
│ SECTOR: Sector A-1          Wave 2/4  Enemies: 3     [top-left panel]   │
│ Wave 2 incoming!                                                         │
│ SCORE:   1,200                                                           │
│ CREDITS: 2,400 cr                                           [RADAR box] │
│                                                             · · ·        │
│                                                             · ★ ·        │
│                                                                          │
│                         GAME WORLD                         [CARGO panel]│
│                                                             Crystal  x3  │
│                                                             Iron     x1  │
│                                                                          │
│ [Hold E] Mine Crystal  (6 ore)      [bottom centre prompt]              │
│                                                                          │
│  SHIELD ████████████░░ 62/80 SP                [bottom-left bars]       │
│  HULL   ████████████████ 100/100 HP                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

### Top-Left Panel
| Line | What it shows |
|------|--------------|
| SECTOR | Current sector name |
| Wave text | Current wave number, total waves, enemies alive — or "Sector Clear" when done |
| SCORE | Running score this session |
| CREDITS | Current credits |

### RADAR (top-right minimap)
The radar is a scaled-down view of the entire 3,200 × 3,200 sector:
- **Cyan dots** — planets
- **Red dots** — enemies
- **Gold dot** — your ship
- **Coloured pixels** — asteroids (coloured by resource type)

Use it to spot enemies approaching from off-screen and to navigate to planets quickly.

### Cargo Panel (right side)
Only appears when you are carrying something. Shows each resource and quantity, plus a **cargo bar** that turns orange when >75% full and red when >95% full.

### Health Bars (bottom-left)
- **SHIELD bar** (top, cyan) — regenerates automatically after 3 seconds of no hits
- **HULL bar** (bottom, red) — only restored by landing on a planet

### Centre Prompts
Context-sensitive messages at the bottom centre of the screen:
- Near a planet: `[E] Land on PlanetName`
- Near an asteroid: `[Hold E] Mine ResourceName (X ore)`

### Flash Messages (centre of screen)
Temporary text that fades out, showing:
- Wave arrival announcements
- Pickup collected
- Kill score bonus
- Sector clear confirmation
- Mission completion hints

---

## 16. Tips & Strategy

### Early Game (Sectors 1–3, Difficulty 1–2)
- **Mine everything.** Your starting 1,500 credits won't buy much. Asteroids are free income.
- **First upgrade: Cargo Bay I (500 cr).** More cargo = more trading income per trip.
- **Sell high-value resources first.** Don't fill your hold with Iron when there are Crystals nearby.
- **Brake early, brake often.** Getting cornered by Scouts is the #1 beginner death.

### Mid Game (Sectors 4–8, Difficulty 3–4)
- **Get Rapid Fire I before facing Elites.** The default 18-frame cooldown is too slow for Elite duels.
- **Check sell prices at every planet before selling.** A Crystal worth 120 base might sell for 165 at one planet and 88 at another.
- **Use the minimap to avoid getting surrounded.** If 5 red dots are converging from all sides, brake hard and pick one direction to break through.
- **Keep Hull Armor upgraded.** Elites deal fast damage and your invincibility frames only help so much.

### Late Game (Sectors 9–12, Difficulty 5)
- **Twin Cannons is a game-changer.** Three bullets per shot at rapid fire essentially triples your DPS.
- **Boss Phase 3 is the hardest moment in the game.** Before Phase 3 triggers (below 25% boss HP), top up your shield by backing off for 3 seconds.
- **Claim your missions before the final boss.** Mission rewards give you credits for upgrades — don't leave them unclaimed.
- **Stack the survivalist build** if dying repeatedly: Heavy Shields II + Hull Armor II + Shield Regen I gives you 170 SP + 230 HP with fast regen. You become nearly unkillable.

### Economy Tips
- **Best trade route pattern:** Mine a full hold of Crystal and Dark Ore → sell at a planet with high SELL@ → buy a cheaper resource → sell that elsewhere → use profits for upgrades.
- **Faction territory affects prices slightly.** Tech Syndicate planets tend to pay more for Nano-Chips. Traders Guild planets usually have more stock across all resources.
- **Never buy Iron unless you have nothing else to do with credits.** At 40 cr base it rarely profits enough to be worth the cargo space.

### Combat Tips
- **Rotate to face enemies before shooting.** Unlike many games, you cannot shoot sideways.
- **Lead fast enemies.** Scouts move at 2.8 px/frame — aim slightly ahead of their direction, not directly at them.
- **Brake is your dodge.** There is no dodge roll. A sudden full brake when a Gunner fires its burst causes all 3 bullets to overshoot.
- **Kill Gunners before Scouts in mixed waves.** Gunner burst fire is more dangerous than Scout dive-bombing at close range.
- **The Boss orbits at a fixed radius.** If you stay inside its orbit, its bullets spray outward away from you. Move in, not out.

---

## 17. Full Stats Reference

### Ship Base Stats

| Stat | Default | Max (fully upgraded) |
|------|---------|---------------------|
| Hull HP | 100 | 230 |
| Shield SP | 80 | 170 |
| Max speed | 7.0 px/frame | 11.0 px/frame |
| Fire cooldown | 18 frames | ~5 frames |
| Shield regen | 0.08 SP/frame | 0.12 SP/frame |
| Cargo slots | 50 | 100 |
| Projectiles per shot | 1 | 3 (Twin Cannons) |
| Starting credits | 1,500 cr | — |

### World Constants

| Constant | Value |
|----------|-------|
| Sector world size | 3,200 × 3,200 px |
| Galaxy sectors | 12 |
| Planets per sector | 2–5 |
| Asteroids per sector | 24–40 (scales with difficulty) |
| Waves per sector | 3 + difficulty (4 to 8 waves) |
| Boss sectors | Every 4th sector |
| Screen resolution | 1,280 × 720 (resizable) |
| Frame rate | 60 FPS |

### Bullet Stats

| Stat | Player | Enemy (basic) |
|------|--------|--------------|
| Speed | 14 px/frame | 8 px/frame |
| Damage | 15 HP | 10 HP |
| Lifetime | 55 frames | 70 frames |
