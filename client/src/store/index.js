import Vue from 'vue'
import Vuex from 'vuex'
import datapage from './modules/datapage';


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    datapage,
  },
});