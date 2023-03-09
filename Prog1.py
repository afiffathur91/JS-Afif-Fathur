import matplotlib.pyplot as plt

# Fungsi untuk menentukan arah titik
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # titik berada pada garis
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise

# Fungsi Convex Hull
def convexHull(points):
    # Jumlah titik kurang dari 3 tidak dapat membentuk convex hull
    if len(points) < 3:
        return []

    # Cari titik dengan y terendah
    ymin = points[0][1]
    min_idx = 0
    for i in range(1, len(points)):
        if points[i][1] < ymin or (points[i][1] == ymin and points[i][0] < points[min_idx][0]):
            ymin = points[i][1]
            min_idx = i

    # Membuat list untuk menghitung convex hull
    hull = []
    p = min_idx
    q = 0
    while True:
        # Tambahkan titik ke hull
        hull.append(points[p])

        # Cari titik terdekat berikutnya di sekitar hull
        q = (p + 1) % len(points)
        for i in range(len(points)):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        # Pindah ke titik berikutnya
        p = q

        # Jika telah kembali ke titik awal, selesaikan hull
        if p == min_idx:
            break

    return hull

# Kumpulan titik
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

# Hitung convex hull
hull = convexHull(points)

# Gambar titik-titik
x = [point[0] for point in points]
y = [point[1] for point in points]
plt.plot(x, y, 'o')

# Gambar convex hull
for i in range(len(hull)):
    if i == len(hull) - 1:
        plt.plot([hull[i][0], hull[0][0]], [hull[i][1], hull[0][1]], 'r')
    else:
        plt.plot([hull[i][0], hull[i+1][0]], [hull[i][1], hull[i+1][1]], 'r')

# Tampilkan plot
plt.show()
