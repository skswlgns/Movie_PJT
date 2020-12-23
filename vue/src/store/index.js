import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'
import cookies from 'vue-cookies'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    flag: false,
    movieDetail: {},
    authToken: null,
    nowUser: {},
    articleDetail: {},
    isLoggedIn: false,
    commentDetail: {},
    flag_movie: false,
    flag_article: false,
    userInfo: null,
  },
  mutations: {
    goDetail(state, movie) {
      state.movieDetail = movie
      router.push({ name: 'MovieDetail' })
    },
    setToken(state, token) {
      state.authToken = token
      if (!state.authToken) {
        state.flag = false
      }
    },
    setNowUser(state, user) {
      state.nowUser = user
    },
    goArticle(state, article) {
      state.articleDetail = article
      router.push({ name: 'ArticleDetail' })
    },
    setMovie(state, movie) {
      state.movieDetail = movie
      
    },
    setLoggin(state, data) {
      state.isLoggedIn = data
    },
    setComment(state, data) {
      state.commentDetail = data
    },
    setFlag_movie(state) {
      state.flag_movie = false

      for(var key in state.movieDetail.like_users) {
        if(state.movieDetail.like_users[key] === state.nowUser.id ) {
          state.flag_movie = true
          console.log('gg')     
        }
    } 
    },
    setArticle(state, data) {
      state.articleDetail = data
    },
    setFlag_article(state) {
      state.flag_article = false

      for(var key in state.articleDetail.like_users) {
        if(state.articleDetail.like_users[key] === state.nowUser.id ) {
          state.flag_article = true
          console.log('gg')     
        }
    } 
    },
    setFlag(state) {
      state.flag = true
    },
    deleteFlag(state) {
      state.flag = false
    },
    userInfoChange(state, data) {
      state.userInfo = data
    },


  },
  actions: {
    getUser(context) {
      context.commit('setToken', cookies.get('auth-token'))
      context.commit('setLoggin', !!cookies.get('auth-token'))
      if (context.state.authToken) { 
        axios.post('http://127.0.0.1:8000/accounts/', null, {
          headers: { Authorization: `Token ${context.state.authToken}` }
        })
          .then(res => {
            context.commit('setNowUser', res.data)
          })
          .catch(err => console.log(err.response))
      }
    },
    heartPush(context) {
      axios.post(`http://127.0.0.1:8000/articles/${context.state.movieDetail.id}/heart/`, null, {
        headers: {
          Authorization: `Token ${context.state.authToken}`
        }
      })
        .then(res => { context.commit('setMovie', res.data)
          context.commit('setFlag_movie')
        })
        .catch(err => console.log(err.response))
    },
    commentGet(context) {
      axios.get(`http://127.0.0.1:8000/articles/${context.state.movieDetail.id}/${context.state.articleDetail.id}/index/`)
        .then(res => { context.commit('setComment', res.data) 
      } )
    },
    thumbUp(context) {
      axios.post(`http://127.0.0.1:8000/articles/${context.state.articleDetail.id}/thumb/`, null, {
        headers: {
          Authorization: `Token ${context.state.authToken}`
        }
      })
        .then(res => { context.commit('setArticle', res.data)
          context.commit('setFlag_article')
        })
        .catch(err => console.log(err.response))
    },
    sendUserInfo(context) {
      if (context.state.authToken) { 
        axios.post('http://127.0.0.1:8000/articles/get_userinfo/', null, {
          headers: { Authorization: `Token ${context.state.authToken}` }
        })
          .then(res => {
            context.commit('userInfoChange', res.data)
          })
          .catch(err => console.log(err.response))
      } else {
        context.commit('userInfoChange', null)
      }
    },
    
  },
  modules: {
  }
})
