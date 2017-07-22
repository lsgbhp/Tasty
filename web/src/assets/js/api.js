import axios from 'axios'

export default {
  install (Vue, options) {
    Vue.prototype.$GET = function (url) {
      return new Promise((resolve, reject) => {
        axios.get(url).then(function (response) {
          resolve(response.data)
        }).catch(e => {
          console.log(e)
          reject(e)
        })
      })
    }
  }
}
