import pytest
from unittest.mock import patch, MagicMock
from src.util.detector import detect_duplicates
# develop your test cases here


@pytest.mark.unit
def test_one_entry():
    data = """
    @article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  doi={10.1007/s00766-023-00405-y}
    }
"""

    with pytest.raises(ValueError):
        duplicate = detect_duplicates(data)
        

@pytest.mark.unit
def test_two_entries_same_doi():
    data = """
    @article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  doi={10.1007/s00766-023-00405-y}
    }
"""
    mockedDAO = MagicMock()

    with pytest.raises(ValueError):
        mockedDAO.parse.return_value = None
        duplicate = detect_duplicates(data)
        

        