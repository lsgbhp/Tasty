import Vue from 'vue'
import Router from 'vue-router'
import VideoList from '@/components/video-list.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'video-list',
      component: VideoList
    }
  ]
})
