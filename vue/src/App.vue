<template>
  <div class="bg_img1" :class="{active: !kidsMovie, bg_img2: kidsMovie}">
    <div class="d-flex bd-highlight mb-3">
      <div class="mr-auto p-2 bd-highlight h3 text-monospace"><router-link to='/' class="text-danger text-decoration-none ">WatchFlix</router-link></div>
      <div class="p-2 bd-highlight h4 text-monospace"><router-link to="/" class="text-monospace text-white text-decoration-none">HOME</router-link></div>
      <div class="p-2 bd-highlight h4 text-monospace"><router-link to="/movie" class="text-monospace text-white text-decoration-none">MOVIE</router-link></div>
      <div class="p-2 bd-highlight h4 text-monospace"><router-link to="/login" class="text-monospace text-white text-decoration-none" v-if="!isLoggedIn">LOGIN</router-link></div>
      <div class="p-2 bd-highlight h4 text-monospace"><router-link to="/signup" class="text-monospace text-white text-decoration-none" v-if="!isLoggedIn">SIGNUP</router-link></div>
      <div class="p-2 bd-highlight h4 text-monospace"><router-link to="/userUpdate" class="text-monospace text-white text-decoration-none" v-if="isLoggedIn">MYPAGE</router-link></div>
      <div class="p-2 bd-highlight h4 text-monospace"><router-link to="/logout" class="text-monospace text-white text-decoration-none" v-if="isLoggedIn" @click.native="onLogout">LOGOUT</router-link></div>
    </div>
    <router-view @login="onLogin" @signup="onSignup" />
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'
import { mapState, mapMutations, mapActions } from 'vuex'

const SERVER_URL = 'http://127.0.0.1:8000/'


export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      movieDetail: {},
      bg_img1: true,
      bg_img2: false, 
      kidsMovie: null,
    }
  },
  methods: {
    onLogin(loginData) {
      axios.post(SERVER_URL + 'rest-auth/login/', loginData)
        .then(res => {
          this.$cookies.set('auth-token', res.data.key)
          this.isLoggedIn = true
          this.sendUserInfo()
          this.goKids()
          this.$router.go()
          
        })
        .catch(() => {
          if(!loginData.username) {
            Swal.fire({
              title: 'Error!',
              text: '아이디를 입력해주세요',
              icon: 'error',
              confirmButtonText: '취소'
            })
          } else if(!loginData.password) {
            Swal.fire({
              title: 'Error!',
              text: '비밀번호를 입력해주세요',
              icon: 'error',
              confirmButtonText: '취소'
            })
          } else {
            Swal.fire({
              title: 'Error!',
              text: '아이디와 비밀번호를 확인해주세요.',
              icon: 'error',
              confirmButtonText: '취소'
            })
          }
        })
    },
    onLogout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(SERVER_URL + 'rest-auth/logout/', null, config)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.deleteFlag()
          this.$router.push('/')
        })
        .catch(err => console.log(err.response))

    },
    onSignup(signupData) {
      axios.post(SERVER_URL + 'rest-auth/signup/', signupData)
        .then(res => {
          this.$cookies.set('auth-token', res.data.key)
          this.isLoggedIn = true
          this.$router.push('/')
          Swal.fire(
            '회원가입 축합니다!',
            '다양한 영화를 추천받아 보세요!',
            'success'
          )
        })
        .catch((err) => {
          if(err.response.data.username) {
            Swal.fire({
              title: 'Error!',
              text: err.response.data.username,
              icon: 'error',
              confirmButtonText: '취소'
            })
          } else if(err.response.data.password1) {
            Swal.fire({
              title: 'Error!',
              text: err.response.data.password1,
              icon: 'error',
              confirmButtonText: '취소'
            })
          } else {
            Swal.fire({
              title: 'Error!',
              text: '비밀번호가 일치하지 않습니다!',
              icon: 'error',
              confirmButtonText: '취소'
            })
          }
        })
    },
    goKids() {
      if(this.userInfo && this.userInfo.kids && this.isLoggedIn) {
        axios.post('http://127.0.0.1:8000/articles/gokids/', this.userInfo, { headers: { Authorization: `Token ${this.$cookies.get('auth-token')}`}})
        .then(res => {
          this.kidsMovie = res.data
        })
        .catch(err => console.log(err.response))
      }
    },
    ...mapActions(['getUser', 'sendUserInfo']),
    ...mapMutations(['deleteFlag'])
  },
  mounted() {
    if (this.$cookies.isKey('auth-token'))
    {this.isLoggedIn = true
     }
    this.getUser()
    this.sendUserInfo()
    this.goKids()
  },
  updated() {
    this.getUser()
    this.sendUserInfo()
  },
  computed: {
    ...mapState(['userInfo'])
  },


}
</script>
<style>
  .bg_img1 {
          z-index: -1024;
          position: fixed;
          background-image: url('https://nobutlisten.files.wordpress.com/2018/01/ironman_poster2.jpg');
          background-size: cover;
          height: 100vh;
          width: 100vw;
          background-color: black;
          background-attachment: fixed;
          overflow-y: scroll;
        }
  .bg_img2 {
      z-index: -1;
      position: fixed;
      background-image: url('https://occ-0-4342-988.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABa7WUDXV4wpLt8GpMqiC6iCivZQNFeVJfYRVSi1c-bt8aiNuX7oFqelKtG76iA9B1WoJmU0_6Y7hHZA7Oi2YDoktyoOl.jpg?r=490');
      background-size: cover;
      height: 100vh;
      width: 100vw;
      background-color: black;
      background-attachment: fixed;
      overflow-y: scroll;
      
    }
</style>
