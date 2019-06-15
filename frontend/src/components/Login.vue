<template>
  <div>
    <vue-webcam ref='webcam'></vue-webcam>
    <hr/>
    <img :src="photo" alt="" style="width:400px;height:300px" />
    <hr/>
    <button type="button" @click="take_photo">Take Photo</button>
  </div>
</template>

<script>
  import VueWebcam from 'vue-webcam';

    export default {
        name: "Login",
      components: { VueWebcam },
      data () {
        return {
          photo: null
        };
      },
      methods: {
        take_photo () {
          this.photo = this.$refs.webcam.getPhoto();
        }
      }
    }
</script>

<style scoped>

</style>
