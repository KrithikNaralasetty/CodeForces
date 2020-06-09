#785A in codeforces
polyhedrons = {
	"Tetrahedron":4,
	"Cube":6,
	"Octahedron":8,
	"Dodecahedron":12,
	"Icosahedron":20
}
n = int(input())
faces=0
for _ in range(n):
	faces+=polyhedrons[input()]
print(faces)