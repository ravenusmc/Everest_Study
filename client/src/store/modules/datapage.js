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
  deathsByExpedition: [
    ['Adventure Consultants', 13], 
    ['Indian expedition', 9], 
    ['Asian Trekking', 9]
  ],
  stateDeathsDrillDown: [],

};

const getters = {
	deathsByStates: (state) => state.deathsByStates,
  deathsByAge: (state) => state.deathsByAge, 
  deathsByExpedition: (state) => state.deathsByExpedition,
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
        commit('setDeathsByAge', res.data['bins_for_age_graph'])
		})
		.catch((error) => {
			console.log(error);
		});
  },

  // getDataForDrillDown: ({commit}, {payload}) => {
  //   const path = 'http://localhost:5000/getDataForDrillDownGraphs';
  //   axios.post(path, payload)
	// 	.then((res) => {
	// 			commit('setStatesDeathsDrillDown', 5)
  //       return res.data
	// 	})
	// 	.catch((error) => {
	// 		console.log(error);
	// 	});
  // },

  async getDataForDrillDown ({commit}, payload) {
    console.log(payload)
    try {
			// Perform an asynchronous operation, for example, an API call
			const res = await axios.post('http://localhost:5000/getDataForDrillDownGraphs', payload);
			// Return the data from the response
      commit('setStatesDeathsDrillDown', 5)
			return res.data;
		} catch (error) {
			console.error('Error in drilldown action:', error);
			throw error;
		}
    // const path = 'http://localhost:5000/getDataForDrillDownGraphs';
    // axios.post(path, payload)
		// .then((res) => {
    //     console.log(res.data)
		// 		commit('setStatesDeathsDrillDown', 5)
    //     return res.data
		// })
		// .catch((error) => {
		// 	console.log(error);
		// });

  },
  
};

const mutations = {

	setDeathsByStates(state, value) {
		state.deathsByStates = value;
	},

  setDeathsByAge(state, value) {
    state.deathsByAge = value 
  }, 

  setDeathsByExpedition(state, value) {
    state.deathsByExpedition = value
  },

  // Mutations for the drill down tables
  setStatesDeathsDrillDown(state, value) {
    state.stateDeathsDrillDown = value
  }

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};