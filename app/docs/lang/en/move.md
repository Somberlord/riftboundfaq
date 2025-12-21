### Move

**Moving** is a **Game Object** moving between two **Locations** (**Battlefields** and **Bases**).

  - For now, only **Units** can be moved.
  - Game objects can be moved between **Battlefields**, or between a **Battlefield** and the **Base** of the player controlling the game object.
  - **Units** can’t be moved to a **Battlefield** already containing **Units** from two other players.

Effects allowing a move may specify additional restrictions.

## Standard Move

All units have access to the Standard Move:

  - Can only be done during one’s Turn, out of **Showdown** and with empty **Chain**.
  - Multiple **Units** can use the **Standard Move** at the same time.
  - The cost for each Unit to use the **Standard** Move is to **Exhaust**.
  - **Units** moving together using **Standard Move** must have the same **Destination**.
  - **Units** moving together using **Standard Move** may come from different **Locations**.
  - **Units** can use the **Standard Move** to move from **Base** to **Battlefield**, or from **Battlefield** to **Base**.
  - **Units** with **Ganking** can use the **Standard Move** to move from **Battlefield** to **Battlefield**.
  - Multiple **Units** with **Ganking** can still move at the same time with a **Standard Move**.

All other Move Restrictions still apply.

## Notes

  - Only Standard Move exhausts units. Every other move does not exhaust Units, and can move exhausted Units.
  - Standard Move CANNOT be combined with other move effects. (ex : Yasuo legend ability)

## Relevant CRD Rules

*106.2.d Base<br/>
143. Standard Move<br/>
407. Move<br/>
736. Ganking*

### __Dates :__

Verified : 2025-12-21<br/>
Updated : 2025-12-21