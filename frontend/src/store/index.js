import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(Vuex);
Vue.use(VueAxios, axios);

export default new Vuex.Store({
  state: {
    validUser: false,
    userType: '',
    auth: '',
  },
  mutations: {
    login(state, userInfo) {
      // setting states
      state.validUser = true;
      state.userType = userInfo.userType;
      state.auth = userInfo.authToken;
      // setting seassion store
      window.sessionStorage.setItem('auth', state.auth);
      window.sessionStorage.setItem('userType', state.userType);
      window.sessionStorage.setItem('validUser', state.validUser);
    },
    logout(state) {
      // setting states
      state.validUser = false;
      state.userType = '';
      state.auth = '';
      // setting seassion store
      window.sessionStorage.setItem('auth', '');
      window.sessionStorage.setItem('userType', '');
      window.sessionStorage.setItem('validUser', false);
    },
    /**
     * Vuex function to ensure that our session data is the same as our store
     * @param {state} state
     */
    updateSession(state) {
      window.sessionStorage.setItem('auth', state.auth);
      window.sessionStorage.setItem('userType', state.userType);
      window.sessionStorage.setItem('validUser', state.validUser);
    },
  },
  getters: {
    validateUserInfo(state) {
      return (
        state.auth == window.sessionStorage.getItem('auth') &&
        state.userType == window.sessionStorage.getItem('userType') &&
        state.validUser &&
        window.sessionStorage.getItem('validUser')
      );
    },
  },
  actions: {},
  modules: {},
});
