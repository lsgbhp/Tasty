import Vue from 'vue'
import Router from 'vue-router'
import VideoList from '@/components/video-list.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',  // 这样URL中不会存在/#/的形式
  routes: [
    {
      path: '/',
      name: 'video-list',
      component: VideoList
    }
  ]
})
