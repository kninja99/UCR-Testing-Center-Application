import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '../views/Login.vue';
import Admin from '../views/Admin.vue';
import AdminRoomSelect from '../views/AdminRoomSelect.vue';
import AdminInbox from '../views/AdminInbox.vue';
import Proctor from '../views/Proctor.vue';
import ProctorRoomSelect from '../views/ProctorRoomSelect.vue';
import ProctorRoomView from '../views/ProctorRoomView.vue';
import Student from '../views/Student.vue';
import Professor from '../views/Professor.vue';

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
  // Admin routes
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
  // Proctor routes
  {
    path: '/proctor',
    name: 'Proctor',
    component: Proctor,
  },
  {
    path: '/proctor/rooms',
    name: 'Proctor-Rooms',
    component: ProctorRoomSelect,
  },
  {
    path: '/proctor/rooms/testTimes',
    name: 'Proctor-Rooms',
    component: ProctorRoomView,
  },
  // Professor Routes
  {
    path: '/professor',
    name: 'professor',
    component: Professor,
  },
  // Student Routes
  {
    path: '/student',
    name: 'student',
    component: Student,
  },
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

export default router;
