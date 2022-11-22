import calc
def test_somme():
    output = calc.somme(2,4)
    assert output == 6
 
def test_produit():
    output = calc.produit(2, 4)
    assert output == 8
     
def test_soustraction():
    output = calc.soustraction(2,4)
    assert output == -2