/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
import Applications from "@/views/Application/Applications";
import Application from "@/views/Application/Application";
import Tenant from "@/views/Tenant/Tenant";
import Tenants from "@/views/Tenant/Tenants";
import EntryNotice from "@/views/Tenant/EntryNotice";

export default [

    {
        path: "/dashboard",
        name: "Dashboard",
    },
    {
        path: "/applications",
        name: "Applications",
        component: Applications
    },
    {
        path: "/applications/:id",
        name: "Application",
        component: Application
    },

    {
        path: "/tenants",
        name: "Tenants",
        component: Tenants,
    },
    {
        path: "/tenants/:id",
        name: "Tenant",
        component: Tenant
    },
    {
        path: "/entry-notice",
        name: "EntryNotice",
        component: EntryNotice
    },
]
