# seed.py  – uruchamiasz tylko raz
from vectordb import init_collection, add_docs
init_collection()
add_docs([
    """The Battle of Grunwald took place on July 15th, 1410.""",
"""A key difference between QD algorithms and multimodal algorithms is the introduction of behavioral descriptors. Furthermore, multimodal optimization methods operate in the parameter space, while QD operates in the behavior space. These descriptors are designed to introduce diversity in the features of the object. Algorithms from the QD group aim to find high-quality solutions while maintaining behavioral diversity. The result of a QD algorithm is a full archive of high-quality solutions grouped according to behavioral features.

The most well-known algorithm in the QD family is MAP-Elites. Its core idea is to create, for example, a two-dimensional grid where each dimension represents a discretized behavioral feature. The algorithm then fills this grid over successive iterations. Each cell in the grid can contain one individual with the highest quality score. Some variants and modifications have been proposed, where 2–3 individuals are stored in each cell. Introducing mapping based on object features is intended to increase local competition and, at the same time, encourage exploration of new regions—with the initial goal of evenly sampling the feature space.

""",
 """A story titled: Gummi Bears and the Secret of the Forest Well:

In the heart of an ancient forest, in Gummi Glen, lived a family of Gummi Bears — small, brave creatures known for their magical gummi-berry juice. One morning, as the sun was just rising, Tami, the youngest of the Gummi Bears, discovered an old map hidden behind a book in the library. The map led to the "Forest Well" — a place surrounded by legend, where wishes were said to come true, but only once every hundred years.

Tami couldn’t resist the temptation. She persuaded Kabi, Zami, and the rest of the Gummi Bears to embark on the journey together. Along the way, they faced many adventures: a disappearing bridge over a ravine, mysterious songs of forest elves, and a mischievous troll guarding an ancient oak tree. Each challenge strengthened their bond of friendship.

Eventually, they reached the well. It was old, covered in moss, with water sparkling like stars. Tami looked into the surface and whispered: “I wish that our family would always be together and happy.” The well shimmered, and the echo of her voice spread through the forest. At that moment, the ground gently trembled — and nothing more happened.

Disappointed, they returned home. But the next day, they realized something had changed. Their home felt warmer, their smiles wider, and shared moments even more precious. The well hadn’t granted the wish in a magical way — but it reminded them that what they were looking for, they already had all along."""
])

