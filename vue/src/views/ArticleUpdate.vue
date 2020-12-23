<template>
  <div class="container">
    <p class='h1 text-center mt-3'>리뷰 수정</p>
    <div class="form-group">
      <label for="exampleFormControlInput1">제목</label>
      <input type="text" class="form-control" id="exampleFormControlInput1" v-model="articleDetail.title">
    </div>
    <div class="form-group">
      <label for="exampleFormControlTextarea1">내용 작성</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="10" v-model="articleDetail.content"></textarea>
    </div>
    <div class="form-group">
      <label for="exampleFormControlSelect1">평정</label>
      <select class="form-control w-25" id="exampleFormControlSelect1" v-model="articleDetail.Rank">
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
      <option>6</option>
      <option>7</option>
      <option>8</option>
      <option>9</option>
      <option>10</option>
      </select>
    </div>

    <div class="text-right">
      <button @click="updateArticle" class='btn btn1'>글 수정</button>    
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'ArticleUpdate',
  data() {
    return {
      updateItem: {
        title: null,
        content: null,
        Rank: null,
      }
    }
  },
  computed: {
    ...mapState(['articleDetail', 'movieDetail'])
  },
  methods: {
    updateArticle() {
      this.updateItem.title = this.articleDetail.title
      this.updateItem.content = this.articleDetail.content
      this.updateItem.Rank = this.articleDetail.Rank
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`http://127.0.0.1:8000/articles/${this.movieDetail.id}/${this.articleDetail.id}/update/`, this.updateItem, config)
        .then((res) => {
          console.log(res.data)
          this.$router.push('/article_detail')
        })
        .catch(err => {
          console.log(err.response)
        })


    },
  },
}
</script>

<style>
  .btn1 {
    background-color: LawnGreen;
    color: whitesmoke;
  }
</style>