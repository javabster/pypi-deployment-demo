from pdb_tools.interaction_extractor import get_protein_ligand_interaction_pdb

PDB_FILE = "pdb_tools/test/datafiles/1a52.pdb"
LIGAND_RESNAME = "EST"
CHAIN = "A"

get_protein_ligand_interaction_pdb(PDB_FILE, CHAIN, LIGAND_RESNAME)
