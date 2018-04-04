module.exports = [
  {
    path: '/',
    template: '<template />'
  },
  {
    name: 'login',
    path: '/login',
    meta: { public: true },
    component: require('./components/login.vue')
  }
]