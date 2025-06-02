import pytest
import math
from calculadora import Calculadora


class TestCalculadora:
    
    @pytest.fixture
    def calc(self):
        """Fixture para criar uma instância da calculadora para cada teste"""
        return Calculadora()
    
    # Testes para soma
    def test_somar_numeros_positivos(self, calc):
        assert calc.somar(2, 3) == 5
    
    def test_somar_numeros_negativos(self, calc):
        assert calc.somar(-2, -3) == -5
    
    def test_somar_positivo_e_negativo(self, calc):
        assert calc.somar(5, -3) == 2
    
    def test_somar_com_zero(self, calc):
        assert calc.somar(5, 0) == 5
        assert calc.somar(0, 0) == 0
    
    # Testes para subtração
    def test_subtrair_numeros_positivos(self, calc):
        assert calc.subtrair(5, 3) == 2
    
    def test_subtrair_numeros_negativos(self, calc):
        assert calc.subtrair(-5, -3) == -2
    
    def test_subtrair_resultado_negativo(self, calc):
        assert calc.subtrair(3, 5) == -2
    
    # Testes para multiplicação
    def test_multiplicar_numeros_positivos(self, calc):
        assert calc.multiplicar(4, 5) == 20
    
    def test_multiplicar_com_zero(self, calc):
        assert calc.multiplicar(5, 0) == 0
        assert calc.multiplicar(0, 5) == 0
    
    # Testes para divisão
    def test_dividir_numeros_positivos(self, calc):
        assert calc.dividir(10, 2) == 5
    
    def test_dividir_por_zero_levanta_excecao(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.dividir(10, 0)
    
    # Testes para raiz quadrada
    def test_raiz_quadrada_numero_positivo(self, calc):
        assert calc.raizQuadrada(9) == 3
        assert calc.raizQuadrada(16) == 4
    
    def test_raiz_quadrada_zero(self, calc):
        assert calc.raizQuadrada(0) == 0
    
    # Testes para exponenciação
    def test_exponenciacao_base_positiva_expoente_positivo(self, calc):
        assert calc.exponenciacao(2, 3) == 8
        assert calc.exponenciacao(5, 2) == 25
    
    def test_exponenciacao_expoente_zero(self, calc):
        assert calc.exponenciacao(5, 0) == 1