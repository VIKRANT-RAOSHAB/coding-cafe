import numpy as np

# ---------------------------------------------------
# NODE COORDINATES (2D)
# ---------------------------------------------------

nodes = {
    "A": (0, 0),      # Bottom left support (pin)
    "B": (1, 0),      # Bottom middle
    "C": (2, 0),      # Bottom right support (roller - only Cy)
    "D": (0.5, 1),    # Middle left
    "E": (1, 2),      # Top (load point)
    "F": (1.5, 1)     # Middle right
}

# ---------------------------------------------------
# MEMBERS (9 bars)
# ---------------------------------------------------

members = [
    ("A", "B"),  # 1
    ("B", "C"),  # 2
    ("A", "D"),  # 3
    ("B", "E"),  # 4
    ("C", "F"),  # 5
    ("D", "E"),  # 6
    ("E", "F"),  # 7
    ("A", "E"),  # 8
    ("C", "E")   # 9
]

member_names = ["AB", "BC", "AD", "BE", "CF", "DE", "EF", "AE", "CE"]

# A = pin (2 reactions), C = roller (1 reaction)
reaction_names = ["Ax", "Ay", "Cy"]

unknowns = member_names + reaction_names
n_unknowns = len(unknowns)

print(f"Equations: 12, Unknowns: {n_unknowns}")

# ---------------------------------------------------
# EXTERNAL LOADS
# ---------------------------------------------------

loads = {
    "A": (0, 0),
    "B": (0, 0),
    "C": (0, 0),
    "D": (0, 0),
    "E": (0, -1),     # 1 kN downward
    "F": (0, 0)
}

# ---------------------------------------------------
# EQUILIBRIUM MATRIX
# ---------------------------------------------------

A = np.zeros((12, 12))
b = np.zeros(12)

joint_list = list(nodes.keys())

for j, joint in enumerate(joint_list):
    
    row_x = 2 * j
    row_y = 2 * j + 1
    
    # External load
    b[row_x] = -loads[joint][0]
    b[row_y] = -loads[joint][1]
    
    # ------------------------------------------------
    # MEMBER CONTRIBUTIONS
    # ------------------------------------------------
    
    for i, (n1, n2) in enumerate(members):
        
        if joint == n1:
            other = n2
        elif joint == n2:
            other = n1
        else:
            continue
        
        x1, y1 = nodes[joint]
        x2, y2 = nodes[other]
        
        dx = x2 - x1
        dy = y2 - y1
        
        length = np.sqrt(dx**2 + dy**2)
        
        cos_theta = dx / length
        sin_theta = dy / length
        
        A[row_x, i] += cos_theta
        A[row_y, i] += sin_theta
    
    # ------------------------------------------------
    # SUPPORT REACTIONS
    # ------------------------------------------------
    
    if joint == "A":
        # Pin support at A
        A[row_x, unknowns.index("Ax")] = 1
        A[row_y, unknowns.index("Ay")] = 1
    
    if joint == "C":
        # Roller support at C (vertical reaction only)
        A[row_y, unknowns.index("Cy")] = 1

# ---------------------------------------------------
# SOLVE MATRIX EQUATION
# ---------------------------------------------------

solution = np.linalg.solve(A, b)

# ---------------------------------------------------
# PRINT RESULTS
# ---------------------------------------------------

print("\n2D TRUSS MEMBER FORCES")
print("-" * 55)
print(f"{'Member':<8} {'Force (kN)':<15} {'Nature':<20}")
print("-" * 55)

for name, value in zip(unknowns, solution):
    
    if name in member_names:
        
        if value > 1e-6:
            nature = "Tension"
        elif value < -1e-6:
            nature = "Compression"
        else:
            nature = "Zero-force"
        
        print(f"{name:<8} {abs(value):>10.3f}    {nature}")
    
    else:
        print(f"{name:<8} {value:>10.3f}    (Reaction)")

print("-" * 55)

