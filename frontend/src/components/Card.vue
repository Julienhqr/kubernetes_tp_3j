<script>
export default {name : 'Card' }
</script>

<template>
  <h1>Card voici</h1>
  
  <img src="src/assets/naruto.jpg">
  <p>As Naruto was born, his home village of Konoha came under
    attack by a nine-tailed fox demon which was sealed in him at
    infancy to protect the people of the village. Due to this fact
    he became distrusted and resented by the people around him during his childhood.
    He, however, aspires to become the Hokage; a title given to the leader
    of Hidden Leaf Village, and as the most poorly performing student in his ninja school,
    he strives to prove his worth to his peers and fellow villagers.
    He is known for his often-used catchphrase "Dattebayo",
    and is connected to most other characters around him
    by either friendship or rivalry.</p>

  <p>
    <label for="name">Name</label>
    <input
        id="name"
        v-model="name"
        type="text"
        name="name"
    >
  </p>
  <button>Button</button>
</template>
