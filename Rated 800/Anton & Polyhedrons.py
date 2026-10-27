polyhedrons_sides = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20,
}
polyhedrons_no = int(input())
polyhedrons = list(input() for _ in range(polyhedrons_no))
total = 0
for i in range(polyhedrons_no):
    total += polyhedrons_sides[polyhedrons[i]]

print(total)