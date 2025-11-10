"""Testit varastoluokalle"""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """luokka testeille"""

    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """testaa tyhjän varaston luonti"""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """testaa oikea tilavuus"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """testaa saldon lisäys"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """testaa lisäys"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """testaa varastosta ottamisen"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """testaa ottaminen """
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)



    def test_negatiivinen_tilavuus(self):
        """neg tilavuuden luominen"""
        varasto = Varasto(-5)
        self.assertEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        """testaa negatiivinen alkusaldo"""
        varasto = Varasto(10, -5)
        self.assertEqual(varasto.saldo, 0)

    def test_liian_suuri_alkusaldo(self):
        """testaa liian iso alkusaldo"""
        varasto = Varasto(1, 20)
        self.assertEqual(varasto.saldo, 1)

    def test_liian_suuri_lisays(self):
        """testaa liian iso lisäys"""
        self.varasto.lisaa_varastoon(30)
        self.assertEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto(self):
        """testaa negativiinen otto"""
        self.assertEqual(self.varasto.ota_varastosta(-5), 0)

    def test_otto_suurempi_kuin_saldo(self):
        """testaa suurempi otto kuin saldo"""
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(10)
        self.assertEqual(saatu, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_oikein(self):
        """testaa että str palauttaa oikein"""
        self.varasto.lisaa_varastoon(6)
        self.assertEqual(str(self.varasto), "saldo = 6, vielä tilaa 4")

    def test_negatiivinen_lisays(self):
        """testaa negatiivinen lisäys"""
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, 0)
