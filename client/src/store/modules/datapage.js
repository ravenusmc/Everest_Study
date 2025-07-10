import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
// import store from '@/store/index';

Vue.use(Vuex);

const data = { 
	deathsByStates: [
    ['Nepal', 132], 
    ['India', 27], 
    ['Japan', 19]
  ],
  deathsByAge: [
    ['10-19', 2], 
    ['20-29', 36], 
    ['30-39', 76], 
    ['40-49', 54], 
    ['50-59', 29], 
    ['60-69', 13], 
    ['70-79', 0], 
    ['80-89', 2]
  ],

};

const getters = {
	deathsByStates: (state) => state.deathsByStates,
  deathsByAge: (state) => state.deathsByAge, 
};

const actions = {

	getDataForGraphs: ({ commit }) => {
		const path = 'http://localhost:5000/getDataForGraphs';
		axios.get(path)
			.then((res) => {
				commit('setDeathsByStates', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

  getDataBasedOnFilters:({commit}, {payload}) => {
    const path = 'http://localhost:5000/getDataBasedOnFilters';
		axios.post(path, payload)
		.then((res) => {
        console.log(res.data)
				commit('setDeathsByStates', res.data['top_nations'])
		})
		.catch((error) => {
			console.log(error);
		});
  }
  
};

const mutations = {

	setDeathsByStates(state, value) {
		state.deathsByStates = value;
	},

  setDeathsByAge(state, value) {
    state.deathsByAge = value 
  }, 

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};