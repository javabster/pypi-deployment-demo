# PDB Tools

PDB Tools is a Python package designed to facilitate the analysis of protein-ligand interactions in PDB (Protein Data Bank) files. It provides utilities to extract ligand atoms, identify neighboring residues, and generate new PDB files for visualization.

---

## Features

- **Find Ligand Atoms**: Extract all atoms of a specified ligand from a PDB structure.
- **Identify Neighbor Residues**: Locate residues within a specified distance from the ligand atoms.
- **Generate Interaction PDB Files**: Create new PDB files containing the ligand and its neighboring residues for visualization.

---

## Installation

To install the package, navigate to the `pdb_tools` directory and run:

```bash
pip install -e .
```

This installs the package in editable mode, allowing you to make changes without reinstalling.

## Usage

### Extract Ligand Atoms
Use the `find_ligand_atoms` function to extract all atoms of a specified ligand from a provided structure and chain:

```python
from pdb_tools.interaction_extractor import find_ligand_atoms
from Bio.PDB import PDBParser

parser = PDBParser(QUIET=True)
structure = parser.get_structure("complex", "path/to/pdb_file.pdb")
ligand_atoms = find_ligand_atoms(structure, "A", "EST")
```

### Find Neighbor Residues
Use the `find_neighbor_residues` function to identify residues near the ligand:

```python
from pdb_tools.interaction_extractor import find_neighbor_residues

neighbor_residues = find_neighbor_residues(structure, ligand_atoms, "A", "EST", 5.0)
```

### Generate Interaction PDB
Use the `get_protein_ligand_interaction_pdb` function to extracts ligand and neighboring residues from a PDB file and save it to a new PDB file.

```python
from pdb_tools.interaction_extractor import get_protein_ligand_interaction_pdb

get_protein_ligand_interaction_pdb("path/to/pdb_file.pdb", "A", "EST", 5.0, "output.pdb")
```


## Testing
Run the tests to ensure everything is working correctly:

```bash
pytest test/interaction_extractor_test.py
```




