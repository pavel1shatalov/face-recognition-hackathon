<template>
    
</template>

<script>
    export default {
        name: "Login",
      data() {
        return {
          video: {},
          canvas: {},
          captures: []
        }
      },
      mounted() {
        this.video = this.$refs.video;
        if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
            this.video.src = window.URL.createObjectURL(stream);
            this.video.play();
          });
        }
      },
      methods: {
        capture() {
          this.canvas = this.$refs.canvas;
          var context = this.canvas.getContext("2d").drawImage(this.video, 0, 0, 640, 480);
          this.captures.push(canvas.toDataURL("image/png"));
        }
      }
    }
</script>

<style scoped>
  body: {
    background-color: #F0F0F0;
  }
  #app {
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  #video {
    background-color: #000000;
  }
  #canvas {
    display: none;
  }
  li {
    display: inline;
    padding: 5px;
  }
</style>
