import tkinter as tk
import math
import sys  #  to detect macOS for mouse-wheel handling

from genetic_algorithm import generate_population, create_new_population, POPULATION_SIZE
from flower_ui import display_flowers, update_scores

COLUMNS = 4
CELL_W, CELL_H = 200, 210
rows = math.ceil(POPULATION_SIZE / COLUMNS)

root = tk.Tk()
root.title("Flower Evolution")
root.geometry("820x600")  # fixed size (was based on rows), +20 px for the scrollbar

generation = 0
population = generate_population()
hovered_flower = None

flower_positions = [
    (100 + CELL_W * (i % COLUMNS), 85 + CELL_H * (i // COLUMNS))
    for i in range(POPULATION_SIZE)
]


def refresh_flowers():
    display_flowers(canvas, population, flower_positions)


def refresh_scores():
    update_scores(canvas, population)
    root.after(100, refresh_scores)


# hover logic moved out of handle_mouse_motion so scrolling can reuse it
def update_hover(x, y):
    global hovered_flower

    new_hovered = None

    for i, (fx, fy) in enumerate(flower_positions):
        distance = math.sqrt((x - fx) ** 2 + (y - fy) ** 2)

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


#  converts window coordinates to canvas coordinates before checking hover
def handle_mouse_motion(event):
    update_hover(canvas.canvasx(event.x), canvas.canvasy(event.y))


def handle_mouse_leave(event):
    global hovered_flower

    if hovered_flower is not None:
        population[hovered_flower].stop_hover()
        hovered_flower = None


# scrolling with the mouse wheel
def scroll(step):
    canvas.yview_scroll(step, "units")
    # the mouse didn't move but the canvas did, so re-check what is under the cursor
    px = canvas.winfo_pointerx() - canvas.winfo_rootx()
    py = canvas.winfo_pointery() - canvas.winfo_rooty()
    update_hover(canvas.canvasx(px), canvas.canvasy(py))


def handle_mouse_wheel(event):  # Windows and macOS
    if sys.platform == "darwin":
        scroll(-event.delta)
    else:
        scroll(-event.delta // 120)


def handle_linux_scroll(event):  # Linux (Button-4 = up, Button-5 = down)
    scroll(-1 if event.num == 4 else 1)


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

# button is now packed before the canvas so it stays visible at the bottom
next_button = tk.Button(
    root,
    text="Next Generation",
    command=evolve
)
next_button.pack(side="bottom", pady=8)

#frame holding the canvas and its scrollbar
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

# canvas now has a fixed view size, a scrollregion covering all rows,
# and a scroll step of 30 px per "unit"
canvas = tk.Canvas(
    canvas_frame,
    width=800,
    height=420,
    bg="white",
    scrollregion=(0, 0, 800, rows * CELL_H),
    yscrollincrement=30
)

# scrollbar linked to the canvas in both directions
scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

canvas.bind("<Motion>", handle_mouse_motion)
canvas.bind("<Leave>", handle_mouse_leave)
canvas.bind("<MouseWheel>", handle_mouse_wheel)      
canvas.bind("<Button-4>", handle_linux_scroll)       
canvas.bind("<Button-5>", handle_linux_scroll)      

refresh_flowers()
refresh_scores()
root.mainloop()