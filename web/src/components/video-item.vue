<template>
  <div class="video-item">
    <p class="title">{{ title }}</p>
    <div class="media">
      <div class="image" v-show="!isPlayVideo" :style="{'background-image': 'url(' + coverImgUrl + ')'}"></div>
      <video v-if="isPlayVideo" :src="videoUrl" autoplay preload="metadata" :height="videoHeight" controls webkit-playsinline></video>
    </div>
    <p>{{ description }}</p>
  </div>
</template>

<script>
export default {
  name: 'video-item',
  props: {
    id: Number,
    title: String,
    description: String,
    isPlayVideo: Boolean,
    coverImgUrl: String,
    videoUrl: String
  },
  computed: {
    videoHeight () {
      return (document.body.clientWidth - 20) * 0.5625
    }
  }
}
</script>

<style>
.video-item {
  border-bottom: 1px solid gainsboro;
  padding: 12px 0;
}
.video-item:last-child {
  border: none;
}
.video-item p {
  margin: 10px;
}
.video-item .title {
  text-align: center;
  font-size: 1.3rem;
}
.video-item .media {
  width: 100%;
  padding-top: 56.25%; /* 16:9 Aspect Ratio */
  position: relative;
}
.video-item .media .image {
  position: absolute;
  width: 100%;
  top: 0;
  bottom: 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.video-item .media video {
  position: absolute;
  width: 100%;
  top: 0;
  bottom: 0;
}
</style>
