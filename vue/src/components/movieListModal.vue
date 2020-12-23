<template>
  <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-danger" data-toggle="modal" :data-target="`#movie${movie.id}`" @click="getVideo">
      예고편 보기
    </button>
    <!-- Modal -->
    <div class="modal fade" :id="`movie${movie.id}`" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true" @click="videoOff">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header bg-white">
            
            <h5 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body embed-responsive embed-responsive-16by9">
            <iframe v-if="flag"
              class="embed-responsive-item" 
              :src="`https://www.youtube.com/embed/${videoUrl}`"
              frameborder="0" allowfullscreen>
            </iframe>
          </div>
          <div class="modal-footer bg-white">
            <button @click="$emit('goDetail')" class="btn btn-danger" data-dismiss="modal">자세히 보기</button>
            <button type="button" class="btn btn-danger" data-dismiss="modal" @click="videoOff">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_KEY = process.env.VUE_APP_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'movieListModal',
  props: {
    movie: Object,
  },
  data() {
    return {
      youTubeUrl: null,
      videoUrl: null,
      flag: false,
    }
  },
  methods: {
    getVideo() {
      this.flag = true
      this.youTubeUrl = this.movie.title + ' trailer'
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.youTubeUrl
        }
      })
        .then(response => {
          this.videoUrl = response.data.items[0].id.videoId
        })
        .catch(err => console.log(err.response))
    },
    videoOff() {
      this.flag = false
    }
  }

}

</script>

<style>
  .modal-header {
    background-color: black;
  }
  .modal-footer {
    background-color: black;
  }

  .modal-backdrop {
    z-index: -10
}


  
</style>