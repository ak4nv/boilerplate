import VueRouter from 'vue-router'

const routes = require('./routes.js')
const router = new VueRouter({ routes })

router.options.linkActiveClass = 'active'
router.beforeEach(function(to, from, next) {
  if (!Session.user && !to.meta.public)
    next({path: '/login', query: {next: to.path}})
  else
    next()
})

module.exports = router