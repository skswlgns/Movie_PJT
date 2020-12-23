<template>
  <div class="container text-center mt-5 p-3">
    <h1 class="text-white">WatchFlix 로그인</h1>
    <div class="d-flex justify-content-center mt-3">
      <input type="text" class="form-control w-50" @keypress.enter="login" placeholder="아이디를 입력해주세요." v-model="loginData.username">
    </div>
    <div class="d-flex justify-content-center mt-3">
      <input type="password" class="form-control w-50" @keypress.enter="login" placeholder="비밀번호를 입력해주세요." v-model="loginData.password">
    </div>
    <button type="submit" class="btn btn-dark w-50 mt-3 text-white" @click="login" >로그인</button>
    <br>
    <img src="@/assets/mask2.jpg" alt="영화 캠페인 사진"  class="w-50 mt-3">
  </div>

</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      loginData: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    login() {
      this.$emit('login', this.loginData)
    }
  }


}
</script>

<style scoped>

</style>