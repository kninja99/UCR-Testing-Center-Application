import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../views/Login.vue';
import Admin from '../views/Admin.vue';
import AdminRoomSelect from '../views/AdminRoomSelect.vue';
import AdminInbox from '../views/AdminInbox.vue';
import Proctor from '../views/Proctor.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/login',
    name: 'Login2',
    component: Login,
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
  },
  {
    path: '/admin/rooms',
    name: 'Admin-Rooms',
    component: AdminRoomSelect,
  },
  {
    path: '/admin/inbox',
    name: 'Admin-Inbox',
    component: AdminInbox,
  },
  {
    path: '/admin/rooms/scheduling',
    name: 'Admin-room-scheduling',
    component: AdminScheduling,
  },
  {
    path: '/proctor',
    name: 'Proctor',
    component: Proctor,
  },
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

export default router;
