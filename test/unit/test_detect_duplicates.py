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
    mockedDAO = MagicMock()

    

    with pytest.raises(ValueError):
        mockedDAO.parse.return_value = []
        detect_duplicates(data)
        

@pytest.mark.unit
def test_duplicates_same_key_DOI():
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
    output = """
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
    mockedDAO.parse.return_value = output
    duplicate = detect_duplicates(data)
    assert len(duplicate) == 1


@pytest.mark.unit    
def test_duplicates_no_key():
    data = """@article{wagner2019status,
  title={Status quo in requirements engineering: A theory and a global family of surveys},
  author={Wagner, Stefan and M{\'e}ndez Fern{\'a}ndez, Daniel and Felderer, Michael and Vetr{\`o}, Antonio and Kalinowski, Marcos and Wieringa, Roel and Pfahl, Dietmar and Conte, Tayana and Christiansson, Marie-Therese and Greer, Desmond and others},
  journal={ACM Transactions on Software Engineering and Methodology (TOSEM)},
  volume={28},
  number={2},
  pages={1--48},
  year={2019},
  publisher={ACM New York, NY, USA}
}

@article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer}
}"""

    duplicate = detect_duplicates(data)
    assert len(duplicate) == 1
    