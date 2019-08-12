import random
from ..base_item import BaseItem


class BlackHole(BaseItem):
    pass


class GalacticLife(BaseItem):
    pass


class Ghost(BaseItem):
    pass


class SpaceMonster(BaseItem):
    pass


class Helium(BaseItem):
    pass


class Hydrogen(BaseItem):
    pass


class Carbon(BaseItem):
    pass


class Water(BaseItem):
    pass


class Ammonia(BaseItem):
    pass


class Nitrogen(BaseItem):
    pass


class Iron(BaseItem):
    pass


class Sulfur(BaseItem):
    pass


class Oxygen(BaseItem):
    pass


class Orbital(BaseItem):
    pass


class AsteroidBelt(Orbital):
    pass


class DysonSurface(Orbital):
    pass


class Rock(BaseItem):
    pass


class Ice(BaseItem):
    pass


class VisitorCity(BaseItem):
    pass


class VisitorInstallation(BaseItem):
    pass


class Ocean(BaseItem):
    pass


class Continent(BaseItem):
    pass


class AncientContinent(BaseItem):
    pass


class MedievalContinent(BaseItem):
    pass


class Sky(BaseItem):
    pass


class TerraformedSky(BaseItem):
    pass


class FutureContinent(BaseItem):
    pass


class FutureSky(BaseItem):
    pass


class PlanetCore(BaseItem):
    pass


class BasePlanet(Orbital):
    composition = PlanetCore,

    @property
    def planet_core(self):
        return next(self.get_items(PlanetCore), None)


class GasGiant(BasePlanet):
    pass


class Moon(BasePlanet):
    GENERATOR_DATA = Ghost.set_probability(0.1),
    TYPES = ("young", "old", "large", "small", "pale", "white", "dark", "black", "old")

    def __init__(self, name=None):
        name = name or "{} moon".format(random.choice(self.TYPES))
        super().__init__(name=name)

    @classmethod
    def get_factories(cls):
        yield from cls.GENERATOR_DATA
        yield Rock
        yield cls.composition

    @property
    def ghost(self):
        return list(self.get_items(Ghost))

    @property
    def rock(self):
        return next(self.get_items(Ice), None)


class TerraformedMoon(Moon):
    pass


class FutureMoon(Moon):
    pass


class PlanetComposition(BasePlanet):
    composition = (
        PlanetCore,
        Moon.set_probability(40),
        Moon.set_probability(20),
        Moon.set_probability(10),
    )

    def __init__(self, name=None):
        super().__init__(name=name or 'planet')

    @property
    def moons(self):
        return list(self.get_items(Moon))


class TelluricPlanet(PlanetComposition):
    def __init__(self, name=None):
        super().__init__(name=name or 'telluric planet')


class InhabitedPlanet(TelluricPlanet):
    continent_factories = Continent.set_count(2, 7),
    ocean_factory = Ocean.set_count(1, 7)
    sky_factory = Sky
    moon_factory = None

    @classmethod
    def get_factories(cls):
        yield from cls.continent_factories
        yield cls.ocean_factory
        yield cls.sky_factory
        if cls.moon_factory is not None:
            yield cls.moon_factory
        yield from cls.composition

    @property
    def continents(self):
        return list(self.get_items(Continent))

    @property
    def oceans(self):
        return list(self.get_items(Ocean))

    @property
    def sky(self):
        return next(self.get_items(Sky), None)


class AncientPlanet(InhabitedPlanet):
    continent_factories = AncientContinent.set_count(2, 7),


class MedievalPlanet(InhabitedPlanet):
    continent_factories = (
        MedievalContinent.set_count(2, 4),
        AncientContinent.set_count(0, 3),
    )


class TerraformedPlanet(InhabitedPlanet):
    sky_factory = TerraformedSky
    moon_factory = TerraformedMoon.set_probability(30)


class FuturePlanet(InhabitedPlanet):
    continent_factories = FutureContinent.set_count(2, 7),
    sky_factory = FutureSky
    moon_factory = FutureMoon.set_probability(30)


class UninhabitedPlanet(TelluricPlanet):
    @classmethod
    def get_factories(cls):
        yield from cls.GENERATOR_DATA
        yield Rock
        yield Ice.set_probability(50)
        yield cls.composition

    @property
    def ice(self):
        return next(self.get_items(Ice), None)

    @property
    def life(self):
        return list(self.get_items(GalacticLife))

    @property
    def rock(self):
        return next(self.get_items(Ice), None)

    @property
    def cities(self):
        return list(self.get_items(VisitorCity))

    @property
    def installations(self):
        return list(self.get_items(VisitorInstallation))


class VisitorPlanet(UninhabitedPlanet):
    GENERATOR_DATA = (
        VisitorCity.set_count(1, 8),
        VisitorInstallation.set_count(2, 6),
        GalacticLife,
    )


class BarrenPlanet(UninhabitedPlanet):
    GENERATOR_DATA = GalacticLife.set_probability(10),


class Star(BaseItem):
    GENERATOR_DATA = (
        Ghost.set_probability(0.1),
        SpaceMonster.set_probability(0.2),
        Hydrogen,
        Helium,
    )
    TYPES = (
        "white", "faint", "yellow", "red", "blue", "green", "purple", "bright", "double", "twin", "triple", "old",
        "young", "dying", "small", "giant", "large", "pale", "dark", "hell", "horrific", "twisted", "spectral"
    )

    def __init__(self, name=None):
        name = name or "{} star".format(random.choice(self.TYPES))
        super().__init__(name=name)


class StarSystem(BaseItem):
    STARS_GENERATOR_DATA = (
        Star,
        Star.set_probability(3),
    )
    PLANET_GENERATOR_DATA = (
        VisitorPlanet.set_probability(3),
        FuturePlanet.set_probability(10),
        FuturePlanet.set_probability(10),
        TerraformedPlanet.set_probability(50),
        TerraformedPlanet.set_probability(20),
        TerraformedPlanet.set_probability(10),
        MedievalPlanet.set_probability(30),
        MedievalPlanet.set_probability(20),
        AncientPlanet.set_probability(50),
        AncientPlanet.set_probability(30),
        AncientPlanet.set_probability(10),
        BarrenPlanet.set_probability(60),
        BarrenPlanet.set_probability(40),
        BarrenPlanet.set_probability(20),
        GasGiant.set_probability(60),
        GasGiant.set_probability(40),
        GasGiant.set_probability(20),
        GasGiant.set_probability(10),
        AsteroidBelt.set_count(0, 2),
    )

    @classmethod
    def get_factories(cls):
        yield from cls.STARS_GENERATOR_DATA
        yield from cls.PLANET_GENERATOR_DATA

    @property
    def stars(self):
        return list(self.get_items(Star))

    @property
    def orbital(self):
        return list(self.get_items(Orbital))


class DysonSphere(StarSystem):
    PLANET_GENERATOR_DATA = (
        DysonSurface,
        FuturePlanet.set_count(1, 8),
        BarrenPlanet.set_probability(60),
        BarrenPlanet.set_probability(40),
        BarrenPlanet.set_probability(20),
        GasGiant.set_probability(60),
        GasGiant.set_probability(40),
        GasGiant.set_probability(20),
        GasGiant.set_probability(10),
        AsteroidBelt.set_count(0, 2),
    )

    @property
    def surface(self):
        return next(self.get_items(DysonSurface), None)


class InterstellarCloud(BaseItem):
    GENERATOR_DATA = (
        Helium,
        Hydrogen,
        Carbon.set_probability(80),
        Water.set_probability(5),
        Ammonia.set_probability(5),
        Nitrogen.set_probability(5),
        Iron.set_probability(5),
        Sulfur.set_probability(5),
        Oxygen.set_probability(5),
    )
    TYPES = (
        "a bright pink", "a faint", "a fading", "a pale", "a fluo", "a glowing", "a green", "a bright green",
        "a dark brown", "a brooding", "a magenta", "a bright red", "a dark red", "a blueish", "a deep blue",
        "a turquoise", "a teal", "a golden", "a multicolored", "a silver", "a dramatic", "a luminous",
        "a colossal", "a purple", "a gold-trimmed", "an opaline", "a silvery", "a shimmering"
    )

    def __init__(self, name=None):
        name = name or "{} interstellar cloud".format(random.choice(self.TYPES))
        super().__init__(name=name)


class Nebula(BaseItem):
    GENERATOR_DATA = (
        GalacticLife.set_probability(15),
        Star.set_probability(2),
        Star.set_probability(2),
        Star.set_probability(2),
        InterstellarCloud.set_count(1, 6),
    )


class GalaxyCenter(BaseItem):
    CHILD_DATA = (
        BlackHole,
        GalacticLife.set_probability(10),
        DysonSphere.set_probability(4),
        DysonSphere.set_probability(2),
        StarSystem.set_count(20, 50),
        Nebula.set_count(0, 12),
    )

    def __init__(self, name=None):
        super().__init__(name=name or 'galactic centre')


class GalaxyArm(BaseItem):
    GENERATOR_DATA = (
        GalacticLife.set_probability(5),
        DysonSphere.set_probability(4),
        DysonSphere.set_probability(2),
        StarSystem.set_count(20, 50),
        Nebula.set_count(0, 12),
        BlackHole.set_probability(20),
        BlackHole.set_probability(20),
    )

    def __init__(self, name=None):
        super().__init__(name=name or 'arm')


class Galaxy(BaseItem):
    GENERATOR_DATA = (
        GalaxyCenter,
        GalaxyArm.set_count(2, 6)
    )

    @property
    def center(self):
        return next(self.get_items(GalaxyCenter), None)

    @property
    def arms(self):
        return list(self.get_items(GalaxyArm))


class Supercluster(BaseItem):
    GENERATOR_DATA = Galaxy.set_count(10, 30),

    def __init__(self, name=None):
        super().__init__(name=name or 'galactic supercluster')

    @property
    def galaxies(self):
        return list(self.get_items(Galaxy))


class Universe(BaseItem):
    GENERATOR_DATA = Supercluster.set_count(10, 30),

    @property
    def superclusters(self):
        return list(self.get_items(Supercluster))
