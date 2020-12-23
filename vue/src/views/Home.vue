<template>
  <div class="bg_img1" :class="{active: !kidsMovie, bg_img2: kidsMovie}">
    <div class="container text-center" v-if="!kidsMovie">
      <p class="h4 text-white mb-3">지금 기분이 어떠신가요?</p>
      <i class="far fa-sad-tear fa-3x emoji ml-3" @click="serachCry" style="color:tomato"></i>
      <i class="far fa-kiss-wink-heart fa-3x emoji ml-3" @click="serachMelloh" style="color:tomato"></i>
      <i class="far fa-grin-tongue-wink fa-3x emoji ml-3" @click="serachThriller" style="color:tomato"></i>
      <i class="far fa-angry fa-3x emoji ml-3" @click="serachAngry" style="color:tomato"></i>
    </div>
      <!-- Button trigger modal -->
      <div class="container text-center mt-3">
        <button type="button" v-if="flag && !kidsMovie" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
        색다른 추천을 원하시나요 ?
        </button>
      </div>
      

      <!-- Modal -->
      <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header bg-white">
              <h5 class="modal-title" id="exampleModalLabel">추천 받으실래요?</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <p>보러가겠습니다.</p>
            </div>
            <div class="modal-footer bg-white">
              <button @click="goForm" type="button" class="btn btn-primary" data-dismiss="modal">추천 받기</button>
              <button type="button" class="btn btn-secondary" data-dismiss="modal">닫기</button>
            </div>
          </div>
        </div>
      </div>
      <div class="container">
        <div class="mt-5" v-if="!kidsMovie && mmovie">
          <div class="container text-center mb-3">
            <span class='h4 text-monoscope text-white mt-3'>그렇다면 이러한 영화들은 어떠세요? </span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70"
            >
            <vueper-slide v-for="i in mmovie" :key="i.id"
            :image="i.imgUrl" class='under' @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="mt-5" v-if="!kidsMovie && suggest1Movie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-white '>회원님의 나이에 맞는 추천!!</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70"
            >
            <vueper-slide v-for="i in suggest1Movie" :key="i.id"
            :image="i.imgUrl" class='under' @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="mt-5" v-if="!kidsMovie && suggest2Movie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-white '>부모님의 향수를 느껴보세요!</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70"
            >
            <vueper-slide v-for="i in suggest2Movie" :key="i.id"
            :image="i.imgUrl" class='under' @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="mt-5" v-if="!kidsMovie && suggest3Movie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-white '>회원님이 좋아할 장르에요!</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70"
            >
            <vueper-slide v-for="i in suggest3Movie" :key="i.id"
            :image="i.imgUrl" class='under' @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="mt-5" v-if="!kidsMovie && suggest4Movie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-white '>당신이 좋아하는 국가의 영화!</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70"
            >
            <vueper-slide v-for="i in suggest4Movie" :key="i.id"
            :image="i.imgUrl" class='under' @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="mt-5" v-if="kidsMovie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-black '>키즈만을 위한 영화!</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70"
            >
            <vueper-slide v-for="i in kidsMovie" :key="i.id"
            :image="i.imgUrl" class='under' @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="mt-5" v-if="!kidsMovie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-white '>이 사이트의 추천영화!</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70"
            >
            <vueper-slide v-for="i in movie_heart" :key="i.id"
            :image="i.imgUrl" class='under' @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="mt-5" v-if="!kidsMovie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-white '>추천 상영영화</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70">
            <vueper-slide v-for="i in movie_now" :key="i.id"
            :image="i.imgUrl" @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="mt-5" v-if="!kidsMovie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-white '>관람객 평점 추천 영화</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70">
            <vueper-slide v-for="i in movie_score" :key="i.id"
            :image="i.imgUrl" @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
        <div class="my-5" v-if="!kidsMovie">
          <div class="text-center mb-3">
            <span class='h4 text-monoscope text-white '>관객 수 추천영화</span>
          </div>
          <vueper-slides
            class="no-shadow"
            :visible-slides="5"
            :slide-ratio="1 / 4"
            :gap="3"
            :bullets='false'
            :slideMultiple='true'
            :autoplay='true'
            :arrows-outside="false"
            :dragging-distance="70">
            <vueper-slide v-for="i in movie_people" :key="i.id"
            :image="i.imgUrl" @click.native="onClick(i.id)"/>
          </vueper-slides>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapMutations} from 'vuex'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

export default {
  name: 'Home',
  components: {
    VueperSlides, VueperSlide
  },
  data() {
    return {
      movie_people: {},
      movie_heart: {},
      movie_score: {},
      movie_now: {},
      cryMovie: {},
      mellohMovie: {},
      thrillerMovie: {},
      angryMovie: {},
      mmovie: null,
      suggest1Movie: null,
      suggest2Movie: null,
      suggest3Movie: null,
      suggest4Movie: null,
      kidsMovie: null,
      bg_img1: true,
      bg_img2: false,
    }
  },
  methods: {
    people() {
      axios.get('http://127.0.0.1:8000/articles/people/')
        .then(res => {
          this.movie_people = res.data
        })
    },
    heart() {
      axios.get('http://127.0.0.1:8000/articles/heart/')
        .then(res => {
          this.movie_heart = res.data
        })
    },
    score() {
      axios.get('http://127.0.0.1:8000/articles/score/')
        .then(res => {
          this.movie_score = res.data
        })
    },
    nowMovie() {
      axios.get('http://127.0.0.1:8000/articles/now/')
        .then(res => {
          this.movie_now = res.data
        })
    },
    serachCry() {
      axios.get('http://127.0.0.1:8000/articles/serach_cry/')
        .then(res => {
          this.cryMovie = res.data
          this.mmovie = res.data
          this.setFlag()
        })
    },
    serachMelloh() {
      axios.get('http://127.0.0.1:8000/articles/serach_melloh/')
        .then(res => {
          this.mellohMovie =res.data
          this.mmovie = res.data
          this.setFlag()
        })
    },
    serachThriller() {
      axios.get('http://127.0.0.1:8000/articles/serach_thriller/')
        .then(res => {
          this.thrillerMovie = res.data
          this.mmovie = res.data
          this.setFlag()
        })
    },
    serachAngry() {
      axios.get('http://127.0.0.1:8000/articles/serach_angry/')
        .then(res => {
          this.angryMovie = res.data
          this.mmovie = res.data
          this.setFlag()
        })
    },
    goForm() {
      if (this.isLoggedIn && !this.userInfo) { 
      this.$router.push('/userForm')}
      else if (this.isLoggedIn && this.userInfo) {
      this.suggest1()
      this.suggest2()
      this.suggest3()
      this.suggest4()
      this.goKids()
      this.$router.push('/')
      }
      else {this.$router.push('/login')}
    },
    suggest1() {
      if(this.userInfo) {
        axios.post('http://127.0.0.1:8000/articles/suggest1/', this.userInfo, { headers: { Authorization: `Token ${this.$cookies.get('auth-token')}`}})
        .then(res => {
          this.suggest1Movie = res.data
        })
        .catch(err => console.log(err.response))
      }
    },
    suggest2() {
      if(this.userInfo) {
        axios.post('http://127.0.0.1:8000/articles/suggest2/', this.userInfo, { headers: { Authorization: `Token ${this.$cookies.get('auth-token')}`}})
        .then(res => {
          this.suggest2Movie = res.data
        })
        .catch(err => console.log(err.response))
      }
    },
    suggest3() {
      if(this.userInfo) {
        axios.post('http://127.0.0.1:8000/articles/suggest3/', this.userInfo, { headers: { Authorization: `Token ${this.$cookies.get('auth-token')}`}})
        .then(res => {
          this.suggest3Movie = res.data
        })
        .catch(err => console.log(err.response))
      }
    },
    suggest4() {
      if(this.userInfo) {
        axios.post('http://127.0.0.1:8000/articles/suggest4/', this.userInfo, { headers: { Authorization: `Token ${this.$cookies.get('auth-token')}`}})
        .then(res => {
          this.suggest4Movie = res.data
        })
        .catch(err => console.log(err.response))
      }
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
    onClick(id) {
      // this.$router.push('/movie_detail', id)
      axios.get(`http://127.0.0.1:8000/articles/${id}/`)
        .then(res => {
          this.setMovie(res.data)
          this.$router.push('/movie_detail')
        })
    },
    ...mapMutations(['setFlag', 'setMovie']),

  },
  mounted() {
    this.people()
    this.heart()
    this.score()
    this.nowMovie()
    this.suggest1()
    this.suggest2()
    this.suggest3()
    this.suggest4()
    this.goKids()
  },
  updated() {
  },
  computed: {
    ...mapState(['flag', 'isLoggedIn', 'userInfo'])
  }

}
</script>

<style>

 .emoji:hover {
   cursor: pointer;
 }
  .bg_img1 {
        z-index: -1;
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