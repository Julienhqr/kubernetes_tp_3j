<script>
import '@coreui/coreui/dist/css/coreui.min.css'
import { CCard, CCardImage, CCardTitle, CCardText, CButton, CCardBody } from '@coreui/vue';

export default {
  name: 'Card',
  components: {
    CCard, CCardImage, CCardTitle, CCardText, CButton, CCardBody
  }
}
</script>

<template>
  <CCard style="width: 30rem">
    <CCardBody>
      <CCardImage orientation="top" src="https://thispersondoesnotexist.com/image"></CCardImage>
      <CCardText>As Naruto was born, his home village of Konoha came under
        attack by a nine-tailed fox demon which was sealed in him at
        infancy to protect the people of the village. Due to this fact
        he became distrusted and resented by the people around him during his childhood.
        He, however, aspires to become the Hokage; a title given to the leader
      </CCardText>

      <p>
        <input id="name" v-model="name" type="text" name="name" placeholder="name">
      </p>
      <CButton color="primary">Valider</CButton>
    </CCardBody>
  </CCard>
</template>

