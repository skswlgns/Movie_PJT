<template>
  <div>
    <p class='h2 text-monospace text-light'>리뷰</p>
    <hr>
    <div class="mb-5">
      <div v-for="article in movieArticle" :key="article.id" class="mb-2">
        <div class="d-flex bd-highlight mb-3 text-light">
          <span @click="goArticle(article)" class="title h4 p-2 bd-highlight"> {{ article.title }} </span>
          <span class="text-secondary title my-auto p-2 bd-highlight"> {{ article.user.username }} </span> 
          <span class="text-secondary my-auto"> | </span>
          <span class="text-secondary my-auto">{{ article.created_at.slice(0,10) }} {{ article.created_at.slice(11,19) }} |  </span>
          <span class="text-secondary mr-auto my-auto">추천: {{ article.like_users.length }}</span>
          <span class="p-2 bd-highligh h5">{{ article.Rank }}</span>
          <div v-if="article.Rank === 10" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 9" class='p-2 bd-highligh h5'>             
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 8" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 7" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 6" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 5" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 4" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 3" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 2" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
          <div v-else-if="article.Rank === 1" class='p-2 bd-highligh h5'>            
            <i class="fas fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
            <i class="far fa-star" style="color:red"></i>
          </div>
        </div>
        <div class='text-monospace text-secondary container text-light' v-if="article.content.length >= 30">
          {{ article.content.slice(0,100) }}...
        </div>
        <div  class='text-monospace text-secondary container text-light' v-else>
          {{ article.content }}
        </div>
        <hr id="hr1">
      </div>
    </div> 

  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import axios from 'axios'


export default {
  name: 'MovieArticle',
  data() {
    return {
      movieArticle: null,
    }
  },
  computed: {
    ...mapState(['nowUser', 'movieDetail'])
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/articles/${this.movieDetail.id}/list/`)
      .then( res => this.movieArticle = res.data )
      .catch( err => console.log(err.response))
  },
  methods: {
    ...mapMutations(['goArticle'])
  }
}
</script>

<style>
  .title:hover {
    cursor: pointer;
    color: red;
  }
  hr#hr1
  {
    border-top: 1px dashed #8c8b8b;
    border-bottom: 1px dashed #fff;
  }
</style>