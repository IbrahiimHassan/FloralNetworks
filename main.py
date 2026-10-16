
import tkinter as tk
import math

from genetic_algorithm import generate_population, create_new_population
from flower_ui import display_flowers, update_scores


root = tk.Tk()
root.title("Flower Evolution")
root.geometry("800x600")

generation = 0
population = generate_population()
hovered_flower = None

flower_positions = [
    (100, 85), (300, 85), (500, 85), (700, 85),
    (100, 295), (300, 295), (500, 295), (700, 295)
]


def refresh_flowers():
    display_flowers(canvas, population, flower_positions)


def refresh_scores():
    update_scores(canvas, population)
    root.after(100, refresh_scores)


def handle_mouse_motion(event):
    global hovered_flower

    new_hovered = None

    for i, (x, y) in enumerate(flower_positions):
        distance = math.sqrt(
            (event.x - x) ** 2 + (event.y - y) ** 2
        )

        if distance <= 55:
            new_hovered = i
            break

    if new_hovered == hovered_flower:
        return

    if hovered_flower is not None:
        population[hovered_flower].stop_hover()

    hovered_flower = new_hovered

    if hovered_flower is not None:
        population[hovered_flower].start_hover()


def handle_mouse_leave(event):
    global hovered_flower

    if hovered_flower is not None:
        population[hovered_flower].stop_hover()
        hovered_flower = None


def evolve():
    global population, generation, hovered_flower

    if hovered_flower is not None:
        population[hovered_flower].stop_hover()
        hovered_flower = None

    population = create_new_population(population)
    generation += 1

    generation_label.config(
        text=f"Generation: {generation}"
    )

    refresh_flowers()


generation_label = tk.Label(
    root,
    text="Generation: 0",
    font=("Arial", 16)
)
generation_label.pack(pady=5)

canvas = tk.Canvas(
    root,
    width=800,
    height=420,
    bg="white"
)
canvas.pack()

canvas.bind("<Motion>", handle_mouse_motion)
canvas.bind("<Leave>", handle_mouse_leave)

next_button = tk.Button(
    root,
    text="Next Generation",
    command=evolve
)
next_button.pack(pady=8)

refresh_flowers()
refresh_scores()
root.mainloop()
