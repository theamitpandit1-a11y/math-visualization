import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

FPS = 30
WIDTH = 1080
HEIGHT = 1920
DPI = 100

os.makedirs("output", exist_ok=True)


def setup():
    fig, ax = plt.subplots(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI)
    fig.patch.set_facecolor("#0b1020")
    ax.set_facecolor("#0b1020")
    ax.axis("off")
    return fig, ax


def branding(ax):
    ax.text(
        0.5, 0.975,
        "IIT MATH OFFICIAL",
        transform=ax.transAxes,
        ha="center",
        va="top",
        color="white",
        fontsize=22,
        fontweight="bold"
    )

    ax.text(
        0.5, 0.955,
        "@iit.math_official",
        transform=ax.transAxes,
        ha="center",
        va="top",
        color="white",
        fontsize=14
    )


def render(fig, animation, filename):
    writer = FFMpegWriter(
        fps=FPS,
        codec="libx264",
        bitrate=5000,
        extra_args=["-pix_fmt", "yuv420p"]
    )

    animation.save(
        f"output/{filename}",
        writer=writer,
        dpi=DPI
    )

    plt.close(fig)


# =========================================================
# VIDEO 1 — INFINITE GEOMETRIC SERIES
# =========================================================

fig, ax = setup()
branding(ax)

ax.text(
    0.5, 0.88,
    "INFINITE SUM = 2?!",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=34,
    fontweight="bold"
)

ax.text(
    0.5, 0.82,
    "1 + 1/2 + 1/4 + 1/8 + ...",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=25
)

pieces = []

for i in range(8):
    x = 0.08 + i * 0.11
    piece = ax.add_patch(
        plt.Rectangle(
            (x, 0.48),
            0.095,
            0,
            transform=ax.transAxes
        )
    )
    pieces.append(piece)

result = ax.text(
    0.5, 0.27,
    "TOTAL → 2",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=34,
    fontweight="bold",
    alpha=0
)


def update1(frame):

    for i, piece in enumerate(pieces):

        if frame >= i * 6:
            height = 0.36 * (0.5 ** i)
            piece.set_height(height)

    if frame > 35:
        result.set_alpha(
            min(1, (frame - 35) / 20)
        )

    return pieces + [result]


anim = FuncAnimation(
    fig,
    update1,
    frames=75,
    interval=1000 / FPS,
    blit=True
)

render(
    fig,
    anim,
    "01_infinite_sum.mp4"
)


# =========================================================
# VIDEO 2 — TANGENT SLOPE
# =========================================================

fig, ax = setup()

ax.set_facecolor("#0b1020")
ax.set_xlim(-2, 2)
ax.set_ylim(-0.5, 4.5)
ax.axis("off")

ax.text(
    0.5, 0.94,
    "A CURVE HAS A SLOPE?!",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=32,
    fontweight="bold"
)

x = np.linspace(-2, 2, 500)
y = x ** 2

ax.plot(
    x,
    y,
    linewidth=4,
    color="white"
)

point, = ax.plot(
    [],
    [],
    "o",
    markersize=13,
    color="white"
)

tangent, = ax.plot(
    [],
    [],
    linewidth=4,
    color="white"
)

formula = ax.text(
    0.5,
    0.10,
    "f'(x) = 2x",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=30,
    fontweight="bold"
)


def update2(frame):

    t = -1.5 + (3 * frame / 89)

    yt = t ** 2
    slope = 2 * t

    xx = np.linspace(
        t - 0.8,
        t + 0.8,
        100
    )

    yy = yt + slope * (xx - t)

    point.set_data([t], [yt])

    tangent.set_data(
        xx,
        yy
    )

    return point, tangent


anim = FuncAnimation(
    fig,
    update2,
    frames=90,
    interval=1000 / FPS,
    blit=True
)

render(
    fig,
    anim,
    "02_tangent_slope.mp4"
)


# =========================================================
# VIDEO 3 — DETERMINANT AREA
# =========================================================

fig, ax = setup()

ax.set_facecolor("#0b1020")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect("equal")
ax.axis("off")

ax.text(
    0.5, 0.94,
    "ONE NUMBER CAN COLLAPSE A DIMENSION",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=25,
    fontweight="bold"
)

square = np.array([
    [-1, -1],
    [1, -1],
    [1, 1],
    [-1, 1],
    [-1, -1]
])

shape, = ax.plot(
    [],
    [],
    linewidth=5,
    color="white"
)

det_text = ax.text(
    0.5,
    0.10,
    "",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=30,
    fontweight="bold"
)


def update3(frame):

    t = frame / 89

    scale_y = 1 - t

    matrix = np.array([
        [1, 0],
        [0, scale_y]
    ])

    transformed = square @ matrix.T

    shape.set_data(
        transformed[:, 0],
        transformed[:, 1]
    )

    det_text.set_text(
        f"det(M) = {scale_y:.2f}"
    )

    return shape, det_text


anim = FuncAnimation(
    fig,
    update3,
    frames=90,
    interval=1000 / FPS,
    blit=True
)

render(
    fig,
    anim,
    "03_determinant_area.mp4"
)


print("ALL VIDEOS RENDERED")
print(os.listdir("output"))
