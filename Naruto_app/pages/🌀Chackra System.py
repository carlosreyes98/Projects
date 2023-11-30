import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥")

st.title("Chakra System")
st.image(Image.open("Naruto_app/images/naru.png"), use_column_width= True, clamp=True)
st.header("Origin:")
st.markdown("On Earth, humans didn't have chakra until Hamura and Hagoromo Ōtsutsuki were born with it, which was a result of their mother Kaguya eating their planet's chakra fruit from the God Tree. Hagoromo spread chakra to others through a practice called ninshū, intending to create peace by using the chakra to connect people's spiritual energy so that they would understand one another without even talking. However, the people did not use chakra in the way Hagoromo hoped, instead using it to connect their inner spiritual and physical energies. They kneaded their inner chakra to amplify and weaponise it, creating what is now known as ninjutsu.")
st.header("How works:")
st.markdown("Chakra is essential to even the most basic jutsu. Through various methods, the most common of which is hand seals, chakra can be controlled and manipulated to create an effect that would not be possible otherwise, such as walking on water, exhaling fire, or creating illusions. Chakra is ordinarily not visible to the unaided eye unless it is highly concentrated or manifested in large amounts.")
st.image(Image.open("Naruto_app/images/chackra molding.png"), use_column_width= True, clamp=True)
st.markdown("Chakra is created when two more primal energies, known collectively as one's stamina, are moulded together. Physical energy is collected from each of the body's cells and can be increased through training, stimulants, and exercise. Spiritual energy is derived from the mind's consciousness and can be increased through studying, meditation, and experience. These two energies becoming more powerful will in turn make the created chakra more powerful.")
st.header("Chackra Control:")
st.markdown("Because chakra takes time and a great deal of training to gradually build up, the key to its use is not actually having large amounts of chakra but instead being able to sufficiently control and conserve it. This is called Chakra Control. In order to have good chakra control, a ninja should only mould as much chakra as they need to perform a given ability. If they mould more chakra than is needed, the excess chakra is wasted and they will tire out faster from its loss. If they dont mould enough chakra, a technique will not be performed effectively, if at all, likely creating problems in a combat situation. Because chakra consists in part of spiritual energy, the user is more easily able to mould the correct amount of chakra by remaining calm and focused.")
st.markdown("When creating a ninjutsu, the two methods of manipulating chakra are referred to as shape transformation and nature transformation:")
st.markdown("-Shape transformation deals with controlling the form, movement, and potency of one's chakra, determining the size, range, and purpose of a technique.")
st.markdown("Nature transformation deals with the moulding and defining of the nature of one's chakra, altering its properties and characteristics for use in techniques. There is also the nature transformations of Yin and Yang, which deals with changing the ratio of spiritual and physical energies within chakra.")
st.markdown("These two methods can be implemented separately or together in order to create a technique, though ninja who can use both simultaneously are said to be rare.")
st.header("Jutsu's:")
st.markdown("(術, literally meaning: techniques/arts/skills) are the mystical arts that a ninja will utilise in battle. To use a jutsu, the ninja will need to use their chakra. To perform one, the ninja will bring out and release the two energies of chakra. By forming hand seals, the ninja is able to manifest the desired technique. Because of the extensive number of hand seals and different combinations, there are thousands of potential jutsu to be discovered.")
st.markdown("Ninshū is the religion and the peaceful precursor of modern ninjutsu created by Hagoromo Ōtsutsuki, the first one to understand and teach the mystery of chakra. The teachings of ninshū were meant to give people a better understanding of themselves, as well as others, and lead the world into an era of peace. Ninshū would eventually come to be known as ninjutsu, a more weaponised version of the Sage's teachings.")
st.header("The Basics:")
st.markdown("There are three basic types of techniques: ninjutsu, genjutsu and taijutsu. Subcategories exist, including fūinjutsu, juinjutsu and senjutsu. There are also kekkei genkai abilities which aren't techniques, but inherited abilities passed down through certain clans. Kekkei genkai can also be attributed to certain parts of the body, such as dōjutsu. Without proper control of their chakra, a ninja will produce ineffective or weakened technique which will lead to them running out of chakra early in a fight. To manipulate their chakra more easily, hand seals can be used. With these hand seals, users can control their chakra and technique with higher efficiency. Different techniques require different hand seals.")
st.markdown("-Ninjutsu: is one of the three main jutsu categories. Ninjutsu is the most nebulous of the three, and may most simply be described as anything that is not genjutsu or taijutsu. Most ninjutsu require chakra and hand seals, but this is not always the case since the mere usage of weaponry qualifies as ninjutsu.")
st.markdown("-Genjutsu: is one of the main jutsu categories which uses chakra. Unlike ninjutsu, the effects of genjutsu are not real, being only sensory illusions experienced by those who fall victim to it. According to the Second Mizukage, genjutsu falls under the broad category of Yin Release.")
st.markdown("-Taijutsu is a basic form of techniques and refers to any techniques involving the martial arts or the optimisation of natural human abilities. Taijutsu is executed by directly accessing the user's physical and mental energies, relying on the stamina and strength gained through training. It typically does not require chakra, though chakra may be used to enhance its techniques. Taijutsu generally requires no hand seals to perform, occasionally making use of certain stances or poses, and are far quicker to use than ninjutsu or genjutsu.")
st.header("Basic Nature Transformations:")
st.markdown("The Five Basic Natures are the five elemental chakra natures, which are the foundation of all elemental ninjutsu. They are so vital to the shinobi lifestyle that each of the Five Great Shinobi Countries is named after one of the five. Each element is naturally weaker than and stronger than another. Basically, if an elemental technique is put against another elemental technique of the same level, but of a stronger nature, then the technique with the superior nature will prevail. However, a technique with a weaker nature can overpower a technique with a stronger nature if the former is of a higher level. For example, fire can overpower a water technique if it is first strengthened by a wind technique.")
st.header("Afinity:")
st.markdown("In general, every person's chakra has an affinity towards one of the five basic nature transformations. Affinity can at times be genetic, or at least common to a particular family; most members of the Uchiha clan have an affinity towards the Fire nature. One's affinity can be identified using pieces of paper made from a special type of tree that is grown and fed with chakra")
st.header("Yin and Yang:")
st.markdown("Aside from the five elemental nature transformations, there are two nature transformations that are the source of all non-elemental techniques, such as the Shadow Imitation Technique, Multi-Size Technique, medical ninjutsu, genjutsu.There is Yin Release, based on the imagination and spiritual energy of a shinobi, and Yang Release, based on the vitality and physical energy of a shinobi. Together, they are used to perform Yin–Yang Release. The transformation of Yin and Yang has to do with altering the balance between spiritual and physical energy in chakra. As explained by Shikamaru Nara, Tayuya's spirit worms were forms of chakra that mostly consist of spiritual energy, thus they require stability and feed upon the physical energy they lack.")

st.image(Image.open("Naruto_app/images/chackra nature.png"), use_column_width= True, clamp=True)
st.header("Combined Nature Transformations:")
st.markdown("By using two or three basic nature transformations simultaneously, one can create a completely new elemental nature with unique properties that wouldn't exist on its own. However, doing this requires a kekkei genkai or, if three elements are used, a kekkei tōta.In the anime, it is further stated that those with the ability to combine the elemental nature transformations possess an affinity for the chakra natures they must simultaneously use.")
