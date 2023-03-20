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
import StudentRoom from '../views/StudentRoom.vue';
import StudentTestView from '../views/StudentTestView.vue';
import Professor from '../views/Professor.vue';
import ProctorTestView from '../views/ProctorTestView.vue';
import ProfessorInbox from '../views/ProfessorInbox.vue';
import ProfessorRoomReserve from '../views/ProfessorRoomReserve';
import ProfessorRoomsView from '../views/ProfessorRoomsView.vue';
import ProfessorResRoomSelect from '../views/ProfessorResRoomSelect.vue';
import ProfessorReservation from '../views/ProfessorReservation.vue';
import StudentInbox from '../views/StudentInbox.vue'
import ProctorInbox from '../views/ProctorInbox.vue'


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
  {
    path: '/admin/rooms/:bldg/:room',
    name: 'Admin-Scheduling',
    component: AdminScheduling,
    meta: {
      needAuth: true,
      userType: 'admin',
    },
  },
  // Proctor routes
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
    path: '/proctor/rooms/:bldg/:room',
    name: 'Proctor-Rooms',
    component: ProctorRoomView,
    meta: {
      needAuth: true,
      userType: 'proctor',
    },
  },
  {
    path: '/proctor/rooms/:bldg/:room/testView',
    name: 'Proctor-Rooms',
    component: ProctorTestView,
    meta: {
      needAuth: true,
      userType: 'proctor',
    },
  },
  {
    path: '/proctor/inbox',
    name: 'Proctor-Inbox',
    component: ProctorInbox,
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
  {
    path: '/professor/reservation/rooms/:bldg/:room',
    name: 'professor-room-reserve',
    component: ProfessorRoomReserve,
    meta: {
      needAuth: true,
      userType: 'professor',
    },
  },
  {
    path: '/professor/rooms',
    name: 'Professor-room',
    component: ProfessorRoomsView,
    meta: {
      needAuth: true,
      userType: 'professor',
    },
  },
  {
    path: '/professor/rooms/:bldg/:room',
    name: 'Professor-res-view',
    component: ProfessorReservation,
    meta: {
      needAuth: true,
      userType: 'professor',
    },
  },
  {
    path: '/professor/reservation/select-room',
    name: 'Professor-room',
    component: ProfessorResRoomSelect,
    meta: {
      needAuth: true,
      userType: 'professor',
    },
  },
  {
    path: '/professor/inbox',
    name: 'Professor-inbox',
    component: ProfessorInbox,
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
    path: '/student/rooms',
    name: 'Student-Rooms',
    component: StudentRoom,
    meta: {
      needAuth: true,
      userType: 'student',
    },
  },
  {
    path: '/student/rooms/testView',
    name: 'Student-Rooms-Test-View',
    component: StudentTestView,
    meta: {
      needAuth: true,
      userType: 'student',
    },
  },
  {
    path: '/student/inbox',
    name: 'Student-Inbox',
    component: StudentInbox,
    meta: {
      needAuth: true,
      userType: 'student',
    },
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
