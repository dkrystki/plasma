// =========================================================
// * Vuetify Material Dashboard - v1.0.0
// =========================================================

// * Product Page: https://www.creative-tim.com/product/vuetify-material-dashboard
// * Copyright 2019 Creative Tim (https://www.creative-tim.com)
// * Licenses under MIT

// * Coded by Creative Tim

// =========================================================

// * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'

// Components
import './components'

// Plugins
import './plugins'
import {sync} from 'vuex-router-sync'

// Application imports
import App from './App'
import router from '@/router'
import store from '@/store'
import vuetify from './plugins/vuetify'
import VueKeyCloak from '@dsb-norge/vue-keycloak-js'
import {Config} from '@/config'

// Sync store with router
sync(store, router);

Vue.config.productionTip = false;


Vue.use(VueKeyCloak, {
    init: {
        // Use 'login-required' to always require authentication
        // If using 'login-required', there is no need for the router guards in router.js
        onLoad: 'login-required'
    },
    config: {
        realm: 'Citygroves',
        url: Config.keycloak.url,
        clientId: 'citygroves-frontend'
    },
    onReady: (keycloak) => {
        /* eslint-disable no-new */
        new Vue({
            vuetify,
            router,
            store,
            keycloak,
            render: h => h(App)
        }).$mount('#app');
    }
});
