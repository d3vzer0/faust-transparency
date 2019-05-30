import axios from 'axios'
import store from '@/store'

axios.defaults.baseURL = 'http://127.0.0.1:5000/api/v1/'

export default axios.create({
  baseURL: axios.defaults.baseURL,
  headers: {
    'Content-Type': 'application/json',
    Authorization: 'Bearer ' + store.getters['auth/access_token']
  }
})
