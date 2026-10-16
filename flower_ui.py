import math


def draw_flower(canvas, flower, x, y, stem_length=70):
    dna = flower.dna

    center_size = dna[0]
    center_color = f"#{dna[1]:02x}{dna[2]:02x}{dna[3]:02x}"
    petal_color = f"#{dna[4]:02x}{dna[5]:02x}{dna[6]:02x}"
    petals = dna[7]

    petal_r = 14
    # Distance from the center to each petal: petals overlap the
    # center edge by 4 px, so they always stay attached to it
    ring = center_size + petal_r - 4

    canvas.create_line(
        x, y,
        x, y + stem_length,
        fill="#2e8b57",
        width=5,
        capstyle="round"
    )

    for i in range(petals):
        angle = 2 * math.pi * i / petals

        px = x + ring * math.cos(angle)
        py = y + ring * math.sin(angle)

        canvas.create_oval(
            px - petal_r, py - petal_r,
            px + petal_r, py + petal_r,
            fill=petal_color,
            outline="black"
        )

    canvas.create_oval(
        x - center_size, y - center_size,
        x + center_size, y + center_size,
        fill=center_color,
        outline="black"
    )


def display_flowers(canvas, population, flower_positions):
    canvas.delete("all")

    for i, flower in enumerate(population):
        x, y = flower_positions[i]

        canvas.create_rectangle(
            x - 75, y - 65,
            x + 75, y + 115,
            outline="gray40",
            width=2
        )

        draw_flower(canvas, flower, x, y)

        canvas.create_text(
            x, y + 85,
            text=f"Flower {i + 1}"
        )

        canvas.create_text(
            x, y + 102,
            text=f"Fitness: {flower.fitness():.2f} sec",
            tags=f"score_{i}"
        )


def update_scores(canvas, population):
    for i, flower in enumerate(population):
        canvas.itemconfigure(
            f"score_{i}",
            text=f"Fitness: {flower.fitness():.2f} sec"
        )