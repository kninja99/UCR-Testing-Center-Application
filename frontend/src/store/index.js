import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex);
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    validUser: false,
    userType: '',
    auth: ''
  },
  mutations: {
    login(state, userInfo) {
      // setting states
      state.validUser = true;
      state.userType = userInfo.userType;
      state.auth = userInfo.authToken;
      // setting seassion store
      window.sessionStorage.setItem("auth",state.auth);
      window.sessionStorage.setItem("userType",state.userType);
      window.sessionStorage.setItem("validUser",state.validUser);
    }
  },
  actions: {},
  modules: {},
});
