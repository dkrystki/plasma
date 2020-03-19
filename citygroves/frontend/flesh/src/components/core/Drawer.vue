<template>
  <v-navigation-drawer
          id="app-drawer"
          app
          dark
          floating
          persistent
          mobile-break-point="991"
          width="260"
  >
    <v-img :src="image" height="100%">
      <v-container align-start fill-height tag="v-list">
        <v-container>
          <v-list-item avatar>
            <v-list-item-avatar color="white">
              <v-img
                      :src="logo"
                      height="34"
                      contain
              />
            </v-list-item-avatar>
            <v-list-item-title class="title">
              Manager
            </v-list-item-title>
          </v-list-item>
          <v-divider/>
          <v-list-item
                  v-for="(link, i) in links"
                  :key="i"
                  :to="link.to"
                  avatar
                  class="v-list-item"
          >
            <v-list-item-action>
              <v-icon>{{ link.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-title
                    v-text="link.text"
            />
          </v-list-item>
        </v-container>
      </v-container>
    </v-img>
  </v-navigation-drawer>
</template>

<script>
    export default {
        data: () => ({
            logo: 'favicon.ico',
            image: "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg",
            links: [
                {
                    to: '/',
                    icon: 'mdi-view-dashboard',
                    text: 'Dashboard'
                },
                {
                    to: '/applications',
                    icon: 'mdi-account',
                    text: 'Applications'
                },
                {
                    to: '/tenants',
                    icon: 'mdi-account',
                    text: 'Tenants'
                },
            ]
        }),
    }
</script>

<style lang="scss">
  #app-drawer {
    .v-list__tile {
      border-radius: 4px;

      &--buy {
        margin-top: auto;
        margin-bottom: 17px;
      }
    }
  }
</style>
