<template>
  <div class="video-box columns is-multiline">
    <div v-for="item in videos" :key="item.id" class="column is-half-tablet">
      <div class="box">
        <div class="content">
          <div class="title">{{ item.title }}</div>
          <p>{{ item.description }}</p>
          <video :src="parseVideoUrl(item.video_url)" preload="metadata" controls webkit-playsinline></video>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'video-item',
  data () {
    return {
      videos: []
    }
  },
  methods: {
    parseVideoUrl (url) {
      return url.replace('https', 'http')
    }
  },
  created () {
    this.$GET('http://localhost:5000').then((data) => {
      this.videos = data.respData
    })
  }
}
</script>

<style scoped>
  .video-box {
    margin: auto;
  }
  .content>p {
    text-align: left;
  }
</style>
