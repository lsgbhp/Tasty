<template>
  <div class="video-list">
    <video-item v-for="item in videos" :key="item.id" @PlayVideo="subVideoPlay"
      :id="item.id"
      :title="item.data.title"
      :description="item.data.description"
      :pauseFlag="item.pauseFlag"
      :coverImgUrl="item.data.cover.feed"
      :videoUrl="item.data.playUrl">
    </video-item>
    <infinite-loading v-if="videos.length >= pageSize && isShow" :on-infinite="onInfinite" ref="infiniteLoading">
      <span slot="no-more">没有啦</span>
    </infinite-loading>
  </div>
</template>

<script>
import {Spinner, MessageBox} from 'mint-ui'
import InfiniteLoading from 'vue-infinite-loading'
import VideoItem from '../components/video-item.vue'

export default {
  components: {
    'mt-spinner': Spinner,
    'video-item': VideoItem,
    InfiniteLoading
  },
  props: {
    url: String,
    isShow: Boolean
  },
  data () {
    return {
      videos: [],
      isLoading: false,
      pageSize: 10
    }
  },
  computed: {
    lastVideoOId () {
      return this.videos.length > 0 ? this.videos[this.videos.length - 1].oid : null
    },
    lastVideoId () {
      return this.videos.length > 0 ? this.videos[this.videos.length - 1].id : null
    }
  },
  methods: {
    fetchData () {
      if (this.isLoading) return
      this.isLoading = true
      this.$GET(this.url, {
        pageSize: this.pageSize,
        lastOId: this.lastVideoOId,
        lastId: this.lastVideoId
      }).then((data) => {
        this.isLoading = false
        if (data.respData.length > 0) {
          for (let item of data.respData) {
            item.pauseFlag = true
          }
          this.videos.push(...data.respData)
          this.$refs.infiniteLoading && this.$refs.infiniteLoading.$emit('$InfiniteLoading:loaded')
        } else {
          this.$refs.infiniteLoading && this.$refs.infiniteLoading.$emit('$InfiniteLoading:complete')
        }
      }, (e) => {
        this.isLoading = false
        this.$refs.infiniteLoading && this.$refs.infiniteLoading.$emit('$InfiniteLoading:loaded')
        MessageBox('Error', e)
      })
    },
    onInfinite () {
      this.fetchData()
    },
    subVideoPlay (id) {
      for (let item of this.videos) {
        item.pauseFlag = (item.id !== id)
      }
    }
  },
  mounted () {
    this.fetchData()
  }
}
</script>

<style>

</style>
