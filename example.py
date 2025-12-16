grid = (
    ("Alice", "Bob", "Carol"),
    ("Dave", "Eve", "Frank"),
    ("Grace", "Heidi", "Ivan"),
)

from cluesbysam_solver import ClueSolver

cs = ClueSolver(grid)

from cluesbysam_solver import INNOCENT, CRIMINAL

p = cs.people
cs.add(p["Frank"] == INNOCENT)

# <Frank> Carol is one of my 3 criminal neighbors
cs.add(p["Carol"] == CRIMINAL)
cs.add(cs.num_criminals(cs.neighbors("Frank")) == 3)

# <Carol> Alice only shares innocent neighbors with Grace
shared_neighbors = cs.neighbors("Alice") & cs.neighbors("Grace")
cs.add(cs.num_innocents(shared_neighbors) == len(shared_neighbors))

# <Dave> The criminals in row 1 are connected
cs.add(cs.connected(CRIMINAL, cs.row(1)))

# <Eve> There are exactly 2 innocents in column C
cs.add(cs.num_innocents(cs.column("C")) == 2)

# <Heidi> Only one row has exactly 2 innocents
from cluesbysam_solver import AtMost, AtLeast

cs.add(AtMost(*(cs.num_innocents(cs.row(i)) == 2 for i in range(1, 4)), 1))
cs.add(AtLeast(*(cs.num_innocents(cs.row(i)) == 2 for i in range(1, 4)), 1))

# <Ivan> The number of criminals in the corners is even
from cluesbysam_solver import Even

cs.add(Even(cs.num_criminals(cs.corners())))
