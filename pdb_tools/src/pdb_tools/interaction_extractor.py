from Bio.PDB import PDBParser, PDBIO, Select
from Bio.PDB import Structure, Atom

# Create selector class
class InteractionSelector(Select):
    """
    DOCSTRING
    """
    def __init__(self, target_chain_id, ligand_resname, neighbor_residues):
        self.target_chain_id = target_chain_id
        self.ligand_resname = ligand_resname
        self.neighbor_residues = neighbor_residues

    def accept_residue(self, residue):
        chain_id = residue.get_parent().id
        is_target_chain = chain_id == self.target_chain_id
        is_ligand = residue.get_resname(
        ) == self.ligand_resname and is_target_chain
        is_neighbor = residue in self.neighbor_residues and is_target_chain
        return is_ligand or is_neighbor


def find_ligand_atoms(structure: Structure,
                      target_chain: str,
                      ligand_resname: str):
    """
    DOCSTRING
    """
    # COMPLETE THIS FUNCTION!!!


def find_neighbor_residues(structure: Structure,
                           ligand_atoms: list[Atom],
                           target_chain: str,
                           ligand_resname: str,
                           distance_cutoff: int = 5.0):
    """
    DOCSTRING
    """
    # COMPLETE THIS FUNCTION!!!


def get_protein_ligand_interaction_pdb(pdb_file: str,
                                       chain: str,
                                       ligand_resname: str,
                                       distance_cutoff: int = 5.0):
    """
    DOCSTRING
    """
    parser = PDBParser(QUIET=True)
    # ADD A CHECK TO MAKE SURE .PDB FILES ARE USED
    structure = parser.get_structure("complex", pdb_file)
    ligand_atoms = find_ligand_atoms(structure, chain, ligand_resname)
    neighbor_residues = find_neighbor_residues(structure, ligand_atoms, chain,
                                               ligand_resname, distance_cutoff)
    selector = InteractionSelector(target_chain_id=chain,
                                   ligand_resname=ligand_resname,
                                   neighbor_residues=neighbor_residues)
    # Write output
    io = PDBIO()
    io.set_structure(structure)
    # ADD NEW ARGUMENT TO SUPPORT CUSTOM OUTPUT NAMES
    io.save("trimmed_complex.pdb", selector)
