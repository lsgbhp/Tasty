<template>
  <mt-loadmore :autoFill="false" :bottom-method="fetchData" @bottom-status-change="handleBottomChange" :bottom-all-loaded="isAllLoaded" ref="loadmore">
    <ul class="columns is-multiline">
      <li v-for="item in videos" :key="item.id" class="column is-12">
        <div class="content">
          <div class="title">{{ item.data.title }}</div>
          <p>{{ item.data.description }}</p>
          <div class="media">
            <div class="image" v-show="!item.isPlayVideo" @click="onClickImage(item.data.id)" :style="{'background-image': 'url(' + item.data.cover.feed + ')'}"></div>
            <video v-if="item.isPlayVideo" :src="item.data.playUrl" autoplay preload="metadata" :height="videoHeight" controls webkit-playsinline></video>
          </div>
        </div>
      </li>
    </ul>
    <!-- <div slot="bottom" class="mint-loadmore-bottom" v-if="!isAllLoaded">
      <span v-show="bottomStatus !== 'loading'" :class="{ 'rotate': bottomStatus === 'drop' }">↑</span>
      <span v-show="bottomStatus === 'loading'">
        <mt-spinner type="triple-bounce" v-show="isLoading"></mt-spinner> 
      </span>
    </div> -->
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
      pageSize: 10,
      isAllLoaded: false,
      isLoading: false,
      bottomStatus: ''
    }
  },
  computed: {
    lastVideoOId () {
      return this.videos.length > 0 ? this.videos[this.videos.length - 1].oid : null
    },
    videoHeight () {
      return (document.body.clientWidth - 20) * 0.5625
    }
  },
  methods: {
    fetchData () {
      if (this.isLoading) return
      this.isLoading = true
      this.$GET('http://192.168.102.10:5000', {
        pageSize: this.pageSize,
        lastOId: this.lastVideoOId
      }).then((data) => {
        this.isLoading = false
        if (data.respData.length > 0) {
          for (let item of data.respData) {
            item.isPlayVideo = false
          }
          this.videos.push(...data.respData)
          if (this.videos.length > data.respData.length) {
            this.$refs.loadmore.onBottomLoaded()
          }
        } else {
          this.isAllLoaded = true
        }
      }, (e) => {
        this.isLoading = false
        MessageBox('Error', e)
      })
    },
    handleBottomChange (status) {
      this.bottomStatus = status
    },
    onClickImage (id) {
      for (let item of this.videos) {
        item.isPlayVideo = item.id === id
      }
    }
  },
  mounted () {
    this.fetchData()
  }
}
</script>

<style scoped>
li {
  border-bottom: 1px solid gainsboro;
  margin: 10px;
}
li:last-child {
  border: none;
}
li .media {
  width: 100%;
  padding-top: 56.25%; /* 16:9 Aspect Ratio */
  position: relative;
}
.media .image {
  position: absolute;
  width: 100%;
  top: 0;
  bottom: 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.media video {
  position: absolute;
  width: 100%;
  top: 0;
  bottom: 0;
}
.mint-loadmore-bottom span {
  display: inline-block;
  transition: .2s linear;
  vertical-align: middle;
}
.mint-loadmore-bottom span.rotate {
  transform: rotate(180deg);
}
</style>
