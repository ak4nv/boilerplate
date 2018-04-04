<template>
  <ajax-form class="form-horizontal centered" @submit="submit" :loading="loading">
    <h4 class="text-center text-gray">Welcome to {{ app_name }}</h4>
    <div class="form-group">
      <div class="col-3">
        <label class="form-label" for="username">Username</label>
      </div>
      <div class="col-9">
        <input required
          id="username"
          ref="login"
          type="text"
          class="form-input"
          placeholder="Username"
          v-model="form.username">
      </div>
    </div>
    <div class="form-group">
      <div class="col-3">
        <label class="form-label" for="password">Password</label>
      </div>
      <div class="col-9">
        <input required
          id="password"
          type="password"
          class="form-input"
          placeholder="Password"
          v-model="form.password">
      </div>
    </div>
    <div class="form-group">
      <div class="col-9 col-ml-auto">
        <button class="btn btn-primary" type="submit">Login</button>
      </div>
    </div>
  </ajax-form>
</template>
<script>
  import ajaxForm from './ajax_form.vue'

  export default {
    components: { ajaxForm },
    data () {
      return {
        form: {
          username: '',
          password: '',
        },
        app_name: Session.app_name,
        loading: false,
      }
    },
    mounted () {
      this.$refs.login.focus()
    },
    methods: {
      submit () {
        this.$http.post('/auth/login', this.form).then(resp => {
          if (resp.data.errors) {
            this.$error(resp.data.errors)
            this.$refs.login.focus()
          } else {
            Session.update(resp.data)
            this.$router.push(this.$route.query.next || {'path': '/'})
          }
        })
      }
    }
  }
</script>
<style scoped>
form {
    width: 400px;
    height: 300px;

    position: absolute;
    top:0;
    bottom: 0;
    left: 0;
    right: 0;

    margin: auto;
}
</style>