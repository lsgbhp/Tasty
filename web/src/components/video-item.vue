<template>
  <div class="video-item">
    <p class="title">{{ title }}</p>
    <div class="media">
      <div class="image" v-show="!isPlayVideo" @click="playVideo(id)" :style="{'background-image': 'url(' + coverImgUrl + ')'}"></div>
      <video ref="video" v-if="isPlayVideo" @play="$emit('PlayVideo', id)" :src="videoUrl" autoplay preload="metadata" :height="videoHeight" controls webkit-playsinline></video>
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
    pauseFlag: Boolean,
    coverImgUrl: String,
    videoUrl: String
  },
  data () {
    return {
      isPlayVideo: false
    }
  },
  watch: {
    pauseFlag (val, oldVal) {
      if (val && !oldVal) {
        this.$refs.video.pause()
      }
    }
  },
  computed: {
    videoHeight () {
      return (document.body.clientWidth > 640 ? 640 : document.body.clientWidth) * 0.5625
    }
  },
  methods: {
    playVideo (id) {
      this.$emit('PlayVideo', id)
      this.isPlayVideo = true
    }
  }
}
</script>

<style>
.video-item {
  border-bottom: 1px solid lavender;
  padding: 8px 0;
}
.video-item:last-child {
  border: none;
}
.video-item p {
  margin: 10px;
  font-size: 0.8rem;
}
.video-item .title {
  text-align: center;
  font-size: 1.2rem;
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
