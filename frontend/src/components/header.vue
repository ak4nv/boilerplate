<template>
  <header class="navbar bg-secondary">
    <section class="navbar-section">
      <a href="/" class="navbar-brand mr-2" v-text="app_name" />
    </section>
    <section class="navbar-section">
      <div class="btn btn-link">Welcome, {{user.firstname}}</div>
      <div class="btn btn-primary btn-sm" @click="logout">Logout</div>
    </section>
  </header>
</template>
<script>
  export default {
    data () {
      return {
        app_name: Session.app_name,
        user: Session.user
      }
    },
    methods: {
      logout () {
        this.$http.post('/auth/logout').then(resp => {
          Session.clear()
          this.$router.push({name: 'login'})
        })
      }
    }
  }
</script>
<style scoped>
  header {
    height: 3rem;
    padding-left: 1rem;
    padding-right: 1rem;
  }
</style>