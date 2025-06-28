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
				console.log(res.data)
				commit('setAgeTicketPriceData', res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},
};

const mutations = {

	setTicketSalesByMovieGenre(state, value) {
		state.ticketSalesByMovieGenre = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};