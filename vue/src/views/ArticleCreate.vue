<template>
  <div class="container">
    <p class='h1 text-center mt-3 text-light'> 리뷰 작성하기 </p>
    <div class="form-group text-white h5">
      <label for="exampleFormControlInput1">제목</label>
      <input type="text" class="form-control" id="exampleFormControlInput1" v-model="createItem.title" placeholder="제목을 작성해주세요">
    </div>
    <br>

    <div class="form-group text-white h5">
      <label for="exampleFormControlTextarea1">내용 작성</label>
      <textarea class="form-control" id="exampleFormControlTextarea1" rows="10" v-model="createItem.content"></textarea>
    </div>
    <div class="form-group h5 text-white">
      <label for="exampleFormControlSelect1">평점</label>
      <select class="form-control w-25" id="exampleFormControlSelect1" v-model="createItem.Rank">
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
      <button @click="createArticle" class="btn btn1">글 생성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import Swal from 'sweetalert2'

export default {
  name: 'ArticleCreate',
  data() {
    return {
      createItem: {
        title: null,
        content: null,
        Rank: 1,
      }
    }
  },
  computed: {
    ...mapState(['movieDetail']),
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`http://127.0.0.1:8000/articles/${this.movieDetail.id}/create/`, this.createItem, config)
        .then(() => {
          this.$router.push('/movie_detail')
        })
        .catch(() => {
          if(!this.createItem.title) {
            Swal.fire({
              title: 'Error!',
              text: '제목을 입력해주세요',
              icon: 'error',
              confirmButtonText: '취소'
            })
          } else if(!this.createItem.content) {
            Swal.fire({
              title: 'Error!',
              text: '내용을 입력해주세요',
              icon: 'error',
              confirmButtonText: '취소'
            })
          }
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