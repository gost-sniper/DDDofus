class Race:
    def __init__(self, name, dd1=None, dd2=None, gestation=0, parcho=None):
        self.name = name
        self.dd1 = dd1
        self.dd2 = dd2
        self.gestation = gestation
        self.parcho = parcho


# Generation 1
class Amande(Race):
    def __init__(self, dd1=None, dd2=None):
        super().__init__("Amande", dd1, dd2)


class Rousse(Race):
    def __init__(self, dd1=None, dd2=None):
        super().__init__("Rousse", dd1, dd2)


class Doree(Race):
    def __init__(self, dd1=None, dd2=None):
        super().__init__("Doree", dd1, dd2)


amande = Amande()
rousse = Rousse()
doree = Doree()


# Generation 2
class AmandeDoree(Race):
    def __init__(self, dd1=amande, dd2=doree):
        super().__init__("Amande & Doree", dd1, dd2)


class RousseAmande(Race):
    def __init__(self, dd1=amande, dd2=rousse):
        super().__init__("Rousse & Amande", dd1, dd2)


class RousseDoree(Race):
    def __init__(self, dd1=rousse, dd2=doree):
        super().__init__("Rousse & Doree", dd1, dd2)


amande_doree = AmandeDoree()
rousse_amande = RousseAmande()
rousse_doree = RousseDoree()


# Generation 3
class Indigo(Race):
    def __init__(self, dd1=rousse_amande, dd2=amande_doree):
        super().__init__("Indigo", dd1, dd2)


class Ebene(Race):
    def __init__(self, dd1=rousse_doree, dd2=amande_doree):
        super().__init__("Ebene", dd1, dd2)


indigo = Indigo()
ebene = Ebene()


# Generation 4
class IndigoEbene(Race):
    def __init__(self, dd1=indigo, dd2=ebene):
        super().__init__("Indigo & Ebene", dd1, dd2)


class RousseIndigo(Race):
    def __init__(self, dd1=rousse, dd2=indigo):
        super().__init__("Rousse & Indigo", dd1, dd2)


class RousseEbene(Race):
    def __init__(self, dd1=rousse, dd2=ebene):
        super().__init__("Rousse & Ebene", dd1, dd2)


class AmandeIndigo(Race):
    def __init__(self, dd1=amande, dd2=indigo):
        super().__init__("Amande & Indigo", dd1, dd2)


class AmandeEbene(Race):
    def __init__(self, dd1=amande, dd2=ebene):
        super().__init__("Amande & Ebene", dd1, dd2)


class DoreeIndigo(Race):
    def __init__(self, dd1=doree, dd2=indigo):
        super().__init__("Dorée & Indigo", dd1, dd2)


class DoreeEbene(Race):
    def __init__(self, dd1=doree, dd2=ebene):
        super().__init__("Dorée & Ebene", dd1, dd2)


indigo_ebene = IndigoEbene()
rousse_indigo = RousseIndigo()
rousse_ebene = RousseEbene()
amande_indigo = AmandeIndigo()
amande_ebene = AmandeEbene()
doree_indigo = DoreeIndigo()
doree_ebene = DoreeEbene()


# Generation 5
class Pourpre(Race):
    def __init__(self, dd1=rousse_amande, dd2=indigo_ebene):
        super().__init__("Pourpre", dd1, dd2)


class Orchidee(Race):
    def __init__(self, dd1=rousse_doree, dd2=indigo_ebene):
        super().__init__("Orchidée", dd1, dd2)


pourpre = Pourpre()
orchidee = Orchidee()

# Generation 6

class PourpreRousse(Race):
    def __init__(self, dd1=rousse, dd2=pourpre):
        super().__init__("Pourpre & Rousse", dd1, dd2)


class OrchideeRousse(Race):
    def __init__(self, dd1=rousse, dd2=orchidee):
        super().__init__("Orchidée & Rousse", dd1, dd2)


class AmandePourpre(Race):
    def __init__(self, dd1=amande, dd2=pourpre):
        super().__init__("Pourpre & Amande", dd1, dd2)


class AmandeOrchidee(Race):
    def __init__(self, dd1=amande, dd2=orchidee):
        super().__init__("Orchidée & Amande", dd1, dd2)


class DoreePourpre(Race):
    def __init__(self, dd1=doree, dd2=pourpre):
        super().__init__("Pourpre & Dorée", dd1, dd2)


class DoreeOrchidee(Race):
    def __init__(self, dd1=doree, dd2=orchidee):
        super().__init__("Orchidée & Dorée", dd1, dd2)


class IndigoPourpre(Race):
    def __init__(self, dd1=indigo, dd2=pourpre):
        super().__init__("Pourpre & Indigo", dd1, dd2)


class IndigoOrchidee(Race):
    def __init__(self, dd1=indigo, dd2=orchidee):
        super().__init__("Orchidée & Indigo", dd1, dd2)


class EbenePourpre(Race):
    def __init__(self, dd1=ebene, dd2=pourpre):
        super().__init__("Pourpre & Ebene", dd1, dd2)


class EbeneOrchidee(Race):
    def __init__(self, dd1=ebene, dd2=orchidee):
        super().__init__("Orchidée & Ebene", dd1, dd2)


class PourpreOrchidee(Race):
    def __init__(self, dd1=pourpre, dd2=orchidee):
        super().__init__("Pourpre & Orchidée", dd1, dd2)


pourpre_rousse = PourpreRousse()
orchidee_rousse = OrchideeRousse()
amande_porpre = AmandePourpre()
amande_orchidee = AmandeOrchidee()
doree_pourpre = DoreePourpre()
doree_orchidee = DoreeOrchidee()
indigo_pourpre = IndigoPourpre()
indigo_orchidee = IndigoOrchidee()
ebene_pourpre = EbenePourpre()
ebene_orchidee = EbeneOrchidee()
pourpre_orchidee = PourpreOrchidee()


# Generation 7

class Ivoire(Race):
    def __init__(self, dd1=indigo_pourpre, dd2=pourpre_orchidee):
        super().__init__("Ivoire", dd1, dd2)


class Turquoise(Race):
    def __init__(self, dd1=ebene_orchidee, dd2=pourpre_orchidee):
        super().__init__("Turquoise", dd1, dd2)


ivoire = Ivoire()
turquoise = Turquoise()


# Generation 8


class IvoireRousse(Race):
    def __init__(self, dd1=rousse, dd2=ivoire):
        super().__init__("Ivoire & Rousse", dd1, dd2)


class TurquoiseRousse(Race):
    def __init__(self, dd1=rousse, dd2=turquoise):
        super().__init__("Turquoise & Rousse", dd1, dd2)


class AmandeIvoire(Race):
    def __init__(self, dd1=amande, dd2=ivoire):
        super().__init__("Ivoire & Amande", dd1, dd2)


class AmandeTurquoise(Race):
    def __init__(self, dd1=amande, dd2=turquoise):
        super().__init__("Turquoise & Amande", dd1, dd2)


class DoreeIvoire(Race):
    def __init__(self, dd1=doree, dd2=ivoire):
        super().__init__("Ivoire & Dorée", dd1, dd2)


class DoreeTurquoise(Race):
    def __init__(self, dd1=doree, dd2=turquoise):
        super().__init__("Turquoise & Dorée", dd1, dd2)


class IndigoIvoire(Race):
    def __init__(self, dd1=indigo, dd2=ivoire):
        super().__init__("Ivoire & Indigo", dd1, dd2)


class IndigoTurquoise(Race):
    def __init__(self, dd1=indigo, dd2=turquoise):
        super().__init__("Turquoise & Indigo", dd1, dd2)


class EbeneIvoire(Race):
    def __init__(self, dd1=ebene, dd2=ivoire):
        super().__init__("Ivoire & Ebene", dd1, dd2)


class EbeneTurquoise(Race):
    def __init__(self, dd1=ebene, dd2=turquoise):
        super().__init__("Turquoise & Ebene", dd1, dd2)


class PourpreIvoire(Race):
    def __init__(self, dd1=pourpre, dd2=ivoire):
        super().__init__("Ivoire & Pourpre", dd1, dd2)


class TurquoisePourpre(Race):
    def __init__(self, dd1=pourpre, dd2=turquoise):
        super().__init__("Turquoise & Pourpre", dd1, dd2)


class IvoireOrchidee(Race):
    def __init__(self, dd1=orchidee, dd2=ivoire):
        super().__init__("Ivoire & Orchidée", dd1, dd2)


class TurquoiseOrchidee(Race):
    def __init__(self, dd1=orchidee, dd2=turquoise):
        super().__init__("Turquoise & Orchidée", dd1, dd2)


class IvoireTurquoise(Race):
    def __init__(self, dd1=ivoire, dd2=turquoise):
        super().__init__("Ivoire & Turquoise", dd1, dd2)


ivoire_rousse = IvoireRousse()
turquoise_rousse = TurquoiseRousse()
amande_ivoire = AmandeIvoire()
amande_turquoise = AmandeTurquoise()
doree_ivoire = DoreeIvoire()
doree_turquoise = DoreeTurquoise()
indigo_ivoire = IndigoIvoire()
indigo_turquoise = IndigoTurquoise()
ebene_ivoire = EbeneIvoire()
ebene_turquoise = EbeneTurquoise()
pourpre_ivoire = PourpreIvoire()
turquoise_pourpre = TurquoisePourpre()
ivoire_orchidee = IvoireOrchidee()
turquoise_orchidee = TurquoiseOrchidee()
ivoire_turquoise = IvoireTurquoise()



# Generation 9
class Emeraude(Race):
    def __init__(self, dd1=ivoire_turquoise, dd2=pourpre_ivoire):
        super().__init__("Emeraude", dd1, dd2)


class Prune(Race):
    def __init__(self, dd1=ivoire_turquoise, dd2=turquoise_orchidee):
        super().__init__("Prune", dd1, dd2)


emerude = Emeraude()
prune = Prune()

# Generation 10

class