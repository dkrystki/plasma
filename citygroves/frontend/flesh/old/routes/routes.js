import DashboardLayout from "../pages/Layout/DashboardLayout.vue";

import Applications from "../pages/Application/Applications.vue";
import Tenants from "../pages/Tenant/Tenants.vue";
import Application from "../pages/Application/Application.vue";
import Notifications from "../pages/Notifications.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "Dashboard",
      },
      {
        path: "applications",
        name: "Applications",
        component: Applications
      },
      {
        path: "applications/:id",
        name: "Application",
        component: Application
      },
      {
        path: "tenants",
        name: "Tenants",
        component: Tenants
      },
      {
        path: "notifications",
        name: "Notifications",
        component: Notifications
      },
    ]
  }
];

export default routes;
