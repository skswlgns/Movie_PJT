<template>
  <div class="container text-center p-5">
    <h1 class="text-light">회원정보 수정</h1>
    <hr>
    <div class="text-left">
      <span class="font-weight-bold h5 mr-5 text-light">성별 : </span>
      <div class="custom-control custom-radio custom-control-inline">  
        <input type="radio" id="customRadioInline1" name="customRadioInline1" class="custom-control-input" v-model="userInfo.gender" value="남자">
        <label class="custom-control-label text-white" for="customRadioInline1">남자</label>
      </div>
      <div class="custom-control custom-radio custom-control-inline">
        <input type="radio" id="customRadioInline2" name="customRadioInline1" class="custom-control-input" v-model="userInfo.gender" value="여자">
        <label class="custom-control-label text-white" for="customRadioInline2">여자</label>
      </div>
    </div>
    <hr>
    <div class="text-left">
      <span class="font-weight-bold h5 mr-5 text-light">좋아하는 장르 : </span>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option" v-model="userInfo.drama">
        <label class="form-check-label text-white" for="inlineCheckbox1">드라마</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2" v-model="userInfo.fear">
        <label class="form-check-label text-white" for="inlineCheckbox2">공포</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3" v-model="userInfo.melloh">
        <label class="form-check-label text-white" for="inlineCheckbox3">멜로/로맨스</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox4" value="option4" v-model="userInfo.thriller">
        <label class="form-check-label text-white" for="inlineCheckbox4">스릴러</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox5" value="option5" v-model="userInfo.comedey">
        <label class="form-check-label text-white" for="inlineCheckbox5">코미디</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox6" value="option6" v-model="userInfo.animation">
        <label class="form-check-label text-white" for="inlineCheckbox6">애니메이션</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox7" value="option7" v-model="userInfo.suspense">
        <label class="form-check-label text-white" for="inlineCheckbox7">서스펜스</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox8" value="option8" v-model="userInfo.action">
        <label class="form-check-label text-white" for="inlineCheckbox8">액션</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="inlineCheckbox9" value="option9" v-model="userInfo.sf">
        <label class="form-check-label text-white" for="inlineCheckbox9">SF</label>
      </div>
    </div>
    <hr>
    <div class="text-left">
      <span class="font-weight-bold h5 mr-5 text-light">나이 : </span>
      <input type="text" class="form-control w-25 d-inline" placeholder="만 나이로 적어주세요 ex) 24" v-model="userInfo.age">
    </div>
    <hr>
    <div class="text-left">
      <span class="font-weight-bold h5 mr-5 text-light">키즈계정 전환 : </span>
      <div class="custom-control custom-radio custom-control-inline">  
        <input type="radio" id="customRadioInline3" name="customRadioInline3" class="custom-control-input" v-model="userInfo.kids" :value="true">
        <label class="custom-control-label text-white" for="customRadioInline3">예</label>
      </div>
      <div class="custom-control custom-radio custom-control-inline">
        <input type="radio" id="customRadioInline4" name="customRadioInline4" class="custom-control-input" v-model="userInfo.kids" :value="false">
        <label class="custom-control-label text-white" for="customRadioInline4">아니오</label>
      </div>
    </div>
    <hr>
    <div class="text-left">
      <span class="font-weight-bold h5 mr-5 text-light">아버지 나이 : </span>
      <input type="text" class="form-control w-25 d-inline" placeholder="년도만 적어주세요 ex) 1960" v-model="userInfo.parent_F">
    </div>
    <div class="text-left">
      <span class="font-weight-bold h5 mr-5 text-light">어머니 나이 : </span>
      <input type="text" class="form-control w-25 d-inline" placeholder="년도만 적어주세요 ex) 1960" v-model="userInfo.parent_M">
    </div>
    <hr>
    <div class="text-left">
      <span class="font-weight-bold h5 mr-5 text-light">좋아하는 국가의 영화 : </span>
      <div class="form-group d-inline">
        <select class="form-control w-25 d-inline" id="exampleFormControlSelect1" v-model="userInfo.Favorite">
          <option>한국</option>
          <option>미국</option>
          <option>일본</option>
          <option>대만</option>
          <option>프랑스</option>
        </select>
      </div>
    </div>
    <button class="btn btn-primary mt-5" @click="createForm">제출</button>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import Swal from 'sweetalert2'
import axios from 'axios'

export default {
  name: 'UserForm',
  computed: {
    ...mapState(['nowUser', 'userInfo'])
  },
  data() {
    return {
    }
  },
  methods: {
    ...mapMutations(['userInfoChange']),
    createForm() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(`http://127.0.0.1:8000/articles/${this.userInfo.id}/form_update/`, this.userInfo, config)
        .then((res) => {
          console.log(res.data)
          this.userInfoChange(res.data)
          this.$router.push('/')
        })
        .catch((err) => {
          Swal.fire({
              title: 'Error!',
              text: '올바른 정보를 입력해주세요. 정확한 추천에 도움이 됩니다!',
              icon: 'error',
              confirmButtonText: '취소'
            })
        console.log(err.response)
        })
    },
  },

}
</script>

<style>

</style>