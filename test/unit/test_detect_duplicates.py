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
        
        detect_duplicates(data)
        

@pytest.mark.unit
def test_duplicates_same_key():
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
        
    duplicate = detect_duplicates(data)
    assert len(duplicate) == 1


@pytest.mark.unit    
def test_two_duplicates_no_key():
    data = """
    @article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  
    }

    @article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  
    }
"""
        
    duplicate = detect_duplicates(data)
    assert len(duplicate) == 1
    
#I structured my test cases to be able to be used by github actions and to be easy to use and simple to understand and implement. I structured them with data sent in, and then what i asserted to find out
#I ensured test independence by keeping them seperate, their own marks and funcions. Important to only have one assert per test.
#I could not run the tests in vsc and had to rely on github actions. I also couldnt figure out how to get the mocking to work and infortunatly this isnt really a Unit test.