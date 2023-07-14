# N-Body Simulation

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Python code for simulating the gravitational interactions between celestial objects using numerical methods and Newton's laws of motion.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The N-Body Simulation is a Python code that models the gravitational interactions between celestial bodies, such as planets or stars, using numerical methods. It applies Newton's laws of motion to calculate the displacements and trajectories of the particles over time.

## Key Features

- **N-Body Simulation**: The code enables the simulation of gravitational interactions among multiple celestial bodies by numerically solving the equations of motion based on Newton's laws. It accurately calculates the trajectories and displacements of the bodies over time, providing a realistic representation of their orbital dynamics.

- **Customizable Parameters**: The code offers adjustable parameters such as the number of bodies, gravitational constant, initial positions, velocities, masses, time step, and total simulation time. This versatility allows researchers to tailor the simulation to specific scenarios and systems, facilitating in-depth investigations into celestial mechanics.

- **Visualization Capabilities**: The code incorporates the matplotlib library to generate high-quality visualizations of the celestial body trajectories. These visual representations enhance the understanding of the simulated dynamics, enabling researchers to analyze the intricate motion and gravitational interactions within the system.

- **Educational Tool**: The simulation code serves as an educational resource for studying celestial mechanics and gravitational interactions. Its intuitive nature allows students and learners to observe and analyze the simulated behaviors of celestial bodies, deepening their comprehension of fundamental concepts in the field.

- **Potential for Expansion**: The code serves as a foundation for further development and research. Researchers can extend the code to include advanced numerical techniques, incorporate additional forces, or simulate complex scenarios. It provides a valuable platform for investigating various aspects of celestial dynamics and advancing our understanding of gravitational systems.


## Installation

1. Clone the repository:
git clone https://github.com/arpmay/N-body-Problem.git

2. Install the required dependencies:
pip install numpy matplotlib


## Usage

1. Set the simulation parameters in the code:
- `k`: Number of bodies
- `G`: Universal Gravitational constant
- `dt`: Timestep in seconds
- `total_time`: Total simulation time

2. Specify the initial positions, velocities, and masses of the particles in the code.

3. Run the simulation:
python main.py

4. Visualize the trajectories of the particles using the provided 3D plot or animation (uncomment the code in `main.py`).

## Example

The animation below showcases an example simulation involving four bodies. The simulation consists of one massive central body and three satellite bodies orbiting around it under the influence of gravitational forces. 

![Particle Trajectories Animation](result.gif)

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

