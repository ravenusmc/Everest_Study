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
};

const getters = {
	deathsByStates: (state) => state.deathsByStates,
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
				commit('setDeathsByStates', res.data)
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

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};