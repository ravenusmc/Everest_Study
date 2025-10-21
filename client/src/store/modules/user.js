import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const data = {
	passwordNoMatch: false,
	loginFlag: false,
};

const getters = {
	// userNotFound: (state) => state.userNotFound,
	passwordNoMatch: (state) => state.passwordNoMatch,
	loginFlag: (state) => state.loginFlag,
};

const actions = {

	signUpUser: (context, payload) => {
        console.log('ACTION')
        console.log(payload)
		const path = 'http://localhost:5000/signUpUser';
		axios.post(path, payload)
			.then((res) => {
                console.log(res)
				router.push({ name: 'login'})
			})
			.catch((error) => {
				console.log(error);
			});
	},

	loginUser: ({ commit }, { payload }) => {
		console.log('HERE')
		const path = 'http://localhost:5000/login';
		axios.post(path, payload)
			.then((res) => {
				if (res.data) {
					if (res.data[0] === true) {
						commit('setLoginFlag', res.data[0]);
						router.push({ name: 'library' });
					}else {
						commit('setLoginFlag', res.data[0]);
						// commit('setUserNotFound', res.data[1]);
						commit('setNoPasswordMatch', res.data[2]);
					}
				} 
			})
			.catch((error) => {
				console.log(error);
			});
	},

	logout: ({ commit }) => {
		commit('setUserNotFound', false);
		commit('setNoPasswordMatch', false);
		commit('setLoginFlag', false);
	},

};

const mutations = {

	setLoginFlag(state, value) {
		state.loginFlag = value;
	},

	setNoPasswordMatch(state, value) {
		state.passwordNoMatch = value 
	}, 

	// setUserNotFound(state, value) {
	// 	state.userNotFound
	// },

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};