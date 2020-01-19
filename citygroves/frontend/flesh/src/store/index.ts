/**
 * Vuex
 *
 * @library
 *
 * https://vuex.vuejs.org/en/
 */

// Lib imports
import * as Vue from 'vue'
import Vuex from 'vuex'

// Store functionality
import {Tenant} from "../apis/backend";

Vue.use(Vuex);

const tenants = {
    namespaced: true,
    state: {
        selectedTenants: []
    },
    mutations: {
        setSelectedTenants(state, selected: Array<Tenant>) {
            state.selectedTenants = selected;
        }
    },
    getters: {
        selectedTenants: state => state.selectedTenants
    }
};


// Create a new store
const store = new Vuex.Store({
        modules: {
            tenants: tenants,
        }
    }
);

export default store


