import DashboardLayout from '../layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../pages/NotFoundPage.vue'

// Admin pages
import Overview from 'src/pages/Overview.vue'
import Livelihood from 'src/pages/Livelihood.vue'
import EventsDeal from 'src/pages/EventsDeal.vue'
import Streetevent from 'src/pages/StreetEvent.vue'
import Login from 'src/pages/Login.vue'
import Graph from 'src/pages/Graph.vue'

const routes = [
  {
    path: '/',
    component: DashboardLayout,
    redirect: '/admin/overview'
  },
  {
    path: '/admin',
    component: DashboardLayout,
    redirect: '/admin/overview',
    children: [
      {
        path: 'overview',
        name: 'Overview',
        component: Overview
      },
      {
        path: 'livelihood',
        name: 'Livelihood',
        component: Livelihood
      },
      {
        path: 'eventsdeal',
        name: 'eventsdeal',
        component: EventsDeal
      },
      {
        path: 'streetevent',
        name: 'streetevent',
        component: Streetevent
      },
      {
        path: 'login',
        name: 'login',
        component: Login
      },
      {
        path: 'overview',
        name: 'overview',
        component: Overview
      },
      {
        path: 'graph',
        name: 'graph',
        component: Graph
      }
    ]
  },
  { path: '*', component: NotFound }
]

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes
