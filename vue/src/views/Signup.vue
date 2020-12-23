<template>
  <div class="container text-center mt-5 p-3">
    <h1 class="text-white">WatchFlix 회원가입</h1>
    <div class="d-flex justify-content-center mt-3">
      <input type="text" class="form-control w-50" @keypress.enter="signup" placeholder="아이디를 입력해주세요." v-model="signupData.username">
    </div>
    <div class="d-flex justify-content-center mt-3">
      <input type="password" class="form-control w-50" @keypress.enter="signup" placeholder="비밀번호를 입력해주세요." v-model="signupData.password1">
    </div>
    <div class="d-flex justify-content-center mt-3">
      <input type="password" class="form-control w-50" @keypress.enter="signup" placeholder="비밀번호를 한번 더 입력해주세요." v-model="signupData.password2">
    </div>
    <button type="submit" class="btn btn-dark w-50 mt-3" @click="signup" >회원가입</button>
    <br>
    <img src="@/assets/mask.jpg" alt="영화 캠페인 사진"  class="w-50 mt-3">
  </div>

</template>

<script>
export default {
  name: 'Signup',
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
      }
    }
  },
  methods: {
    signup() {
      this.$emit('signup', this.signupData)
    }
  }


}
</script>

<style scoped>

</style>