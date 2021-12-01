import { createStore } from 'vuex'

export default createStore({
  state: {
    user:''
  },
  mutations: {
    login(state,uname){
      state.user = uname;
    }
  },
  actions: {
  },
  modules: {
  }
})
