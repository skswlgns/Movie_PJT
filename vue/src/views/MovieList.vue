<template>
  <div class="container">
    <div class="overflow-auto mt-5">
      <b-table
        id="my-table"
        :items="movieList"
        :per-page="perPage"
        :current-page="currentPage"
        small
        v-model="moiveAnother"
        v-show="ans"
      ></b-table>
      <div class="container">
        <b-card-group  columns >
          <b-card  v-for="movie in moiveAnother" :key="movie.pk"
                :img-src="movie.imgUrl"
                img-alt= "영화 포스터" 
                img-top >
            <h4 class="card-title text-center">
                {{movie.title}}
            </h4>

            <div class="mb-4">
              <span>
                <b-badge class="card-text float-left" variant="success">
                  {{ movie.Audience_score }}
                </b-badge>
              </span>
              <span class="card-text float-right">
                <i class="fas fa-heart mt-1" style="color:red"></i>{{ movie.heart }}
              </span>
            </div>

            <div slot="footer">
                <movieListModal :movie="movie" @goDetail="goDetail(movie)" />
            </div>
          </b-card>
        </b-card-group>
      </div>
      <div class="d-flex justify-content-center mt-5">
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
        ></b-pagination>
      </div>
    </div>
  <br>
  <br>
  <br>
  <br>
  <br>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import axios from 'axios'
import movieListModal from '@/components/movieListModal.vue'

const SERVER_URL = 'http://127.0.0.1:8000/articles/'

export default {
  name: "MovieList",
  components: {
    movieListModal,
  },
  data() {
    return {
      movieList: [],
      perPage: 9,
      currentPage: 1,
      moiveAnother: [],
      ans: false,
    }
  },
  mounted() {
      axios.get(SERVER_URL)
        .then(res => {
          this.movieList = res.data
        })
        .catch(err => {console.log(err.response)})
    },
  computed: {
    rows() {
      return this.movieList.length
    },
  },
  methods: {
    ...mapMutations(['goDetail'])
  }
}
</script>

<style>
  #bg-img {
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
</style>