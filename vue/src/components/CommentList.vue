<template>
  <div class="container">
    <p class="h2 mt-2 text-light">댓글 {{ commentDetail.length }}</p>
    <div class="mb-3">
      <input v-if="isLoggedIn" type="text" class="w-50" v-model="createItem.content" @keypress.enter="createComment">
      <button v-if="isLoggedIn" @click="createComment" class="ml-2 btn btn-secondary">등록</button>
    </div>
    <ul v-for="comment in commentDetail" :key="comment.id" class='p-0'>
      <li>
        <p class='text-monoscape h5 text-white'>{{ comment.user.username }}</p>
        <span class="text-monospace ml-2 text-white">{{ comment.content }}</span>
        <div class="text-right mt-4 mr-4">
          <i class="far fa-meh fa-lg"></i>
        </div>
        <button v-if="nowUser.id === comment.user.id" @click="commentDelete(comment.id)" class="btn btn1 ml-3">
          삭제
        </button>
        <hr id="hr1">
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapActions } from 'vuex'
import Swal from 'sweetalert2'

export default {
  name: 'CommentList',
  data() {
    return {
      createItem: {
        content: null,
      },
    }
  },
  computed: {
    ...mapState(['movieDetail', 'articleDetail', 'commentDetail', 'isLoggedIn', 'nowUser']),
  },
  methods: {
    ...mapActions(['commentGet']),

    createComment() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`http://127.0.0.1:8000/articles/${this.movieDetail.id}/${this.articleDetail.id}/create/`, this.createItem, config)
        .then(() => {
          this.commentGet()
          this.createItem.content = null
        })
        .catch(() => {
          if(!this.createItem.content) {
            Swal.fire({
              title: 'Error!',
              text: '내용을 입력해주세요',
              icon: 'error',
              confirmButtonText: '취소'
            })
          }
        })
    },
    commentDelete(ID) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`http://127.0.0.1:8000/articles/${this.movieDetail.id}/${this.articleDetail.id}/${ID}/delete/`, null, config)
        .then(() => {
          this.commentGet()
        })
    },

    },
  mounted() {
    this.commentGet()
  },

}
</script>

<style>
  ul {
    list-style-type: none;
  }

  hr#hr1
  {
    border-top: 1px dashed #8c8b8b;
    border-bottom: 1px dashed #fff;
  }

  .btn1 {
    background-color: LawnGreen;
    color: whitesmoke
  }
</style>