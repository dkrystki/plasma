<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <notifications></notifications>

    <side-bar>
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/applications">
        <md-icon>person</md-icon>
        <p>Applications</p>
      </sidebar-link>
      <sidebar-link to="/tenants">
        <md-icon>person</md-icon>
        <p>Tenants</p>
      </sidebar-link>
      <sidebar-link to="/notifications">
        <md-icon>person</md-icon>
        <p>Rooms</p>
      </sidebar-link>
      <sidebar-link to="/notifications">
        <md-icon>person</md-icon>
        <p>Inspections</p>
      </sidebar-link>
      <sidebar-link to="/notifications">
        <md-icon>notifications</md-icon>
        <p>Notifications</p>
      </sidebar-link>
    </side-bar>

    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content> </dashboard-content>

      <content-footer v-if="!$route.meta.hideFooter"></content-footer>
    </div>
  </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu.vue";

export default {
  components: {
    TopNavbar,
    DashboardContent,
    ContentFooter,
    MobileMenu
  }
};
</script>

