<template>
  <div>
    <img id="avatar" src="../assets/avatar.jpg">

    <tab :titles="tabTitle" :firstSelected="tabTitle[0]"></tab>

    <video-item v-for="item in videos" :key="item.id"
      :id="item.id"
      :title="item.data.title"
      :description="item.data.description"
      :isPlayVideo="item.isPlayVideo"
      :coverImgUrl="item.data.cover.feed"
      :videoUrl="item.data.playUrl">
    </video-item> 
  </div>

</template>

<script>
import {Spinner, MessageBox} from 'mint-ui'
import VideoItem from '../components/video-item.vue'
import Tab from '../components/tab/tab.vue'

export default {
  components: {
    'mt-spinner': Spinner,
    'video-item': VideoItem,
    'tab': Tab
  },
  data () {
    return {
      tabTitle: ['最新', '最热'],
      videos: [],
      pageSize: 10,
      isAllLoaded: false,
      isLoading: false
    }
  },
  computed: {
    lastVideoOId () {
      return this.videos.length > 0 ? this.videos[this.videos.length - 1].oid : null
    }
  },
  methods: {
    fetchData () {
      if (this.isLoading) return
      this.isLoading = true
      this.$GET('http://localhost:5000/api/index', {
        pageSize: this.pageSize,
        lastOId: this.lastVideoOId
      }).then((data) => {
        this.isLoading = false
        if (data.respData.length > 0) {
          for (let item of data.respData) {
            item.isPlayVideo = false
          }
          this.videos.push(...data.respData)
        } else {
          this.isAllLoaded = true
        }
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
#avatar {
  width: 20%;
  max-width: 180px;
  border-radius: 50%;
  display: block;
  margin: 12px auto;
}
</style>
