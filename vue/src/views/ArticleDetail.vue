<template>
  <div class="container">
    <hr>
    <div class="text-center">
      <span class="h2 text-monospace text-light">{{ articleDetail.title }}</span>
    </div>
    <hr>
    <div class="d-flex bd-highlight mb-3">
      <span class="h5 text-monospace mr-auto p-2 bd-highlight text-white">작성: {{ articleDetail.user.username }}</span>      
      <div v-if="articleDetail.Rank === 10" class='p-2 bd-highlight text-white'>
        나의 평점:        
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 9" class='p-2 bd-highligh h5 text-white'>  
          나의 평점:            
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 8" class='p-2 bd-highligh h5 text-white'> 
          나의 평점:            
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 7" class='p-2 bd-highligh h5 text-white'>  
          나의 평점:           
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 6" class='p-2 bd-highligh h5 text-white'> 
          나의 평점:           
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 5" class='p-2 bd-highligh h5 text-white'>  
          나의 평점:           
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 4" class='p-2 bd-highligh h5 text-white'>   
          나의 평점:          
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 3" class='p-2 bd-highligh h5 text-white'>   
          나의 평점:          
          <i class="fas fa-star" style="color:red"></i>
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 2" class='p-2 bd-highligh h5 text-white'>       
          나의 평점:      
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>
        <div v-else-if="articleDetail.Rank === 1" class='p-2 bd-highligh h5 text-white'>    
          나의 평점:        
          <i class="fas fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
          <i class="far fa-star" style="color:red"></i>
        </div>  
    </div>
    
    <div class="mb-5 container">
      <p class="h6 text-monospace text-white" style="white-space:pre-line;">{{ articleDetail.content }}</p>
    </div>
    <div class="text-right text-white">
          <p>작성일: {{ articleDetail.created_at.slice(0,10) }} {{ articleDetail.created_at.slice(11,19) }}</p>
        </div>
    <div class="text-right">
      <button v-if="nowUser.id === articleDetail.user.id" @click="$router.push('/article_update')" class="btn btn1">수정</button>
      <button v-if="nowUser.id === articleDetail.user.id" @click="articleDelete" class='ml-2 btn btn1'>삭제</button>
    </div>
    <div class="mx-auto">
      <div class="mx-auto circle">
        <div v-if="flag_article" class="mt-4 mr-4 thumb" @click="thumbUp">
            <i class="fas fa-thumbs-up fa-2x" style="color:blue"></i>
            <span class="ml-2 h4">{{ articleDetail.like_users.length }}</span>
        </div>
        <div v-else class="mt-4 mr-4 thumb" @click="thumbUp">
          <i class="far fa-thumbs-up mt-1 fa-2x" style="color:blue"></i>
          <span class="ml-2 h4">{{ articleDetail.like_users.length }}</span>
        </div>
    </div>
    </div>
    <CommentList />
  </div>
</template>
<script>
import CommentList from '@/components/CommentList.vue'
import { mapState, mapMutations, mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'ArticleDetail',
  components: {
    CommentList,
  },

  computed: {
    ...mapState(['articleDetail', 'movieDetail', 'nowUser', 'flag_article']),
  },
  methods: {
    ...mapMutations(['goDetail' ,'setFlag_article', 'setArticle']),
    ...mapActions(['thumbUp']),

    articleDelete() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`http://127.0.0.1:8000/articles/${this.movieDetail.id}/${this.articleDetail.id}/delete/`, null, config)
        .then(() => {
          this.goDetail(this.movieDetail)
        })

    }
  },
  mounted() {
    this.setFlag_article()
    this.setArticle(this.articleDetail)
  },

}
</script>

<style>
  .btn1 {
    background-color: LawnGreen;
    color: whitesmoke;
  }
  .thumb:hover {
    cursor: pointer;
  }

  .circle {
    width: 100px;
    height: 100px;
    line-height: 100px;
    border-radius: 50%;
    background:MintCream;
    text-align: center;
  }
</style>