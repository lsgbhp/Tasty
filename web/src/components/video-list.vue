<template>
  <mt-loadmore :bottom-method="fetchData" :bottom-all-loaded="isAllLoaded" ref="loadmore">
    <ul class="columns is-multiline">
      <li v-for="item in videos" :key="item.id" class="column is-half-tablet">
        <div class="box">
          <div class="content">
            <div class="title">{{ item.data.title }}</div>
            <p>{{ item.data.description }}</p>
            <video :src="item.data.playUrl" preload="none" controls webkit-playsinline></video>
          </div>
        </div>
      </li>
    </ul>
    <mt-spinner slot="bottom" class="spinner" type="triple-bounce" color="#26a2ff" v-if="!isAllLoaded" v-show="isLoading"></mt-spinner>
  </mt-loadmore>
</template>

<script>
import {Spinner, Loadmore, MessageBox} from 'mint-ui'

export default {
  name: 'video-item',
  components: {
    'mt-spinner': Spinner,
    'mt-loadmore': Loadmore
  },
  data () {
    return {
      videos: [],
      isAllLoaded: false,
      isLoading: false,
      pageSize: 20
    }
  },
  computed: {
    lastVideoId () {
      return this.videos.length > 0 ? this.videos[this.videos.length - 1].id : 'null'
    }
  },
  methods: {
    fetchData () {
      this.isLoading = true
      this.$GET('http://localhost:5000', {
        pageSize: this.pageSize,
        lastOId: this.lastVideoId
      }).then((data) => {
        this.isLoading = false
        this.videos = data.respData
      }, (e) => {
        this.isLoading = false
        MessageBox('Error', e)
      })
    }
  },
  mounted () {
    this.fetchData()
  }
}
</script>

<style scoped>
.spinner {
  text-align: center;
  display: block;
  margin-bottom: 20px;
}
</style>
