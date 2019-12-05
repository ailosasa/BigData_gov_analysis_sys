import DashboardLayout from '../layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../pages/NotFoundPage.vue'

// Admin pages
import Login from 'src/pages/Login.vue'
import Graph from 'src/pages/Graph.vue'
import Test from 'src/pages/Test.vue'
import UpdateDatabase from 'src/pages/UpdateDatabase.vue'
import SearchData from 'src/pages/SearchData.vue'
import UserManage from 'src/pages/UserManage.vue'
import UnsolvedRole from 'src/pages/UnsolvedRole.vue'
const routes = [
  {
    path: '/',
    component: DashboardLayout,
    redirect: '/admin/login'
  },
  {
    path: '/admin',
    component: DashboardLayout,
    redirect: '/admin/login',
    children: [
      {
        path: 'login',
        name: 'login',
        component: Login
      },
      {
        path: 'graph',
        name: 'graph',
        component: Graph
      },
      {
        path: 'updatedatabase',
        name: 'updatedatabase',
        component: UpdateDatabase
      },
      {
        path: 'searchdata',
        name: 'searchdata',
        component: SearchData
      },
      {
        path: 'usermanage',
        name: 'usermanage',
        component: UserManage
      },
      {
        path: 'unsolvedrole',
        name: 'unsolvedrole',
        component: UnsolvedRole
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
