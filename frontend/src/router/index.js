import Vue from 'vue';
import store from '../store';
import VueRouter from 'vue-router';
import Login from '../views/Login.vue';
import Admin from '../views/Admin.vue';
import AdminRoomSelect from '../views/AdminRoomSelect.vue';
import AdminInbox from '../views/AdminInbox.vue';
import Proctor from '../views/Proctor.vue';
import AdminScheduling from '../views/AdminScheduling.vue';
import ProctorRoomSelect from '../views/ProctorRoomSelect.vue';
import ProctorRoomView from '../views/ProctorRoomView.vue';
import Student from '../views/Student.vue';
import Professor from '../views/Professor.vue';
import ProctorTestView from '../views/ProctorTestView.vue';

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
    meta: {
      needAuth: true,
      userType: 'admin',
    },
  },
  {
    path: '/admin/rooms',
    name: 'Admin-Rooms',
    component: AdminRoomSelect,
    meta: {
      needAuth: true,
      userType: 'admin',
    },
  },
  {
    path: '/admin/inbox',
    name: 'Admin-Inbox',
    component: AdminInbox,
    meta: {
      needAuth: true,
      userType: 'admin',
    },
  },
  // Proctor routes
  {
    path: '/admin/scheduling',
    name: 'Admin-Scheduling',
    component: AdminScheduling,
  },
  {
    path: '/proctor',
    name: 'Proctor',
    component: Proctor,
    meta: {
      needAuth: true,
      userType: 'proctor',
    },
  },
  {
    path: '/proctor/rooms',
    name: 'Proctor-Rooms',
    component: ProctorRoomSelect,
    meta: {
      needAuth: true,
      userType: 'proctor',
    },
  },
  {
    path: '/proctor/rooms/testTimes',
    name: 'Proctor-Rooms',
    component: ProctorRoomView,
    meta: {
      needAuth: true,
      userType: 'proctor',
    },
  },
  // Professor Routes
  {
    path: '/professor',
    name: 'professor',
    component: Professor,
    meta: {
      needAuth: true,
      userType: 'professor',
    },
  },
  // Student Routes
  {
    path: '/student',
    name: 'student',
    component: Student,
    meta: {
      needAuth: true,
      userType: 'student',
    },
  },
  {
    path: '/proctor/rooms/testTimes/testView',
    name: 'Proctor-Rooms',
    component: ProctorTestView,
  },
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

router.beforeEach((to, from, next) => {
  // checking for login authentication
  if (to.meta.needAuth) {
    // authenticating data with store
    if (
      store.getters.validateUserInfo &&
      to.meta.userType == store.state.userType
    ) {
      next();
    } else {
      next('/login');
    }
  } else {
    next();
  }
});

export default router;
