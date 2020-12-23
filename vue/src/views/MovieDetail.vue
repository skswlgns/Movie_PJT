<template>
  <div>
  
    <div class="container mt-4" >
      <div class="text-center text-white" >
        <span class='h2 mr-2'>{{ movieDetail.title }}</span>
        <span v-if="movieDetail.Screening == '상영중'"  class="badge-info h3 ml-2">상영중</span>
      </div>
      <hr>
      <div class="d-flex justify-content-between bd-highlight mb-3 p-0 m-o">      
        <div class="mr-auto p-2 bd-highlight">
          <span class="h4 mr-2 text-light">관람객평점</span>
          <span v-if=" movieDetail.Audience_score === 10" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
          </span>
          <span v-else-if="8 <= movieDetail.Audience_score < 10" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="6 <= movieDetail.Audience_score < 8" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else-if="4 <= movieDetail.Audience_score < 6" class='h5 mr-2'>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <span v-else class="h5 mr-2">
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </span>
          <p class="badge badge-success"> {{ movieDetail.Audience_score }}</p>
          <br>
          <span class="text-light h5 mr-3">개요</span>
          <span class="text-monospace text-white">{{ movieDetail.summary }}</span>
          <span class="text-white-50"> | </span>
          <span class="text-monospace text-white">{{ movieDetail.country }}</span> 
          <span class="text-white-50"> | </span>
          <span class="text-monospace text-white">{{ movieDetail.Showtimes }}</span>
          <span class="text-white-50"> | </span>
          <span class="text-monospace text-white">{{ movieDetail.Release_date }}</span>
          <br>
          <span class="text-light h5 mr-3">감독</span>
          <span class="text-monospace text-white">{{ movieDetail.movie_director }}</span>
          <br>
          <span class="text-light h5 mr-3">배우</span>
          <span class="text-monospace text-white">{{ movieDetail.Actors }}</span>
          <br>
          <span class="text-light h5 mr-3">등급</span>
          <span class="text-monospace text-white">{{ movieDetail.Rating }}</span>
          <br>
          <span class="text-light h5 mr-3">관객수</span>
          <span class="text-monospace text-white">{{ movieDetail.attendance }}</span>
          <br>

          <div class="text-center text-light my-4 h5">
            줄거리
          </div>
          <p class="text-monospace text-white">{{ movieDetail.content }}</p>

          <div v-if="movieDetail.Screening === '상영중'" class='text-center'>
            <p class="h5 mt-5 mb-2 text-light ">예매하기</p>
            <a href="http://www.cgv.co.kr/ticket/"><button class="btn btn-light mr-3" style="color:red">CGV</button></a>
            <a href="https://www.lottecinema.co.kr/NLCHS/Ticketing"><button class="btn btn-danger mr-3" style="color:white">롯데시네마</button></a>
            <button class='mega btn'><a href="https://www.megabox.co.kr/booking" class='text-white text-decoration-none'>메가박스</a></button>
          </div>
          <div v-else class="text-center">
            <p class="h5 mt-5 mb-3 text-light ">스트리밍</p>
            <a href="https://www.youtube.com/feed/storefront?bp=ogUCKAI%3D" class='mr-4'><img src="https://image.flaticon.com/icons/svg/1384/1384060.svg" alt="" style="height: 54px"></a>
            <a href="https://www.netflix.com/kr/" class="mr-4"><img src="https://www.flaticon.com/premium-icon/icons/svg/2504/2504929.svg" alt="" style="height: 54px"></a>
            <a href="https://serieson.naver.com/movie/home.nhn"><img src="https://www.naver.com/favicon.ico" alt="" style="height: 54px"></a>
          </div>
          
          <div v-if="flag_movie" class="text-right mt-4 mr-4 heart text-white" @click="heartPush">
            <i class="fas fa-heart mt-1 fa-2x" style="color:red"></i>
            <span class="ml-2 h4">{{ movieDetail.heart }}</span>
          </div>
          <div v-else class="text-right mt-4 mr-4 heart text-white" @click="heartPush">
            <i class="far fa-heart mt-1 fa-2x" style="color:red"></i>
            <span class="ml-2 h4">{{ movieDetail.heart }}</span>
          </div>

        </div>      
        <img :src="movieDetail.imgUrl" alt="" class="w-50 bd-highlight">
      </div>
      <hr>

      <div class="text-right text-white">
        <button @click="$router.push('/article_create')" class="btn btn-secondary">리뷰 작성하기</button>
      </div>
      <MovieArticle/>

    </div>
</div>
</template>
 

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import MovieArticle from '@/components/MovieArticle.vue'

export default {
  name: 'MovieDetail',
  components: {
    MovieArticle,
  },
  data() {
    return {
    }
  },
  computed: {
    ...mapState(['movieDetail', 'nowUser', 'flag_movie']),
  },
  methods: {
    ...mapActions(['heartPush']),
    ...mapMutations(['setFlag_movie'])
  },
  mounted() {
    this.setFlag_movie()
  },


  

}
</script>

<style>
 .mega {
    background-color: purple;
  }
  .heart:hover {
    cursor: pointer;
  }

</style>