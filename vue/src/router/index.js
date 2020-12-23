import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import MovieList from '@/views/MovieList.vue'
import MovieDetail from '@/views/MovieDetail.vue'
import ArticleDetail from '@/views/ArticleDetail.vue'
import ArticleCreate from '@/views/ArticleCreate.vue'
import ArticleUpdate from '@/views/ArticleUpdate.vue'
import UserForm from '@/views/UserForm.vue'
import UserUpdate from '@/views/UserUpdate.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter(to, from, next) {
      if (Vue.$cookies.isKey('auth-token')) {
        next('/')
      } else {
        next()
      }    }
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/movie',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/movie_detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/article_detail',
    name: 'ArticleDetail',
    component: ArticleDetail
  },
  {
    path: '/article_create',
    name: 'ArticleCreate',
    component: ArticleCreate
  },
  {
    path: '/article_update',
    name: 'ArticleUpdate',
    component: ArticleUpdate
  },
  {
    path: '/userForm',
    name: 'UserForm',
    component: UserForm
  },
  {
    path: '/userUpdate',
    name: 'UserUpdate',
    component: UserUpdate,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
