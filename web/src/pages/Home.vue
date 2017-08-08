<template>
  <div>
    <div class="home-header">
      <div class="header-info">
        <img src="../assets/avatar.jpg">
        <span>深夜食堂</span>
      </div>
      <tab :titles="tabTitle" :firstSelected="tabTitle[0]" v-model="selectedTab"></tab>
    </div>
    <div class="home-container">
      <video-list url="http://localhost:5000/api/index"
        v-show="selectedTab === tabTitle[0]"
        :isShow="selectedTab === tabTitle[0]">
      </video-list>  
      <video-list url="http://localhost:5000/api/popular"
        v-show="selectedTab === tabTitle[1]" 
        :isShow="selectedTab === tabTitle[1]">
      </video-list> 
    </div>
  </div>
</template>

<script>
import Tab from '../components/tab.vue'
import VideoList from '../components/video-list.vue'

export default {
  components: {
    'tab': Tab,
    'video-list': VideoList
  },
  data () {
    return {
      tabTitle: ['最新', '最热'],
      selectedTab: '最新'
    }
  }
}
</script>

<style scoped>
.home-header {
  z-index: 1;
  background-color: white;
  position: fixed;
  width: 100%;
  max-width: 640px;
  height: 80px;
}
.home-header .header-info {
  display: flex;
  justify-content: center;
  box-sizing: border-box;
  padding-top: 10px;
  text-align: center;
  vertical-align: middle
}
.home-header .header-info img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 6px;
}
.home-header .header-info span {
  height: 30px;
  line-height: 30px;
  display: inline-block;
  font-size: 1.2rem;
  color: orange;
  margin-left: 6px;
}
.home-container {
  padding-top: 80px;
}
</style>
