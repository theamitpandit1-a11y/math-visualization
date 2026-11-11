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
    fig, ax = plt.subplots(
        figsize=(WIDTH / DPI, HEIGHT / DPI),
        dpi=DPI
    )

    fig.patch.set_facecolor("#080b14")
    ax.set_facecolor("#080b14")
    ax.axis("off")

    return fig, ax


def branding(ax):
    ax.text(
        0.5, 0.965,
        "IIT MATH OFFICIAL",
        transform=ax.transAxes,
        ha="center",
        va="top",
        color="white",
        fontsize=22,
        fontweight="bold"
    )

    ax.text(
        0.5, 0.942,
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
# VIDEO 1 — INFINITE SUM
# =========================================================

fig, ax = setup()
branding(ax)

ax.text(
    0.5, 0.875,
    "INFINITE SUM = 2?!",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=34,
    fontweight="bold"
)

ax.text(
    0.5, 0.825,
    "1 + 1/2 + 1/4 + 1/8 + ...",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=24
)

# Large visual area
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

rectangles = []

start_x = 0.08
y = 0.47

for i in range(8):
    width = 0.82 * (0.5 ** i)

    rect = plt.Rectangle(
        (start_x, y),
        width,
        0.10,
        fill=False,
        linewidth=4,
        edgecolor="white"
    )

    ax.add_patch(rect)
    rectangles.append(rect)

    start_x += width

result = ax.text(
    0.5, 0.27,
    "The pieces approach a total of 2",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=22,
    alpha=0
)

answer = ax.text(
    0.5, 0.20,
    "1 + 1/2 + 1/4 + ... = 2",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=32,
    fontweight="bold",
    alpha=0
)


def update1(frame):

    # 30 sec total
    progress = frame / 899

    # Sequential reveal
    for i, rect in enumerate(rectangles):

        start = i / 8
        end = (i + 1) / 8

        if progress < start:
            rect.set_alpha(0)

        elif progress >= end:
            rect.set_alpha(1)

        else:
            rect.set_alpha(
                (progress - start) / (end - start)
            )

    if progress > 0.65:
        result.set_alpha(
            min(1, (progress - 0.65) / 0.12)
        )

    if progress > 0.80:
        answer.set_alpha(
            min(1, (progress - 0.80) / 0.12)
        )

    return rectangles + [result, answer]


anim = FuncAnimation(
    fig,
    update1,
    frames=900,
    interval=1000 / FPS,
    blit=True
)

render(
    fig,
    anim,
    "01_infinite_sum.mp4"
)


# =========================================================
# VIDEO 2 — TANGENT / DERIVATIVE
# =========================================================

fig, ax = setup()

fig.patch.set_facecolor("#080b14")
ax.set_facecolor("#080b14")

ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-0.8, 4.8)

ax.axis("off")

ax.text(
    0.5, 0.965,
    "IIT MATH OFFICIAL",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=22,
    fontweight="bold"
)

ax.text(
    0.5, 0.942,
    "@iit.math_official",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=14
)

ax.text(
    0.5, 0.875,
    "A CURVE HAS A SLOPE?!",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=32,
    fontweight="bold"
)

x = np.linspace(-2, 2, 600)
y = x ** 2

curve, = ax.plot(
    x,
    y,
    linewidth=4,
    color="white"
)

point, = ax.plot(
    [],
    [],
    "o",
    markersize=14,
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
    fontsize=32,
    fontweight="bold",
    alpha=0
)

explanation = ax.text(
    0.5,
    0.055,
    "Derivative = instantaneous slope",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=20,
    alpha=0
)


def update2(frame):

    progress = frame / 899

    # Point moves slowly along the curve
    t = -1.5 + 3.0 * progress

    yt = t ** 2
    slope = 2 * t

    xx = np.linspace(
        t - 0.75,
        t + 0.75,
        120
    )

    yy = yt + slope * (xx - t)

    point.set_data([t], [yt])
    tangent.set_data(xx, yy)

    if progress > 0.65:
        formula.set_alpha(
            min(1, (progress - 0.65) / 0.12)
        )

    if progress > 0.80:
        explanation.set_alpha(
            min(1, (progress - 0.80) / 0.12)
        )

    return point, tangent, formula, explanation


anim = FuncAnimation(
    fig,
    update2,
    frames=900,
    interval=1000 / FPS,
    blit=True
)

render(
    fig,
    anim,
    "02_tangent_slope.mp4"
)


# =========================================================
# VIDEO 3 — DETERMINANT
# =========================================================

fig, ax = setup()

fig.patch.set_facecolor("#080b14")
ax.set_facecolor("#080b14")

ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.4, 2.4)

ax.set_aspect("equal")
ax.axis("off")

ax.text(
    0.5, 0.965,
    "IIT MATH OFFICIAL",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=22,
    fontweight="bold"
)

ax.text(
    0.5, 0.942,
    "@iit.math_official",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=14
)

ax.text(
    0.5, 0.875,
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
    fontsize=32,
    fontweight="bold"
)

explanation = ax.text(
    0.5,
    0.055,
    "Area scales by |det(M)|",
    transform=ax.transAxes,
    ha="center",
    color="white",
    fontsize=20,
    alpha=0
)


def update3(frame):

    progress = frame / 899

    # Start with a square and gradually flatten it
    scale_y = 1 - progress

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

    if progress > 0.75:
        explanation.set_alpha(
            min(1, (progress - 0.75) / 0.12)
        )

    return shape, det_text, explanation


anim = FuncAnimation(
    fig,
    update3,
    frames=900,
    interval=1000 / FPS,
    blit=True
)

render(
    fig,
    anim,
    "03_determinant_area.mp4"
)


print("===================================")
print("ALL 3 VIDEOS RENDERED SUCCESSFULLY")
print("===================================")

for filename in sorted(os.listdir("output")):
    print(filename)
