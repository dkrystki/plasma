import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import Dashboard from "@/pages/Dashboard.vue";
import Applications from "@/pages/Applications.vue";
import Application from "@/pages/Application.vue";
import Notifications from "@/pages/Notifications.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard
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
        path: "notifications",
        name: "Notifications",
        component: Notifications
      },
    ]
  }
];

export default routes;
