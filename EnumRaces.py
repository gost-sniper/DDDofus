class Race:
    def __init__(self, name, dd1=None, dd2=None, gestation=0, parcho=None, generation=None):
        self.name = name
        self.dd1 = dd1
        self.dd2 = dd2
        self.generation = generation
        self.gestation = gestation
        self.parcho = parcho


class Rousse(Race):
    def __init__(self, dd1=None, dd2=None, gestation=48, parcho="Parchemin Doré", generation=1):
        super().__init__("Rousse", dd1, dd2, gestation, parcho, generation)


class Amande(Race):
    def __init__(self, dd1=None, dd2=None, gestation=48, parcho="Parchemin Doré", generation=1):
        super().__init__("Amande", dd1, dd2, gestation, parcho, generation)


class Doree(Race):
    def __init__(self, dd1=None, dd2=None, gestation=48, parcho="Parchemin Doré", generation=1):
        super().__init__("Dorée", dd1, dd2, gestation, parcho, generation)


class RousseAmande(Race):
    def __init__(self, dd1=Rousse, dd2=Amande, gestation=60, parcho="Petit Vitalité", generation=2):
        super().__init__("Rousse & Amande", dd1, dd2, gestation, parcho, generation)


class RousseDoree(Race):
    def __init__(self, dd1=Rousse, dd2=Doree, gestation=60, parcho="Petit sagesse", generation=2):
        super().__init__("Rousse & Dorée", dd1, dd2, gestation, parcho, generation)


class AmandeDoree(Race):
    def __init__(self, dd1=Amande, dd2=Doree, gestation=60, parcho="Petit sagesse", generation=2):
        super().__init__("Amande & Dorée", dd1, dd2, gestation, parcho, generation)


class Indigo(Race):
    def __init__(self, dd1=RousseAmande, dd2=AmandeDoree, gestation=72, parcho="Petit chance", generation=3):
        super().__init__("Indigo", dd1, dd2, gestation, parcho, generation)


class Ebene(Race):
    def __init__(self, dd1=RousseDoree, dd2=AmandeDoree, gestation=72, parcho="Petit Agilité", generation=3):
        super().__init__("Ebène", dd1, dd2, gestation, parcho, generation)


class RousseIndigo(Race):
    def __init__(self, dd1=Rousse, dd2=Indigo, gestation=84, parcho="Petit Vitalité", generation=4):
        super().__init__("Rousse & Indigo", dd1, dd2, gestation, parcho, generation)


class RousseEbene(Race):
    def __init__(self, dd1=Rousse, dd2=Ebene, gestation=84, parcho="Petit Vitalité", generation=4):
        super().__init__("Rousse & Ebène", dd1, dd2, gestation, parcho, generation)


class AmandeIndigo(Race):
    def __init__(self, dd1=Amande, dd2=Indigo, gestation=84, parcho="Petit chance", generation=4):
        super().__init__("Amande & Indigo", dd1, dd2, gestation, parcho, generation)


class AmandeEbene(Race):
    def __init__(self, dd1=Amande, dd2=Ebene, gestation=84, parcho="Petit Agilité", generation=4):
        super().__init__("Amande & Ebène", dd1, dd2, gestation, parcho, generation)


class DoreeIndigo(Race):
    def __init__(self, dd1=Doree, dd2=Indigo, gestation=84, parcho="Petit sagesse", generation=4):
        super().__init__("Dorée & Indigo", dd1, dd2, gestation, parcho, generation)


class DoreeEbene(Race):
    def __init__(self, dd1=Doree, dd2=Ebene, gestation=84, parcho="Petit sagesse", generation=4):
        super().__init__("Dorée & Ebène", dd1, dd2, gestation, parcho, generation)


class IndigoEbene(Race):
    def __init__(self, dd1=Indigo, dd2=Ebene, gestation=84, parcho="Petit chance", generation=4):
        super().__init__("Indigo & Ebène", dd1, dd2, gestation, parcho, generation)


class Pourpre(Race):
    def __init__(self, dd1=RousseAmande, dd2=IndigoEbene, gestation=96, parcho="Petit force", generation=5):
        super().__init__("Pourpre", dd1, dd2, gestation, parcho, generation)


class Orchidee(Race):
    def __init__(self, dd1=RousseDoree, dd2=IndigoEbene, gestation=96, parcho="Petit intelligence", generation=5):
        super().__init__("Orchidée", dd1, dd2, gestation, parcho, generation)


class PourpreRousse(Race):
    def __init__(self, dd1=Rousse, dd2=Pourpre, gestation=108, parcho="Moyen force", generation=6):
        super().__init__("Pourpre & Rousse", dd1, dd2, gestation, parcho, generation)


class OrchideeRousse(Race):
    def __init__(self, dd1=Rousse, dd2=Orchidee, gestation=108, parcho="Moyen intelligence", generation=6):
        super().__init__("Orchidée & Rousse", dd1, dd2, gestation, parcho, generation)


class AmandePourpre(Race):
    def __init__(self, dd1=Amande, dd2=Pourpre, gestation=108, parcho="Moyen force", generation=6):
        super().__init__("Amande & Pourpre", dd1, dd2, gestation, parcho, generation)


class AmandeOrchidee(Race):
    def __init__(self, dd1=Amande, dd2=Orchidee, gestation=108, parcho="Moyen Vitalité", generation=6):
        super().__init__("Amande & Orchidée", dd1, dd2, gestation, parcho, generation)


class DoreePourpre(Race):
    def __init__(self, dd1=Doree, dd2=Pourpre, gestation=108, parcho="Moyen sagesse", generation=6):
        super().__init__("Dorée & Pourpre", dd1, dd2, gestation, parcho, generation)


class DoreeOrchidee(Race):
    def __init__(self, dd1=Doree, dd2=Orchidee, gestation=108, parcho="Moyen sagesse", generation=6):
        super().__init__("Dorée & Orchidée", dd1, dd2, gestation, parcho, generation)


class IndigoPourpre(Race):
    def __init__(self, dd1=Indigo, dd2=Pourpre, gestation=108, parcho="Moyen chance", generation=6):
        super().__init__("Indigo & Pourpre", dd1, dd2, gestation, parcho, generation)


class IndigoOrchidee(Race):
    def __init__(self, dd1=Indigo, dd2=Orchidee, gestation=108, parcho="Moyen chance", generation=6):
        super().__init__("Indigo & Orchidée", dd1, dd2, gestation, parcho, generation)


class EbenePourpre(Race):
    def __init__(self, dd1=Ebene, dd2=Pourpre, gestation=108, parcho="Moyen Agilité", generation=6):
        super().__init__("Ebène & Pourpre", dd1, dd2, gestation, parcho, generation)


class EbeneOrchidee(Race):
    def __init__(self, dd1=Ebene, dd2=Orchidee, gestation=108, parcho="Moyen Agilité", generation=6):
        super().__init__("Ebène & Orchidée", dd1, dd2, gestation, parcho, generation)


class PourpreOrchidee(Race):
    def __init__(self, dd1=Pourpre, dd2=Orchidee, gestation=108, parcho="Moyen intelligence", generation=6):
        super().__init__("Pourpre & Orchidée", dd1, dd2, gestation, parcho, generation)


class Ivoire(Race):
    def __init__(self, dd1=IndigoPourpre, dd2=PourpreOrchidee, gestation=120, parcho="Grand chance", generation=7):
        super().__init__("Ivoire", dd1, dd2, gestation, parcho, generation)


class Turquoise(Race):
    def __init__(self, dd1=EbeneOrchidee, dd2=PourpreOrchidee, gestation=120, parcho="Grand Agilité", generation=7):
        super().__init__("Turquoise", dd1, dd2, gestation, parcho, generation)


class IvoireRousse(Race):
    def __init__(self, dd1=Rousse, dd2=Ivoire, gestation=132, parcho="Grand Vitalité", generation=8):
        super().__init__("Ivoire & Rousse", dd1, dd2, gestation, parcho, generation)


class TurquoiseRousse(Race):
    def __init__(self, dd1=Rousse, dd2=Turquoise, gestation=132, parcho="Grand Vitalité", generation=8):
        super().__init__("Turquoise & Rousse", dd1, dd2, gestation, parcho, generation)


class AmandeIvoire(Race):
    def __init__(self, dd1=Amande, dd2=Ivoire, gestation=132, parcho="Grand chance", generation=8):
        super().__init__("Amande & Ivoire", dd1, dd2, gestation, parcho, generation)


class AmandeTurquoise(Race):
    def __init__(self, dd1=Amande, dd2=Turquoise, gestation=132, parcho="Grand Vitalité", generation=8):
        super().__init__("Amande & Turquoise", dd1, dd2, gestation, parcho, generation)


class DoreeIvoire(Race):
    def __init__(self, dd1=Doree, dd2=Ivoire, gestation=132, parcho="Grand sagesse", generation=8):
        super().__init__("Dorée & Ivoire", dd1, dd2, gestation, parcho, generation)


class DoreeTurquoise(Race):
    def __init__(self, dd1=Doree, dd2=Turquoise, gestation=132, parcho="Grand sagesse", generation=8):
        super().__init__("Dorée & Turquoise", dd1, dd2, gestation, parcho, generation)


class IndigoIvoire(Race):
    def __init__(self, dd1=Indigo, dd2=Ivoire, gestation=132, parcho="Grand chance", generation=8):
        super().__init__("Indigo & Ivoire", dd1, dd2, gestation, parcho, generation)


class IndigoTurquoise(Race):
    def __init__(self, dd1=Indigo, dd2=Turquoise, gestation=132, parcho="Grand chance", generation=8):
        super().__init__("Indigo & Turquoise", dd1, dd2, gestation, parcho, generation)


class EbeneIvoire(Race):
    def __init__(self, dd1=Ebene, dd2=Ivoire, gestation=132, parcho="Grand Agilité", generation=8):
        super().__init__("Ebène & Ivoire", dd1, dd2, gestation, parcho, generation)


class EbeneTurquoise(Race):
    def __init__(self, dd1=Ebene, dd2=Turquoise, gestation=132, parcho="Grand Agilité", generation=8):
        super().__init__("Ebène & Turquoise", dd1, dd2, gestation, parcho, generation)


class PourpreIvoire(Race):
    def __init__(self, dd1=Pourpre, dd2=Ivoire, gestation=132, parcho="Grand force", generation=8):
        super().__init__("Pourpre & Ivoire", dd1, dd2, gestation, parcho, generation)


class TurquoisePourpre(Race):
    def __init__(self, dd1=Pourpre, dd2=Turquoise, gestation=132, parcho="Grand force", generation=8):
        super().__init__("Turquoise & Pourpre", dd1, dd2, gestation, parcho, generation)


class IvoireOrchidee(Race):
    def __init__(self, dd1=Orchidee, dd2=Ivoire, gestation=132, parcho="Grand intelligence", generation=8):
        super().__init__("Ivoire & Orchidée", dd1, dd2, gestation, parcho, generation)


class TurquoiseOrchidee(Race):
    def __init__(self, dd1=Orchidee, dd2=Turquoise, gestation=132, parcho="Grand intelligence", generation=8):
        super().__init__("Turquoise & Orchidée", dd1, dd2, gestation, parcho, generation)


class IvoireTurquoise(Race):
    def __init__(self, dd1=Turquoise, dd2=Ivoire, gestation=132, parcho="Grand Agilité", generation=8):
        super().__init__("Ivoire & Turquoise", dd1, dd2, gestation, parcho, generation)


class Emeraude(Race):
    def __init__(self, dd1=PourpreIvoire, dd2=IvoireTurquoise, gestation=144, parcho="Puissant force", generation=9):
        super().__init__("Emeraude", dd1, dd2, gestation, parcho, generation)


class Prune(Race):
    def __init__(self, dd1=TurquoiseOrchidee, dd2=IvoireTurquoise, gestation=144, parcho="Puissant intelligence",
                 generation=9):
        super().__init__("Prune", dd1, dd2, gestation, parcho, generation)


class RousseEmeraude(Race):
    def __init__(self, dd1=Rousse, dd2=Emeraude, gestation=156, parcho="Puissant Vitalité", generation=10):
        super().__init__("Rousse & Emeraude", dd1, dd2, gestation, parcho, generation)


class RoussePrune(Race):
    def __init__(self, dd1=Rousse, dd2=Prune, gestation=156, parcho="Puissant Vitalité", generation=10):
        super().__init__("Rousse & Prune", dd1, dd2, gestation, parcho, generation)


class AmandeEmeraude(Race):
    def __init__(self, dd1=Amande, dd2=Emeraude, gestation=156, parcho="Puissant Vitalité", generation=10):
        super().__init__("Amande & Emeraude", dd1, dd2, gestation, parcho, generation)


class AmandePrune(Race):
    def __init__(self, dd1=Amande, dd2=Prune, gestation=156, parcho="Puissant Vitalité", generation=10):
        super().__init__("Amande & Prune", dd1, dd2, gestation, parcho, generation)


class DoreeEmeraude(Race):
    def __init__(self, dd1=Doree, dd2=Emeraude, gestation=156, parcho="Puissant sagesse", generation=10):
        super().__init__("Dorée & Emeraude", dd1, dd2, gestation, parcho, generation)


class DoreePrune(Race):
    def __init__(self, dd1=Doree, dd2=Prune, gestation=156, parcho="Puissant sagesse", generation=10):
        super().__init__("Dorée & Prune", dd1, dd2, gestation, parcho, generation)


class IndigoEmeraude(Race):
    def __init__(self, dd1=Indigo, dd2=Emeraude, gestation=156, parcho="Puissant chance", generation=10):
        super().__init__("Indigo & Emeraude", dd1, dd2, gestation, parcho, generation)


class IndigoPrune(Race):
    def __init__(self, dd1=Indigo, dd2=Prune, gestation=156, parcho="Puissant chance", generation=10):
        super().__init__("Indigo & Prune", dd1, dd2, gestation, parcho, generation)


class EbeneEmeraude(Race):
    def __init__(self, dd1=Ebene, dd2=Emeraude, gestation=156, parcho="Puissant force", generation=10):
        super().__init__("Ebène & Emeraude", dd1, dd2, gestation, parcho, generation)


class EbenePrune(Race):
    def __init__(self, dd1=Ebene, dd2=Prune, gestation=156, parcho="Puissant Agilité", generation=10):
        super().__init__("Ebène & Prune", dd1, dd2, gestation, parcho, generation)


class PourpreEmeraude(Race):
    def __init__(self, dd1=Pourpre, dd2=Emeraude, gestation=156, parcho="Puissant force", generation=10):
        super().__init__("Pourpre & Emeraude", dd1, dd2, gestation, parcho, generation)


class PourprePrune(Race):
    def __init__(self, dd1=Pourpre, dd2=Prune, gestation=156, parcho="Puissant force", generation=10):
        super().__init__("Pourpre & Prune", dd1, dd2, gestation, parcho, generation)


class OrchideeEmeraude(Race):
    def __init__(self, dd1=Orchidee, dd2=Emeraude, gestation=156, parcho="Puissant intelligence", generation=10):
        super().__init__("Orchidée & Emeraude", dd1, dd2, gestation, parcho, generation)


class OrchideePrune(Race):
    def __init__(self, dd1=Orchidee, dd2=Prune, gestation=156, parcho="Puissant intelligence", generation=10):
        super().__init__("Orchidée & Prune", dd1, dd2, gestation, parcho, generation)


class IvoireEmeraude(Race):
    def __init__(self, dd1=Ivoire, dd2=Emeraude, gestation=156, parcho="Puissant chance", generation=10):
        super().__init__("Ivoire & Emeraude", dd1, dd2, gestation, parcho, generation)


class IvoirePrune(Race):
    def __init__(self, dd1=Ivoire, dd2=Prune, gestation=156, parcho="Puissant chance", generation=10):
        super().__init__("Ivoire & Prune", dd1, dd2, gestation, parcho, generation)


class TurquoiseEmeraude(Race):
    def __init__(self, dd1=Turquoise, dd2=Emeraude, gestation=156, parcho="Puissant Agilité", generation=10):
        super().__init__("Turquoise & Emeraude", dd1, dd2, gestation, parcho, generation)


class TurquoisePrune(Race):
    def __init__(self, dd1=Turquoise, dd2=Prune, gestation=156, parcho="Puissant Agilité", generation=10):
        super().__init__("Turquoise & Prune", dd1, dd2, gestation, parcho, generation)


class EmeraudePrune(Race):
    def __init__(self, dd1=Emeraude, dd2=Prune, gestation=156, parcho="Puissant intelligence", generation=10):
        super().__init__("Emeraude & Prune", dd1, dd2, gestation, parcho, generation)


