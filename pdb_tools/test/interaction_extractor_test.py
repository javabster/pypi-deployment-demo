from Bio.PDB import PDBParser
from pdb_tools.interaction_extractor import find_ligand_atoms, find_neighbor_residues

PDB_FILE = "datafiles/1a52.pdb"


def test_find_ligand_atoms():
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("complex", PDB_FILE)
    lig_atoms = find_ligand_atoms(structure, "A", "EST")
    assert len(lig_atoms) == 20


def test_find_neighbor_resiudes():
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("complex", PDB_FILE)
    lig_atoms = find_ligand_atoms(structure, "A", "EST")
    neighbor_residues = find_neighbor_residues(structure, lig_atoms, "A", "EST", 5)
    assert len(neighbor_residues) == 19
