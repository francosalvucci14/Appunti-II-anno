# Interval Partitioning

**Interval partitioning**.
- Lecture j starts at $s_j$ and finishes at $f_j$.
- **Goal**: find _**minimum**_ number of _classrooms_ to schedule _**all**_ lectures
- so that no two occur at the same time in the same room.

Ex: This schedule uses 4 classrooms to schedule 10 lectures.

![[appunti asd/mod ii/immagini/Pasted image 20230329093504.png|center]]

Ex: This schedule uses only 3.

![[appunti asd/mod ii/immagini/Pasted image 20230329094927.png|center]]

## Lower Bound on Optimal Solution

>[!definition]- Depth
>The **depth** of a set of open intervals is the maximum number that contain
>any given time.

**Key observation**. Number of classrooms **needed** $\geq$ _depth_
**Ex**: depth of schedule below $=3\implies$ schedule below is **optimal**

a, b, c all contain 9:30 (depth of 9.30 = 3)

**Q**. Does there always exist a schedule equal to depth of intervals?

![[appunti asd/mod ii/immagini/Pasted image 20230329095349.png|center]]


