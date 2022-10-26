from django.test import TestCase

# Create your tests here.
# 1 - Testes de unidade testam apenas uma parte atômica do sistema enquanto que testes
# funcionais parecem mais com testes de integração, o qual utiliza algumas partes do sistema.

# 2 - Testes de unidade são rodados inteiramente (a suíte toda) com uma frequência muito grande.
# Enquanto que teste funcionais não precisam de uma frequência tão grande uma vez que eles
# estão atreladas a uma funcionalidade específica do sistema então, se estivermos mechendo em outra
# parte do sistema, não faz sentido testar a primeira (se ela for desacoplada da última.)
