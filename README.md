# FloralNetworks 🌸

An interactive genetic algorithm written in Python that evolves a population of flowers. There is no fixed fitness function here: **you** decide which flowers are the best by hovering your mouse over them. The longer you hover, the fitter the flower, and the more likely it is to pass its genes to the next generation.

Made for the CSEN1121 (Computational Intelligence and Neural Networks) course at the German University in Cairo, Winter 2026.

## Goal of the project

The goal is to understand the basic ideas behind genetic algorithms (selection, crossover and mutation) by building one from scratch, with no GA libraries. The flowers should slowly change over the generations and start to look like the ones the user preferred.

## How it works

Every flower has a DNA of 8 genes:

| Index | Gene | Range |
|-------|------|-------|
| 0 | Size of the center | 20 to 30 |
| 1-3 | Center color (R, G, B) | 0 to 255 |
| 4-6 | Petal color (R, G, B) | 0 to 255 |
| 7 | Number of petals | 0 to 7 |

The population always has 8 flowers. Each generation works like this:

1. **Fitness:** the time (in seconds) the mouse spent over a flower.
2. **Selection:** roulette wheel selection, so a flower with more hover time has a bigger chance of being chosen as a parent.
3. **Crossover:** single point crossover between two parents gives two children.
4. **Mutation:** a randomly chosen gene of each child gets a new random value.
5. **Replacement:** the 8 children replace the old population when you press **Next Generation**.

## Project structure

```
FloralNetworks/
├── main.py                 # Tkinter window, mouse hover handling, Next Generation button
├── flower.py               # Flower class: DNA and hover time (fitness)
├── flower_ui.py            # Drawing the flowers from their DNA and showing the scores
├── genetic_algorithm.py    # Population, selection, crossover, mutation, new generation
└── README.md
```

## Requirements

- Python 3.8 or newer
- Tkinter (it comes with the normal Python installer on Windows and macOS)

On Linux you may need to install it first:

```bash
sudo apt install python3-tk
```

## How to run

```bash
git clone https://github.com/<your-username>/FloralNetworks.git
cd FloralNetworks
python main.py
```

Then move the mouse over the flowers you like, and press **Next Generation**. Repeat for as many generations as you want.

## Results

These screenshots are from one of our runs, where we kept hovering over flowers with green centers and mauve petals.

**Generation 0:** the random starting population.

<img width="986" height="635" alt="Screenshot 2026-10-14 013910" src="https://github.com/user-attachments/assets/636e5521-c2ca-4cae-a4eb-bbbaf901e0a4" />


**Generation 1:** traits of the most hovered flowers start to appear.

<img width="972" height="625" alt="Screenshot 2026-10-14 013950" src="https://github.com/user-attachments/assets/9e5ab0fc-f72e-4759-90c2-9d8d7ea30cf4" />


**Generation 2:** more petals, and green centers with mauve petals become common.

<img width="978" height="635" alt="Screenshot 2026-10-14 014020" src="https://github.com/user-attachments/assets/38188f9c-a1b8-46ff-8d57-ae6c3c9a0ceb" />


**Generation 3:** mauve petals and green centers dominate.

<img width="979" height="625" alt="Screenshot 2026-10-14 014050" src="https://github.com/user-attachments/assets/52f82c2d-db65-4dd0-b120-83df790491bb" />


**Generation 4:** the green center is in almost every flower.

<img width="976" height="632" alt="Screenshot 2026-10-14 014129" src="https://github.com/user-attachments/assets/05618254-3026-43c7-b5c2-2778f7be950d" />


**Generation 14:** the population is much more uniform: about 7 petals, light purple petals and mostly green centers, with a bit of variation left from mutation.



## Team

- Salma Ibrahim: `Flower` class (`flower.py`) and `flower_ui.py`
- Ibrahim Hassan: `genetic_algorithm.py`
- Eyad Alaaeldin: `main.py`

## Course

German University in Cairo, Faculty of Media Engineering and Technology
CSEN1121 Computational Intelligence and Neural Networks, Assignment 1
Supervised by Prof. Dr. Mohammed Abdel-Megeed Salem and Eng. Dinah Waref Shalaby
