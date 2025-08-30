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
  causeOfDeath: [
    ['Fall', 63], 
    ['Avalanche', 51], 
    ['Exposure', 25]
  ],
  deathsByMonth: [
    ['Jan', 3], 
    ['Mar', 3], 
    ['Apr', 72], 
    ['May', 175], 
    ['Jun', 16], 
    ['Jul', 1], 
    ['Aug', 4], 
    ['Sep', 28], 
    ['Oct', 36], 
    ['Nov', 1], 
    ['Dec', 4]
  ],
  heatMapCauseLocationData: [],
  startDate: "1921-06-05",
  endDate: "2025-05-15",
  bins: 10, 
};

const getters = {
	deathsByStates: (state) => state.deathsByStates,
  deathsByAge: (state) => state.deathsByAge, 
  deathsByExpedition: (state) => state.deathsByExpedition,
  causeOfDeath: (state) => state.causeOfDeath,
  deathsByMonth: (state) => state.deathsByMonth,
  heatMapCauseLocationData: (state) => state.heatMapCauseLocationData,
  startDate: (state) => state.startDate, 
  endDate: (state) => state.endDate, 
  bins: (state) => state.bins, 
};

const actions = {

	getDataForGraphs: ({ commit }) => {
		const path = 'http://localhost:5000/getInitialDataForGraphs';
		axios.get(path)
			.then((res) => {
        console.log(res.data['Heat_Map_Data'])
				commit('setHeatMapCauseLocationData', res.data['Heat_Map_Data'])
			})
			.catch((error) => {
				console.log(error);
			});
	},

  getDataBasedOnFilters:({commit}, {payload}) => {
    commit('setBins', payload['numberOfBins'])
    commit('setStartDate', payload['firstDate'])
    commit('setEndDate', payload['lastDate'])
    const path = 'http://localhost:5000/getDataBasedOnFilters';
		axios.post(path, payload)
		.then((res) => {
				commit('setDeathsByStates', res.data['top_nations'])
        commit('setDeathsByAge', res.data['bins_for_age_graph'])
        commit('setDeathsByExpedition', res.data['data_for_expeditions'])
        commit('setCauseOfDeath', res.data['top_Causes_of_death'])
        commit('setDeathsByMonth', res.data['deaths_by_month'])
		})
		.catch((error) => {
			console.log(error);
		});
  },

  async getDataForDrillDown ({ getters }, payload) {
    try {
      payload['startDate'] = getters.startDate
      payload['endDate'] = getters.endDate
			const res = await axios.post('http://localhost:5000/getDataForDrillDownGraphs', payload);
			return res.data;
		} catch (error) {
			console.error('Error in drilldown action:', error);
			throw error;
		}
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

  setCauseOfDeath(state, value) {
    state.causeOfDeath = value
  },

  setDeathsByMonth(state, value) {
    state.deathsByMonth = value
  },

  setHeatMapCauseLocationData(state, value) {
    state.heatMapCauseLocationData = value
  },

  setStatesDeathsDrillDown(state, value) {
    state.stateDeathsDrillDown = value
  },

  setStartDate(state, value) {
    state.startDate = value 
  },

  setEndDate(state, value) {
    state.endDate = value
  },

  setBins(state, value) {
    state.bins = value
  }, 

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};