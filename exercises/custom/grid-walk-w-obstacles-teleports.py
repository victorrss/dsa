"""
# Grid Walk with Obstacles and Teleports

You are given:
- `rows`, `cols`: dimensions of a `rows x cols` grid with cells from `(0,0)` to `(rows-1, cols-1)`.
- `obstacles`: a list of blocked cells (you cannot enter them).
- `teleports`: a list of pairs `((r1, c1), (r2, c2))`. If you step on `(r1, c1)`, you must immediately teleport to `(r2, c2)`.

Start at `(0,0)` and walk in **row-major** order:
- From `(r, c)` move to `(r, c+1)`.
- If `c == cols - 1`, move to `(r+1, 0)`.

Return:
- the **number of steps** required to reach `(rows-1, cols-1)`,
- `-1` if you **enter an obstacle** (by walking or by teleport),
- `-2` **only** if there is a **cycle inside a teleport chain** (e.g., A → B → A while resolving teleports).
  Re-visits caused by normal walking do **not** count as cycles.

**Counting rules**
- A normal move to the next row-major cell counts as **+1 step**.
- Each teleport jump counts as **+1 step**.

**Edge cases**
- If `(0,0)` is an obstacle, return `-1`.
- If you land on an obstacle via teleport, return `-1`.
- If you resolve teleports and detect a cycle, return `-2`.

---

## Examples

**Example 1**  
`rows=2, cols=3, obstacles=[], teleports=[]`  
Path: `(0,0)->(0,1)->(0,2)->(1,0)->(1,1)->(1,2)` → **5 steps**  
**Output:** `5`

**Example 2**  
`rows=1, cols=4, obstacles=[(0,2)], teleports=[]`  
Walking from `(0,1)` to `(0,2)` hits an obstacle → **-1**  
**Output:** `-1`

**Example 3**  
`rows=2, cols=3, obstacles=[], teleports=[((0,1),(1,2))]`  
Steps: `(0,0)->(0,1)` (+1), teleport `(0,1)->(1,2)` (+1) = **2**  
**Output:** `2`

**Example 4**  
`rows=1, cols=4, teleports=[((0,1),(0,2)), ((0,2),(0,1))]`  
Teleport loop between `(0,1)` and `(0,2)` → **-2**  
**Output:** `-2`

---

## Constraints (suggested)
- `1 ≤ rows, cols`
- Coordinates in `obstacles` and `teleports` are valid grid cells.
"""

def traverse_grid(rows, cols, obstacles, teleports):
    """
    Regras:
      - Anda em row-major: (r,c+1); se c==cols-1 => (r+1,0)
      - Entrou em obstáculo => -1
      - Ciclo só em cadeia de teleports:
          ao entrar numa célula, se ela já foi source de teleport antes => -2
      - Chegou em (rows-1, cols-1) => retorna passos
      - Mover conta +1 passo; cada teleport conta +1 passo
    """
    if rows <= 0 or cols <= 0:
        return -1

    last = (rows - 1, cols - 1)
    obs = set(obstacles)
    tp = dict(teleports)

    if (0, 0) in obs:
        return -1

    def next_cell(r, c):
        if c + 1 < cols:
            return (r, c + 1)
        if r + 1 >= rows:
            return None
        return (r + 1, 0)

    teleport_sources_seen = set()  # guarda sources já usados em cadeia de teleports

    def bt(r, c, steps):
        # ciclo só na cadeia de teleports: se entrar em um source já visto, -2
        if (r, c) in teleport_sources_seen:
            return -2

        # obstáculo ao entrar
        if (r, c) in obs:
            return -1

        # chegou no fim
        if (r, c) == last:
            return steps

        # se é teleport, teleporta imediatamente e marca o source
        if (r, c) in tp:
            teleport_sources_seen.add((r, c))
            nr, nc = tp[(r, c)]
            return bt(nr, nc, steps + 1)

        # movimento normal: próxima célula em row-major
        nxt = next_cell(r, c)
        if nxt is None:
            # por segurança (normalmente já teria retornado ao chegar no last)
            return steps

        nr, nc = nxt
      
        return bt(nr, nc, steps + 1)

    return bt(0, 0, 0)

assert traverse_grid(2, 3, [], []) == 5
assert traverse_grid(1, 4, [(0,2)], []) == -1
assert traverse_grid(2, 3, [], [((0,1),(1,2))]) == 2
assert traverse_grid(1, 4, [], [((0,1),(0,2)), ((0,2),(0,1))]) == -2
assert traverse_grid(2, 2, [(1,1)], [((0,1),(1,1))]) == -1
