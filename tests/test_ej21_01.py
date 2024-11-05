from src.ej21_01 import comprobar_edad

def test_comprobar_edad(edad):
    assert comprobar_edad(18) == True
    assert comprobar_edad(13) == False
    assert comprobar_edad(-18) == None