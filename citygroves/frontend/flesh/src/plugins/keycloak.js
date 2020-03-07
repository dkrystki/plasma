import Vue from 'vue'
import VueKeyCloak from '@dsb-norge/vue-keycloak-js'

Vue.use(VueKeyCloak, {
    config: {
        realm: 'MyRealm',
        url: 'keycloak-http/auth',
        clientId: 'MyClientId'
    }
});
