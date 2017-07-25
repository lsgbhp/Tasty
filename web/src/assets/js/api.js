import axios from 'axios'
import {Indicator} from 'mint-ui'

export default {
  install (Vue, options) {
    Vue.prototype.$GET = function (url, params) {
      return new Promise((resolve, reject) => {
        Indicator.open()
        axios.get(url, {params: params}).then(function (response) {
          Indicator.close()
          resolve(response.data)
        }).catch(e => {
          Indicator.close()
          console.log(e)
          reject(e)
        })
      })
    }
  }
}
