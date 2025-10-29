# 💻 CHEM 281 Lab: Deploying Code

## 🧪 Goal

The goal of this lab is to:

1. Familiarize yourself with **python package deployment and BioPython**.
2. Learn how to **deploy a python package**. 
3. Practice using **bioinformatics code** and **BioPython**.
4. Complete the missing functions and **deploy to the test PyPi server**.

---

## 🗂️ Provided

- A `docker` file to set up the dev environment.
- Bioinformatics module in `pdb_tools/` and associated tests `pdb_tools/test/`.

---

## 💻 Setup
```bash
./docker_build.sh # You may need to chmod +x

./docker_run.sh # You may need to chmod +x

cd pdb_tools

pip install -e . # -e means editable, so we don't need to keep installing while editing

pytest test/interaction_extractor_test.py
# Both tests should fail!

python3 runner.py
# Should fail because the functions are empty!
```

## ✅ Tasks
In the repo you should see the main file `src/pdb_tools/interaction_extractor.py`. This file contains the following functions and classes:

1. get_protein_ligand_interaction_pdb
2. InteractionSelector
3. find_neighbor_residues
4. find_ligand_atoms

`get_protein_ligand_interaction_pdb` is mostly done, but you should add some checks to ensure the user only supplies PDB files, as well as supporting a new argument: output_file which should default to None. If the user does not pass in an output_file, the name should be derived from the input PDB file with `_out` appended.

`find_ligand_atoms` is completely empty and you need to complete it. From the tests you can see what the ligand resname could be, as well as looking through other PDB files. Your goal is to find and collect all ligand atoms and return them as a list.

```python
def find_ligand_atoms(structure: Structure,
                      target_chain: str,
                      ligand_resname: str)
```

`find_neighbor_residues` is completely empty and you need to complete it. The distance cut off is used to determine which atoms are close enough to be considered an interaction. You need to find all the residues that are within the distance cutoff of ANY ligand atoms. Hint: BioPython Atom objects have a `__sub__` method so you can directly subtract 2 atoms to get a distance.

```python
def find_neighbor_residues(structure: Structure,
                           ligand_atoms: list[Atom],
                           target_chain: str,
                           ligand_resname: str,
                           distance_cutoff: int = 5.0)
```

Write DOCSTRINGS for all the functions using the Sphinx convention: https://www.sphinx-doc.org/en/master/.

Add some information into the README.md that is in the package directory: `pdb_tools/README.md`. This is what will be shown on your package page on test PyPi, so add some info about the project and functions, as well as how to use it.

Once your tests are passing, you can move on to building and deploying!
1) Edit the `project.toml` file with your own project name and other metadata.
   - https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
2) cd into pdb_tools and run `python3 -m build`. You should now see a `dist/`
3) Create a test PyPi account (https://test.pypi.org/) and generate an API key.
   - Account settings -> scroll down to API tokens
4) Run `twine upload --repository testpypi dist/*`. You will need to provide the API key here.
5) View the page on test.pypi.org. It should tell you the page if the previous step was successful.
6) Exit out of the docker container and create a new container.
7) Confirm there are no installations by running `python3 runner.py`. It should fail.
8) Install the package from test pypi using the command on the project page.
9) Run `python3 runner.py` and you should get an output file which you can visualize using PyMOL.

PyMOL: https://www.pymol.org/

### Extra time
Can you change the color of the exported ligand so when we visualize it, its colored differently from the residues immediately?
