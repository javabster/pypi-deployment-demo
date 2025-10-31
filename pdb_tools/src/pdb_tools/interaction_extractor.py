from Bio.PDB import PDBParser, PDBIO, Select
from Bio.PDB import Structure, Atom

# Create selector class
class InteractionSelector(Select):
    """
    Selector to extract ligand and neighboring residues from a PDB structure.

    Parameters
    ----------
    target_chain_id : str
        The chain identifier where the ligand is located.
    ligand_resname : str
        The residue name of the ligand.
    neighbor_residues : set
        A set of neighboring residues within a specified distance from the ligand.
    
    Methods
    -------
    accept_residue(residue)
        Determines whether a residue should be included in the output based on
        whether it is the ligand or a neighboring residue.
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
    Finds and returns all atoms of the specified ligand in the given structure.

    Parameters
    ----------
    structure : Structure
        The PDB structure to search.
    target_chain : str
        The chain identifier where the ligand is located.
    ligand_resname : str
        The residue name of the ligand.
    
    Returns
    -------
    list[Atom]
        A list of Atom objects representing the ligand atoms.
    """
    ligand_atoms = []
    for model in structure:
        for chain in model:
            if chain.id == target_chain:
                for residue in chain:
                    if residue.get_resname() == ligand_resname:
                        for atom in residue:
                            ligand_atoms.append(atom)
    return ligand_atoms



def find_neighbor_residues(structure: Structure,
                           ligand_atoms: list[Atom],
                           target_chain: str,
                           ligand_resname: str,
                           distance_cutoff: int = 5.0):
    """
    Finds and returns residues within a specified distance from the ligand atoms

    Parameters
    ----------
    structure : Structure
        The PDB structure to search.
    ligand_atoms : list[Atom]
        A list of Atom objects representing the ligand atoms.
    target_chain : str
        The chain identifier where the ligand is located.
    ligand_resname : str
        The residue name of the ligand.
    distance_cutoff : int, optional
        The distance cutoff to consider a residue as a neighbor (default is 5.0 Å).

    Returns
    -------
    set
        A set of residues that are within the specified distance from the ligand atoms.
    """
    # COMPLETE THIS FUNCTION!!!
    neighbor_residues = set()
    for model in structure:
        for chain in model:
            if chain.id == target_chain:
                for residue in chain:
                    if residue.get_resname() != ligand_resname:
                        for atom in residue:
                            for lig_atom in ligand_atoms:
                                distance = atom - lig_atom 
                                if distance <= distance_cutoff:
                                    neighbor_residues.add(residue)
                                    break
    return neighbor_residues


def get_protein_ligand_interaction_pdb(pdb_file: str,
                                       chain: str,
                                       ligand_resname: str,
                                       distance_cutoff: int = 5.0,
                                       output_file: str = None):
    """
    Extracts ligand and neighboring residues from a PDB file and saves to a new PDB file.
    
    Parameters
    ----------
    pdb_file : str
        Path to the input PDB file.
    chain : str
        Chain identifier where the ligand is located.
    ligand_resname : str
        Residue name of the ligand.
    distance_cutoff : int, optional
        Distance cutoff to consider a residue as a neighbor (default is 5.0 Å).
    output_file : str, optional
        Path to the output PDB file. If not provided, a default name will be used.
    
    Returns
    -------
    None
    """
    parser = PDBParser(QUIET=True)
    # ADD A CHECK TO MAKE SURE .PDB FILES ARE USED
    if not pdb_file.lower().endswith('.pdb'):
        raise ValueError("Input file must be a .pdb file")

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
    if output_file:
        io.save(output_file, selector)
    else:
        filename = pdb_file.rsplit('/', 1)[-1].rsplit('.', 1)[0]
        output_filename = f"{filename}_output.pdb"
        io.save(output_filename, selector)
