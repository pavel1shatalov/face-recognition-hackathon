<template>
  <WebCam
    ref="webcam"
    :deviceId="deviceId"
    width="auto"
    height="100%"
    @cameras="onCameras"
    @camera-change="onCameraChange"
    :isFrontCam="frontCam"
    :googleKey="googleKey" >
  </WebCam>
</template>

<script>
  import { WebCam } from 'vue-cam-vision'
  export default {
    name: "Login",
    data () {
      return {
        captures: [],
        imgReport: [],
        frontCam: false,
        webcam: null,
        img: null,
        camera: null,
        deviceId: null,
        devices: [],
        googleKey: config.googleVisionKey
      }
    },
    components: {
      WebCam
    }
  }
</script>

<style scoped>

</style>
