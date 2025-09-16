# Optimal EV Charging Stations

## Project Overview

Optimal EV Charging Stations is a tool designed to help plan, optimize, and evaluate the placement and capacity of electric vehicle (EV) charging stations using heuristic and optimization techniques. The system supports multiple algorithms and distance-based models to help decision-makers (city planners, utility companies) minimize overall cost, travel distance, and ensure service coverage.

---

## Features

- Support for multiple optimization algorithms: **Genetic Algorithm**, **Particle Swarm Optimization**, and custom heuristics.  
- Ability to compute virtual distance and evaluate trade-offs between number of stations versus user access and travel distance.  
- Web interface (using `app.py` and HTML templates) to allow interactive selection of parameters and visualization of results.  
- Generation of “best EV Charging Station” configurations output via `best_evcs.py`, plus supporting modules for capacity, clustering, and optimization.  

---

## Tech Stack

| Component | Technology / Tools |
|-----------|-----------------------|
| Backend / Logic | Python |
| Optimization algorithms | Genetic Algorithm, Particle Swarm Optimization |
| Web Interface | Flask / HTML templates |
| Data handling | CSV / local data files in `data/` folder |
| Additional modules | `virtual_distance.py`, `evsc_optimization.py` etc. |

---

## How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Nishant232/Optimal-EV-Charging-Stations.git
   cd Optimal-EV-Charging-Stations
   ```

2. **Install dependencies**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Prepare data**  
   Put your data files (locations, demand points etc.) into the `data/` folder. Sample files are provided.

4. **Run the app / interface**  
   ```bash
   python app.py
   ```
   Then open your browser at `http://localhost:5000` (or whichever port shown) to interact with the interface.

5. **Run optimization scripts directly**  
   For command‑line execution of specific algorithms, e.g.:  
   ```bash
   python genetic_algo.py
   python particle_swarm.py
   ```

---

## Usage Examples

- Use Genetic Algorithm to minimize the sum of distances users must travel to nearest charging station.  
- Compare Particle Swarm vs Genetic Algorithm in terms of computation time and quality of placement.  
- Visual interface allows parameter tuning: number of stations, coverage radius, demand distribution.

---

## Results & Performance

> _Fill in with your own metrics here_

- Achieved X% reduction in average travel distance vs naive / uniform placement.  
- Execution time: Genetic Algorithm took ~Y seconds for data size of N, Particle Swarm ~Z seconds.  
- Supported up to M demand points / users in test cases, with coverage radius R km.

---

## File Structure

```
Optimal-EV-Charging-Stations/
├── app.py                       # Main web/Flask application
├── templates/                   # HTML templates for UI
├── data/                        # Input data files (locations, demands)
├── genetic_algo.py              # Genetic algorithm implementation
├── particle_swarm.py            # PSO implementation
├── evsc_optimization.py          # Modules to run optimization and result aggregation
├── virtual_distance.py           # Distance calculation utilities
├── best_evcs.py                  # Script to generate the best configuration
├── GOA.py                        # Possibly a “Grasshopper optimization algorithm” or another method
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## Contributing

If you'd like to contribute:

1. Fork the repo  
2. Create a new branch for your feature or bugfix  
3. Write tests if applicable  
4. Open a Pull Request describing your changes  

---

## License

Specify license (MIT / GPL / your choice) once finalized.

---

## Contact

**Nishant**  
GitHub: [@Nishant232](https://github.com/Nishant232)  
